import string

BASE62 = string.digits + string.ascii_letters

def encode_base62(num: int, length: int = 6) -> str:
    base = len(BASE62)
    chars = []

    while num > 0:
        num, rem = divmod(num, base)
        chars.append(BASE62[rem])

    code = ''.join(reversed(chars))
    return code.rjust(length, '0')
