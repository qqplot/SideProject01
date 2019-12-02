from sys import argv

script, file_name = argv

print(f"{file_name} 파일을 지우려 합니다.")
print("취소하려면 CTRL + C (^C)를 입력하세요.")
print("진행하려면 리턴 키를 누르세요.")

input("?")

print("파일 여는 중...")
destination = open(file_name, 'w', encoding='utf-8')

print("파일 내용을 지웁니다. 안녕히!")
destination.truncate

print("이제 세 줄에 들어갈 내용을 부탁드릴게요.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("이 내용을 파일에 씁니다.")

destination.write(line1)
destination.write("\n")
destination.write(line2)
destination.write("\n")
destination.write(line3)
destination.write("\n")

print("마지막으로 닫습니다.")
destination.close()
