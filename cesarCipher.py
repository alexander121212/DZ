# -*- coding: utf-8 -*-

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

plaintext = "IamOK"


def cesarEncryption(plainText, alph, key=3):
    cipherText = ""
    for symbol in plainText:
        if symbol in alph:
            if alph.index(symbol)+ int(key) <= len(alph):
                cipherText+=alph[alph.index(symbol) + int(key)-1]
            else:
                cipherText+=alph[(alph.index(symbol)+ int(key)) - len(alph)-1]


    return (cipherText)

def cesarDecryption(cipherText, alph, key=3):
    plainText = ""
    for symbol in cipherText:
        if symbol in alph:
            if alph.index(symbol)- int(key) >= 0:
                plainText+=alph[alph.index(symbol) - int(key)+1]
            else:
                plainText+=alph[len(alph) - (int(key) - alph.index(symbol))+1]


    return (plainText)

