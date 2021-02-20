## Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin
    * Interpreted diller compiler dilin eksine kodlari  setir-setir oxuyuub maşın koduna çevirir.Buda 
      onu cevirme zamanaı complier dile gore daha daha yavas edir çünki daha cox calisir.Amma interpreted
      dilde buglari tapmaq daha asanddir.Bunun sebebi interpreted  dilde bir setrde sef varsa o setrde ve onnan sonraki
      setrlerdeki isi dayndirir.Eyer onnan evvelki setrde kodlar duzgun isdiyirse o kodlar calisir.İnterpreted dillere `
      Javascript,Python,Php 
      ` kimi diller daxildir
    
## Interpreted və compiler dillər arasında olan fərqləri izah edin
    * Complier diller interpreted dillere gore  daha suretlidir.Sebebi Compiler diller  butovlukde oxunub  ve hetta 
      bosluqlarida oxuyub masin koduna cevrilir.Compiler dillerde bug     
      tapmaq daha cetindi 
      cunki complier dillerde kodun istenilen yerinde olan koddaki sefde kodun calismasi dayandirilir.Cevirme zamani complier evvelceden kodun tutacagi yeri kod ucun ayirir .
      
## Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin
    * `str`- (`string`)-bu data tipi her hansi bir yere bir yazi,cumle,boyuk bir metn yazmag istedikde istifade olunur
      
    * `int`-  (`integer`)-tam reqemleri ifade edir

    * `float`-tam olmayan reqemleri ifade edir

    * `bool` -sedece iki deyer ala bilir `true ve false` ikilik say sisteminde 0 ve 1 kimi dusune bilersiniz

    *  'list,tuple'-birden cox dataya  sahib ola bilen bir tipdir
        lakin `tuple `data tipinin  deyerleri  deyistirile bilmez

    *  `dict`-bu data tipinde datalari yerlesdirmek ucun onlara key-ler elave edirikki onlari cagiran 
        zaman onlari key-leri ile cagira bilirik.Keyler eyni adda ola bilmez

## Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin
    * OOP gorulen isleri obyektler uzerinden gorduyumuz bir proqramlama uslubudur.OOP yaranma meqsedi
      gorulen isleri parcalara ayirmaq ve az kod yazaraq zaman qazanmaga komek edir.Class komeyi ile yaranan obyektlerde metod yazib istediyimiz vaxt istediyimiz yerde cagira bilerik.Buda bize eksta komek olur.

## Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?
    * 
    
## local və global variable nədir izah edin
    * variable-yaradan vaxt onun hara yerləşdiyi önəmlidir.Əyər var-ı istədiyiniz yerdən cağıra biləsiniz onda `globalda`

      yəni bütün funksiyaların vəya kod bloklarını xaricində yaradasınız.Yox əyər var-ı yalnız müəyyən yerlərdə vəya bir funksiyanın içində istifadə edə bilərsiniz.Bunun üçün onu istifadə edəcəyiniz funksiyanın içində yəni `localda`
      yaradmalısınız
    
## Python type conversion haqqında izahat verin
    * Bir data tipini bize lazım olmadığı üçün tipini dəyiştirməyə ehtiyacımız olur 
      Örnək üçün `"50"+50` bizə error verəcək çünki birinci 50 tipi string digərinin tipi integer  oldugu üçün stringde `+` birləştirmədə istifədə olunur integerde isə toplama üçün onların tipləri bir birinə uyğun gəlmir.Bunu
      həll etmək üçün `int("50")+50` yazmağımız kifayətdir
      
## init nədir?
    * Bir constructor metodu-dur yeni onun sayesinde Class-larda obyektler yaradmaq mümkündür.Eyer çöoldən əlaqe
      qqurmaq istiyirksə `self` parametri əlavə edilmelidir
## self nədir?
    * Class İçindəki özəllikləri istifadə üçün istifadə olunur.Class larda istifadə olunarkən `__init__` metoduna  və    digər metodlara `self` parametr olaraq verilmelidir.
      self  yazıldığı class-ı ifadə edir .İçindəki property-leri istifade etmek istəyiriksə `self.Propname`  yazırıq
## *args,*kwargs nədir? nə zaman istifadə olunur?
## Python module nədir?
## Python package nədir?
## pass nədir? Nə zaman istifadə olunur?
## List metodlarından 5 ədəd metodun izahatını yazın
## List və dict hansı hallarda istifadə olunur?
## Dict metodlarından 5 ədəd metodun izahatını yazın