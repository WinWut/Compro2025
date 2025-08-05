current=str(input("Input current time: "))
nap=int(input("Input nap time: "))
snooze=int(input("Input snooze time: "))
hr,mn=[int(i) for i in current.split(":")]

currentnap=0
print("Nap time starts.")
while True:
    
    mn+=1
    
    if mn==60:
        hr+=1
        mn=0
    if hr==24:
        hr=0
        
    if currentnap==nap:
        ch=str(input("Alarm rings. Dismiss or Snooze: "))
        if ch=="Snooze":
            nap=snooze
            currentnap=0
        elif ch=="Dismiss":
            break
    
    currentnap+=1
    print(f"{hr:0{2}d}:{mn:0{2}d}")
    
    