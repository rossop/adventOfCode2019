from day05.day05 import IntCode as IntCode
from itertools import permutations
with open('day07_input.txt') as f:
    memory = list(map(int, f.read().rstrip('\n').split(",")))

class AmpIntCode(IntCode):
    def __init__(self, mem, inputs):
        IntCode.__init__(mem)
        self.inputs = inputs

    def ampTest(self):
        if self.inputs:
            val = self.inputs.pop(0)
            super().compute()




def amplifier_test(memory,inputs):
    ic = IntCode(memory)
    print(inputs)
    val = inputs.pop()
    print(val)

    if val:
        ic.i = val
        ic.compute()
        amplifier_test(ic.mem, inputs)

    else:
        return ic.out

results = []
inputs = []
for lst in permutations(range(5), 5):
    lst = list(lst)
    lst.append(False)
    inputs.append(lst)
    lst.reverse()
    results.append(amplifier_test(memory, lst))

print(results)
maximum_output = max(results)
pos = results.index(maximum_output)
print(inputs[pos])
print(maximum_output)