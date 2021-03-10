textB = open('./klingon-textoB.txt')
contPreposition,contVerb,contFirstPersonVerb = 0,0,0
lyricsList = list()
foo = ["s", "l", "f", "w" , "k"]
for line in textB:
    for lyric in line:
        if lyric != " " and lyric != "\n":
            lyricsList.append(lyric)
        else:
            if len(lyricsList) >= 8 and lyricsList[-1] in foo:
                contVerb += 1
                if lyricsList[0] not in foo:
                    contFirstPersonVerb += 1 
            if len(lyricsList) == 3 and "d" not in lyricsList and lyricsList[-1] not in foo:
                contPreposition += 1
            del lyricsList[:]       
print(f"Number of prepositions: {contPreposition}")
print(f"Number of verbs: {contVerb}")
print(f"Number of first person verb: {contFirstPersonVerb}")