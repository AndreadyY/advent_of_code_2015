from math import floor

with open('input/day_01.txt', 'r') as f:
    text = f.read()
  #part1
    up = text.count('(')
    down = text.count(')')
    pos=up-down
    print('position=',pos)

  #part2
    s = text.strip()
    floor=0
    for i, ch in enumerate(s,start=1):
        if ch=='(':
            floor=floor+1
        elif ch==')':
            floor=floor-1

        if floor==-1:
            print('stop:',i)
            break
#use Copilot(https://m365.cloud.microsoft/).
#prompt:
# 1.A method to replace elements in a string with numbers and filter out positions where the result of an expression is -1.
# 2.Why isn't this code working?