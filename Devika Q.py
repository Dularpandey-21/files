f=open("Devika.txt","r")
a=f.read()
count=a.split()
n="Navya"
for i in count:
    if i==n:
        pass
    else:
        print(i)
f.close()