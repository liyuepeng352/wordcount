# wordcount

A tiny command-line tool that counts the number of words in a text file.

## Usage

```bash
python wordcount.py path/to/file.txt
```

This prints the word count to stdout.

## How it works

Words are separated by whitespace (spaces, tabs, newlines). The counting
logic lives in `count_words()` inside `wordcount.py`.

## Running the tests

```bash
pytest
```
