with open('input/day_03.txt', 'r') as f:
    text = f.read()
    s=text.strip()
    #part1
    x=0
    y=0
    visit=set()
    visit.add((x,y))

    for i in s:
        if i=='^':
            y=y+1
        elif i=='v':
            y=y-1
        elif i=='>':
            x=x+1
        elif i=='<':
            x=x-1
        visit.add((x,y))
        number=len(visit)
    print(number)

#part2
santa=s[::2]
robo=s[1::2]
sx=0
sy=0
rx=0
ry=0
santa_visit=set()
robo_visit=set()
santa_visit.add((0,0))
robo_visit.add((0,0))

for i in santa:
    if i == '^':
        sy = sy + 1
    elif i == 'v':
        sy = sy - 1
    elif i == '>':
        sx = sx + 1
    elif i == '<':
        sx = sx - 1
    santa_visit.add((sx, sy))
for a in robo:
    if a == '^':
        ry = ry + 1
    elif a == 'v':
        ry = ry - 1
    elif a == '>':
        rx = rx + 1
    elif a == '<':
        rx = rx - 1
    robo_visit.add((rx, ry))

new_visit = santa_visit|robo_visit
newnumber = len(new_visit)

print(newnumber)
#use Copilot(https://m365.cloud.microsoft/)
#prompt：
# 1.can you inspire me on how to understand the question in digital way?
# 2.what is the difference between set& dictionary?
# 3.how to deduplicate?
# 4.What is the code to retrieve a number every other digit?
# 5.how to merge the two sets together
# 6.why the code isn't working?
#I try to shorten but my brain is not that enough to make it smooth:(