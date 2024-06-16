from colorama import Fore, Style

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

                       iletişim == ig: xsecit""")
