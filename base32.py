from base_32_64_dict import *


def to_base32(text: str):

    text.encode("ascii")
    to_bin = ''

    for i in text:
        to_bin = ''.join(format(x, '08b') for x in bytearray(text, 'utf-8'))

    flag = len(to_bin) % 5
    if len(to_bin) % 40 != 0:
        while len(to_bin) % 5 != 0:
            to_bin += "0"

    l_code = []
    for i in range(0, len(to_bin), 5):
        l_code.append(to_bin[i:i + 5])

    text_end = ""
    for i in range(len(l_code)):
        text_end += alf_dict_32[l_code[i]]
    if flag == 3:
        text_end += "======"
    if flag == 1:
        text_end += "===="
    if flag == 4:
        text_end += "==="
    if flag == 2:
        text_end += "="
    print(text_end)
    return text_end


def to_ascii32(text: str):
    text_end = ""
    flag = text.count("=", -6)
    text_b32 = text.strip('=')

    for i in text_b32:
        text_end += dict_alf_32[i]
    while len(text_end) % 5 != 0:
        text_end += "0"
    if flag == 6:
        text_end = text_end[:-2]
    if flag == 4:
        text_end = text_end[:-4]
    if flag == 3:
        text_end = text_end[:-1]
    if flag == 1:
        text_end = text_end[:-3]

    text_end = bytes.fromhex(hex(int(text_end, 2))[2:]).decode(encoding="utf-8")
    print(text_end)
    return text_end
