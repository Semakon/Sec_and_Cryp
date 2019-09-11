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

    print(caesar(lab_1_2, 5))
