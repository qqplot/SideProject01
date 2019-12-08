ten_kind = "사과 귤 까마귀 전화기 빛 설탕"

print("잠깐 아직 목록에 10개가 들어있지 않으니 한 번 고쳐봅시다.")

stuff = ten_kind.split(' ')
other_stuff = ["낮", "밤", "노래", "부메랑", "옥수수", "바나나", "아이", "어른"]

while len(stuff) != 10:
    # next_one = other_stuff.pop()
    next_one = pop(other_stuff)
    print("추가: ", next_one)
    stuff.append(next_one)
    print(f"이제 {len(stuff)} 항목이 있습니다.")

print("한 번 볼까요! ", stuff)

print("이걸로 무언가 해봅시다.")

print(stuff[1])
print(stuff[-1]) # wow, good!!
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
