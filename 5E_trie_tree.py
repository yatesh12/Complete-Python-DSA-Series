# trie_tree.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print(f"Inserted word: {word}")

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print(f"Word '{word}' not found")
                return False
            node = node.children[char]
        if node.is_end_of_word:
            print(f"Word '{word}' found")
        else:
            print(f"Prefix '{word}' found but not a complete word")
        return node.is_end_of_word

    def delete(self, word):
        self._delete_helper(self.root, word, 0)

    def _delete_helper(self, node, word, depth):
        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                return len(node.children) == 0
            return False

        char = word[depth]
        if char in node.children:
            can_delete = self._delete_helper(node.children[char], word, depth + 1)
            if can_delete:
                del node.children[char]
                return len(node.children) == 0
        return False

# Example usage
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.search("app")
    trie.search("apple")
    trie.search("banana")
