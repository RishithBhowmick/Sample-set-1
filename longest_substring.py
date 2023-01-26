def longest_sub_string(s1,s2):
    if s1=="" or s2=="":
        return ""
    if s1==s2:
        return s1
    l1 = len(s1)
    l2 = len(s2)
    if l1<l2:
        l = l1
        while(l!=0):
            for i in range(0,l1-l+1):
                sub_s = s1[i:i+l]
                if sub_s in s2:
                    return sub_s
            
            l-=1
        return ""
    else:
        l = l2
        while(l!=0):
            for i in range(0,l2-l+1):
                sub_s = s2[i:i+l]
                if sub_s in s1:
                    return sub_s
            
            l-=1
        return ""

print(longest_sub_string("abcdef","qwertyuiopabcdef"))
print(longest_sub_string("abcdef","qwerty"))
print(longest_sub_string("",""))
print(longest_sub_string("abc","abc"))
print(longest_sub_string("zzzaaab","abc"))
print(longest_sub_string("aaaa","bbbb"))
