from finite_automata import NFA, DFA

filename = input('Enter the name of the NFA file: ')

file = open(filename+'.txt', 'r')
lines = file.readlines()
file.close()


nfa = NFA()   ## the constructor of the classes from the file finite_automata
#
# dfa = DFA(

nfa.construct_nfa_from_file(lines)
print(nfa.transition_functions)
import tester
# nfa.construct_nfa_from_file(lines)
# #print(nfa.transition_functions)  ##nfa becomes the object of the
# dfa.convert_from_nfa(nfa)
print('>>>>>>>>>>>>> ')

#nfa2.print_nfa()
#dfa.print_dfa()
print(tester.trsn_stts(nfa.transition_functions))