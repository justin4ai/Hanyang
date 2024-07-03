# Practice 15. Autocomplete system
import sys
BUILD_TRIE = 'T'
AUTOCOMPLETE = 'A'
ENDS_HERE = '#'

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:

            if c not in t:

                t[c] = {}

            t = t[c]

        t[ENDS_HERE] = True

    def search(self, word):
        t = self.trie
        for c in word:

            if c not in t: return ['No matching word']

            t = t[c]
        return self.get_words(t, prefix)

    def get_words(self, t, prefix):
        words = []
        if (ENDS_HERE in t) and (t[ENDS_HERE]): # If prefix itself is a matching word
            words.append(prefix)

        for char, child in t.items():

            if char != ENDS_HERE: # If not the end -> go deeper
                words.extend(self.get_words(child, prefix + char))

        return words

if __name__ == '__main__':
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if op == BUILD_TRIE:
        if len(words) != 2:
          raise Exception("BUILD_TRIE: invalid input")
        n = int(words[1])
        strings = []
        while n:
          i += 1
          strings.append(lines[i].strip())
          n -= 1
        Trie = Trie()
        for word in strings:
            Trie.insert(word)
      elif op == AUTOCOMPLETE:
        if len(words) != 2:
          raise Exception("AUTOCOMPLETE: invalid input")
        prefix = words[1]
        outFile.write(' '.join(Trie.search(prefix)) + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1
