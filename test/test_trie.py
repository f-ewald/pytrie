from trie import Trie
from pytest import mark


def test_init() -> None:
    t = Trie()
    assert t is not None


def test_add() -> None:
    t = Trie()
    t.add("hello")
    assert t._root.has_child("h")


def test_has_word(hello_world_trie: Trie) -> None:
    assert hello_world_trie.has_word("hello")
    assert hello_world_trie.has_word("world")
    assert not hello_world_trie.has_word("hell")


def test_has_prefix(hello_world_trie: Trie) -> None:
    assert hello_world_trie.has_prefix("hell")
    assert hello_world_trie.has_prefix("wo")
    assert not hello_world_trie.has_prefix("a")


def test_find_prefix(hello_world_trie: Trie) -> None:
    prefix = hello_world_trie.find_prefix("hel")
    assert isinstance(prefix, list)
    assert len(prefix) == 1


def test_len() -> None:
    t = Trie()
    assert len(t) == 0

    t.add("hello")
    assert len(t) == 1

    t.add("world")
    assert len(t) == 2


@mark.parametrize("s,expected", [
    ("hello", True),
    ("he", False),
    ("world", True),
    ("wo", False),
])
def test_contains(hello_world_trie: Trie, s: str, expected: bool) -> None:
    if expected:
        assert s in hello_world_trie
    else:
        assert s not in hello_world_trie
