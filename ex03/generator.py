from random import random


def generator(text, sep=" ", option=None):
    lst = text.split(sep) if type(text) is str else ['ERROR']
    lst = lst if not option else sorted(lst, key=lambda _: random()) if option == 'shuffle' else sorted(
        lst) if option == 'ordered' else set(lst) if option == 'unique' else ['ERROR']
    for word in lst:
        yield word
