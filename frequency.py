# -*- coding: utf-8 -*-
import cesarCipher, math
try:
    f = open('text', 'r')
except IOError:  print ("No file")



table = []

s = f.read()
def tableFiller(table, string):
    for symbol in string:
        if  symbol.lower() not in table and symbol.lower() != ' ':
            table.append(symbol.lower())
            table.append(1)
        elif symbol.lower() in table:
            table[table.index(symbol.lower())+1] +=1

tableFiller(table, s)
crypt = cesarCipher.cesarEncryption(s, "abcdefghijklmnopqrstuvwxyz", 3)
tableCipher = []
tableFiller(tableCipher,crypt)

all_symb = 0
for i in xrange(len(tableCipher)):
    if i % 2 != 0:
        all_symb+=tableCipher[i]


for i in xrange(len(tableCipher)):
    if i % 2 != 0:
        tableCipher[i] = "%0.9f" % (float(tableCipher[i]) / float(all_symb))


def frecRecover(encText, tableForRec):
    frecTable = ['e', 0.127, 	't',0.0906,	'a',0.0817,	'o',0.0751,	'i',0.0697,	'n',0.0675,	's',0.0633,	'h',0.0609,
             'r',0.0599,	'd',0.0425,	'l',0.0403,	'c',0.0278,	'u',0.0276,	'm',0.0241,	'w',0.0236,	'f',0.0223,	'g',0.0202,
             'y',0.0197,	'p',0.0193,	'b',0.0149,	'v',0.0098,	'k',0.0077,	'x',0.0015,	'j',0.0015,	'q',0.001,		'z',0.0005]
    currTable = []
    plainText = ""
    for j in xrange(len(tableForRec)):
        if j % 2 != 0:
            min = 1000
            curr=0
            for i in xrange(len(frecTable)):
                if i % 2 != 0:
                    if abs(float(tableForRec[j]) - float(frecTable[i])) < min:
                        curr = frecTable[i-1]
                        min = abs(float(tableForRec[j]) - float(frecTable[i]))
            currTable.append(tableForRec[j-1])
            currTable.append(curr)

    for some_sim in encText:
        plainText+=currTable[currTable.index(some_sim)+1]

    return plainText




print(frecRecover(crypt, tableCipher))

f.close()
