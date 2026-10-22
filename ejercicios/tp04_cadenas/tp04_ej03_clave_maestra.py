clave = 18293
str_clave = str(clave)
largo = len(str_clave)

clave1 = []
clave2 = []


for i in range(largo):
    if (i + 1) % 2 != 0:
        clave1.append(str_clave[i])
    else:
        clave2.append(str_clave[i])
clave1 = "".join(clave1)
clave2 = "".join(clave2)

print(clave1)
print(clave2)
