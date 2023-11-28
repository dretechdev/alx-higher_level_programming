#!/usr/bin/python3
for i in range(97, 123):
    character = chr(i)
    if character not in ('q', 'e'):
        print("{}".format(character), end='')
