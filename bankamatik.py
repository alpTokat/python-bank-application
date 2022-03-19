hesaplar = [{"ad": "Alp Tokat","hesapNo":"123456789","bakiye":3000,"ekHesap":2000},
            {"ad": "Ahmet Tokat","hesapNo": "987654321","bakiye":2000,"ekHesap":1000}]

def hesapGiris(dictList):
    print(f"Hosgeldin sistemi giris yapildi")
    inputKey = input("t:Para transfer\nc:Para cekme\ny:Para Yatirma")
    if inputKey == "y":
        hesapYatirma(dictList)
    elif inputKey == "c":
        hesapCekme(dictList)
    elif inputKey == "t":
        paraTransfer(dictList)
        
        
def hesapCekme(hesap):
    cekmeTutar = int(input("Cekmek istediginiz tutari giriniz: "))
    if hesap["bakiye"] > cekmeTutar:
        hesap["bakiye"] -= cekmeTutar
        print("Guncel bakiyeniz:{}".format(hesap["bakiye"]))
    else:
        print("Yetersiz Bakiye")    
        
        
def hesapYatirma(hesap):
    yatirmaTutar = int(input("Yatirmak istediginiz tutari giriniz: "))
    hesap["bakiye"] += yatirmaTutar
    print("Guncel bakiyeniz:{}".format(hesap["bakiye"]))

def paraTransfer(hesap):
    transferHesap = input("Transfer edeceginiz hesabin hesap numarasini giriniz: ")
    transferTutar = int(input("Transfer edilecek tutari giriniz: "))
    kontrol = False
    for bul in range(0,len(hesaplar)):
        if transferHesap == hesaplar[bul]["hesapNo"]:
            kontrol = True
            hesap["bakiye"] -= transferTutar
            hesaplar[bul]["bakiye"] += transferTutar
    if kontrol == False:
        print("Gondermek istedigini hesap numarasini eksik veya yanlis girdiniz")
    else: 
        print("Guncel Bakiyeniz:{}".format(hesap["bakiye"]))         

hesapNo = input("9 haneli hesap Numaranizi Giriniz: ")
kontrol = False       
for x in range(0,len(hesaplar)):
    if hesapNo == hesaplar[x]["hesapNo"]:
        hesapGiris(hesaplar[x])
        kontrol = True
if kontrol == False:
    print("Hesap numarasini yanlis yada eksik tuslandiniz")
print(hesaplar)