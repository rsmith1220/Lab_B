def minimi(primero,ultimo):
    import graphviz
    import re
    from pythomata import SimpleDFA
    # from determinar import DFA
    import pydot


    graph = graphviz.Source.from_file("process.gv")

    #se crea un txt
    with open("process.txt", "w") as f:
        f.write(graph.source)

    #se lee el txt
    with open("process.txt", "r") as f:
        contents = f.read()

    states=set()
    alphabet=set()
    accepting_states=set()

    transition_function={}


    #transition function from txt
    for line in contents.splitlines():
        if "->" in line:
            source, target = line.split(" -> ")
            # print(source )

            source = source.strip().split(' ')[0].strip()
            states.add(source)

            target = target.strip().split("[")[0].strip()
            states.add(target)

            # print(target)

            label = line[line.find("[") + 1:line.find("]")]
            if label != "":
                label = label.replace("label=", "").strip()
            # print(label)

            # alphabet[label]=None
            alphabet.add(label)

            transition_function[source]={label:target}

    with open('process.txt', 'r') as file:
        dot_file = file.read()
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
            accepting_states.add(str(last_state))
            break



        elif "rankdir" in line:
            pass  # Ignore the graph direction specification
        elif "size" in line:
            pass  # Ignore the graph size specification

    dfa = SimpleDFA(states, alphabet, str(first_state), accepting_states, transition_function)
    cadena=input("Ingrese cadena para revisar: ")
    # print(states)
    # print(alphabet)
    # print(first_state)
    # print(accepting_states)


    print("La cadena es aceptada (AFD) : ",dfa.accepts(cadena))
    
    graph = dfa.minimize().trim().to_graphviz()
    graph.render("AFD_mini")
    
    # dfa = DFA(states, alphabet, transition_function, 'c0', 'c3')

    """ # Call the run method on an input string
    input_str = 'aab'
    result = dfa.run(input_str)
    print(result) """