import math


def english_letter_freq():
    # Returns a dictionary of letter frequencies (in %) in the English language
    # Source: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
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
    # Computes the letter frequencies (in %) of a given text and returns them as a dictionary
    # Only works on lower case letters
    freq = {}
    n = 0
    for l in text:
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
    # Computes the statistical distance between letters from two dictionaries
    # Only works on lower case letters
    d = 0
    for l in lang_freq:
        shift = chr(((ord(l) - 97 + k) % 26) + 97)
        # print(l, "->", shift)
        if shift in text_freq:
            d += abs(lang_freq[l] - text_freq[shift])
    return d / 2


def create_bigrams(c):
    # Puts all occurring bigrams of a text in a dictionary
    # Assumes text still contains reading symbols
    bi = dict()
    for a in range(len(c)):
        if a + 1 < len(c):
            first = c[a]
            second = c[a + 1]
            if (first, second) in bi:
                bi[(first, second)] += 1
            else:
                if 97 <= ord(first) < 123 and 97 <= ord(second) < 123:
                    bi[(first, second)] = 1
    return bi


def top_bigrams(bi, n):
    # Sorts a dictionary of bigrams and returns top n
    top = []
    for k in bi:
        if not top:
            top.append((k, bi[k]))
        else:
            for i in range(len(top)):
                if bi[k] >= top[i][1]:
                    top.insert(i, (k, bi[k]))
                    break
            top.append((k, bi[k]))
    # print(top[:10])
    return top[:n]


def key_length(c, bi):
    # Attempts to find the length of a key corresponding to a vigenere cipher using
    # the cipher text and its top occurring bigram
    pos = []
    x = bi[0][0]
    y = bi[0][1]
    # Find all occurrences of the bigram
    for i in range(len(c)):
        if i + 1 >= len(c):
            # End of text
            break
        a = c[i]
        b = c[i + 1]
        if a == x and b == y:
            # Bigram found
            pos.append(i)
    # print(pos)
    # assert(len(pos) == bi[0][1])

    # Calculate distance between individual occurrences
    d = []
    for i in range(len(pos)):
        if i + 1 < len(pos):
            d.append(pos[i + 1] - pos[i])
    # print(d)

    # Find greatest common divisor between distances
    gcds = {}
    key_len = (0, 0)
    for i in range(len(d) - 1):
        for j in range(i + 1, len(d)):
            gcd = math.gcd(d[i], d[j])
            # print("gcd(", d[i], ",", d[j], ") =", gcd)
            if gcd <= 3:
                continue
            if gcd in gcds:
                gcds[gcd] += 1
            else:
                gcds[gcd] = 1
            if gcds[gcd] > key_len[1]:
                key_len = (gcd, gcds[gcd])
    return key_len[0]


def freq_with_step(lang_freq, c, start, key_len):
    # Assumes c consists of only lower case letters
    new_c = []
    for i in range(start, len(c), key_len):
        new_c += c[i]
    freq = letter_freq(new_c)

    minus = 100
    j = -1
    for i in range(26):
        dist = stat_dist(lang_freq, freq, i)
        if dist < minus:
            minus = dist
            j = i
    # print("Min: ", minus, "at", j, "->", chr(j + 97))
    return chr(j + 97)
