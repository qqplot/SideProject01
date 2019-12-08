import random
from urllib.request import urlopen
import sys

words_URL = "http://learncodethehardway.org/words.txt"
words = []

sentences = {
    "class %%%(%%%):" :
        "%%% (이)라는 이름의 클래스를 만드는데 %%% 의 일종이다. (is-a)",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "클래스 %%% 은/는 self와 @@@ 매개변수를 받는 이름이 *** 인 함수를 가졌다. (has-a)" ,
    "class %%%(object):\n\tdef ***(self, @@@)":
        "클래스 %%% 은/는 self와 @@@ 매개변수를 받는 이름이 *** 인 함수를 가졌다. (has-a)",
    "*** = %%%()":
        "*** 변수를 %%% 클래스의 인스턴스 하나로 정한다.",
    "***.***(@@@)":
        "*** 변수에서 *** 함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
    "***.*** = '***'":
        "*** 변수에서 *** 속성을 받아야 *** (으)로 값을 정한다."
}

# 문장을 먼저 연습하고 싶은가
if len(sys.argv) == 2 and sys.argv[1] == "korean":
    sen_forward = True
else:
    sen_forward = False

# 웹사이트에서 단어를 불러온다
for word in urlopen(words_URL).readlines():
    words.append(str(word.strip(), encoding="utf-8"))

def transform(code, sen):
    class_names = [w.capitalize() for w in random.sample(words, code.count("%%%"))]
    other_names = random.sample(words, code.count("***"))
    results = []
    para_names = []

    for i in range(0, code.count("@@@")):
        para_cnt = random.randint(1,3)
        para_names.append(', '.join(random.sample(words, para_cnt)))

    for sen in code, sen:
        result = sen

        # 가짜 클래스 이름
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # 가짜 매개변수 목록
        for word in para_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# CTRL-D를 누를 때까지 계속한다.
try:
    while True:
        codes = list(sentences.keys())
        random.shuffle(codes)

        for code in codes:
            sen = sentences[code]
            question, answer = transform(code, sen)
            if sen_forward:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"answer: {answer}\n\n")

except EOFError:
    print("\n끝")
