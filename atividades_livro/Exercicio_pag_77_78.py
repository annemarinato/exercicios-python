
#Exercicio da pagina 77|78 3.4, 3.5, 3.6 e 3.7
convidados = ['Rosa', 'Natan','Alyson']

print(len(convidados))

print(convidados[0],',' ,convidados[1],'e' ,convidados[2], ",\ngostaria de te convida-los para esse momento especial\n")
#print(convidados[1],",\nconto com sua presença neste momento especial\n")
#print(convidados[2],",\nvocê é muito importante, por isso conto com sua presença\n")


ausente = convidados.pop(1)  #aqui removi o elemento da lista do indice 1, que no caso é o Natan
convidados.insert(1, 'Assis') #aqui eu inseri o Assis na lista de convidados no indice que removi

print(convidados[0],',' ,convidados[1],'e' ,convidados[2], ",\ngostaria de te convida-los para esse momento especial\n")
#aqui está a nova lista de convidados com a pessoa que nao poderá comparecer
print(len(convidados))

convidados.append('Natalia') #adicionei os elementos no final da lista e ai ficaram no indice 3 e 4
convidados.append('Nicolly') #para isso utilizei o metodo append que adiciona no fim da lista, enquanto insert substitui

print(convidados[3],'e',convidados[4], '\ncomo nem todos puderam comparecer, estou convidando vocês também')
print(len(convidados))

convidados.insert(0,'Livia')
convidados.insert(1,'Joyce')
convidados.insert(4,'Heloisa') #inseri cada um dos convidados em uma lista, substituindo a posição de cada um, onde a 'rosa' estaria em 
convidados.append('Monique') #primeiro da lista, e agora está no terceiro indice

print("\nGostaria de convida-las para o jantar nesta noite", convidados[0],',',convidados[1],'e',convidados[4],'.\n')

print(convidados[0], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[1], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[2], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n") 
print(convidados[3], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[4], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[5], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[6], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[7], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(convidados[8], ",agora que todos nós estamos reunidos eu encontrei uma mesa maior para todos nós\n")
print(len(convidados))

print(convidados[0],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto")
convidados.pop(0) #remove a livia que esta no indice 0, e quem passa a valer 0 é a joyce e a rosa passa a valer 1

print(convidados)
print(len(convidados))

print(convidados[1],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
convidados.pop(1) #remove a rosa que está no indice 1, e quem passa a ser indice 2 é o assis
print(convidados)
print(len(convidados))

print(convidados[2],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
convidados.pop(2) 
print(convidados)
print(len(convidados))

print(convidados[3],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
convidados.pop(1)
print(convidados)
print(len(convidados))

print(convidados[4],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
convidados.pop(2)
print(convidados)
print(len(convidados))

print(convidados[3],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
del convidados[3]
print(convidados)
print(len(convidados))

print(convidados[2],",infelizmente não sera mais possivel o jantar dessa noite, pois houve um imprevisto\n")
del convidados[2]
print(convidados)
print(len(convidados))

 #aqui eu coloquei em cada execuçao o print convidados para se ter ideia de quem esta sendo eliminado e quem esta mudando de lado
 #em cada indice, ao inves de eu ter que escrever em cada um

print(convidados[0], 'e',convidados[1],"vocês ainda poderão comparecer em meu jantar")


#Iniciado no dia 22 e concluido no dia 24//12/2025