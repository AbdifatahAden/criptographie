def normalizeOpenTextByGrilleCardanSize(textOpen):
    List=[]
    if(len(textOpen)%10!=0):
        for i in range(len(openText)-1,len(openText)+len(openText)%10,1):
            textOpen+="#"
    for i in range(0,len(openText),10):
        List.append(openText[i:i+10])
    return List

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
    print(matrix,size)
    print(grille)
    print(turnCardan(grille,10))
    textCipher=""
    mytest=[[0 for i in range(len(matrix[0][:]))] for j in range(len(grille))]
    #while len(textCipher)!=len(textOpen):
    for i in range(len(grille)):
        p=0
        grille=turnCardan(grille,10)
        mytest=turnCardan(mytest,10)
        for j in range(len(grille)):
            if grille[i][j]==1:
                textCipher+=matrix[i][:]
                mytest[p][:]=textCipher
                p+=1
                '''for k in range(len(matrix[i][:])):
                    textCipher+=matrix[i][k]'''
                textCipher=" "
            
    print(textCipher)
    return mytest
openText="шифррешеткаявляетсячастнымслучаемшифрамаршрутнойперестановки"
#print(generateMatrix(openText))
#permEncrypt=permutationEncryption(openText)
#print("Cipher text",permEncrypt[0])
#print("Decoded Text",decodePermutationEncrypt(permEncrypt[0],permEncrypt[2])[1])

print(Cardan(openText))