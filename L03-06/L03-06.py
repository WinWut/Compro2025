txt='''When the night has come
And the land is dark
And the moon is the only light we'll see
No I won't be afraid
Oh, I won't be afraid
Just as long as you stand, stand by me
So darling, darling
Stand by me, oh stand by me
Oh stand, stand by me
Stand by me
If the sky that we look upon
Should tumble and fall
Or the mountain should crumble to the sea
I won't cry, I won't cry
No, I won't shed a tear
Just as long as you stand, stand by me
And darling, darling
Stand by me, oh stand by me
Oh stand now, stand by me
Stand by me
Darling, darling
Stand by me, oh stand by me
Oh stand now, stand by me, stand by me
Whenever you're in trouble won't you stand by me
Oh stand by me, oh won't you stand now, stand
Stand by me'''
topk=5
texts=txt.split()
words={}
for i in texts: #count
    if i.lower() not in words:
        words[i]=1
    else:
        if i.lower() in words:
            words[i.lower()]+=1
            
words_tup=list(words.items())
for i in range(len(words_tup)-1):
    for j in range(len(words_tup)-1-i):
        if words_tup[j][1]<words_tup[j+1][1]:
            words_tup[j],words_tup[j+1]=words_tup[j+1],words_tup[j]


output={}
k_current=0
rank=1
prev=0
for key,value in words_tup:
    
    if words[key]==prev:
        output[rank-1].append(key)
        continue
    if k_current>=topk:
        break
    else:
        output[rank]=[key]
        rank+=1
        k_current+=1
        prev=value
            
for i in output:
    temp=[]
    for j in output[i]:
        temp.append(f"{j}: {words[j]}")
    print(", ".join(temp))
        
