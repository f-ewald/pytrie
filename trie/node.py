from collections.abc import ValuesView


class Node:
    def __init__(self, value: str, children: dict[str, "Node"]) -> None:
        if value is None:
            raise ValueError("value cannot be None")

        if children is None:
            raise ValueError("children cannot be None")

        self._value: str = value
        self._children: dict[str, "Node"] = children
        self._is_word: bool = False

    @property
    def char(self):
        return self._value

    @property
    def is_word(self):
        return self._is_word

    @property
    def children(self) -> ValuesView["Node"]:
        return self._children.values()

    @property
    def is_leaf(self):
        return len(self._children) == 0

    def child(self, char) -> "Node":
        return self._children[char]

    def has_child(self, char) -> bool:
        return char in self._children

    def add_child(self, child: "Node") -> None:
        if self.has_child(child.char):
            raise ValueError(f"Child '{child.char}' already exists.")
        self._children[child.char] = child

    def __str__(self) -> str:
        return f"<Node({self._value})>"

    def __repr__(self):
        return str(self)
