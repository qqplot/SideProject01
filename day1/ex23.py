import sys
script, input_encoding, error = sys.argv

def main(lang_file, encode, errors):
    line = lang_file.readline()

    if line:
        line_print(line, encode, errors)
        return main(lang_file, encode, errors)


def line_print(line, encode, errors):
    next_lang = line.strip()
    live_byte_line = next_lang.encode(encode, errors=errors)
    cook_string = live_byte_line.decode(encode, errors=errors)



    print(live_byte_line, "<=======>", cook_string)

languages = open("languages.txt", encoding='utf-8')

main(languages, input_encoding, error)
