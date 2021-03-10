
textB = open('./klingon-textoB.txt')
alfabet = ['k','b','w','r','q','d','n','f','x',
           'j','m','l','v','h','t','c','g','z','p','s']

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

t = len(alfabet)
g = []
for x in range(t):
	g.append([])

cont = 0
co = 0
for x in alfabet:
    for i in l:
        if i != "":
            if i[0] == x:
                
                g[cont].append(i)
            else:
                pass
    cont += 1
del l                                             
print(g)

