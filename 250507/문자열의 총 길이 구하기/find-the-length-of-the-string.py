word_list = input().split()

word_sum = 0

for word in word_list :
    word_sum += len(word)


print(word_sum)