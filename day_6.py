

import pandas as pd
#part1
#use Copilot(https: // m365.cloud.microsoft /)
#prompt:How can I write an instruction that can split an instruction so that it corresponds to a 0/1 transformation of a point in a coordinate system?
def order_line(line: str):
    line = line.strip()

    if line.startswith("turn on"):
        cmd = "on"
        rest = line[len("turn on "):]
    elif line.startswith("turn off"):
        cmd = "off"
        rest = line[len("turn off "):]
    else:
        cmd = "toggle"
        rest = line[len("toggle "):]

    p1, p2 = rest.split(" through ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))

    return cmd, x1, y1, x2, y2

#use Copilot(https: // m365.cloud.microsoft /)
#prompt:How can I create a 1000x1000 table using 0/1 to represent on and off states,
N = 1000

grid = pd.DataFrame(0, index=range(N), columns=range(N))

def apply_part1(grid, cmd, x1, y1, x2, y2):
    if cmd == "on":
        grid.iloc[y1:y2+1, x1:x2+1] = 1
    elif cmd == "off":
        grid.iloc[y1:y2+1, x1:x2+1] = 0
    else:
        grid.iloc[y1:y2+1, x1:x2+1] = 1 - grid.iloc[y1:y2+1, x1:x2+1]


with open("input/day_06.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        cmd, x1, y1, x2, y2 = order_line(line)
        apply_part1(grid, cmd, x1, y1, x2, y2)

print("light_on:", int(grid.values.sum()))

#part2
#use Copilot(https: // m365.cloud.microsoft /)
#prompt:How to write an if statement to determine the number in the current cell and assign a value to it?

def apply_part2(grid, cmd, x1, y1, x2, y2):
    block = grid.iloc[y1:y2 + 1, x1:x2 + 1]

    if cmd == "on":
        grid.iloc[y1:y2 + 1, x1:x2 + 1] = block + 1
    elif cmd == "toggle":
        grid.iloc[y1:y2 + 1, x1:x2 + 1] = block + 2
    else:
        grid.iloc[y1:y2 + 1, x1:x2 + 1] = (block - 1).clip(lower=0)

#↓this is the original one I wrote,it is too slow to have the result, I use the new one↑.
        # for y in range(y1, y2+1):
        #for x in range(x1, x2+1):
            #bright=grid.iloc[y,x]
           # if cmd=='on':
                #grid.iloc[y,x]=bright+1
           # elif cmd=='toggle':
                #grid.iloc[y,x]=bright+2
            #elif cmd=='off':
                #if bright>0:
                    #grid.iloc[y,x]=bright-1
                #else:
                    #grid.iloc[y,x]=0


N2 = 1000
grid = pd.DataFrame(0, index=range(N2), columns=range(N2))

with open("input/day_06.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
                continue
        cmd, x1, y1, x2, y2 = order_line(line)
        apply_part2(grid, cmd, x1, y1, x2, y2)


print("Brightness:", int(grid.values.sum()))




