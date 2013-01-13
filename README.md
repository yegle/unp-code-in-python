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
3. Run the corresponding code using `unp run intro/daytimetcpcli.py`.
4. If you need to run code with arguments, add the argument at the end.
   e.g. `unp run intro/daytimetcpcli.py 127.0.0.1`

## `unp` command usage

This is a small wrapper command for running/editing the Python code provided.

To use the `unp` command, you need to specify the action you want and
the target of the action.

Some simple examples of using the command:

1. Running code: `unp run intro/byteorder.py`
    * Running with arguments: `unp run intro/daytimetcpcli.py 127.0.0.1`
2. Show which script is executed: `unp show intro/byteorder.py`
3. Editing the script: `unp edit intro/byteorder.py`
    * It's recommended to install this package in some virtual
      environment, so editing scripts doesn't need root permission.
4. Listing scripts using wildcard or directory name (not yet
   implemented): `unp ls intro/`

## How to run without the `unp` command?

Actually it's hard to run without organizing the code into a package.
But it's possible to run the code without the `unp` command. Here's a
simple example code:

    import sys

    if __name__ == '__main__':
        from unp.intro import byteorder
        byteorder.main(sys.argv[0], sys.argv[1:])

If you really want to run the code somewhere else, you need to take care
of the somewhat complex imports in the code.
