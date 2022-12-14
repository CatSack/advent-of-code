import ast

f = open("day13.txt", "r")

packets = []
for lines in f.read().split("\n\n"):
    pair = lines.split("\n")
    packets.append((ast.literal_eval(pair[0]), ast.literal_eval(pair[1])))

def dfs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return
    elif isinstance(left, list) and isinstance(right, list):
        for i, j in zip(left, right):
            r = dfs(i, j)
            if r != None:
                return r
        if len(left) < len(right):
            return True
        if len(right) < len(left):
            return False
        else:
            return
    else:
        if isinstance(left, int):
            return dfs([left], right)
        else:
            return dfs(left, [right])

total = 0
for index, packet in enumerate(packets):
    if dfs(packet[0], packet[1]):
        total += index + 1

print(total)