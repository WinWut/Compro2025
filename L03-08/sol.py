# text=str(input("Text: "))
# substring=str(input("Substring: "))
text_input="Hey jude Don’t make it bad"
text=text_input.split()
substring="ude"
result=""
for word in text:
    for i in range(len(word)-len(substring)+1):
        if word[i:i+len(substring)]==substring: 
            result=text_input.replace(substring,f"[{substring}]")
if result:
    print(result)
else:
    print("Not found")
        
    