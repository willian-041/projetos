#Imprimir o nome completo e o menu para o cliente
print("Bem vindos a loja de Marmitas do [Willian Wagner Sentone Arf]")

#Menu para o cliente
print("Menu:")
print("Tamanho P - Bife Acebolado (BA): R$16,00")
print("Tamanho P - Filé de Frango (FF): R$15,00")
print("Tamanho M - Bife Acebolado (BA): R$18,00")
print("Tamanho M - Filé de Frango (FF): R$17,00")
print("Tamanho G - Bife Acebolado (BA): R$22,00")
print("Tamanho G - Filé de Frango (FF): R$21,00")

#Acumulador para somar os valores dos pedidos
total = 0.0

#Implementar while, break, continue
while True:
    #Input do sabor e verificação de validade
    sabor = input("Digite o sabor desejado (BA/FF): ").upper()
    if sabor not in ['BA', 'FF']:
        print("Sabor inválido. Tente novamente.")
        continue  # Pula para a próxima iteração do loop
    
    #Input do tamanho e verificação de validade
    tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue 

    #Calcular o preço com base no sabor e tamanho usando if, elif e else
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16.0
        elif tamanho == 'M':
            preco = 18.0
        else:  
            preco = 22.0
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15.0
        elif tamanho == 'M':
            preco = 17.0
        else: 
            preco = 21.0

    #Adiciona o preço ao total
    total += preco

    #Pergunta se deseja pedir mais alguma coisa
    mais_pedido = input("Deseja pedir mais alguma coisa? (sim/não): ").lower()
    if mais_pedido != 'sim':
        break  

#Print do acumulador com o total dos pedidos
print(f"Total do pedido: R${total:.2f}")


print("Cálculo realizado por [Willian Wagner Sentone Arf]")
