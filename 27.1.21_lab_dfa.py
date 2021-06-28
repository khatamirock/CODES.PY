# dfa implement
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol

#declared dfa.............
dfa= DeterministicFiniteAutomaton() #initializes the object......

# declaration of state
state0 = State(0)
state1= State(1)
state2= State(2)
state3= State(3)

#init symbol
symba=Symbol('a')
symbb=Symbol('b')


#adding starting state

dfa.add_start_state(state0)
dfa.add_final_state(state3)

#adding the transitions........................

dfa.add_transition(state0,symba,state1)
dfa.add_transition(state0,symbb,state0)
dfa.add_transition(state1,symba,state2)
dfa.add_transition(state1,symbb,state0)
dfa.add_transition(state2,symba,state0)
dfa.add_transition(state2,symbb,state3)
dfa.add_transition(state3,symba,state3)
dfa.add_transition(state3,symbb,state0)


#checking the string if its accepted or rejected..........

dfa_result1=dfa.accepts([symba,symba,symbb])
dfa_result2=dfa.accepts( [ 'a','b','a','a','b' ] )
dfa_result3=dfa.accepts( [ 'a','b','a','b','a' ] )
print(dfa_result1,dfa_result2,dfa_result3)

import numpy as np

data=np.array([ 'aa','abab','abaab','aaab','abaab' ])

for i in data:
  lst=[]
  for j in i:
    lst.append(j)
  if dfa.accepts(lst):
    print(lst,'lst accepted broah....')
  else:
    print(lst,' nah false.....')
