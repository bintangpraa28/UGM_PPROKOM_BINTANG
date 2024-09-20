A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

#program a A U B
print(A | B)

#program b B U C
print(B.union(C))

#program c B U C U D
print(B | C | D)

#program d A U B U C U D
print(A.union(B, C, D))