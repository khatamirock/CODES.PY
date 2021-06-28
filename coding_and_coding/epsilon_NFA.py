from automata.base.automaton import Automaton
from automata.fa.fa import FA
from automata.fa.nfa import NFA



lst={'b':{'b','e'},'c':{'d'},'d':{'d'}}

trss={}
##  making the transition states for 0-9 automation..........
for y in lst:
    xx={}
    xx={str(x):lst[y]  for x in range(10)}
    ###print(xx)
    trss[y] = xx

###  print(trss)
### created from the automation loop above..................
tr={'a': {'': {'b'}},
'b': {'':{'c'},'0': {'b', 'e'}, '1': {'b', 'e'}, '2': {'b', 'e'}, '3': {'b', 'e'}, '4': {'b', 'e'}, '5': {'b', 'e'}, '6': {'b', 'e'}, '7': {'b', 'e'}, '8': {'b', 'e'}, '9': {'b', 'e'}},
'c': {'':{'d'},'0': {'d'}, '1': {'d'}, '2': {'d'}, '3': {'d'}, '4': {'d'}, '5': {'d'}, '6': {'d'}, '7': {'d'}, '8': {'d'}, '9': {'d'}},
'd': {'':{'f'},'0': {'d'}, '1': {'d'}, '2': {'d'}, '3': {'d'}, '4': {'d'}, '5': {'d'}, '6': {'d'}, '7': {'d'}, '8': {'d'}, '9': {'d'}},
'e':{'':{'d'}},
'f':{}

}


nfa = NFA(
    states={'a', 'b', 'c','d','e','f'},
    input_symbols={'0','1','2','3','4','5','6','7','8','9'},
    transitions=tr,
    initial_state='a',
    final_states={'f'}

)
str = '1'
str=input('give a valid ibput(0-9)\n')

if nfa.accepts_input(str):
    print('accepted')
else:
    print('rejected')