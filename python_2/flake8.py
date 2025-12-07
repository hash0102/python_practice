# noqaを指定しないため、flake8でエラー
noqa_sample = lambda x: 2 + x

# noqaを指定しているためエラーにならない
noqa_sample = lambda x: 2 + x  # noqa: E731
