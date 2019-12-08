def cheeseAndCracker(num_chs, box_crk):
    print(f"치즈가 {num_chs}개 있어요!")
    print(f"크래커가 {box_crk} 상자 있어요!")
    print("파티 벌이기에 충분하네요!!")
    print("담요 한 장 가져오세요.\n")

print("함수에 숫자를 바로 넣어줄 수 있습니다.")
cheeseAndCracker(20, 30)


print("스크립트의 변수를 쓸 수도 있구요.")
num_chs = 20
box_crk = 30

cheeseAndCracker(num_chs, box_crk)


print("안에서 계산을 해도 됩니다.")
cheeseAndCracker(10+10, 5+6)

print("합쳐서 변수도 쓰고 계산도 할 수도 있습니다.")
cheeseAndCracker(num_chs + 10, box_crk + 6)
