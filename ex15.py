from sys import argv

script, file_name = argv

text = open(file_name, encoding='utf-8')

print(f"파일 {file_name}의 내용:")
print(text.read())

print("파일 이름을 다시 입력해주세요.")
file_again = input("> ")

text_again = open(file_again, encoding='utf-8')

print(text_again.read())
