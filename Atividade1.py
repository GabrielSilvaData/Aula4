compra = float(input('insira o valor da compra:'))
if compra >=250:
    desconto = compra *0.16
    valor_total = compra - desconto
    print(f'O valor é:{valor_total}')

else:   
    print(f'O valor é: {compra}')

