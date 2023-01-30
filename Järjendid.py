


#slovo_list="Ellujäämine õppimise teele"

#a=int(input("Valige üksus, mille soovite eemaldada"))
#if a>0 and a<len(slovo_list):
#    slovo_list.pop(a-1)
#    print(slovo_list)
#else:
#    print("ei ole see postion")



#a=input("Valige täht, mille soovite eemaldada")
#a=a.lower()
#listcopy_list=[]
#for t in (slovo_list):
#    listcopy_list.append(t.lower())
#print(listcopy_list)
#h=listcopy_list.count(a)

#if h>0:
#    for i in range(h):
#        listcopy_list.remove(a)
#else:
#    print("Seda kirja pole olemas")
#print(listcopy_list)



#a=input("Sisestage täht")
#i=int(input("Sisestage soovitud positsiooni number"))
#slovo_list.insert(i-1,a)
#print(slovo_list)




#1-6 funktsioonid

#järjend=[]
#print("Valige teile kõige rohkem meeldiv valik vahemikus 1 kuni 6")
#while True:
#    print("1-sõnad suurtähtedega")
#    print("2-väikeste tähtedega sõnad")
#    print("3-Stringi poolitamine eraldajaga ")
#    print("4-Teisendab stringi esimese tähemärgi suurtähtedeks ja kõik muud märgid väiketähtedeks")
#    print("5-Teisendab väikesed tähed suurtähtedeks ja suurtähed väiketähtedeks")
#    print("6-Teisendab iga sõna esimese tähe suurtähtedeks ja kõik ülejäänud väiketähtedeks")
#    print("0-Väljund")
#    pan_Am=float(input())
#    if pan_Am==1:
#        a=input("Sisestage täht või sõna: ")
#        print(a.upper())
#        print(f"on lisatud {a} ",järjend)
        
#    elif pan_Am==2:
#        b=input("Sisestage täht või sõna: ")
#        print(b.lower())
#        print(f"on lisatud {b} ",järjend)

#    elif pan_Am==3:
#        s=input("Sisestage täht või sõna: ")
#        print(s.split())
#        print(f"on lisatud {s} ",järjend)

#    elif pan_Am==4:
#        c=input("Sisestage täht või sõna: ")
#        print(c.capitalize())
#        print(f"on lisatud {c} ",järjend)

#    elif pan_Am==5:
#        v=input("Sisestage täht või sõna: ")
#        print(v.swapcase())
#        print(f"on lisatud {v} ",järjend)

#    elif pan_Am==6:
#        b=input("Sisestage täht või sõna: ")
#        print(b.title())
#        print(f"on lisatud {b} ",järjend)

#    elif pan_Am==0:
#        break


nimed=("Anna","Inna","Olga","Anna","Inga","Anna")

nimi=input("Mis nimi on vaja otsida?")
n=nimed.count(nimi)
for i in range(n):
    j=nimed.index(nimi,i)
    print(f"{nimi} on {j}. kohal")
