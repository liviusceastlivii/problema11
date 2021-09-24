n=int(input('Dati numarul de elemente din vector='))
z=[]
# if n<10:
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    z.extend([x])
print(z)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(z[:5])

print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:',*z[::-1])
b=sorted(z)
b.sort(reverse=True)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(z)
c.sort(reverse=True)
print(c)

print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        y=z[i]
        d.extend([y])
print(d)

print('e) Afişează pe ecran media aritmetică a componentelor pare:', sum(c) / len(c))
d = []
for k in range(0, len(z)):
    if z[k] % 2 != 0:
        y = z[k]
        d.extend([y])

print('f) Afişează pe ecran doar componentele impare: ', *d)
x, y = eval(input('Dati valorile x, y: '))
e = []
for l in z:
    if (l > x) and (l % y != 0):
        e.extend([l])
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
g=[]
for i in z:
    if(i>x) and (i%y!=0):
        g.extend([i])
        print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')

h=[]
for i in z:
    if ((i>x)and(i<y)):
        z=i
        h.extend([z])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')

u=[]
for i in e:
    if i<0:
        u.extend([z.index(i)])
print(u)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j = z.copy()
j[0] = min(z)
print('k) Înlocuieşte prima componentă a tabloului cu componenta cu valoare minimă din tabloul respectiv: ', j)
j = z.copy()
j[j.index(min(j))] = j[0]


print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=z.copy()
l[z.index(min(l))]=l[0]
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for q in z:
    if (q % 2 == 0):
        m.extend([q])
        print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for w in z:
    if (w % 3 == 0):
        n.extend([w])
        print(n)
