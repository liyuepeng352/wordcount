from wordcount import count_words


def test_counts_simple_sentence():
    assert count_words("hello world") == 2


def test_counts_multiple_spaces_as_one_separator():
    assert count_words("hello   world") == 2


def test_counts_words_across_newlines():
    assert count_words("hello\nworld\nfoo") == 3


def test_counts_zero_words_in_empty_string():
    assert count_words("") == 0


def test_counts_zero_words_in_whitespace_only_string():
    assert count_words("   \n\t  ") == 0
