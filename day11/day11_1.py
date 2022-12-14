import math

f = open("day11.txt", "r")

class Monkey():
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0
    
    def inspect(self, item):
        self.inspections += 1
        if(self.operation == "*old"):
            self.items[item] *= self.items[item]
        elif(self.operation.startswith("*")):
            self.items[item] *= int(self.operation[1:])
        else:
            self.items[item] += int(self.operation[1:])
        self.items[item] = math.floor(self.items[item] / 3)
        if(self.items[item] / self.test == math.floor(self.items[item] / self.test)):
            return (self.true, self.items.pop(item))
        else:
            return (self.false, self.items.pop(item))

def parse_monkey(raw):
    lines = raw.split("\n")
    items = [int(x) for x in lines[1][18:].split(", ")]
    operation = lines[2][23] + lines[2][25:]
    test = int(lines[3][20:])
    true = int(lines[4][28:])
    false = int(lines[5][29:])
    return Monkey(items, operation, test, true, false)

text = f.read()

raw_monkeys = text.split("\n\n")
monkeys = []
for raw_monkey in raw_monkeys:
    monkeys.append(parse_monkey(raw_monkey))

for i in range(20):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            result = monkey.inspect(0)
            monkeys[result[0]].items.append(result[1])

monkey_inspections = []
for monkey in monkeys:
    monkey_inspections.append(monkey.inspections)
monkey_inspections.sort()
print(monkey_inspections)
print(monkey_inspections[-1] * monkey_inspections[-2])