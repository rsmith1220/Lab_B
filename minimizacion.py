def minimizacion():
    import graphviz
    import re
    from pythomata import SimpleDFA


    graph = graphviz.Source.from_file("process.gv")

    #se crea un txt
    with open("process.txt", "w") as f:
        f.write(graph.source)

    #se lee el txt
    with open("process.txt", "r") as f:
        contents = f.read()

    states={'','a0','a1','0'}
    alphabet={'','a'}
    initial_state=""
    accepting_states={}

    transition_function={}


    #transition function from txt
    for line in contents.splitlines():
        if "->" in line:
            source, target = line.split(" -> ")
            print(source )

            source = source.strip().split(' ')[0].strip()
            # states[source]=None

            target = target.strip().split("[")[0].strip()
            # states[target]=None

            print(target)

            label = line[line.find("[") + 1:line.find("]")]
            if label != "":
                label = label.replace("label=", "").strip()
            print(label)

            # alphabet[label]=None

            transition_function[source]={label:target}


        elif "rankdir" in line:
            pass  # Ignore the graph direction specification
        elif "size" in line:
            pass  # Ignore the graph size specification

    dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)
    # dfa_minimized = dfa.minimize()
    graph = dfa.minimize().to_graphviz()
    graph.render("path_to_file")

minimizacion()