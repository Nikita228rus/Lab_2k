from base_32_64_dict import *


def to_base64(text: str):

    text.encode("ascii")
    to_bin = ''

    for i in text:
        to_bin = ''.join(format(x, '08b') for x in bytearray(text, 'utf-8'))

    l_code = []
    for i in range(0, len(to_bin), 6):
        l_code.append(to_bin[i:i + 6])

    flag = 0
    while len(to_bin) % 24 != 0:
        to_bin += "00000000"
        flag += 1

    text_end = ""
    for i in range(len(l_code) - flag):
        text_end += alf_dict[l_code[i]]
    for i in range(flag):
        text_end += "="

    return text_end


def to_ascii64(text: str):
    text_end = ""
    flag = text.count("=", -2)
    text_b64 = text.strip('=')
    for i in text:
        text_end += dict_alf[i]
    while len(text_end) % 24 != 0:
        text_end += "0"
    for i in range(flag):
        text_end = text_end.replace("00000000", "")
    text_end = bytes.fromhex(hex(int(text_end, 2))[2:]).decode(encoding="utf-8")
    return text_end
