#Server untuk client

#kegiatan 1
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind (("", 50003))
s.listen (1)
print ("Penjawab otomatis sudah siap")
data = ""
kata = {"nama" : "Anisa Ghoyatul Firdaus",
        "NIM" : "L200180135",
        "angkatan" : "2018",
        "keluar" : "siap!"}
while data.lower() != "keluar" :
    komm, addr = s.accept()
    while data.lower() != "keluar" :
        data = komm.recv (1024)
        if data.lower () == "keluar" :
            print "siap!"
            s.close()
            break
        print ("Pertanyaan:") , data
        if kata.has_key(data) :
            komm.send (kata[data])
        else :
            komm.send ("Maaf, pertanyaan tidak dimengerti")


#kegiatan 2
import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind (("", 50002))
s.listen (5)
print "Server sudah siap"
perintah = ""


while perintah.lower () != "quit" :
    komm, addr = s.accept()
    while perintah.lower () != "quit" :
        perintah = komm.recv (1024)
        if perintah.lower () == "machine" :
            respon = platform.machine ()
            komm.send (respon)
        elif perintah.lower () == "system" :
            respon = platform.system ()
            komm.send (respon)
        elif perintah.lower () == "release" :
            respon = platform.release ()
            komm.send (respon)
        elif perintah.lower () == "version" :
            respon = platform.version ()
            komm.send (respon)
        elif perintah.lower () == "node" :
            respon = platform.node ()
            komm.send (respon)
        else :
            komm.send ("uknown command")


#kegiatan 3
import socket

def piramid (la = 0 , lb = 0):
    L = la * 4 * lb
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind (("", 50008))
s.listen (5)
print "Server sudah siap"
data = ""

while 1 :
    komm, addr = s.accept () 
    while data.lower () != "keluar" :
        data = komm.recv (1024)
        print "Pesan :" , data
        if data.find ("parameter") != -1 : 
            param, value = data.split ("-")
            if param == "parameter" :
                a = float (value)
                x = value
                komm.send ("parameter dicatat")
            elif data == "hitung" :
                komm.send ("luas piramida dengan luas alas {} dan luas bidang {} adalah {}", format(x, piramida(la, lb)))
            else :
                komm.send ("tidak ada")
