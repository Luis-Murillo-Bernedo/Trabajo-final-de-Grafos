diccionario = {"a": 0,
               "b": 1,
               "c": 2,
               "d": 3,
               "e": 4,
               "f": 5,
               "g": 6,
               "h": 7,
               "i": 8,
               "j": 9,
               "k": 10,
               "l": 11,
               "m": 12,
               "n": 13,
               "o": 14,
               "p": 15,
               "q": 16,
               "r": 17,
               "s": 18,
               "t": 19,
               }

matriz_distancias=[]

#Creacion de matriz de distancias entre nodos
for i in range(20):
    fila=[]
    for j in range(20):
        fila.append(500)
    matriz_distancias.append(fila)

for i in range(20):
    for j in range(20):
        if(i==j):
            matriz_distancias[i][j]=0

matriz_distancias[0][1]=45
matriz_distancias[1][2]=70
matriz_distancias[2][4]=50
matriz_distancias[3][1]=48
matriz_distancias[3][4]=47
matriz_distancias[4][2]=50
matriz_distancias[4][5]=150
matriz_distancias[4][8]=46
matriz_distancias[5][9]=40
matriz_distancias[6][0]=95
matriz_distancias[7][3]=49
matriz_distancias[7][6]=48
matriz_distancias[8][4]=46
matriz_distancias[8][7]=75
matriz_distancias[8][10]=54
matriz_distancias[9][5]=40
matriz_distancias[9][8]=144
matriz_distancias[9][11]=37
matriz_distancias[10][8]=54
matriz_distancias[10][11]=148
matriz_distancias[10][12]=47
matriz_distancias[11][9]=37
matriz_distancias[11][13]=51
matriz_distancias[12][10]=47
matriz_distancias[12][14]=148
matriz_distancias[12][15]=50
matriz_distancias[13][11]=51
matriz_distancias[13][12]=162
matriz_distancias[13][16]=52
matriz_distancias[14][17]=55
matriz_distancias[15][12]=50
matriz_distancias[15][14]=158
matriz_distancias[15][18]=51
matriz_distancias[16][13]=52
matriz_distancias[16][15]=152
matriz_distancias[16][19]=30
matriz_distancias[17][18]=205
matriz_distancias[18][15]=51
matriz_distancias[18][19]=174
matriz_distancias[19][16]=30
matriz_distancias[19][18]=174

nodo_inicio=input("Ingrese el punto de partida: ")
nodo_llegada=input("Ingrese el punto objetivo: ")
#Funciones de metodo codicioso
def menor(iteracion):
    n=len(iteracion)
    for j in range(n):
        for i in range(n-1):
            if(iteracion[i]>iteracion[i+1]):
                AUX=iteracion[i]
                iteracion[i]=iteracion[i+1]
                iteracion[i+1]=AUX
    return iteracion[0]

def rutas_minimas(lista1,lista2):
    for i in range(len(lista1)):
        if(lista1[i]<lista2[i]):
            return 1
    return 0

def seleccion(nodoSeleccionado,nodoFinal,eleccion):
    seleccionados=[]
    controlador=0
    indicador=0
    while(nodoSeleccionado!=nodoFinal):
        seleccionados.append(nodoSeleccionado)
        
        evaluacion=[]
        identificadores=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        #Extraccion de datos de la tabla de distancias
        for i in matriz_distancias[diccionario[nodoSeleccionado]]:
            evaluacion.append(i)
        #Eliminar datos de los nodos ya seleccionados
        posiciones=[]
        for i in seleccionados:
            posiciones.append(diccionario[i])
        for posicion in sorted(posiciones,reverse=True):
            del evaluacion[posicion]
            del identificadores[posicion]
        
        #Actualizacion de datos en lista dada imposibilidad de ciertas rutas o existencia de rutas alternas (a partir de la segunda iteracion)
        if(controlador>0):
            for i in range(len(evaluacion)):
                if(evaluacion[i]==500):
                    evaluacion[i]=listaux[i]
                else:
                    evaluacion[i]=evaluacion[i]+indicador
            #Determinacion de las rutas menores posibles en el momento
            condicion=rutas_minimas(evaluacion,listaux)
            if(condicion==0):
                for i in range(len(evaluacion)):
                    evaluacion[i]=listaux[i]
     
        evalaux=[]
        for i in evaluacion:
            evalaux.append(i)
        indicador=menor(evalaux)
        controlador=controlador + 1
        #Determinar nuevo nodo a seleccionar
        k=0
        id=identificadores[0]
        while(evaluacion[k]!=indicador):
            k=k+1
            id=identificadores[k]

        claves=list(diccionario.keys())
        nodoSeleccionado=claves[id]
        
        listaux=[]
        for i in evaluacion:
            if(i!=indicador):
                listaux.append(i)
    if(eleccion==0):
        return seleccionados
    else:
        return indicador



vertices=seleccion(nodo_inicio,nodo_llegada,0)
vertices.append(nodo_llegada)
minimo=seleccion(nodo_inicio,nodo_llegada,1)
#Matriz con nombre de calles
matriz_cuadras=[]
for i in range(20):
    row=[]
    for j in range(20):
        row.append("")
    matriz_cuadras.append(row)

