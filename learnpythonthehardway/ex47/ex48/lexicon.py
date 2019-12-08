lex = {
        'north' : 'direction',
        'south' : 'direction',
        'east' : 'direction',
        'west' : 'direction',
        'below' : 'direction',
        'over' : 'direction',
        'left' : 'direction',
        'right' : 'direction',
        'behind' : 'direction',
        'go' : 'verb',
        'stop' : 'verb',
        'kill' : 'verb',
        'eat' : 'verb',
        'the' : 'stop',
        'in' : 'stop',
        'of' : 'stop',
        'bear' : 'noun',
        'princess' : 'noun',
        'door' : 'noun',
    }

def scan(sentence):
    # sentence = input("> ")
    words = sentence.split()

    result = []

    for word in words:
        num_Chk = trans_numbers(word)
        if str(type(num_Chk)) == "<class 'NoneType'>":
            if word in lex:
                result.append((lex[word], word))
            else:
                result.append(('error', word))
        else:
            result.append(('number', num_Chk))
    return result

def trans_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
