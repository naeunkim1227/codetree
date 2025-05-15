text = input()
pattern = input()

# Please write your code here.


def search_char(text,pattern) :
    text_l ,pattern_l = len(text),len(pattern)
    if text_l < pattern_l :
        return -1
    
    for i in range(text_l - 1) :
        if text[i] + text[i + 1] == pattern :
            return i
    
    
    return -1



result = search_char(text,pattern)
print(result)