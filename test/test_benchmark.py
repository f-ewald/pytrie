from trie.trie import Trie


def test_benchmark_init(benchmark) -> None:
    benchmark(Trie)


def test_benchmark_add(benchmark) -> None:
    t = Trie()
    benchmark(lambda: t.add('hello'))


def test_benchmark_add_large(benchmark, generated_words) -> None:
    def add():
        t = Trie()
        for word in generated_words:
            t.add(word)

    benchmark(add)
