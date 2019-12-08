#argv를 쓴 스크립트와 비슷한 함수
def two_print(*argv):
    argv1, argv2 = argv
    print(f"argv1: {argv1}, argv2: {argv2}")

# 좋아요. 사실 *args는 필요없습니다. 그냥 이렇게 하죠.
def two_print_diff(argv1, argv2):
    print(f"argv1: {argv1}, argv2: {argv2}")

# 이 함수는 실행인자를 하나만 받습니다
def one_print(argv1):
    print(f"argv1: {argv1}")

# 이 함수는 실행인자를 하나도 받지 않습니다.
def zero_print():
    print("아무것도 받지 않음")

two_print('규병', '채')
two_print_diff('규병', '채')
one_print('하나!')
zero_print()
