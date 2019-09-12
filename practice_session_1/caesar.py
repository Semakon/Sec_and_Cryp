def english_letter_freq():
    return {
        'a': 8.2,
        'b': 1.5,
        'c': 2.8,
        'd': 4.2,
        'e': 12.7,
        'f': 2.2,
        'g': 2.0,
        'h': 6.1,
        'i': 7.0,
        'j': 0.1,
        'k': 0.8,
        'l': 4.0,
        'm': 2.4,
        'n': 6.7,
        'o': 7.5,
        'p': 1.9,
        'q': 0.1,
        'r': 6.0,
        's': 6.3,
        't': 9.0,
        'u': 2.8,
        'v': 1.0,
        'w': 2.4,
        'x': 0.1,
        'y': 2.0,
        'z': 0.1
    }


def letter_freq(text):
    freq = {}
    n = 0
    for l in text.lower():
        if 97 <= ord(l) < 123:
            n += 1
            if l in freq:
                freq[l] += 1
            else:
                freq[l] = 1
    for k in freq:
        freq[k] = (freq[k] / n) * 100
    return freq


def stat_dist(lang_freq, text_freq, k):
    d = 0
    for l in lang_freq:
        shift = chr(((ord(l) - 97 + k) % 26) + 97)
        # print(l, "->", shift)
        if shift in text_freq:
            d += abs(lang_freq[l] - text_freq[shift])
    return d / 2


def caesar(ciph, k):
    plain = ""
    for s in ciph.lower():
        if 97 <= ord(s) <= 97 + 26:
            plain += chr((ord(s) - 97 - k) % 26 + 97)
        else:
            plain += s
    return plain


if __name__ == "__main__":
    lab_1_2 = "BMFY NX FKKQZJSHJ? IJHWJFXNSL DTZW BNXMJX, FSI GJNSL XFYNXKNJI BNYM BMFY NX JSTZLM KTW DTZ."

    # Brute force:
    # for i in range(26):
    #     print(caesar(lab_1_2, i))

    # print(caesar(lab_1_2, 5))

    minus = 100
    j = -1
    freq = letter_freq(lab_1_2)
    eng_freq = english_letter_freq()
    for i in range(26):
        dist = stat_dist(eng_freq, freq, i)
        if dist < minus:
            minus = dist
            j = i
    print("Min: ", minus, " at ", j)
    print("Result: ", caesar(lab_1_2, j))
