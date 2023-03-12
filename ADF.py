import graphviz
g = graphviz.Digraph('finite_state_machine', filename='process.gv')
g.attr(rankdir='LR', size='8,5')





def AFD(postfix):

    acepta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
    labels = []
    letras =[]

    completo=[]

    jelly = 0
    contar = len(labels)
    ultimo = ''

    for token in postfix:
        labels.append(token)
        completo.append(token)

    

    while contar < 1:
        try:
            token = labels.pop()
        except:
            break

        if token == '*':
            if len(labels)>1:
                extra = labels.pop()
                letras.append(extra)
                if ultimo == '':
                    g.edge('a0','0',extra)
                else:
                    g.edge('a0',ultimo,extra)
            try:
                nombre = labels.pop()
            except:
                nombre=token
            if nombre in acepta:
                g.edge('a0','a1',label=nombre)
                g.edge('a1','a1',label=nombre)
                ultimo = 'a1'
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
                ultimo = 'b2'
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
                ultimo = 'c3'
            elif nombre == '*':
                if len(labels)>1:
                    extra = labels.pop()
                    letras.append(extra)
                    if ultimo == '':
                        g.edge('a0','0',extra)
                    else:
                        g.edge('a0',ultimo,extra)
                try:
                    nombre = labels.pop()
                except:
                    nombre=token
                if nombre in acepta:
                    g.edge('a0','a1',label=nombre)
                    g.edge('a1','a1',label=nombre)
                    ultimo = 'a1'
                else:
                    pass

        elif token == '?':
            try:
                nombre=labels.pop()
            except:
                nombre=token
            if nombre in acepta:
                try:
                    otro=labels.pop()
                    g.edge('d0','d1',label=otro)
                    g.edge('d1','d2',label=nombre)
                    g.edge('d0','d2',label=nombre)
                    ultimo = 'd2'
                except:
                    g.edge('d0','d1', label=nombre)
                    ultimo = 'd1'

        else:
            letras.append(token)

    size=len(letras)
    if size>0:
        while jelly!=size:
            if ultimo == '':
                ultimo = 'e0'
            nombre = letras.pop()
            g.edge(ultimo,str(jelly),label=nombre)
            ultimo = str(jelly)
            jelly+=1

    g.view()


