''' 진법 변환
    - n진법 -> 10진법: int(x, n)
    - 10진법 -> 2, 8, 16진법: bin(x), oct(x), hex(x)
    - 10진법 -> n진법: convert_base(x, n)
    - a진법 -> b진법: convert_base(x, b, a)
'''

def convert_base(x:str, to_base:int, from_base:int=10):
    x = int(x) if from_base==10 else int(x, from_base)
    share, remainder = divmod(x, to_base)
    if share==0:
        return str(remainder)
    else:
        return convert_base(share, to_base) + str(remainder)
