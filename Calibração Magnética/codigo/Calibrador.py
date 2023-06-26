
# Autor principal: Thiago Henrique Ferreira da Silva-LODESTAR-UNB (https://github.com/kaleno)

# Este código apresenta a função apresentar os parâmetros de calibração de cum conjunto de dados em um csv.

# Campo em torno de 25uT no lab.

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import PySimpleGUI as sg
'''
Desejamos encontrar x0, y0, z0, a,b,c tais que ajustem a seguinte equação:

(x-x0)**2/a**2 + (y-y0)**2/b**2 + (z-z0)**2/c**2 = R**2

x,y,z são as componentes de campo coletadas do magnetômetro e R é o valor do módulo esperado no ambiente. 



1) Resolver o caso para os Mínimos Quadrados com a finalidade de encontrar x0, y0, z0.

M  =[[ X**2   , X*Y    , X*Z    , -X*Y**2    , -X*Z**2    , X   ],
     [ Y*X    , Y**2   , Y*Z    , -Y**3      , -Y*Z**2    , Y   ],
     [ Z*X    , Z*Y    , Z**2   , -Z*Y**2    , -Z**3      , Z   ],
     [ X*Y**2 , Y**3   , Z*Y**2 , -Y**4      , -Z**2*Y**2 , Y**2],
     [ X*Z**2 , Y*Z**2 , Z**3   , -Y**2*Z**2 , -Z**4      , Z**2],
     [ X      , Y      , Z      , -Y**2      , -Z**2      , 1   ]]

N = [ X**3      , Y*X**2    , Z*X**2    , Y**2*X**2 , Z**2*X**2 , X**2  ]

Note que:
N =M*W => M**(-1) * N = W

W = [ A , B , C , D , E , F]

Assim,
x0 = A/2
y0 = B/(2*D)
z0 = C/(2*E)

2) Reajustar as amostras de forma que x' = x - x0; y' = y - y0; z' = z - z0;

Desejamos encontrar a,b,c tais que ajustem a seguinte equação:

(x')**2/a**2 + (y')**2/b**2 + (z')**2/c**2 = R**2

x',y',z' são as componentes de campo coletadas e reajustadas e R é o valor do módulo esperado no ambiente.

Resolver o caso para os Mínimos Quadrados com a finalidade de encontrar a, b, c.

M = [[ Y**4      , Z**2*Y**2 , -Y**2],
     [ Y**2*Z**2 , Z**4      , -Z**2],
     [ Y**2      , Z**2      , -1   ]]

N = [-X**2*Y**2, -X**2*Z**2 ,-X**2]

Note que:

N = M*W => M**(-1)*N = W

W = [ G, H, I]

Assim,

a = (I/(R**2))**(0.5)
b = (I/(G*R**2))**(0.5)
c = (I/(H*R**2))**(0.5)

Logo obteve-se o valor de x0,y0,z0,a,b,c e pode-se corrigir as medidas do sensor com as seguinte fórmula.

xr = (x-x0)/a
yr = (y-y0)/b
zr = (z-z0)/c'''


# D representa todos os dados coletados do magnetômetro.
# R representa a magnitude do campo magnético em um determinado local.


def offset(D,R):
    M = np.array([[ 0.0    , 0.0    , 0.0      , 0.0          , 0.0          , 0.0   ],
                  [ 0.0    , 0.0    , 0.0      , 0.0          , 0.0          , 0.0   ],
                  [ 0.0    , 0.0    , 0.0      , 0.0          , 0.0          , 0.0   ],
                  [ 0.0    , 0.0    , 0.0      , 0.0          , 0.0          , 0.0   ],
                  [ 0.0    , 0.0    , 0.0      , 0.0          , 0.0          , 0.0   ],
                  [ 0.0    , 0.0    , 0.0     , 0.0           , 0.0          , 0.0   ]])

    N = np.array([0.0,     0.0,     0.0,     0.0,     0.0,     0.0])

    for B in D:
        X = float(B[0])
        Y = float(B[1])
        Z = float(B[2])
        M += np.array([[ X**2   , X*Y    , X*Z    , -X*Y**2    , -X*Z**2    , X   ],
                       [ Y*X    , Y**2   , Y*Z    , -Y**3      , -Y*Z**2    , Y   ],
                       [ Z*X    , Z*Y    , Z**2   , -Z*Y**2    , -Z**3      , Z   ],
                       [ X*Y**2 , Y**3   , Z*Y**2 , -Y**4      , -Z**2*Y**2 , Y**2],
                       [ X*Z**2 , Y*Z**2 , Z**3   , -Y**2*Z**2 , -Z**4      , Z**2],
                       [ X      , Y      , Z      , -Y**2      , -Z**2      , 1.0 ]])

        N += np.array([ X**3 , Y*X**2 , Z*X**2 , Y**2*X**2 , Z**2*X**2 , X**2 ])
    C = np.linalg.solve(M, N)
    X0 = C[0]/2 
    Y0 = C[1]/(2*C[3])
    Z0 = C[2]/(2*C[4])
    #print(D[0])
    #print(X0)
    #print(Y0)
    #print(Z0)
    for i in range(len(D)):
        D[i][0], D[i][1], D[i][2] = D[i][0] - X0, D[i][1] - Y0, D[i][2] - Z0
    #print(D[0])
    M = np.array([[ 0.0 , 0.0  , 0.0],
                  [ 0.0 , 0.0  , 0.0],
                  [ 0.0 , 0.0  , 0.0]])

    N = np.array([0.0 , 0.0  , 0.0 ])
    for B in D:
        X = float(B[0])
        Y = float(B[1])
        Z = float(B[2])
        M += np.array([[ Y**4      , Z**2*Y**2 , -Y**2],
                       [ Y**2*Z**2 , Z**4      , -Z**2],
                       [ Y**2      , Z**2      , -1.0  ]])

        N += np.array([-X**2*Y**2, -X**2*Z**2 ,-X**2])

    C = np.linalg.solve(M, N)
    a = (C[2]/(R**2))**0.5
    b = (C[2]/(C[0]*R**2))**0.5
    c = (C[2]/(C[1]*R**2))**0.5
    for i in range(len(D)):
        D[i][0], D[i][1], D[i][2] = D[i][0]/a, D[i][1]/b, D[i][2]/c
    #print(D[0])
    #print("X0:",X0,"\nY0:",Y0,"\nZ0:",Z0,"\na:",a,"\nb:",b,"\nc:",c)
    return [X0,Y0,Z0,a,b,c][:]

