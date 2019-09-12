import math
from caesar import letter_freq as lq
from caesar import english_letter_freq as elq


def create_bigrams(c):
    # Puts all occurring bigrams of a text in a dictionary
    # Assumes text still contains reading symbols
    bi = dict()
    c = c.lower()
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
            if gcd <= 3:
                continue
            if gcd in gcds:
                gcds[gcd] += 1
            else:
                gcds[gcd] = 1
            if gcds[gcd] > key_len[1]:
                key_len = (gcd, gcds[gcd])
    return key_len[0]


def vigenere(c):
    bigrams = create_bigrams(c)
    top_bi = top_bigrams(bigrams, 1)
    key_len = key_length(c, top_bi)
    freq = lq(c)
    eng_freq = elq()

    pass


if __name__ == "__main__":
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
    print(key_length(lab_1_2, top_bigrams(create_bigrams(lab_1_2), 1)))