matriz_cuadras[0][1]="Jiron Abancay - Cuadra 2"
matriz_cuadras[1][2]="Jiron Abancay - Cuadra 1"
matriz_cuadras[2][4]="Avenida Cesar Vizcarra - Cuadra 6"
matriz_cuadras[3][1]="Calle Arica - Cuadra 2"
matriz_cuadras[3][4]="Calle Tacna - Cuadra 2"
matriz_cuadras[4][2]="Avenida Cesar Vizcarra - Cuadra 6"
matriz_cuadras[4][5]="Calle Tacna - Cuadra 1"
matriz_cuadras[4][8]="Avenida Cesar Vizcarra - Cuadra 5"
matriz_cuadras[5][9]="Avenida Mineria - Cuadra 6"
matriz_cuadras[6][0]="Jiron Ilo"
matriz_cuadras[7][3]="Calle Arica - Caudra 1"
matriz_cuadras[7][6]="Calle Moquegua - Cuadra 3"
matriz_cuadras[8][4]="Avenida Cesar Vizcarra - Cuadra 5"
matriz_cuadras[8][7]="Calle Moquegua - Cuadra 2"
matriz_cuadras[8][10]="Avenida Cesar Vizcarra - Cuadra 4"
matriz_cuadras[9][5]="Avenida Mineria - Cuadra 6"
matriz_cuadras[9][8]="Calle Moquegua - Cuadra 1"
matriz_cuadras[9][11]="Avenida Mineria - Cuadra 5"
matriz_cuadras[10][8]="Avenida Cesar Vizcarra - Cuadra 4"
matriz_cuadras[10][11]="Calle Ramon Casilla"
matriz_cuadras[10][12]="Avenida Cesar Vizcarra - Cuadra 3"
matriz_cuadras[11][9]="Avenida Mineria - Cuadra 5"
matriz_cuadras[11][13]="Avenida Mineria - Cuadra 4"
matriz_cuadras[12][10]="Avenida Cesar Vizcarra - Cuadra 3"
matriz_cuadras[12][14]="Calle los rosales - Cuadra 2"
matriz_cuadras[12][15]="Avenida Cesar Vizcarra - Cuadra 2"
matriz_cuadras[13][11]="Avenida Mineria - Cuadra 4"
matriz_cuadras[13][12]="Calle los rosales - Cuadra 1"
matriz_cuadras[13][16]="Avenida Mineria - Cuadra 3"
matriz_cuadras[14][17]="Calle los rosales - Cuadra 3"
matriz_cuadras[15][12]="Avenida Cesar Vizcarra - Cuadra 2"
matriz_cuadras[15][14]="Calle Mariategui - Cuadra 2"
matriz_cuadras[15][18]="Avenida Cesar Vizcarra - Cuadra 1"
matriz_cuadras[16][13]="Avenida Mineria - Cuadra 3"
matriz_cuadras[16][15]="Calle Mariategui - Cuadra 1"
matriz_cuadras[16][19]="Avenida Mineria - Cuadra 2"
matriz_cuadras[17][18]="Calle Ignacio Prado"
matriz_cuadras[18][15]="Avenida Cesar Vizcarra - Cuadra 1"
matriz_cuadras[18][19]="Avenida Mineria - Cuadra 1"
matriz_cuadras[19][16]="Avenida Mineria - Cuadra 2"
matriz_cuadras[19][18]="Avenida Mineria - Cuadra 1"

if(nodo_inicio!=nodo_llegada):
    print("Los vertices seleccionados fueron:",vertices)
    print("--------------------------------------------------------------------------") 
    
    print("La distancia de la ruta más corta es:",minimo)
    '''
    ruta=[nodo_llegada]
    min=500
    
    #Determinar ruta en vertices
    i=len(vertices)-1
    while(i>0):
        #Determinar peso de la arista a considerar
        for j in range(20):
            if(matriz_distancias[diccionario[vertices[i-1]]][j]!=500 and j==diccionario[vertices[i]] and matriz_distancias[diccionario[vertices[i-1]]][j]<min):
                min=matriz_distancias[diccionario[vertices[i-1]]][j]
        
        #Seleccionar el vertice para añadir a la ruta
        if(min!=500):
            for k in range(20):
                if(matriz_distancias[diccionario[vertices[i-1]]][k]==min):
                    ruta.insert(0,vertices[k])
        i=i-1
        
    #Mostrar ruta en calles
    print("--------------------------------------------------------------")                        
    print("Las calles que se pasan son (en ese orden):")
    for i in range(len(ruta)-1):
        print(matriz_cuadras[diccionario[ruta[i]]][diccionario[ruta[i+1]]])
    print(ruta)
    '''
    #Mostrar ruta en calles
    print("--------------------------------------------------------------")                        
    print("Las calles que se pasan son (en ese orden):")
    for i in range(len(vertices)-1):
        print(matriz_cuadras[diccionario[vertices[i]]][diccionario[vertices[i+1]]])

else:
    print("Ya se encuentra en el punto al que quiere llegar")
