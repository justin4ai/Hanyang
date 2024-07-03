# Practice 4. Palindromes and Balance
import sys
from collections import deque


## I'm supposing that there will be no empty string input like " " since
## I don't know whether I should regard it as palindrome & balanced one or not

def isPalindrome(string):

  # Solution 1
  # return True if string == string[::-1] else False # Time complexity : O(n) # Time complexity : O(n)

  # Solution 2
  myDeq = deque()
  myStack = []

  for char in string:
    myDeq.append(char)
    myStack.append(char)

  for i in range(len(string)):
    if myDeq.popleft() != myStack.pop():
      return False

  return True

  # Time complexity : O(n)


def balance(string):

  myStack = [] # Stack for remembering openers which had not met corresponding closers yet
               # But in real appending, I append the closer instead of the opener for easier comparison
               # in each stack popping
  myHash = {'(' : ')', '{' : '}', '[' : ']'} # To match the opener and the corresponding closer


  for char in string:

    if char in myHash.values(): #### 1) If we meet closers

      if len(myStack) != 0: # And there remains something to pop
        top = myStack.pop() # The latest element is popped out and stored in ,,top'' variable

        if char == top: pass # Check if those two closers are the same

        else: return False # Not the same -> already not balanced

      else: return False # If there's nothing to pop


    elif char in myHash: #### 2) - If we meet openers
      myStack.append(myHash[char]) # Append the corresponding closer to my stack

    else: pass #### 3) - Neither opener or closer -> do nothing


  if len(myStack) == 0: return True # If the final stack is empty, which means every pair matches.

  else: return False # If there remains unmatched one(s)

  # Time complexity : O(n)



if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == 'P':
        if len(words) != 2:
          raise Exception("PALINDROME: invalid input")
        ret = "T" if isPalindrome(words[1]) else "F"
        outFile.write(ret+"\n")
      elif op == 'B':
        if len(words) != 2:
          raise Exception("BALANCE: invalid input")
        ret = "T" if balance(words[1]) else "F"
        outFile.write(ret+"\n")
      else:
        raise Exception("Undefined operator")

        
