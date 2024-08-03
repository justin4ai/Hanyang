import sys
import numpy as np
import math
from collections import Counter
from pprint import pprint


def entropy(target):

    unique_categories, cnts = np.unique(target, return_counts=True) # ex. ['A', 'B', 'B', 'C', 'B'] -> ['A', 'B', 'C']
    return np.sum([( (- cnts[idx]) / np.sum(cnts)) * math.log2(cnts[idx] / np.sum(cnts)) for idx in range(len(unique_categories))])


def entropy_after_n_split_info(partitions, n):
    
    entropy_after, split_info = 0, 0
    for feature_partition, target_partition in partitions.values():

        d = (len(feature_partition) / n) # d cannot be 1
        entropy_after += d * entropy(target_partition)
        split_info -= d * math.log2(d)

    return entropy_after, split_info


def gain_ratio_func(partitions, n, info_current):

    info_after, split_info = entropy_after_n_split_info(partitions, n)
    gain = info_current - info_after
    gain_ratio = gain / split_info

    return gain_ratio


def multiway_split(feature, target, idx):

    partitions, feature_split = {}, feature[:, idx]
    unique_categories = np.unique(feature_split) # target cannot be empty
    for category in unique_categories:

        indices = [True if feature_value == category else False for feature_value in feature_split]
        partitions[category] = [feature[indices], target[indices]]

    return partitions


def best_split(feature, target, used_features):
    #global used_features
    best_gain, partition, n, info_current = -1, {}, len(feature), entropy(target)

    for idx in range(feature.shape[1]): # idx stands for each feature index

        if idx in used_features: continue # prevent re-using. If every feature has been used, return partition as {}
        
        partitions = multiway_split(feature, target, idx)
        gain_ratio = gain_ratio_func(partitions, n, info_current)

        if gain_ratio >= best_gain: best_gain, partition = gain_ratio, {'index' : idx, 'partition' : partitions}

    return partition


def fit_decision_tree(feature, target, used_features):

    subtrees = {}
    if len(np.unique(target)) == 1:  # classifying ends!
        prediction = Counter(target).most_common(1)[0][0]
        return {'class' : prediction}

    partition = best_split(feature, target, used_features)

    if len(partition) == 0: # empty partition stands for all-features-used
        prediction = Counter(target).most_common(1)[0][0]
        return {'class' : prediction}
    
    if len(partition['partition']) == 0: # empty partition stands for no-entity-to-be-clasified-left
        prediction = Counter(target).most_common(1)[0][0]
        return {'class' : prediction}


    for category in partition['partition'].keys():
        feature_partition, target_partition = partition['partition'][category]
        subtree = fit_decision_tree(feature_partition, target_partition, used_features + [partition['index']])
        subtrees[category] = subtree

    return {'index' : partition['index'], 'subtrees' : subtrees}

######################################################## Fitting function ends ######################################################################
######################################################## Prediction function starts ######################################################################

def pick_majority(tree, classes):

    #cnt = {'acc': 0, 'unacc': 0}
    cnt = {label : 0 for label in classes} # for generalization
    stack = [tree]

    while stack:
        cursor = stack.pop()

        if 'class' in cursor:
            if cursor['class'] in cnt:
                cnt[cursor['class']] += 1

        else:
            for key in cursor['subtrees'].keys():
                stack.append(cursor['subtrees'][key])

    return cnt



def predict_decision_tree(classifier, feature, classes):

    tree = classifier.copy()
    while 'subtrees' in tree.keys(): # still not reaching class node

        category = feature[tree['index']] # to follow the order of pre-fit classifier(tree)

        if category in tree["subtrees"].keys():
            tree = tree["subtrees"][category]
        
        else:
            # random_key = list(tree['subtrees'].keys())[0] # 313/346
            # tree = tree['subtrees'][random_key]

            cnt = pick_majority(tree, classes) # 321/346
            #print(f"Unseen in training set. Classes count in subtree : {cnt}")

            return [max(cnt, key=cnt.get)] # won't go further. I don't want to overfit my model
        
    #print(f"Seen in training set. Classified as {tree['class']}")    
    return [tree["class"]]

    

if __name__ == '__main__':

    train_path = 'datasets/' + sys.argv[1]
    test_path = 'datasets/' + sys.argv[2]
    output_path = 'datasets/' + sys.argv[3]

    flag = -1
    columns = []

    with open(train_path, 'r') as file:
        features_train, labels_train = [], []

        for line in file:
            data_train = [att for att in line.strip().split()]
            
            if flag == -1:
                columns = data_train # feature names including target feature
            else:
                features_train.append(data_train[:-1])
                labels_train.append(data_train[-1])

            flag += 1
    
    classes = np.unique(labels_train)
    classifier = fit_decision_tree(np.array(features_train), np.array(labels_train), [])
    #pprint(classifier)
    #print(classifier['subtrees']['<=30']['subtrees']['yes'].keys())

    flag = -1
    cnt_ = 0
    output = []
    with open(test_path, 'r') as file:

        for line in file:
            if flag == -1:
                output.append(columns)

            else:
                features = [att for att in line.strip().split()]
                features += predict_decision_tree(classifier, features, classes)
                output.append(features)

            flag += 1

    with open(output_path, "w") as file:
        for row in output:
            line = "\t".join(str(value) for value in row) + "\n"
            file.write(line)

    
