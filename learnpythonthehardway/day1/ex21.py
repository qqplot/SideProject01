def plus(a, b):
    print(f"덧셈 {a} + {b}")
    return a + b

def minus(a, b):
    print(f"뺄셈 {a} - {b}")
    return a - b

def multiple(a, b):
    print(f"곱하기 {a} * {b}")
    return a * b

def divide(a, b):
    print(f"나누기 {a} / {b}")
    return a / b

print("함수만으로 계산해봅시다!")

age = plus(20, 9)
height = minus(190, 4)
weight = multiple(11, 10)
iq = divide(100, 2)

print(f"나이: {age}, 키: {height}, 몸무게: {weight}, IQ: {iq}")
