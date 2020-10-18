alphabet = [chr(i) for i in range(ord('а'),ord('я')+1)] + [' ']

# Ключ
keyRaw = '\u0434\u0430\u0431\u0438\u0432\u0433\u0439\u0436\u0437\u043A\u0435' #@param {type:"string"}
key = list(map(lambda x: alphabet.index(x), filter(lambda x: x in alphabet, keyRaw.lower())))

# Исходный текст                                                       млыеад ня  оыиса кыы вмт ьб   бшб аб еойм ас  тктк мнмоалжт                                                                                                 
encoded_text = '\u043C\u043B\u044B\u0435\u0430\u0434 \u043D\u044F  \u043E\u044B\u0438\u0441\u0430 \u043A\u044B\u044B \u0432\u043C\u0442 \u044C\u0431  \u0431\u0448\u0431 \u0430\u0431 \u0435\u043E\u0439\u043C \u0430\u0441  \u0442\u043A\u0442\u043A \u043C\u043D\u043C\u043E\u0430\u043B\u0436\u0442'
def chunks(s, n):
    for st in range(0, len(s), n):
        yield s[st:st+n]

# обратная перестановка ключа
keyh = [key.index(i) for i in range(len(key))]

# По ключу получим размер сетки и получим саму сетку
l = len(encoded_text)%len(key) # кол-во длинных
lc = len(encoded_text)//len(key)+(1 if l else 0) # длина длинных
s = len(key) - l # кол-во коротких
sc = lc - 1 # длина коротких
grid = [list(encoded_text[st*lc:st*lc+lc]) for st in range(l)]+[list(encoded_text[l*lc+st*sc:l*lc+st*sc+sc]) for st in range(s)]
dec_grid = [[z[i] for z in [grid[i] for i in keyh] if len(z) > i] for i in range(lc)]

decoded_text = list(sum([x if i%2==0 else list(reversed(x)) for i, x in enumerate(list(list(x) for x in dec_grid))], []))
print("Decoded text:", ''.join(decoded_text))
