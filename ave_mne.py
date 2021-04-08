engUpp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
engLow = 'abcdefghijklmnopqrstuvwxyz'
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encoding(text):
    stp = len(text)
    new_text = ''
    for i in range(len(text)):
        if text[i] in engUpp:
            alp = engUpp
        else:
            alp = engLow
        new_text = new_text + alp[(26 + alp.index(text[i]) + int(stp)) % 26]
    return new_text


tx = list(input())
st = ''
word = ''
for i in range(len(tx)):
    if tx[i] not in eng:
        st += tx[i]
    else:
        word += tx[i]
        if i == len(tx) - 1 or tx[i + 1] not in eng:
            st += encoding(word)
            word = ''
print(st)
