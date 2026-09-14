#Problem 3.4: Errors in summation
s = 0
M = 3

for i in range(M):      #range M gives (0, 1, 2), not (1, 2, 3)
    s += 1/2*k**2       #k is undefined and the expression is missing parentheses

print(s)            

#correct version:
s = 0
M = 3
k = 1
for i in range(k, M+1):
    s += 1/((2*i)**2)

print(s)


#Problem 3.5: Sum as a while loop:
s = 0
count = 1
M = 3

while count <= M:
    s += 1/((2*count)**2)
    count += 1

print(s)


#Problem 3.7: Table showing population growth
import math
    
def N_b(t, B=50000, C=9, k=0.2):
    return B/(1+C*(math.e)**-(k*t))

t = []
N = []

for i in range(0, 49, 4):
    t.append(i)
    N.append(N_b(i))

for n in range(len(N)):
    print(t[n], "h: ", round(N[n], 2))

#Problem 3.8: Nested list
#a)
tN1 = []
tN1.append(t)
tN1.append(N)

for k in range(len(tN1[0])):
    print(tN1[0][k], int(tN1[1][k]))

#b)
tN2 = []
for element in range(len(tN1[0])):
    values = []
    values.append(t[element])
    values.append(int(N[element]))
    tN2.append(values)

for element1 in range(len(tN2)):
    print(tN2[element1][0], tN2[element1][1])