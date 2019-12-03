from sys import argv

script, input_file = argv

def all_print(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_one_line(num_lines, file):
    print(num_lines, file.readline())

curr_file = open(input_file, encoding='utf-8')

print("파일 전체를 출력해봅시다.\n")

all_print(curr_file)

print("이번에는 테이프처럼 되감아봅시다.")

rewind(curr_file)

print("세 줄을 출력해봅시다.")

curr_line_num = 1
print_one_line(curr_line_num, curr_file)

curr_line_num += 1
print_one_line(curr_line_num, curr_file)

curr_line_num += 1
print_one_line(curr_line_num, curr_file)
