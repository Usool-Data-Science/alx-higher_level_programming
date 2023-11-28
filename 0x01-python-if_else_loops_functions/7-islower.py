#!/usr/bin/python3
def islower(var):
    lower = "abcdefghijklmnopqrstuvwxyz"
    if not var:
        raise ValueError()
    if var in lower:
        return True
    else:
        return False
