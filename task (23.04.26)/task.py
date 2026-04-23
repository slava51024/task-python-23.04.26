def product_of_nonzero_digits(n):
    """Вычисляет произведение ненулевых цифр числа n (без преобразования в строку)"""
    product = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            product *= digit
        n //= 10
    return product

def main():
    A = int(input("Введите A: "))
    B = int(input("Введите B: "))
    K = int(input("Введите K: "))
    
    found_numbers = []
    
    for num in range(A, B + 1):
        if product_of_nonzero_digits(num) == K:
            found_numbers.append(num)
    
    if not found_numbers:
        print("Подходящих чисел нет")
    else:
        print(f"Количество: {len(found_numbers)}")
        print(f"Минимум: {min(found_numbers)}")
        print(f"Максимум: {max(found_numbers)}")

if __name__ == "__main__":
    main()