def ct_vvl(str):
    dic = {'a':0, "e" : 0 ,"i" : 0 ,'o' : 0 ,"u" : 0 }
    for e in str :
        if e in dic.keys():
            dic[e]+=1
    return dic

print(ct_vvl("I am a awesome person"))