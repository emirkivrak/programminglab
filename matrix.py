## summing two matrix

def matrixsum(m1,m2):
        finalmatrix=[]
        for i in range(len(m1)):
            finalmatrix.append([])
                for j in range(len(m1[])):
                    finalmatrix[i].append(m1[i][j]+m2[i][j])
        return finalmatrix

###########################################

## substracting two matrix

def matrixsub(m1,m2):
        finalmatrix=[]
        for i in range(len(m1)):
            finalmatrix.append([])
            for j in range(len(m1[])):
                finalmatrix[i].append(m1[i][j]-m2[i][j])
        return finalmatrix

##########################################

## finding scalar product

def scalarproduct(x,m1):
    finalmatrix=[]
    for i in range(len(m1)):
        finalmatrix.append([])
        for j in range(len(m1[])):
            finalmatrix[i].append(m1[i][j]*x)
    return result

###########################################

## finding inner product

def vertorinnerproduct(v,w):
    size = len(v)
    finalmatrix=[]
    for i in range(size):
        finalmatrix.append(0)
    for i in range(size):
        finalmatrix[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+finalmatrix[i]
    return t

#############################################

## eksikler --- matrix çarpımı ---

    
