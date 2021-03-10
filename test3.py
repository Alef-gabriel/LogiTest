from  math import sqrt
alfabet = ['k','b','w','r','q','d','n','f','x',
           'j','m','l','v','h','t','c','g','z','p','s']


textB = open('./klingon-textoA.txt')

l = []
lyricsList = list()

for line in textB:
    for lyric in line:
        if lyric != " " and lyric != "\n":
            lyricsList.append(lyric)
        else:
            phrase = "".join(lyricsList)
            l.append(phrase)
            del lyricsList[:]
