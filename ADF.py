import graphviz
g = graphviz.Digraph('finite_state_machine', filename='process.gv')
g.attr(rankdir='LR', size='8,5')





def AFD(postfix):

    acepta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
    labels = []
    contar = len(labels)

    for token in postfix:
        labels.append(token)

    while contar < 1:
        try:
            token = labels.pop()
        except:
            break

        if token == '*':
            try:
                nombre = labels.pop()
            except:
                nombre=token
            if nombre in acepta:
                g.edge('a0','a1',label=nombre)
                g.edge('a1','a1',label=nombre)
            else:
                pass
        elif token == "|":
            try:
                nombre=labels.pop()
            except:
                nombre=token
            
            if nombre in acepta:
                g.edge('b0','b1',label=labels.pop())
                g.edge('b0','b2',label=nombre)
            else:
                pass

        elif token == "+":
            try:
                nombre = labels.pop()
            except:
                nombre=token

            if nombre in acepta:
                otro=labels.pop()
                g.edge('c0','c1',label=otro)
                g.edge('c1','c2',label=otro)
                g.edge('c1','c3',label=nombre)
                g.edge('c2','c2',label=otro)
                g.edge('c2','c3',label=nombre)

        elif token == '?':
            try:
                nombre=labels.pop()
            except:
                nombre=token
            if nombre in acepta:
                otro=labels.pop()
                g.edge('d0','d1',label=otro)
                g.edge('d1','d2',label=nombre)
                g.edge('d0','d2',label=nombre)

    g.view()