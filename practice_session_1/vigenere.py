def create_bigrams(c):
    # Assuming reading symbols are still in the cipher text
    bi = dict()
    c = c.lower()
    print(c)
    for a in range(len(c)):
        if a + 1 < len(c):
            first = c[a]
            second = c[a + 1]
            # print(first, second, ": ", a)
            if (first, second) in bi:
                bi[(first, second)] += 1
            else:
                if 97 <= ord(first) <= 123 and 97 <= ord(second) <= 123:
                    bi[(first, second)] = 1
    return bi


def top_bigrams(bi, n):
    top = []
    # print(bi)
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


def vigenere(c):
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
    print(top_bigrams(create_bigrams(lab_1_2), 10))
