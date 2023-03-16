from pyformlang.finite_automaton import EpsilonNfa, Nfa, NfaToDfa, Symbol

# Create an epsilon NFA
epsilon_nfa = EpsilonNfa()

epsilon_nfa.add_start_state(0)
epsilon_nfa.add_final_state(3)

epsilon_nfa.add_transition(0, 'ε', 1)
epsilon_nfa.add_transition(0, 'ε', 7)
epsilon_nfa.add_transition(1, Symbol('a'), 2)
epsilon_nfa.add_transition(2, Symbol('b'), 3)
epsilon_nfa.add_transition(7, Symbol('a'), 8)
epsilon_nfa.add_transition(8, Symbol('b'), 3)

# Convert epsilon NFA to NFA
nfa = Nfa.from_epsilon_nfa(epsilon_nfa)

# Convert NFA to DFA
nfa_to_dfa_converter = NfaToDfa()
dfa = nfa_to_dfa_converter.convert(nfa)

# Print the resulting DFA
print(dfa)
