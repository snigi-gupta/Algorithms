# https://www.geeksforgeeks.org/trie-insert-and-search/
# https://leetcode.com/explore/learn/card/trie/150/introduction-to-trie/1045/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertNode(self, newWord):
        current = self.root
        for ch in newWord:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.isEnd = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.isEnd

    def searchPrefix(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        """
        Is 
        """
        # if current.isEnd:
        #     return False
        return True


if __name__ == "__main__":
    obj = Trie()
    words = ['jack', 'jacques', 'jaqueline','adam', 'eve']
    search_words = ['jack', 'ada', 'jackq']
    for word in words:
        obj.insertNode(word)
    for word in search_words:
        print(obj.search(word))
    print("------")
    print(obj.searchPrefix('ja'))
    print(obj.searchPrefix('adam'))
    print(obj.searchPrefix('jc'))
