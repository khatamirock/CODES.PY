from pyformlang.finite_automaton import NondeterministicFiniteAutomaton ,Symbol, State
#declare NFA object

nfa= NondeterministicFiniteAutomaton()

# step-1 : declare states
state0=State(0)
state1=State(1)
state2=State(2)
state3=State(3)
state4=State(4)

##########    stepII: declare Symbolsh....
sym_a=Symbol('a')
sym_b=Symbol('b')
sym_c=Symbol('c')
sym_d=Symbol('d')

# step -III : add start and end state
nfa.add_start_state(state0)
  #final state as it have got 2 final state..................
nfa.add_final_state(state3)
nfa.add_final_state(state4)

## adding all the transition state
nfa.add_transition(state0,sym_a,state1)
nfa.add_transition(state1, sym_b,state1)

nfa.add_transition(state1, sym_c,state2)

nfa.add_transition(state1, sym_b,state4)
nfa.add_transition(state1, sym_c,state4)
nfa.add_transition(state1, sym_d,state3)


# now start checking..........
flag= nfa.is_deterministic()
if flag==True:
  print('Deterministic bro....')
else:
  print('False!! dude.....!! !')

import numpy as np
string =  np.array( ['abd','abbc','abbb','ab','abbd',  'abcd','aba','acd','abc'  ]
                   )

for s in string:
  lst=[]
  if nfa.accepts(s):
    print(s,'is accepted')
  else:
    print(s,'is false')

