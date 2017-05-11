d = { 'animales': ['perro','gato','loro'],
      'personas': ['garay'],
      'aliens':['chumichumi']
}
d['personas'].append('verdun')
print (d['personas'])

f=open ("alessa.txt", "w")
f.write("prueba metodo 1")
f.close()

with open ("alessa.txt","w") as f:
    f.write ("prueba metodo 2")

l=[]
f=open("alessa.txt","r")
for line in f:
    l.append(line)
    print(line)
f.close

g=[1,2,3,4]
f=open("alessa2.txt","w")
g=open("alessa3.txt","w")
for item in l:
    f.write(str(item)+"\n")
f.close

h=[]
f=open("alessa2.txt","r")
for line in f:
    h.append((line))
f.close
