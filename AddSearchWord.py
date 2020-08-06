class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        
        if '.' not in word:
            return word in self.word_dict[len(word)]

        for w in self.word_dict[len(word)]:
            success = True
            for index, ch in enumerate(word):
                if ch != w[index] and ch != '.':
                    success = False
                    break

            if success:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
