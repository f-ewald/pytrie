from pytest import fixture

from trie import Trie

from string import ascii_letters
from random import choice


@fixture
def hello_world_trie() -> Trie:
    t = Trie()
    t.add("hello")
    t.add("world")
    return t


@fixture
def generated_words() -> list[str]:
    n = 1_000_000
    words = []
    for _ in range(n):
        s = []
        for i in range(6):
            s.append(choice(ascii_letters))
        words.append("".join(s))
    return words
