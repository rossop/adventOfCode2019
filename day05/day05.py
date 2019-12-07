import urllib


class IntCode():
    # Updated to a class after reading @datagubbe.se Solution. Opted for class after problem 7 asked to reuse intcode
    def __init__(self, mem=None):
        if not mem:
            self.read_input()
        else:
            self.mem = mem

        self.ptr = 0  # pointer value
        self.ops = {
            # opcode: [ func, default param mode]
            # param modes are matched to self.fetchers
            1: [self.op_add, [0, 0, 1]],  # day03
            2: [self.op_mul, [0, 0, 1]],  # day03
            3: [self.op_input, [1]],
            4: [self.op_output, [0]],
            5: [self.op_jump_if_true, [0, 0]],
            6: [self.op_jump_if_false, [0, 0]],
            7: [self.op_lt, [0, 0, 1]],
            8: [self.op_eq, [0, 0, 1]],
            99: [self.op_halt, []]
        }
        self.fetchers = [
            self.position_fetch,
            self.immediate_fetch
        ]

    def read_input(self):
        """
        Read input from a text file
        :return: :insList: list of instructions
        """
        with open('day05_input.txt') as f:
            self.mem = list(map(int, f.read().rstrip('\n').split(",")))

    def position_fetch(self, addr):
        """
        fetch param value from address (position mode)
        :param addr:
        :return: updates memory
        """
        return self.mem[addr]

    def immediate_fetch(self, val):
        """
        passthrough of immediate param value
        :param val:
        :return: integer of fetched value
        """
        return int(val)

    def inc(self, i=1):
        """
        Increases Pointer
        :param i: Value to increse pointer by
        :return: None
        """
        self.ptr += i
        return None

    def op_add(self, params):
        val1, val2, res_addr = params
        self.mem[res_addr] = val1 + val2
        self.inc()
        return True

    def op_mul(self, params):
        val1, val2, res_addr = params
        self.mem[res_addr] = val1 * val2
        self.inc()
        return True

    def op_input(self, params):
        dest_addr = params.pop()
        i = 1  # input("IntCode input> ")
        self.mem[dest_addr] = i
        self.inc()
        return True

    def op_output(self, params):
        out = params.pop()
        print("   " + str(out))
        self.inc()
        return True

    def op_jump_if_true(self, params):
        comp, addr = params
        if comp:
            self.ptr = addr
        else:
            self.inc()
        return True

    def op_jump_if_false(self, params):
        comp, addr = params
        if not comp:
            self.ptr = addr
        else:
            self.inc()
        return True

    def op_lt(self, params):
        v1, v2, addr = params
        self.mem[addr] = int(v1 < v2)
        self.inc()
        return True

    def op_eq(self, params):
        v1, v2, addr = params
        self.mem[addr] = int(v1 == v2)
        self.inc()
        return True


    def op_halt(self, empty_params):
        return False

    def compute(self):
        instr = str(self.mem[self.ptr])
        instr_param_modes = []

        if len(instr) > 2:
            op = int(instr[-2:])
            instr_param_modes = [int(c) for c in instr[:-2]]
            instr_param_modes.reverse()
        else:
            op = int(instr)

        # Fetch operation and param modes
        op_fun, def_param_modes = self.ops[op]
        param_modes = def_param_modes[:]  # copy list

        for i in range(0, len(instr_param_modes)):
            # replace instruction parameter modes over default ones
            param_modes[i] = instr_param_modes[i]

        params = []
        for i in range(0, len(def_param_modes)):
            raw = self.mem[self.ptr + 1]  # add 1 to account for current op
            pm = param_modes[i]
            # fetch param with desired method and populate param list
            params.append(self.fetchers[pm](raw))  # TODO ??
            self.inc()   # increases the pointer for each param

        print(params)
        res = op_fun(params)  # op_fun will set pointer as desired

        if res:
            self.compute()
        else:
            print("___Intcode Halted ___")


def download_input():
    """
    TODO: upgrade so that now on you don't need to dowload imputs, and make it a general file you can run from every
        problem
    :return: input as list
    """
    link = "https://adventofcode.com/2019/day/5/input"
    with urllib.request.urlopen(link) as f:
        input = f.read()
        print(input)


ic = IntCode()
ic.compute()
print(ic.mem)

