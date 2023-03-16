import re
import pydot

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def is_valid_input(self, input_str):
        for char in input_str:
            if char not in self.alphabet:
                return False
        return True

    def is_accept_state(self, state):
        return state in self.accept_states

    def run(self, input_str):
        if not self.is_valid_input(input_str):
            return False

        current_state = self.start_state
        for char in input_str:
            current_state = self.transitions.get((current_state, char))
            if current_state is None:
                return False

        return self.is_accept_state(current_state)


# Read the DFA definition from a DOT file
with open('NFA', 'r') as f:
    dot_file = f.read()



graph = pydot.graph_from_dot_data(dot_file)[0]

# Get the first state
first_state = None
for edge in graph.get_edges():
    source = edge.get_source()
    target = edge.get_destination()
    if not any(e for e in graph.get_edges() if e.get_destination() == source):
        first_state = source
        break

# Get the last state
last_state = None
for edge in graph.get_edges():
    source = edge.get_source()
    target = edge.get_destination()
    if not any(e for e in graph.get_edges() if e.get_source() == target):
        last_state = target
        break



# Extract the DFA parameters from the DOT file
pattern = r'(?<=\[\slabel=\")(.*?)(?=\")|(?<=->\s)(.*?)(?=\s\[label=)(.*?)(?=\])'
matches = re.findall(pattern, dot_file)
states = set()
alphabet = set()
transitions = {}
start_state = None
accept_states = set()

for line in dot_file.splitlines():
        if "->" in line:
            source, target = line.split(" -> ")
            # print(source )

            source = source.strip().split(' ')[0].strip()
            states.add(source)

            target = target.strip().split("[")[0].strip()
            states.add(target)

for match in matches:
    if match[0] != '':
        states.add(match[0])
    if match[1] != '' and match[2] != '':
        state_from, state_to, char = match
        # states.add(state_from)
        # states.add(state_to)
        alphabet.add(char)
        transitions[(state_from, char)] = state_to
    elif match[1] != '':
        start_state = match[1]
    elif match[2] != '':
        accept_states.add(match[1])

# Create an instance of the DFA class
dfa = DFA(states, alphabet, transitions, first_state, last_state)

print(transitions)

# Call the run method on an input string
input_str = 'b'
result = dfa.run(input_str)
print(result)
