textB = open('./klingon-textoB.txt')
contPreposition = 0
lyricsList = list()
foo = ["s", "l", "f", "w" , "k"]
for line in textB:
    for lyric in line:
        if lyric != " " and lyric != "\n":
            lyricsList.append(lyric)
        else:
            if len(lyricsList) == 3 and "d" not in lyricsList and lyricsList[-1] not in foo:
                contPreposition += 1
            del lyricsList[:]       
print(contPreposition)