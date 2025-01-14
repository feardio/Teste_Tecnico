def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

def fibonacci_sequence(limit):
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

print("Sequência de Fibonacci até o limite informado:", fibonacci_sequence(number))