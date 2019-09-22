from decryption_utils import english_letter_freq as elf
from decryption_utils import letter_freq as lf
from decryption_utils import stat_dist as sd


def shift(c, lang_freq):
    # Attempts to find the key of a shift cipher encrypted cipher text
    text_freq = lf(c.lower())
    minus = 100
    j = -1
    for i in range(26):
        dist = sd(lang_freq, text_freq, i)
        if dist < minus:
            minus = dist
            j = i
    return j


def decr_shift(c, k):
    # Decrypts a shift cipher using a given key
    plain = ""
    for s in c.lower():
        if 97 <= ord(s) <= 97 + 26:
            plain += chr((ord(s) - 97 - k) % 26 + 97)
        else:
            plain += s
    return plain


if __name__ == "__main__":
    exercise1a = "JOVJVSHAL DHZ PUCLUALK MVBY AOVBZHUK FLHYZ HNV PU H " \
                 "ZTHSS CPSSHNL PU OVUKBYHZ HUK OHZ AOYPCLK LCLY ZPUJL"

    key = shift(exercise1a, elf())
    print("Found key:", key)
    print("Result:")
    print(decr_shift(exercise1a, key))
