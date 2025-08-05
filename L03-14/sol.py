dna="CGTCGTCCTACAGCATGAGCATCATCAGCCCATTGTCATGC"

transforms={'A':'U','C':'G','G':'C','T':'A'}

rna=""
for i in dna:
    for j in transforms:
        if i==j:
            rna+=transforms[j]
namino=0
foundstart=False
# rna="GCAUGAGCCAGUACACCUAAAGU"
rnaamino=""
stopcolon=["UAA","UGA","UAG"]
for i in range(len(rna)-2):
    count=0
    if not foundstart:
    
        temp=""
        temp+=rna[i]+rna[i+1]+rna[i+2]
        
        
    if temp=="AUG":
        foundstart=True
        for j in range(i,len(rna[i:]),3):

            if rna[j:j+3] in stopcolon:
                break
            rnaamino+="["+rna[j:j+3]+"]"
            count+=1
            left=j+3
    
#             rnaamino+="["+rna[i]
        rnaamino+=rna[left:]
        break
    rnaamino+=rna[i]

print(f"{count} Amino acid(s)")