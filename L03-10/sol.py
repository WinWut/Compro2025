nwords=int(input("Input number of words: " ))
words_list=[]
for i in range(nwords):
    words_list.append(str(input("")))

# words_list=['approach', 'answer', 'knight', 'flutter', 'kamikaze', 'lockup', 'keep off']
words={}
for i in words_list:
    if i[0] not in words:
        words[i[0]]=1
    else:
        words[i[0]]+=1

maxn=-99999
wordsmax=""
for i in words:
    
    if words[i]> maxn:
        maxn=words[i]
        wordsmax=i

count=0
result=[]
for i in words_list:
    if i[0]==wordsmax:
        count+=1
        result.append(i)
print("The popular character is", wordsmax)
print("The character is used in", count,"words.")
for i in result:
    print(i)
