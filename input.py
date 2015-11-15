import re
def makearray(file):
    with open(file, "r") as opened:
        array = opened.read().rsplit("|",3)
        return array

math = makearray("MathAdvisors.txt")
advisors = re.split(r'\n{1,}', math)
#advisors= [ re.sub(r'\n', ' ', advisor) for advisor in advisors ]
#advisors = [ re.split(r',', advisor, maxsplit=2) for advisor in advisors]

for advisor in advisors:
    print(advisor)