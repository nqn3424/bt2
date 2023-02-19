from simpleai.search import CspProblem, backtrack

def constraint_func(names, values):
    return values[0] != values[1]
    
if __name__=='__main__':
    names = ('WA', 'NT', 'SA', 'Q', 'NSW','V')

colors = dict((name, ['red', 'green', 'blue']) for name in
names)

constraints = [
(('WA', 'NT'), constraint_func),
(('WA', 'SA'), constraint_func),
(('NT', 'Q'), constraint_func),
(('NT', 'SA'), constraint_func),
(('SA', 'Q'), constraint_func),
(('SA', 'NSW'), constraint_func),
(('SA', 'V'), constraint_func),
(('Q', 'NSW'), constraint_func),
(('NSW', 'V'), constraint_func),
]

problem = CspProblem(names, colors, constraints)
output = backtrack(problem)
print('\nColor map:\n')
for k, v in output.items():
    print(k, '==>', v)
