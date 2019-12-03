print("모든 것을 연습해봅시다.")
print('\\를 이용해 \n 새줄이나 \t 탭을 하는 탈출 문자열에 대해 \'알아야만\'합니다.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")


five = 10 - 2 + 3 - 6
print(f"이 값은 다섯입니다: {five}")

def secret_formula(begin):
    젤리알 = begin * 500
    그릇 = 젤리알 / 1000
    상자 = 그릇 / 100
    return 젤리알, 그릇, 상자

starting = 10000
젤리, 그릇, 상자 = secret_formula(starting)

#문자열을 포맷하는 다른 방법
print("시작점: {}".format(starting))
# f"" 문자열을 쓰는 것과 같지요.
print(f"젤리 {젤리}알, {그릇}그릇, {상자}상자가 있습니다.")


starting = starting / 10

print("이렇게도 할 수 있습니다.")
formula = secret_formula(starting)
#리스트를 포맷 문자열에 적용하기
print("젤리 {}알, {}그릇, {}상자가 있습니다.".format(*formula))
