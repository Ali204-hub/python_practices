"""A case-sensitive Trie (prefix tree) for efficient word lookup.

Insertion, search, prefix checks, and deletion take O(L) time, where L is
word length. Listing words under a prefix also depends on the output size.

Run: python data_structures/trie.py
"""


class _TrieNode:
    """One node in the prefix tree."""

    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.is_word = False


class Trie:
    """Store unique, non-empty strings and support prefix-based lookup."""

    def __init__(self) -> None:
        self._root = _TrieNode()
        self._size = 0

    @staticmethod
    def _validate_word(word: str, *, allow_empty: bool = False) -> None:
        if not isinstance(word, str):
            raise TypeError("Trie values must be strings.")
        if not allow_empty and not word:
            raise ValueError("Trie words cannot be empty.")

    def insert(self, word: str) -> bool:
        """Insert a word; return False when it already exists."""
        self._validate_word(word)
        node = self._root

        for character in word:
            node = node.children.setdefault(character, _TrieNode())

        if node.is_word:
            return False

        node.is_word = True
        self._size += 1
        return True

    def _find_node(self, prefix: str) -> _TrieNode | None:
        node = self._root
        for character in prefix:
            node = node.children.get(character)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        """Return True only when the complete word has been inserted."""
        self._validate_word(word)
        node = self._find_node(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Return True when at least one stored word has this prefix."""
        self._validate_word(prefix, allow_empty=True)
        node = self._find_node(prefix)
        if node is None:
            return False
        return node.is_word or bool(node.children)

    def delete(self, word: str) -> bool:
        """Delete a complete word and prune unused nodes; return success."""
        self._validate_word(word)
        node = self._root
        path: list[tuple[_TrieNode, str, _TrieNode]] = []

        for character in word:
            child = node.children.get(character)
            if child is None:
                return False
            path.append((node, character, child))
            node = child

        if not node.is_word:
            return False

        node.is_word = False
        self._size -= 1

        for parent, character, child in reversed(path):
            if child.is_word or child.children:
                break
            del parent.children[character]

        return True

    def words_with_prefix(self, prefix: str = "") -> list[str]:
        """Return all matching words in lexicographical order."""
        self._validate_word(prefix, allow_empty=True)
        start = self._find_node(prefix)
        if start is None:
            return []

        words: list[str] = []
        stack: list[tuple[_TrieNode, str]] = [(start, prefix)]

        while stack:
            node, current = stack.pop()
            if node.is_word:
                words.append(current)
            for character in sorted(node.children, reverse=True):
                stack.append((node.children[character], current + character))

        return words

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def __len__(self) -> int:
        return self._size


def main() -> None:
    """Show prefix search with a small set of programming terms."""
    words = Trie()
    for word in ("python", "pycharm", "pytorch", "javascript", "java"):
        words.insert(word)

    print("Words starting with 'py':", words.words_with_prefix("py"))
    print("Is 'java' stored?", words.search("java"))


if __name__ == "__main__":
    main()
