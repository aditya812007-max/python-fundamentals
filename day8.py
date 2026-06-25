name = []
with open("day8_name.txt","r") as day8_name:
     for line in sorted(day8_name):
          name.append(line.rstrip())
for name in sorted(name,reverse=True)          :
     print(f"hello,{name}")