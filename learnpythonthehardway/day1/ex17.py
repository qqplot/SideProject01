from sys import argv
from os.path import exists

script, origin_file, copy_file = argv

print(f"{origin_file}에서 {copy_file}로 복사합니다.")

# 이 두 줄은 한 줄로도 쓸 수 있습니다. 어떻게 해야 할까요?
input_text = open(origin_file, encoding='utf-8').read()

print(f"입력 파일은 {len(input_text)} 바이트입니다.")

print(f"출력 파일이 존재하나요? {exists(copy_file)}")
print("준비되었습니다. 계속하려면 리턴을, 취소하려면 CTRL-C를 누르세요.")
input(">> ")

out_file = open(copy_file, 'w', errors='utf-8')
out_file.write(input_text)

print("좋습니다. 모두 완료되었습니다.")

out_file.close()
#input_text.close()
