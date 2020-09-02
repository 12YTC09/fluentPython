
#-*- coding : utf-8 -*-

"""
Utility functions for normalized Unicode string comparison

1. Using Normal Form C, case sensitive:

2. Using Normal From C with case folding:


"""


from unicodedata import normalize



def nfc_equal(str1,str2):
    return normalize('NFC',str1) == normalize('NFC',str2)

def fold_equal(str1,str2):
    return (normalize('NFC',str1).casefold() == normalize('NFC',str2).casefold())





