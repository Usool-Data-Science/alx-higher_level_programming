#!/usr/bin/python3
def islower(var):
    lower = "abcdefghijklmnopqrstuvwxyz"
    try:
        if var in lower:
            return True
    except Exception as e:
        print("{}".format(e))
    else:
        return False
