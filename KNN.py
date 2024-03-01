import numpy as np
import matplotlib.pyplot as pl
c1=[(4,2),(4,2.5),(4.70,3),(4.9,4),(5,5),(4.3,3.5),(5.5,3.8)]
c2=[(7,8),(7.45,6.8),(8.2,6.8),(7.55,6.89),(6.78,8.5),(7.9,8),(7.89,6)]
Test=(6,6)
Dist1=[]
Dist2=[]

def Euclidian(m,Test):
    sub=m-Test
    M=sub*sub
    sum=0
    for i in range(len(M)):
        sum=sum+M[i]
    Q=np.sqrt(sum)
    return Q

for i in range (len(c1)):
    Z=np.array(Test)
    np.array(c1[i])
    a=c1[i]
    Dist1.append(Euclidian(a,Z))
for i in range (len(c2)):
    Z=np.array(Test)
    np.array(c2[i])
    a=c2[i]
    Dist2.append(Euclidian(a,Z))

for i in range(len(Dist1)-1):
    for j in range (len(Dist1)-i-1):
        if Dist1[j]> Dist1[j+1]:
            temp=Dist1[j]
            Dist1[j]=Dist1[j+1]
            Dist1[j+1]=temp
print(Dist1)

for i in range(len(Dist2)-1):
    for j in range (len(Dist2)-i-1):
        if Dist2[j]> Dist2[j+1]:
            temp=Dist2[j]
            Dist2[j]=Dist2[j+1]
            Dist2[j+1]=temp
print(Dist2)

if Dist1[0] < Dist2[0]:
    print("the test coordinate belongs to : CATEGORY 1")
else :
    print("the test coordinate belongs to : CATEGORY 2")

Xcordc1=[]
Ycordc1=[]
for i in range(len(c1)):
    K=c1[i]
    for j in range(1):
        Xcordc1.append(K[j])
        Ycordc1.append(K[j+1])

Xc1=np.array(Xcordc1)
Yc1=np.array(Ycordc1)

Xcordc2=[]
Ycordc2=[]

for i in range(len(c2)):
    K=c2[i]
    for j in range(1):
        Xcordc2.append(K[j])
        Ycordc2.append(K[j+1])

Xc2=np.array(Xcordc2)
Yc2=np.array(Ycordc2)

Xtest=Test[0]
YTest=Test[1]

pl.scatter(Xc1,Yc1)
pl.scatter(Xc2,Yc2)
pl.scatter(Xtest,YTest)
pl.show()