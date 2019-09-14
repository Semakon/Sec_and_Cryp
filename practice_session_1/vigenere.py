import math
from caesar import letter_freq as lq
from caesar import english_letter_freq as elq
from caesar import stat_dist as sd


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

    return top[:n]


def key_length(c, bi):
    # Attempts to find the length of a key corresponding to a vigenere cipher using
    # the cipher text and its top occurring bigram
    pos = []
    x = bi[0][0][0]
    y = bi[0][0][1]
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
    print(pos)
    # assert(len(pos) == bi[0][1])

    # Calculate distance between individual occurrences
    d = []
    for i in range(len(pos)):
        if i + 1 < len(pos):
            d.append(pos[i + 1] - pos[i])
    print(d)

    # Find greatest common divisor between distances
    gcds = {}
    key_len = (0, 0)
    for i in range(len(d) - 1):
        for j in range(i + 1, len(d)):
            gcd = math.gcd(d[i], d[j])
            if gcd <= 3:
                continue
            if gcd in gcds:
                gcds[gcd] += 1
            else:
                gcds[gcd] = 1
            if gcds[gcd] > key_len[1]:
                key_len = (gcd, gcds[gcd])
                # print(key_len)
    return key_len[0]


def freq_with_step(lang_freq, c, k):
    # Assumes c consists of only lower case letters
    new_c = []
    for i in range(0, len(c), k):
        new_c += c[i]
    freq = lq(new_c)

    minus = 100
    j = -1
    for i in range(26):
        dist = sd(lang_freq, freq, i)
        if dist < minus:
            minus = dist
            j = i
    print("Min: ", minus, "at", j, "->", chr(j + 97))


def vigenere(text):
    # Turn text into all lower case letters
    c = ""
    for l in text.lower():
        if 97 <= ord(l) < 123:
            c += l

    # Create
    bigrams = create_bigrams(c)
    top_bi = top_bigrams(bigrams, 1)
    key_len = key_length(c, top_bi)
    eng_freq = elq()

    print("Suspected Key Length: ", key_len)
    freq_with_step(eng_freq, c, key_len)
    # for i in range(key_len):
    #     freq_with_step(eng_freq, c, i + 1)
    # pass


if __name__ == "__main__":
    temp = "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, " \
           "there live the blind texts. Separated they live in Bookmarksgrove right at the coast of " \
           "the Semantics, a large language ocean. A small river named Duden flows by their place " \
           "and supplies it with the necessary regelialia. It is a paradisematic country, in which" \
           " roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no " \
           "control about the blind texts it is an almost unorthographic life One day however a small " \
           "line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar." \
           " The Big Oxmox advised her not to do so, because there were thousands of bad Commas, " \
           "wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She " \
           "packed her seven versalia, put her initial into the belt and made herself on the way. " \
           "When she reached the first hills of the Italic Mountains, she had a last view back on " \
           "the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the " \
           "subline of her own road, the Line Lane.".lower()
    test = ""
    key = "key"
    i = 0
    for l in temp:
        if 97 < ord(l) <= 123:
            k = ord(key[i]) - 97

            i += 1 % len(key)
    lab_1_2 = "Auge y bxwfcxc xl wrpk shbrt eiwemsttrnwr, mg kj awtrtgu ztyseg zr xl wrpk. Rwx" \
              "qrvyms hj pjrlvbrt vvvi bw pccjtw e pquc dk e pkgftk. Xug tfpgkrf kcmm mf erjaxh" \
              "pkgftkxrzk. Rwx guceet fexgj rwx qrujyvx lntu rd kinf. Jmbxsag nfd peavj rd kinf" \
              "zr bnwg eyyczi vv syrd se fvagrtg. Jfu ih guceet bx octi xl e fgtptm. Fbvy rwx" \
              "trtjmc mlnv jccww gjv ktlwniv ycw xug flt mlnv xcil mg uymjeh xpfu iai fgtptm ana" \
              "km raeaiv gi, uyg qkftk trqgjt llbwcb chx og rzax xb. Ukssrmai kft vmcjvpixbg vf" \
              "bxlgbxvp iai fgtptm mf erjaxh ptpnitrnnpqxl." \
              "Hvhwcgxrg vpntl ss eiwemsttrnwr gnp sc ttwvgi mg aeefvp ih yfg rls vea jzbt mlr" \
              "uvagxx zgjqpzi ogkrtk se yfphx. Gvrycgl yfg r itr auktf xl e fgtptm xuck fxwif vyc" \
              "hxgegk ktlwnivq. Iai ptpnihkecgfxv qrvyms girf emi ui fgtptm. Zntzmjl trqgjt vea" \
              "wjc iai fcdc bxxuqu zjm hvhwcgxrg mvwh, ls gjvw rtraqk ptth rctf dmlrt’j ktlwnivq." \
              "Hbrpg kft Verurp rbtugi fpl sanp yh feaa bcnl ef vyc cnqogi mu eigvvph br gjv" \
              "yailndvr, xm mf grqxec ptrazxh oa kpnbrt ccj iai xgpq. Rbtugiq iaeg ccjdp fvncgdgw" \
              "bh bcnl eeg tppvorf sw bhvr efkeeik ovrwhhf."
    vigenere(test)
