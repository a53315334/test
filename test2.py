totlePeople = input("Person:")
data = list(range(1,int(totlePeople)+1))
num=0
queue = 0
while len(data) > 2:
   i=0
   while i < len(data):
        num += 1
        if (num == 3):
           data.pop(i)
           num = 0
           queue +=1
        else :
            i+=1
if len(data) < 3:
    for i in data:
        queue +=1
print("lsat person:"+ str(data[len(data)-1]) + ", last priority:" + str(queue))