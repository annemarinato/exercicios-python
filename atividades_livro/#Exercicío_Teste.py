#Exercicío_Teste

first_name = input("Digite seu primeiro nome ")
last_name = input("Digite seu sobrenome ")

gender = input("Insira seu gênero F ou M ")

if gender == "F":
    full_name = f"{first_name} {last_name}"
    message = f"Seja bem-vinda, {full_name.title()}"
    print(message)
elif gender == "M":
    full_name = f"{first_name} {last_name}"
    message = f"Seja bem-vindo, {full_name.title()}"
    print(message)
else:
    print("Insira um valor válido")

