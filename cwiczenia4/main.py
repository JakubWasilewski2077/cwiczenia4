#zadanie1
# zbiorA = []
# for x in range(1,11):
#     zbiorA.append(1-x)
# print(zbiorA)
#
# zbiorB = []
# for x in range(8):
#     zbiorB.append(4**x)
# print(zbiorB)
#
# zbiorC = []
# for x in zbiorB:
#    if x % 2 == 0:
#        zbiorC.append(x)
# print(zbiorC)
import random

A = [1-x for x in range(1,11)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

#zadanie2
listy1 = []
for x in range(10):
    listy1.append(int(random.uniform(0, 100)))
print("lista 1: ",listy1)
listy2 = [x for x in listy1 if x % 2 == 0]
print("lista 2: ", listy2)

#zadanie3
produkty = {'mleko':'sztuki','cukierki':'kg', 'kielbaski':'sztuki'}
print(produkty)
produkty_sztuki = [x for x,y in produkty.items() if y == 'sztuki']
print(produkty_sztuki)

#zadanie4




