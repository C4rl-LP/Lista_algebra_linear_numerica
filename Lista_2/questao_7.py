# definindo funções úteis 

def norm_l2(x):
    sum = 0
    for i in x:
        sum += i**2
    return sum**(1/2)

def subtracao(x, y):
    result  = [0]*len(x)
    for i in range(len(x)):
        result[i] += x[i] - y[i]
    return result

def inerproduct(x,y):
    result = 0
    for i in range(len(x)):
        result += x[i]*y[i]
    return result

def escalarproduct(alpha, x):
    result = [0]*len(x)
    for i in range(len(x)):
        result[i] = x[i]*alpha
    return result

def ext_product(v:list) -> list:
    n = len(v)

    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            M[i][j] = v[i] * v[j]

    return M

def extend_matrix(M:list, k:int) -> list:
    M = [row[:] for row in M]
    rest = k - len(M)
    for row in M:
        for _ in range(rest):
            row.insert(0,0)
    
    new_rows = []
    for j in range(rest):
        new_row = [0]*k
        new_row[j] = 1
        new_rows.append(new_row)

    matrix = new_rows + M
    return matrix



def transpose(A):
    m = len(A)
    n = len(A[0])

    T = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]

    return T


def matrix_product(A, B):
    m = len(A)
    p = len(B)
    n = len(B[0])

    C = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            s = 0
            for k in range(p):
                s += A[i][k] * B[k][j]

            C[i][j] = s

    return C

def sinal(x):
    if x[0] >= 0:
        return 1
    return -1
def matrix_sub(A, B):
    m = len(A)
    n = len(A[0])

    C = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]

    return C 

def Matrix_mult(k, M):
    matrix = [[0 for _ in range(len(M))] for _ in range(len(M[0])) ]
    for i in range(len(M)):
        for j in range(len(M[0])):
            matrix[i][j] = k*M[i][j]
    return matrix

def eye(n):
    matrix = [[0 for _ in range(n)] for _ in range(n) ]
    for i in range(len(matrix)):
        matrix[i][i] = 1

    return matrix

def house(A):
    R = A.copy()

    m = len(A)
    n = len(A[0])
    w =[]

    for i in range(len(A[0])-1):
        x = [R[j][i] for j in range(i, len(A))]

        modx = norm_l2(x)
        
        v = x.copy()
        v[0] += -sinal(x)*modx # a soma é ||x||e_1 + x
        
        modv = norm_l2(v)
        if modv == 0:
            modv = 1
        
        
        w.append(v)
        F = ext_product(v)
        F = Matrix_mult(2/modv**2, F)
        F = matrix_sub(eye(len(F)), F)
        F = extend_matrix(F, m)
        R = matrix_product(F, R)

    return R, w

def Q(w):
    Qs = []
    for v  in w:
        modv = norm_l2(v)
        if modv == 0:
            modv = 1
        F = ext_product(v)
        F = matrix_sub(eye(len(F)),Matrix_mult(2/modv**2, F))
        M = extend_matrix(F, len(A))
        Qs.append(M)

    Q = Qs[0]
    for i in range(1, len(Qs)):
        Q = matrix_product(Q, Qs[i])
    return Q


A = [
    [1,2,3],
    [4,5,6],
    [7,8,10]
]

R,w = house(A)
Q = Q(w)

print(R)
print("--")
print(Q)
print("--")
print(A)
print("--")
print(matrix_product(Q, R))

#Agradecimentos ao Igor Roberto Alves turma 1. 