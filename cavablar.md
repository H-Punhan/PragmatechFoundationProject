# Ders müddətində verilən sualların cavabları

 ###  index->value ile key->value yanasmalari arasindaki ferqler

  * BIldiyimiz kimi arraylerin elementlerini gormek ucun onlari index deyerleri
   ile cagiririq.Obyektlerde de ise deyerleri gormek ucun key-i cagirmaliyiq
   `
     a=[1,2,3] 
     a[0] 
     o={
   name:'p'
   age:19
   }
   a.name-2
   `
   
    a[0]-burada arrayin index deyeri ile cagirilib
   
   
    o.name-burada obyektin key deyerini cagiririq
   
   
   
   

 ### listin built-in metodlari nelerdir:

 * append() yeni bir element elave edir
 * clear() butun elementleri silir
 * copy() listin copyalarini return edir
 * count() listde secilen elementin uzunlugunu gosterir
 * remove() listde secilen elementi silir 

 ### string-in built-in metodlari nelerdir:
 * capitalize() ilk herfi boyuk edir
 * casefold() butun herfleri kicik edir
 * count() secilen yazinin sayini gosterir
 * iscumeric() stringin reqem olub olmadigini yoxlayir
 * swapcase() stringde olan boyuk herfleri kicik,kicik herfleri boyuk edir

 ### hazir metod istifade etmeden once neler arasdirilmalidir?

 * Hazır metod istifadə etmədən öncə metodun nə olduğunu bilməliyik
   Metod proqramda istifadə olunmaq və kodun təkrar olunmaması üçün yazılmış  kod parçasıdır.Metodları normal function-lardan fəqrli olaraq bir class-a bağlı olur və bağlı olduğu classın icindeki məlumatlarla birlikdə işləyə bilər
   
 * metodun syntax-nı bilməliyik
 
 * istifade qaydasını bilməliyik
  
  
 
 ### class construktor nedir? class ucun ne ehemiyyet dasiyir?

  * constructor bir classdan obyekt yaradmağa kömək edən metoddur.Əyər  constructor olmasa bir classdan defelerle yeni bir obyekt yarada bilmərik.Yəni sadəcə bir obyekt yarada bilərik.
     
 
 ### bir class-da nece eded construktor olabiler

  * Constructor 1 dene  ola biler 
 
 ### constructor ve metod arasindaki ferqler nelerdir

  *  constructor metodlar normal metodlardan ayıran əsas cəhət constructor metodlar vasitəsi ilə yeni yeni data yaradılır
     .Normal metod lar var olan data ilə işləyə bilərlər.Fərlərdən biridə odurki constructor lar adlar cağırılmır onlar sadece yeni data yaradılan zaman paremetr vasitəsi ilə    avtomatik çağırılır.Metodları isə class üzərindən cağırmaq mümkündür.
    
  

 
 ### void ve return function ferqlerini izah edin

  * İksini izah etmək üçün tesevur edin hesabla adlı bir functionımız var bu function-ımızın iki parametri var.Biz   bu      functiona  iki dəyər  verirk.Functiona  verdiyimiz deyeri icinde hesablayıb cavabî return ile
  qaytardıqda bu functionu deyişkene elave ede bilerik anlayacaginiz bir functionda 
  return varsa bu func  deyisken kimi istifade etmek olur.Indi ise return istifade etmirik ve etdiyimiz addımları 
  tekrar edirik amma biz burda return etmediyimiz ucun hemin deyer functionın icinde qalır biz bu deyeri sadece 
  ekrana yazdıra bilerik.Void function ile Return functionun ferqi budur
  
 
 ### parametr ve argument arasinda ferqler nelerdir
 
  * 
    `write(a,b){
    console.log(a,b)
    }
    write(1,1)
    `
    Burada a,b  parametr 1,1 argument dir

