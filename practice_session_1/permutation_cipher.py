import itertools


def perms(text, perm):
    k = len(perm)
    s = ""
    for i in range(0, len(text), k):
        for j in range(k):
            s += text[i + perm[j] - 1]
        s += " "
    return s + "(" + str(perm) + ")"


def test_perms(text, var, pad):
    for p in itertools.permutations(var, len(var)):
        p = list(p)
        for j in range(len(pad)):
            p.append(pad[j])
        print(perms(text, p))


def decr_perm(c, k):
    s = ""
    for i in range(0, len(c), len(k)):
        for j in range(len(k)):
            s += c[i + k[j] - 1]
    return s


if __name__ == "__main__":
    exercise1b = "VCALIUTOTNOCINISOMTUPUNLNCADUTSRLUACEAFAO" \
                 "CEOXEEWRVTENIESOIAMSNEAMWRCEIHHERTEETCRCOA" \
                 "AAETINESEINEHVWNPALIOLETSDHETTEHDFEOOETAAC" \
                 "CERNEVEEYTFALULKOIMARSHNEOSDFEAAHRTOTRYWNT" \
                 "EOINCLNHIGNAGHNTGHRMFOTERRETESUEKTNIHLIWTF" \
                 "IHNEHSTEEATHRTATHORYITYFBUTORSRHWIONMRODLE" \
                 "APNESADHSDEENBAEMDEDBDEIEAWNSOTUICVSWSHUPP" \
                 "LEIBEHLTHEENTASEMSEVSLTATEIRBTEODERUKTAELH" \
                 "AWLIISODHTEITHNWMEHSTEPEMPLTUEABHVYAEEFNHE" \
                 "TLIESERTOMNNCETBSYMDUESHCMNUAOADAPCOSSEHMT" \
                 "EALNECVSIRNNEAGRAAIEWDCNOEFGORLORFOSYMEAEP" \
                 "LOLBOTLWGRRGTIHLETNLEATHOWYEAUDRRPAKCPRERL" \
                 "OTIHSNMOCEAKNSIVNALOASARTGEYRELASMYOLRPSUE" \
                 "CTTHDIEWRCSAERTTOSWRRAOWTIEHLRHERAESECTMLO" \
                 "POEOYMLSSTWTIHHNIGEADRPEENYITSOIPDFOUSENQU" \
                 "IATOCCOAASTNHITCTOERHIDLTRNOAEEDTRXUTONSOE" \
                 "NAERESCSTIEYELDTRHIEMNNEEIERPASSOTSRHTEOTE" \
                 "FIBNASENXSXDXIE"

    # var = [2, 4, 6, 7]
    # pad = [5, 1, 3]
    # test_perms(exercise1b, var, pad)

    key = [2, 6, 4, 7, 5, 1, 3]
    decr = decr_perm(exercise1b, key)
    for i in range(0, len(decr), len(key) * 6):
        print(decr[i:i + len(key) * 6])
