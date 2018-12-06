#Client untuk server

#kegiatan 1
import socket

hostname = "localhost"
pesan = ""
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ((hostname, 50003))
print ("mesin penjawab otomatis sudah siap")
while pesan.lower() != "keluar" :
    pesan = raw_input ("Pertanyaan :")
    s.send (pesan)
    if pesan.lower() != "keluar" :
        response = s.recv (1024)
        print ("Jawaban") , response
s.close ()

#kegiatan 2
import socket

hostname = "localhost"
pesan = ""
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ((hostname, 50002))
print "program komunikasi tentang server"
while pesan.lower () != "quit" :
    pesan = raw_input ("Command :")
    s.send (pesan)
    if pesan.lower == "quit" :
        s.close ()
        break
    elif pesan.lower () != "quit" :
        response = s.recv (1024)
        print "Response :" , response
s.close ()

#kegiatan 3
import socket

hostname = "localhost"
pesan = ""
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ((hostname, 50008))
print "menghitung luas piramida"

while luasalas and luasbidang  != "keluar" :
    luasalas = int(input ("luas alas :"))
    s.send (luasalas)
    luasbidang = int(input("luas bidang :"))
    if luasalas.lower () and luasbidang.lower == "keluar" :
        response = s.recv (1024)
        print "respon : -"
        s.close ()
        break
    elif luasalas.lower () and luasbidang () != "keluar" :
        response = s.recv (1024)
        print "respon :" , response
s.close ()
