import datetime


def tänane_kuupäev():
    # annab meile tänase kuupäeva
    return datetime.date.today()

def kuupäev_str(kp):
    # saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return kp.strftime("%d.%m.%y")

def arvuta_visiidi_kuupäev(p_külastuse_kuupäev):
    #p_külastus_kuupäev = viimane külastus
    p_täna = tänane_kuupäev()
    # liidame pool aastat (182 päeva) viimasele 
    p_uus_visiidiaeg = p_külastuse_kuupäev + datetime.timedelta(182)
    if p_uus_visiidiaeg <= p_täna:
        p_uus_visiidiaeg = p_täna + datetime.timedelta(1)
    return p_uus_visiidiaeg

print("Hambaid tuleks lasta kontrollida vähemalt kaks korda aastas.")
print("Millal viimati hambaarsti juures käisid?")

try:

    visiidi_kuupäev = input("Sisesta kuupäev (kujul pp.kk.aaaa): ")
    #toimub logi_fail.txt'sse kirjutamine
    logi_fail_a = open("logi_fail.txt", "a")
    logi_fail_a.write(str(visiidi_kuupäev)+"\n")
    logi_fail_a.close()

    i_päev, i_kuu, i_aasta = map(int, visiidi_kuupäev.split('.'))
    külastuse_kuupäev = datetime.date(i_aasta, i_kuu, i_päev)
    if külastuse_kuupäev > tänane_kuupäev():
        print("Tulevikus ei saanud visiidil käia.")
    else:
        print("Viimane külastus oli: " + kuupäev_str(külastuse_kuupäev))
        uus_külastus = arvuta_visiidi_kuupäev(külastuse_kuupäev) 
        print("Peaksid minema uuele visiidile umbes: " + kuupäev_str(uus_külastus))
except Exception as külastus_viga:
    print("Sisestasid kuupäeva vales formaadis!")
    # errorid kantakse logifaili
    logi_fail_a = open("logi_fail.txt", "a")
    logi_fail_a.write(str(külastus_viga)+"\n")
    logi_fail_a.close()

