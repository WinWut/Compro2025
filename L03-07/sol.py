words={"arm":["n","แขน"],
       "hello":["v","สวัสดี"],
       "beautiful":["adj","สวย"],
       "toilet":["n","ห้องน้ำ"],
       "kick":["v","เตะ"],
       "handsome":["adj","หล่อ"]}
while True:
    text=str(input(""))
    if text=="0":
        break
    if text not in words:
        print("Word not in dictionary.")
        continue
    while True:
        ch=(input(""))
        if ch=="1":
            print(words[text][0])
            break
        elif ch=="2":
            print(words[text][1])
            break
        else:
            print("Invalid option.")
