velho = int(raw_input("valor: "))
atual = int(raw_input("valor: "))
soma  = velho + atual
while atual >= velho:
    novo  = int(raw_input("valor: "))
    soma  = soma + novo
    velho = atual
    atual = novo
print "SOMA: ", soma
