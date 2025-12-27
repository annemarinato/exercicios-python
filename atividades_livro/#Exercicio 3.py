#Exercicio 3.8 pagina 81
#25/12/25

locais = ['japao','eua','canada','coreia','china']

print("\nlista original:")
print(locais)
print("\n----------------------------------------------------------")

print("\nlista alfabetica:")
print(sorted(locais))

print("\nlista orignal novamente:")
print(locais)

print("\n----------------------------------------------------------")

locais.reverse()
print("\nLista aos contrário:")
print(locais)

locais.reverse()
print("\nLista original novamente:")
print(locais)

locais.sort()
print("\nLocais em ordem alfabetica")
print(locais)

locais.sort(reverse=True)
print("\nLocais em ordem alfabetica reversa")
print(locais)