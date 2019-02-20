def numeros_pares(valor1,valor2):
    lista = []
    i = valor1
    while i <= valor2:
        lista.append(i)
        i = i+1
    for num in lista:
        if num%2 == 0 :
            print(f'O número {num} é par!')
    return True

valor1 = int(input('Digite o numero inicial'))
valor2= int(input('Digite o numero final'))



numeros_pares(valor1, valor2)

