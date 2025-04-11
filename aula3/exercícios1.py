#  sabendo que hoje é dia de desconto de 13% em qualquer camiseta que vc comprar, desenvolva um programa para 
# que voçê possa saber o valor do desconto e o valor final de uma camiseta que na semana passada, vc viu que estava por um valor de R$: 83,00

# entrada 
valor_camisa = float(input('informe valor: '))

# processamento
val_desconto = valor_camisa * 0.13
valor_final = valor_camisa - val_descontogit 

# saida
print('desconto: ', "%.2f" % val_desconto)
print('valor final: ', valor_final)

# esse programa calcula do desconto