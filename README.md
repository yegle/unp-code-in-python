unp-code-in-python
==================

Unix Network Programming code in Python3

## Why

Python is more expressive than C

## Why Python3

Why python2?

Besides, most codes should be able to run under Python 2.6 or 2.7 (maybe
needs some import from `__future__`)

## I found a bug

Please send a pull request to me. Note: make sure your commits have
detailed commit message

## How to run the code?

1. `pip install -e
   git+https://github.com/yegle/unp-code-in-python.git#egg=unp`
2. In the UNP book, you'll find the text under example code, something
   like `intro/daytimetcpcli.c`
3. Run the corresponding code using `unp run intro/daytimetcpcli`.
4. If you need to run code with arguments, add the argument at the end.
   e.g. `unp run intro/daytimetcpcli 127.0.0.1`
