#coding:utf8
import base64
stringv = base64.b64encode("FIT{}")
key = "key"

def strint(str_list1,str_list2):
    orstr_list1 = [ord(i) for i in str_list1]
    orstr_list2 = [ord(j) for j in str_list2]
    return orstr_list1,orstr_list2


def padd(stirng_v1,string_v2):
    list_stirng_v1,list_stirng_v2 = strint(list(stirng_v1),list(string_v2))
    ex = len(list_stirng_v1)-len(list_stirng_v2)
    if ex >= 0:
        for i in range(ex):
            list_stirng_v2.append(0)
        return list_stirng_v1,list_stirng_v2
    else:
        for i in range(abs(ex)):
            list_stirng_v1.append(0)
        return list_stirng_v1,list_stirng_v2

def encrypt(flag,key):
    stringv,key = padd(flag,key)
    print stringv
    print key
    return [i^j for i,j in zip(stringv[::-1],key)],key

def hex_l(a):
    a_hex = []
    for i in a:
        a_hex.append("%02x" % i)
    return "".join(a_hex)

def mai(stringv,key):
    fl = encrypt(stringv,key)
    sa=hex_l(fl[0])
    fl = hex_l(fl[1])
    return sa,":",fl

mai(stringv,key)
