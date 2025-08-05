txt=str(input("Text: "))
# txt="SUN TON BOW GOD LOT KID FAX BAT FAT CAR EAT FEE SEA MAP DRY SPY TAP"
texts=txt.split()
prev=""
chains=[]
chain=[]
for word in texts:
    diff=0
    
    if not prev:
        prev=word
    else:
#         print(prev,word)
        for k in range(len(word)):
                             
            if prev[k]!=word[k]:
                diff+=1
#         print(diff)
        
        if diff>=3:
            chains.append(chain)
            chain=[word]
        else:
            chain.append(word)
        prev=word
        
if chain:
    chains.append(chain)

maxlen=-99999999
for i in range(len(chains)):
    if len(chains[i])>maxlen:
        maxlen=len(chains[i])

print(f"{len(chains)} Chain(s). Maximum length is {maxlen} word(s).")