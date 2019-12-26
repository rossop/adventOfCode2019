
class NanoFactory():
    def __init__(self):
        with open('day14_input.txt') as f:
            equations = {}
            for line in f:
                line = line.rstrip('\n')
                formula = line.split(' => ')
                print(formula)
                product = formula[1]
                reactant = formula[0]
                splitted_product= product.split(' ')
                prod_amm = splitted_product[0]
                product = splitted_product[1]
                reactant_list = reactant.split(', ')
                reactants = []
                for reactant in reactant_list:
                    reactants.append(tuple(reactant.split(' ')))
                equations[product] = [prod_amm, reactants]
        self.formulas = equations
        self.reactants = dict.fromkeys(equations.keys(),[])
        self.reactants['FUEL'] = 1

    def make(self,stuff, quantity = 1):
        reaction = self.formulas(stuff)
        self.reactants[stuff] -= quantity


    def check_balance(self):
        for product in



# ingridient_list = [(ammount, ingridient)]
# formulas = {product: prod_amm, ingridient_list}

a = NanoFactory()
print(a)
print()