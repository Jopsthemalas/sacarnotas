def sacar_dinheiro(valor, disponibilidade_notas):
    """
    Função para calcular o menor número de notas para um valor de saque específico.

    Parâmetros:
    valor (int): O valor que o usuário deseja sacar.
    disponibilidade_notas (dict): Dicionário com a quantidade de notas disponíveis.

    Retorna:
    Uma lista de notas que serão entregues ao usuário ou uma mensagem de erro se o valor do saque for inválido.
    """
    if valor < 10 or valor % 10 != 0:
        return 'Valor inválido. Digite um valor que seja múltiplo de 10.'

    notas = [100, 50, 20, 10]
    resultado = []

    for nota in notas:                          #1
        while valor >= nota and disponibilidade_notas[nota] > 0:
            valor -= nota
            disponibilidade_notas[nota] -= 1
            resultado.append(nota)

    if valor != 0:  # Se após o loop ainda restar valor, significa que não há notas suficientes
        return 'Não há notas suficientes para realizar este saque.'

    return resultado

# Representa a disponibilidade de notas no caixa eletrônico
disponibilidade_notas = {100: 1, 50: 1, 20: 2, 10: 3}

valor_saque = int(input("Digite o valor que deseja sacar: "))
print(sacar_dinheiro(valor_saque, disponibilidade_notas))