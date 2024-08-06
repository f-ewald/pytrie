from .node import Node
from typing import Optional


class Trie:
    def __init__(self):
        self._root: Node = Node("-", {})
        self._num_words = 0

    def add(self, s) -> None:
        """Add a string to the trie."""
        is_new = False
        p = 0
        n = self._root
        while p < len(s):
            char = s[p]
            if not n.has_child(char):
                n.add_child(Node(char, {}))
                is_new = True
            n = n.child(char)
            p += 1
        n._is_word = True
        if is_new:
            self._num_words += 1

    def find_prefix(self, s) -> list[Node]:
        n = self._find_node(s)
        if not n:
            return []

        for child in n.children:
            pass
        return None

    def has_prefix(self, s: str) -> bool:
        n: Optional[Node] = self._find_node(s)
        if not n:
            return False
        return True

    def has_word(self, s: str) -> bool:
        n: Optional[Node] = self._find_node(s)
        if not n:
            return False
        return n.is_word

    def _find_node(self, s: str) -> Optional[Node]:
        p: int = 0
        n: Node = self._root
        while p < len(s):
            char = s[p]
            if not n.has_child(char):
                return None
            n = n.child(char)
            p += 1
        return n

    def __len__(self) -> int:
        """Number of words in the trie."""
        return self._num_words

    def __contains__(self, item) -> bool:
        return self.has_word(item)
