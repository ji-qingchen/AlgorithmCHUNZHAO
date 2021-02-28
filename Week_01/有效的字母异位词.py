 s = "anagram"
 t = "nagarax"

# 非函数版
he = {}
if len(s) != len(t):
    print('False')

else:
    for char in s:
        if char in he:
            he[char] += 1
        else:
            he[char] = 1
    print(he)
    for char2 in t:
        if char2 in he:
            he[char2] -= 1
        else:
            print('False')
    for value in he.values():
        if value != 0:
            print('False')
    print('True')                 #无处安放的true


#函数版
def isAnagram( s: str, t: str) -> bool:
    he = {}
    if len(s) != len(t):
        return False
    else:
        #根据字符串s建立dict
        for char in s:     
            if char in he:
                he[char] += 1
            else:
                he[char] = 1
        
        #检验字符串t
        for char2 in t:
            if char2 in he:
                he[char2] -= 1
            else:
                return  False
        for value in he.values():
            if value != 0:
                return False
        return True                    
