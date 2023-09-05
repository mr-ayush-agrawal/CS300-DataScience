def Ceaser(text , shift):
    text = text.upper()
    print(text)
    lst = ""
    for e in text:
        n = ord(e) + shift
        if n > ord('Z'):
            n-=26
        lst+=chr(n)
    return lst

print(Ceaser("Ayush",1))