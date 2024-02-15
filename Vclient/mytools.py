import string,random
def enc(data: str, key: int):
    res = [chr(ord(i) + key) if i != ' ' else ' ' for i in data]
    return ''.join(res)
def generateRandomWord(len=random.randint(0,20),letters=list(string.ascii_lowercase)):
    x=""
    for _ in range(len):
        x+=random.choice(letters)
    return x

#print(enc('The quick brown fox jumps over the lazy dog', 2))
#print(enc('Vjg swkem dtqyp hqz lworu qxgt vjg nc|{ fqi', -2))
#print(generateRandomWord(10))