### iterator ve iterable nedir  ?

  * iterator iterable obyekte iteration qazandiran obyektdir.
    Iteration qabiliyeti olan obyektlere Iterable obyekt deyilir
    Iterable obyektler uzerinde gezine bilen obyektlerdir.`for ve while ` kimi looplarla 
    uzerinde gezmek mumkundur.Iterable obyektlere lists,array,dictionary ler aiddir.

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
    * Metodlar istenilen 
    hallarda istifade edile biler.Meselen uzun bir metnin uzunlugu tapmaq,
    listden bir deyer silmek veya elave etmek kimi bir cox işlerde istifade olunur
    
    
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
    * args funksiyalarda islenen bir parametrdir.Funksiyada islenen zaman  istediyimiz qeder
      parametr gondermek isteyirik burada komeyimize args catir eyer `*argName` yazarsaq bu bize `tuple` qayıdar
      
    * kwargs ise  funksiyada  parametre `**kwargsName` yazırıq buda bizə `dict` qaytarır
## Python module nədir?
    * Pythonda hazır kodları bir cox yerdə istifadə etmək istəyirik ve onu ayrı bir python faylına yazıb istədiyimiz    
      python faylında cağıra bilirik .Cağırdığımız bu fayl module adlanır.Modullar iki yerə ayrılır.Bizim yazdığımız ve 
      hazır modullar.
## Python package nədir?
    * Modullardan ibaret bir fayldır.
## pass nədir? Nə zaman istifadə olunur?
    * Python da funksyanı və ya bəzi kodları boş buraxmaq istəyiriksə funksyanın içinə pass kəliməsi əlavə edilir.
## List metodlarından 5 ədəd metodun izahatını yazın
    * append() liste element elave etmek ucun istifade olunur
    * remove() listden element silmek ucun istifade olunur
    * pop() icine verilen index deyeri uzre element silir
    * sort() listdeki elementleri siralayir
    * reverse() listdeki elementleri tersine edir
## List və dict hansı hallarda istifadə olunur?
    * Elimizde sadece adlar var bu adları ve onları bir data içine yığmalıyıq 
    liste yığaraq bizim üçün semereli olacaq
    * Bude fe ise elimizde bir cox insana aid detallı melumat var amma liste yığa bilmerik
    çünkı onları elde etmeye çalîşsaq bu melumatların kime aid oldugunu bilmeyeceyik 
    Eyer onları dicte elave etsek  melumatları elde etmek daha asan olacaq
## Dict metodlarından 5 ədəd metodun izahatını yazın
    * pop() verilen keyi silir
    * clear() butun keyleri silir
    * copy() listin kopyasını qaytarır
    * get() secilmis keyin deyerini gosterir
    * update() verilen keyin deyerini deyisir 


# Yeni suallar
## Python class nədir?
  * Sadə yolla desək class-obyekt yardamaga komek eden bir şablondur.Örnək olaraq bir maşın zavodumuz var.Burada maşına aid olan ortaq ozəlliklər var.Bu  özəlliklərlə  biz bu zavodu istifadə edə bilmərik amma bu zavod vasitəsi minlərlə ilə yeni maşınlar düzəldə bilərik.Bu düzəltəcəyimiz maşının adı obyektdir.
## Python object nədir?
  * Proqramlamada gördüyümüz hər şey obyektdir.Yəni real həyatdan istənilən canlı və cansız hər şeyi obyekt olaraq ifadə edə bilərik.Bu obyektlərin real həyatdakı özəlliklərini obyektə əlavə edə bilərik.
## Python construktor nədir?
  * Bu metod bir class-ın qurucu metodudur.Bu metod vasitəsi ilə ibyektlə yaradılır.Əyər bu metod istifadə edilməsə belə class-ın sadəcə bir obyekt yaradmağa kömək edən default bir constructoru olur.Bu metodlar yalnız bir obyekti yaradarkən çağrılır yəni onları çağıra bilmərik.
## object property nədir
  * Bir obyektin əsas hissəsi olan propert-lər obyektin novunə görə dəyişiklik göstərə bilər.Məsələn adı soyadı yası kimi 
  məlumatlar daşıyan hissələr property lər sayılır.
## objct method nədir
  * kod təkrarını azaldmaq üçün yazılan hazır kod parçalarıdır.Metodlar iki yerə ayrılır hazır metodlar və sonradan yazılan metodlar.Metodlar yaradıldığı classın propertyləri ilə işləyə bilir ve class üzərindən cağrıla bilir.

## oop inheritance nədir?