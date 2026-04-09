# #Estrutura If   
# idade = int(input('insira a idade:'))
# if idade >= 18:
#     print('Você é adulto')
# else:
#     print('Você não é adulto')
# #---------------------------------------------

# pontos = int(input('informe os pontos:'))
# if pontos >= 100:
#     print('Excelente')
# elif pontos >= 50:
#     print('Bom desempenho')
# elif pontos >=25:
#     print('Satisfatório')
# else:
#     print('Pratique mais')

# #operadores AND e OR
# usuario = input('Nome:')
# senha = input('Senha:')

# if usuario =='admin' and senha == '1234':
#     print ('Login realizado com sucesso')
# else:
#     print('Usuário ou senha incorretos')                    

# Exemplo IFs encadeado
nota = 10
if nota >= 9:
     print('A')
elif nota >=7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('E')
#IFs não encadeado

nota = 10
if nota >= 9:
     print('A')
if nota >=7:
    print('B')
if nota >= 5:
    print('C')
if nota >= 3:
    print('D')
else:
    print('E')

# IFs aninhados
nota = float(input('Insira a nota:'))
frequencia = float(input('Insira a frequência:'))

if nota >= 7:
    #aprovado por nota, mas precisa checar a frequência!
  if frequencia >= 75:
    print('Aluno aprovado por Nota e Frequência!')
  else: 
    print('Reprovado por Frequência!')
else:
  print('Reprovado por Nota baixa!')

