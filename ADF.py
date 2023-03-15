import graphviz
import minimizacion
g = graphviz.Digraph('finite_state_machine', filename='process.gv')
g.attr(rankdir='LR', size='8,5')





def AFD(postfix):

    acepta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
    labels = []
    letras =[]
    tokens=[]

    completo=[]
    primero=''
    verificar = 0
    

    jelly = 0
    contar = len(labels)
    ultimo = ''

    for token in postfix:
        labels.append(token)
        if token not in acepta:
            tokens.append(token)
        else:
            completo.append(token)
        
    if labels[0] == '*':
        primero = 'a0'
    elif labels[0] == "|":
        primero = 'b0'
    elif labels[0] == '+':
        primero= 'c0'
    elif labels[0] == '?':
        primero = 'd0'

    while contar < 1:
        try:
            token = labels.pop()
            tokens.append(token)
        except:
            break

        if token == '*':
            if len(labels)>=2:
                extra = labels.pop()
                if extra in acepta:
                    letras.append(extra)
                else:
                    pass
                if ultimo == '' and len(token)>0 and extra in acepta:
                    g.edge('a0','0',extra)
                    # pass
                    
                elif extra in acepta:
                    g.edge('a0',ultimo,extra)

                elif extra == '?':
                    nez=labels.pop()
                    g.edge('a0','0',label=labels[1])
                    g.edge('0','1',label=nez)

                else:
                    pass
                    
                try:
                    nombre = labels.pop()
                except:
                    nombre=token
                if nombre in acepta and verificar == 0:
                    try:
                        g.edge('a0','a1',label=nez)
                        g.edge('a1','a1',label=nez)
                        ultimo = 'a1'
                    except:
                        g.edge('a0','a1',label=nombre)
                        g.edge('a1','a1',label=nombre)
                        ultimo = 'a1'

                elif nombre == '|' or extra == '|':
                    try:
                        nombre=labels.pop()
                    except:
                        nombre=token
                
                    if nombre in acepta:
                       otro=labels.pop()
                       if otro in acepta:
                           g.edge('b0','b1',label=otro)
                           g.edge('b0','b2',label=nombre)
                           g.edge('b2','b2',label=nombre)
                           g.edge('b0','0',extra)
                           ultimo = 'b2'
                           break
                elif nombre == '?'or extra == '?':
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
            elif len(labels)==1:
                extra = labels.pop()
                # letras.append(extra)
                g.edge('a0','0',extra)
                g.edge('0','0',extra)
            else:
                pass


        elif token == "|":
            try:
                nombre=labels.pop()
            except:
                nombre=token
            
            if nombre in acepta:
                otro=labels.pop()
                if otro in acepta:
                    g.edge('b0','b1',label=otro)
                    g.edge('b0','b2',label=nombre)
                    ultimo = 'b2'
                elif otro == '*':
                    g.edge('a0','a2',label=nombre)
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

        elif token == "+":
            try:
                nombre = labels.pop()
            except:
                nombre=token

            if nombre in acepta:
                otro=labels.pop()
                if otro in acepta:
                    g.edge('c0','c1',label=otro)
                    g.edge('c1','c2',label=otro)
                    g.edge('c1','c3',label=nombre)
                    g.edge('c2','c2',label=otro)
                    g.edge('c2','c3',label=nombre)
                    ultimo = 'c3'
                elif otro == '*':
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
    print(ultimo)
    minimizacion.minimi(primero,ultimo)

