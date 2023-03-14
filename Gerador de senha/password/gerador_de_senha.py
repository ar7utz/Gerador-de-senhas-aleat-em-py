import random
print('Teste de gerador de senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@123456789'

numero = input('Quantas senhas você quer criar? ')
numero = int(numero)

tamanho = input('Qual tamanho deseja para sua senha? (em caracteres) ')
tamanho = int(tamanho)

print('Aqui estão suas senhas! ')

for senha in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(chars)
    print(senhas)