# Mostra os resultados

def show(vector,H):
    text = f'''Os coeficientes de correção do magnetômetro são:
x0: {vector[0]} 
y0: {vector[1]}
z0: {vector[2]}
a: {vector[3]}
b: {vector[4]}
c: {vector[5]}

Tais que melhor satisfazem a equação:
(x-x0)**2/a**2 + (y-y0)**2/b**2 + (z-z0)**2/c**2 = R**2

em que |R| = {H} uT  no ambiente de trabalho

As equações de correção são:

xc = (x-x0)/a
yc = (y-y0)/b
zc = (z-z0)/c
Onde:
-x0,y0,z0 são as cordenadas de offset
-a,b,c são fatores de escala de cada eixo
-x,y,z são medidas brutas do magnétômetro
-xc,yc,zc são as medidas em uT corrigidas após a calibração'''
    sg.popup_scrolled(text)
# Lê um arquivo csv.


def readcsv():
    file = sg.popup_get_file("Selecione um arquivo CSV com os dados do magnetômetro")
    with open(file) as f:
        leitura = f.read(-1)
    return leitura


# Transforma uma string em um vetor de dados Chamado B.


def dados(leitura):
    B = []
    #print("----------------------")
    for linha in leitura.split("\n"):
        if linha == "":
            continue
        # print(linha)
        Bx = float(linha.split(",")[0])
        By = float(linha.split(",")[1])
        Bz = float(linha.split(",")[2])
        B += [[Bx,By,Bz]]
    #print("----------------------")
    return B[:]

def main():
    leitura = readcsv()
    D = dados(leitura)[:]
    #print(D[0])
    X = []
    Y = []
    Z = []
    for i in range(len(D)):
        X += [D[i][0]]
        Y += [D[i][1]]
        Z += [D[i][2]]
    X = np.array([X])
    Y = np.array([Y])
    Z = np.array([Z])
    # create 3d axes
    ax = plt.axes(projection='3d')
    ax.scatter(X, Y, Z, marker=".",s=1, color='blue') 

    # MODULO DO CAMPO MAGNÉTICO NO LABORATÓRIO
    H0 = 25.7337
    Calibration_vector = offset(D,H0)
    #print(Calibration_vector)
    X = []
    Y = []
    Z = []
    for i in range(len(D)):
        X += [D[i][0]]
        Y += [D[i][1]]
        Z += [D[i][2]]
    X = np.array([X])
    Y = np.array([Y])
    Z = np.array([Z])
    # create 3d axes


    # ax = plt.axes(projection ='3d') 
    ax.scatter(X, Y, Z,marker = ".",s = 1, color ='red')
    ax.grid(visible = True, axis = 'both')
    # ax.set_adjustable('datalim', share=True)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    zmin, zmax = ax.set_zlim3d()
    # Ordenando os valores:
    if xmax>ymax:
        if xmax > zmax:
            vmax = xmax
        else:
            vmax = zmax
    else:
        if ymax > zmax:
            vmax = ymax
        else:
            vmax = zmax

    if xmin < ymin:
        if xmin < zmin:
            vmin = xmin
        else:
            vmin = zmin
    else:
        if ymin < zmin:
            vmin = ymin
        else:
            vmin = zmin
    x_0,y_0,z_0 = np.zeros((3,3))
    u, v, w = np.array([[60,0,0],[0,60,0],[0,0,60]])
    ax.quiver(x_0,y_0,z_0,u,v,w,arrow_length_ratio=0.1, color = 'black')

    x_direction = [1,0]
    y_direction = [1,-1]
    ax.set_xlim(xmin = 4*vmin/3,xmax = 4*vmax/3)
    ax.set_ylim(ymin = 4*vmin/3,ymax = 4*vmax/3)
    ax.set_zlim(zmin = vmin,zmax = vmax)
    ax.set_aspect("auto")
    plt.subplots_adjust()
    plt.show()
    show(Calibration_vector,H0)
    
main()
