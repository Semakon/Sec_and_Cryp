from decryption_utils import create_bigrams, top_bigrams, \
    key_length, freq_with_step
from decryption_utils import english_letter_freq as elq


def vigenere(text):
    # Turn text into all lower case letters
    c = ""
    for l in text.lower():
        if 97 <= ord(l) < 123:
            c += l

    # Find top 3 bigrams and use them to find a possible key
    bigrams = create_bigrams(c)
    top_bi = top_bigrams(bigrams, 3)
    result = []
    for j in range(3):
        key_len = key_length(c, top_bi[j])
        eng_freq = elq()

        # print("Suspected Key Length:", key_len)
        key = ""
        for i in range(key_len):
            key += freq_with_step(eng_freq, c, i, key_len)
        result.append(key)
    return result


def encrypt_vig(plain, key):
    # Encrypts a plain text with vigenere encryption with a key
    # (key must only contain lower case letters)
    if not key or len(key) < 1:
        return plain
    cipher = ""
    i = 0
    for l in plain:
        if 97 <= ord(l) < 123:
            k = ord(key[i]) - 97
            new_l = chr(((ord(l) - 97 + k) % 26) + 97)
            # print(l, "->", new_l, "(i:", i, ", k:", k, ")")
            cipher += new_l
            i = (i + 1) % len(key)
        else:
            cipher += l
    return cipher


def decrypt_vig(cipher, key):
    # Decrypts a cipher text with vigenere decryption with a key
    # (key must only contain lower case letters)
    if not key or len(key) < 1:
        return cipher
    plain = ""
    i = 0
    for l in cipher:
        if 97 <= ord(l) < 123:
            k = ord(key[i])
            new_l = chr(((ord(l) - k) % 26) + 97)
            # print(l, "->", new_l, "(i:", i, ", k:", k - 97, ")")
            plain += new_l
            i = (i + 1) % len(key)
        else:
            plain += l
    return plain


if __name__ == "__main__":
    exercise1c = "FFX ZSGST UALWLFD CL RTC PVFWR UP FFX ZSGST " \
                 "UALWLFD CL RTC TUQTSTR IMKSR TG G JUQM VT " \
                 "CSSYDITIZP QULERKBQEWULE MY JZLGYGOYE HBEWWSURR " \
                 "NWGST ZK TTYWZIY YGRAVFD WT EGGWLPZCQQ AP IVSXG " \
                 "VMBSEHF LAULS YGJWPBZ FQJELBTQ ZMGPBZHD. ORRTMNNV " \
                 "EVK JUQM, PB THY AGPKLBE TUPY, BBK BZH YRMZBSWDS " \
                 "ALFGE AVP FKLMGLZOYQK, RTC YPFDH YSOF EPGEG UD " \
                 "ECOLB HCTBQPL KOES LPAK MOS DSIMZB VLBEIXW NA. " \
                 "MOS ZFOEULTS ZTGZ GZQIPFPR OLZSFLFLPRC HCKZWZBY " \
                 "RTPHBUS HNC MEXZ, CQHKL XGLAWYU YCHCG LBEFOCE. " \
                 "MY AVP CXGSGGHZ DSBCZ UHURPFY, MZJR VBP HNC " \
                 "SPXHH AMXYYGW VT RWFY (MJLV QLZRCP RAL DJFGKUB " \
                 "HM YSILS, MDMLF EVK NTYKHCS KNM NSBSH TH), ZFQ " \
                 "MEKSDH UD FFX HBNWKLF UHURPFY PQKTPBD " \
                 "FKJMRBCSWM OLFYVA. HSS IMXMLZID CL PTMWLG, EVK " \
                 "JUEAAVZIYC AD TSSIOTBDGT, AVP AGSEMELIX OZ " \
                 "FMJBJOCBGQESL, AVP HKKBJX VT LFZCYGL HBO HNC " \
                 "ERTAIP CL XQSL DSCS GJX BXZHCCECP. RAL ZZQGRUMG " \
                 "HBO IRRUKTAS QOZC AD MOS SOTEULZ NOCRKLE YKL " \
                 "IYYTMIL, TUR EVKPQ GL ZDPQAJMRBVB EVGR FFXF ALM " \
                 "TMF FTCS PLOQFCW HH LZR. RTC EPGE QUTQPXK CYZE " \
                 "RTC LJIWDZSDYE HBO OXATGMLQEIXYX KHUIXSTRE MY AVP " \
                 "AKBURXYFLBKYZ YGK ATRJJQ CTZHPFT PQEBVBD, KNGOF " \
                 "MOSY QUKBPBZSO HNC WLHDB HCXJP DHY HSS MPQCDZ. " \
                 "VPBIC, QVMHBE GORQQ ULMZBJ RTGL YSLZS UQPX UCE " \
                 "QULEGWLFPR GQ BYKA CQ QULFCFWCCOXW MAVVIYHY. RTC " \
                 "IYWXOXW MAVVIYHY, AAKBUU QFUK TCESSYWYRUA PYWESXQ, " \
                 "MJLV VPOBGXW BUTWIKLOCW AVP DRYOCL PBNZABQB BU HSS " \
                 "CMZBXYG WWYR. RGOL CQ HNC ECOLB PBZPUCL HFP O " \
                 "ICXCUYOEWUL AD ZYSPY GAOMFWZTGNKQLMZ WY HNC MPMZ " \
                 "OYR GPOFBASNHAPQ (RAL SIQKNFGHUG MSOLS RAL DJFGKUBL " \
                 "VT RWFY MLW AVP VGLSGGN ULFJCZQ HM PLPEJAL). MOS " \
                 "DSBCZ UHURPFY MZ YGAWAOZCD’Q EPGE KUL BPTPGPG LMD " \
                 "RALWC BURMZEL TPOZSDCL, YOYUOLS DKVA DIVCDJTAWGSY " \
                 "MR RAL VTUNCER HY ZLFMCER HM HSSOP FWILG, EC ZFQ " \
                 "YKAWDHXW IGMO KSWIF FFXF KPFK CJCVBHPR. ZFQGK " \
                 "HFNVORQAMBFLZ GLP YKAWDHOA RCTAICSY UQPX PATHGRQB " \
                 "MOFZIMFASM AVP VKJXCGPGEWI UAPEK OYR HCKMGK. HSS " \
                 "MPQCD PBQZACZAX PB CCSYZ ANSHFFK, YZB MOS CSBGHYE " \
                 "VT RFKAA-PHTOY OXRUQMPQ DHEJQQ WBFTBM RTC " \
                 "KLBLWYQMLVL QLIMFF RAL WXOMGZYMPCY CL CGPHWSLB " \
                 "GPFGLAG LBJ RDYOLZWSXQ. BYBUHTBMQ MLW ZQFZVRGPXZ " \
                 "OWZABULZ AC LBZGBYMLF’D ZOQF UXYS XOJC, IFBSS " \
                 "LRBCZRNYSCG LJAADLR EC ZFQ YVAILZ YGFCL AC " \
                 "ASXQALTSZJ KORZCLZ HSS CMZBXYG. WSMCZBL " \
                 "JWCQAJMRXK HZ TAPFFXY QZAVJQKXUH EVK " \
                 "QGNXYZLHOTQQ HM HSS CMZBXYG."

    possible_keys = vigenere(exercise1c)
    print("Possible keys:", possible_keys)
    for key in possible_keys:
        print("\nResult of", key)
        print(decrypt_vig(exercise1c.lower(), key))
