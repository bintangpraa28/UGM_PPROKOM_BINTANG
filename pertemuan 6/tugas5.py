A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

#program a A symmetric difference B
print(A ^ B)

#program b B symmetric difference A
print(B ^ A)

#program c A symmetric difference C
print(A.symmetric_difference(C))

#program d B symmetric difference C
print(B.symmetric_difference(C))