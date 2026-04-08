compra = float(input('Insira o valor da compra:'))
forma_de_pagamento =input('o pagamento é a vista ou parcelado:')
if compra >=250 and forma_de_pagamento == 'a vista':
    desconto = compra *0.16
    valor_total = compra - desconto
    print(f'O valor com desconto é:{valor_total}')
else:
    print(f'O valor é:{compra}')








