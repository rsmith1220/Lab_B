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

    alphabet={'a0','a1','b0','b1','b2','c0','c1','c2','c3','d0','d1','d2','e0','0'}
    initial_state=None
    accepting_states=None

    transition_function={}


    #transition function from txt
    for line in contents.splitlines():
        if "->" in line:
            source, target = line.split(" -> ")
            print(source )
            
            target = target.strip().split("[")[0].strip()

            print(target)

            label = line[line.find("[") + 1:line.find("]")]
            if label != "":
                label = label.replace("label=", "").strip()
            print(label)

            transition_function[source]={label:target}


        elif "rankdir" in line:
            pass  # Ignore the graph direction specification
        elif "size" in line:
            pass  # Ignore the graph size specification

    print (transition_function)


minimizacion()