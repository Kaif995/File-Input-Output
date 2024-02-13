word="xlearning"
with open ("practice.txt" , "r") as f:
    data=f.read()

if(data.find(word) !=-1):
   print("Found")
else:
    print("Word Not found")
