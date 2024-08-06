from trie import Node
from pytest import mark, raises


@mark.parametrize("c,children,valid", [
    ("", {}, True),
    ("a", {}, True),
    ("b", {}, True),
    ("C", {}, True),
    ("X", {}, True),
    (" ", {}, True),
    (None, {}, False),
    ("a", None, False),
])
def test_init(c, children, valid) -> None:
    if valid:
        n = Node(c, children)
    else:
        with raises(ValueError):
            Node(c, children)


@mark.parametrize("node,expected", [
    (Node("h", {}), False),
    (Node("a", {}), False),
    (Node("", {}), False),
])
def test_is_word(node, expected) -> None:
    assert expected == node.is_word


def test_children() -> None:
    n = Node("a", {})
    assert n.children is not None



@mark.parametrize("s", [
    ("",),
    ("a",),
    ("b",),
])
def test_str(s) -> None:
    n = Node(s, {})
    assert str(n) == f"<Node({s})>"


@mark.parametrize("s", [
    ("",),
    ("a",),
    ("b",),
])
def test_repr(s) -> None:
    n = Node(s, {})
    assert n.__repr__() == f"<Node({s})>"
