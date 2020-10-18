def grilleCardan(m,k):
    grilleCardan=[
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    ]
    '''[1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]'''
    return grilleCardan
def normalizeOpenTextByGrilleCardanSize(textOpen):
    List=[]
    a=grilleCardan(1,2)
    countOneInGrille=(len(a)//2)*len(a[0][:])//2
    if(len(textOpen)%countOneInGrille!=0):
        for i in range(len(openText)-1,len(openText)+len(openText)%countOneInGrille,1):
            textOpen+="#"
    for i in range(0,len(openText),countOneInGrille):
        List.append(openText[i:i+countOneInGrille])
    return List
def turnCardan(x,size):
    y=[[0 for i in range(size)] for j in range(len(x))]
    k=0
    for i in range(len(x)-1,-1,-1):
        for j in range(size):
            y[k][j]=x[i][j]
        k+=1
    return y
def Cardan(textOpen):
    grille=grilleCardan(1,1)
    size=len(grilleCardan(1,1))
    matrix=normalizeOpenTextByGrilleCardanSize(openText)
    mylist=grille
    textCipher=""
    print(matrix)
    p=0
    count=0
    M=[]
    print(len(grille),len(grille[0][:]))
    for k in range(4):
        p=0
        for i in range(len(grille)):
            for j in range(len(grille[i][:])):
                if grille[i][j]==1:
                    textCipher=matrix[k][p]
                    mylist[i][j]=matrix[k][p]
                    #print(p,mylist)
                    count+=1
                    p+=1
    
    grille=grilleCardan(1,1)
    grille=turnCardan(grille,10)
    #print(count)
    print(textCipher)
    return mylist
openText="шифррешеткаявляетсячастнымслучаемшифрамаршрутнойперестановки"
#print(generateMatrix(openText))
#permEncrypt=permutationEncryption(openText)
#print("Cipher text",permEncrypt[0])
#print("Decoded Text",decodePermutationEncrypt(permEncrypt[0],permEncrypt[2])[1])

print(Cardan(openText))    