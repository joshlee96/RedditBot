# Open all the text files
def makearray(file):
    with open(file, "r") as opened:
        arrayname = []
        names = []
        programs = []
        emails = []
        arrayname = opened.read().splitlines()
        for x in arrayname:
            i = 0
            arrayname = x.split('|')

            while i < 3:
                if arrayname[i] == None:
                    break
                elif i == 0:
                    names.append(arrayname[1])
                elif i == 1:
                    programs.append(arrayname[0])
                elif i == 2:
                    emails.append(arrayname[2])
                i = i + 1
            i = 0

        return (names, programs,emails)





def printgraph(n, p, e):
    i = 0
    thestring = "Program|Name|Email\n:--|:--|:--\n"
    for eachvalue in e:
        thestring = thestring + p[i] + "|" + n[i] + "|" + e[i] + "@uwaterloo.ca\n"
        i = i + 1

    return thestring

