count=0
with open("active.txt", "r") as f:
    data = f.read()
    num=data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
print(count)
   #We can also do this!
# with open("active.txt", "r") as f:
#     data = f.read()
#     print(data)
# num=""
# for i in range(len(data)):
#     if (data[i] ==","):
#         print(int(num))
#         num=""
#     else :
#         num+=data[i]