f = open("day1.txt", "r")

greatest = 0
total_sum = 0
for line in f.readlines():
    if(line == "\n"):
        greatest = max(total_sum, greatest)
        total_sum = 0
    else:
        total_sum += int(line)

print(greatest)