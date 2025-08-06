#crash course

print("hello world")#begginer

#comments pake #comment gitu

x= 5
y=10
print(x+y)

#x itu variable dan 5 itu value

A=str(12)
b=float(12)
a= int(13399)

print(A)
print(b)
print(a)
#type data int,float,str kalau int itu angka bulat,float desimal,
#str itu string tapi string adalah intinya string itu huruf dan ga perlu diubah ke angka
#tapi bisa angka dan huruf tanpa quotes 

#bagian 2 Data types
#str Text
#int float =numeric
#bool boolean type
#list,tuple,range =sequence types
x=1
y=2.8
print(type(x))
print(type(y))
#type() itu untuk mengetahui tipe dari data variable
#int itu angka bulat float itu desimal

#python ga punya datatype khusus untuk karakter
#maksudnya adalah datatype khusus untuk karakter itu ga ada
#tapi bisa pake string artinya bisa huruf dan angka

a="nigger"
print(a[1])

#len adalah untuk mengetahui panjang dari string
print(len(a))

#boolean itu buat true atau false

print(5>10)
print(10<12)
print(5==5)

#if statements bahasa simpel nya adalah jika sesuatu maka lakukan sesuatu
#contoh :
x=5
b=10

if x<b:
    print("x lebih kecil dari b")
else:
    print("x lebih kecil dari b")


list=["nigger","sucks","asshole"]
print(len(list))
print(len(list[0]))
#list itu adalah kumpulan data yang bisa diakses dengan index index adalah
#angka dimulai dari 0 
#nah print len list 0 itu ga bisa karena list itu adalah kumpulan data
#jadi by all means itu adalah data dari list itu sendiri
#ingat index itu adalah angka dimulai dari 0

#tuples adalah kumpulan data yang tidak bisa diubah
#jadi kalau list itu bisa diubah tapi tuples itu tidak bisa diubah
#contoh tuples
tuple = ["nigger"]
print(tuple[0])

#set adalah kumpulan data yang tidak bisa ditambahkan dan duplikat
set = ["banna","piano","margaret","banna","piano"]
print(set)

#dictionari adalah kumpulan data yang memiliki key dan value
dict = {
    "name": "Margaret",     
    "age": 30,
    "city": "New York"
}
print(dict["name"]) #tapi hampir mirip dengan set ga boleh ada yang sama
#jadi kalau set itu adalah kumpulan data yang tidak bisa ditambahkan dan duplikat
#tapi kalau dictionary itu adalah kumpulan data yang memiliki key dan value

#conditional statements adalah pernyataan yang bisa dieksekusi
#contoh conditional statements
x = 5   
if x > 5:
    print("x lebih besar dari 5")
elif x == 5:    #elif itu adalah else if 
    print("x sama dengan 5")
else:
    print("x lebih kecil dari 5")

#while loop adalah perulangan yang akan terus berjalan selama kondisi terpenuhi
#contoh while loop
i = 1
while i < 6:
    print(i)
    i += 1  #i += 1 itu sama dengan i = i + 1 #artinya adalah i itu akan bertambah 1 setiap kali perulangan

    #tapi kalau i itu lebih besar dari 6 maka perulangan akan berhenti
