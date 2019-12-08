from day05.day05 import IntCode as IntCode
from itertools import permutations
with open('day07_input.txt') as f:
    memory = list(map(int, f.read().rstrip('\n').split(",")))
ic = False

def amplifier(memory,inputs):
    ic = IntCode(memory)
    print(inputs)
    val = inputs.pop()
    print(val)

    if val:
        ic.i = val
        ic.compute()
        amplifier(ic.mem, inputs)

    else:
        return ic.out

results = []
inputs = []
for lst in permutations(range(5), 5):
    lst = list(lst)
    lst.append(False)
    inputs.append(lst)
    lst.reverse()
    results.append(amplifier(memory, lst))

print(results)
maximum_output = max(results)
pos = results.index(maximum_output)
print(inputs[pos])
print(maximum_output)