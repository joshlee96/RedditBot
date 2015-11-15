# Open all the text files
def makearray(file):
    with open(file, "r") as opened:
        arrayname = []
        names = []
        programs = []
        emails = []
        while arrayname != None:
            arrayname = opened.read().splitlines()
            for x in arrayname:
                i = 0
                arrayname = x.split('|')

                while i < 3:
                    if arrayname[i] == None:
                        break
                    elif i == 0:
                        names.append(arrayname[0])
                    elif i == 1:
                        programs.append(arrayname[1])
                    elif i == 2:
                        arrayname[2] = arrayname[2].rsplit('\n', 3)
                        emails.append(arrayname[2])
                    i = i + 1
                i = 0

            for eachline in names:
                print(eachline)
            for eachline in programs:
                print(eachline)
            a = 0
            while a < len(emails):
                print(emails[a])
                a = a + 1

sci = makearray("science.txt")
