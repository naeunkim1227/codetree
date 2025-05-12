A = input()

# Please write your code here.


def palindrome(s) :
    for i in range(len(s)) :
        if s[i] != s[len(s) - i - 1] :
            return "No"
    return "Yes"


print(palindrome(A))