from automata.base.automaton import Automaton
from automata.fa.fa import FA
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
#####    the transition states ............

### the NFA class from automata library..........................
nfa = NFA(
    states={'a', 'b', 'c','d','e'},
    input_symbols={'1', '0'},
    transitions={

        ### the transition as prescribed on sheet..........
        'a': {'0': {'a'},'1':{'a','b'}},
        'b': {'0': {'c','e'}, '1': {'c'}},
        'c': {'1': {'d'}},
        'd':{},
        'e':{'1':{'d'}}
    },

    initial_state='a',
    final_states={'c','d'}

)
str = input('give and input valid_only{0,1}')



print('converted>>>>>>>>')

#### check if the NFA accepts::::::::::::::
dfa2 = DFA.from_nfa(nfa)
if nfa.accepts_input(str):
    print('NFA accepted')
else:
    print('NFA rejected')

if dfa2.accepts_input(str):
    print('DFA accepted')
else:
    print('DFA rejected')

## the converted DFA from the NFA .... printin the usable properties...

print('initial stated :' )
print( dfa2.initial_state)
print('final states : ')
print(dfa2.final_states)
print('the transitions : ')
print(dfa2.transitions)

