# Calculadora CLI: Apenas 4 opoerações básicas (adição, subtração, multiplicação e divisão).
print("Bem-vindo à Calculadora CLI!")
choice = input(
    "Escolha a operação (adição, subtração, multiplicação, divisão): ").strip().lower()
if choice not in ['adição', 'subtração', 'multiplicação', 'divisão']:
    print("Operação inválida. Por favor, escolha uma das opções: adição, subtração, multiplicação, divisão.")
    exit(1)

# Criar adição
if choice == 'adição':
    raw_add = input("Digite os números para somar, separados por espaço: ")

    def add_all(*args):
        """Soma todos os números fornecidos."""
        return sum(args)
    print(add_all(*map(float, raw_add.split())))

# Criar subtraçã
if choice == 'subtração':
    raw_subtract = input(
        "Digite os números para subtrair, separados por espaço: ")

    def subtract_all(*args):
        """Subtrai todos os números fornecidos, da esquerda para a direita."""
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    print(subtract_all(*map(float, raw_subtract.split())))

# Criar multiplicação
if choice == 'multiplicação':
    raw_multiply = input(
        "Digite os números para multiplicar, separados por espaço: ")

    def multiply_all(*args):
        """Multiplica todos os números fornecidos."""
        result = args[0]
        for num in args[1:]:
            result *= num
        return result
    print(multiply_all(*map(float, raw_multiply.split())))

# Criar divisão
if choice == 'divisão':
    print(" Nota: A divisão por zero não é permitida.")
    print(" Nota: A divisão de decimal exige ponto final. Exemplo: 5.5")
    raw_divide = input(
        "Digite os números para dividir, separados por espaço: ")

    def divide_all(*args):
        """Divide todos os números fornecidos, da esquerda para a direita."""
        result = args[0]
        for num in args[1:]:
            if num == 0:
                print("Erro: Divisão por zero não é permitida.")
                return None
            result /= num
            return result
    print(divide_all(*map(float, raw_divide.split())))
