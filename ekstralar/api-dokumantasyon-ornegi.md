## Arayüz Dokümantasyonu Referans Örneği

> **Translated to Turkish by** himmetcanumutlu

0. Kullanıcı girişi - **POST** `/api/login/`

      Geliştirici：骆昊

      Sürüm numarası：v1

      Son değişiklik zamanı：

      Arayüz açıklaması：Giriş başarılı olduktan sonra kullanıcı token'i üretilir veya güncellenir.

      Kullanım yardımı：Test veritabanında aşağıdaki tabloda gösterildiği gibi kullanılabilir dört hesap önceden tanımlıdır.

      | Kullanıcı adı | Kullanıcı parolası | Rol         |
      | ---------- | -------- | ------------ |
      | jackfrued  | 123456   | yönetici       |
      | wangdachui | 123123   | normal kullanıcı     |
      | hellokitty | 123123   | emlak danışmanı |
      | wuzetian   | 123456   | ev sahibi         |

      İstek parametreleri：

      | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama     |
      | -------- | ------ | -------- | -------- | -------- |
      | username | string | evet       | mesaj gövdesi   | kullanıcı adı   |
      | password | string | evet       | mesaj gövdesi   | kullanıcı parolası |

      Yanıt bilgisi：

      - Giriş başarılı：

        ```JSON
        {
            "code": 30000,
            "message": "Kullanıcı girişi başarılı",
            "token": "f83e0f624e2311e9af1f00163e02b646"
        }
        ```

      - Giriş başarısız：

        ```JSON
        {
            "code": 30001,
            "message": "Kullanıcı adı veya parola hatalı"
        }
        ```

1. SMS doğrulama kodu gönderme - **GET** `/api/mobile_code/{yurt içi cep telefonu numarası}/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：Belirtilen cep telefonu numarasına SMS doğrulama kodu gönderen arayüz; cep telefonu numarası yurt içi numara olmalıdır ve yol parametresi olarak URL'ye yazılır. Arayüz SMS gönderiminin başarılı olduğunu gösterdiğinde, belirtilen cep telefonu numarası SMS'i almaz; çünkü kullanılan üçüncü taraf SMS platformunun verdiği test SMS'leri bitmiştir.

   Kullanım yardımı：Yurt içi cep telefonu numarası şimdilik uluslararası alan kodunu desteklemez.

   İstek parametreleri：Yok.

   Yanıt bilgisi：

   - İstek başarılı：

     ```JSON
     {
         "code": 10001,
         "msg": "SMS doğrulama kodu başarıyla gönderildi"
     }
     ```

   - İki istek arasındaki süre 60 saniyeden az：

     ```JSON
     {
         "code": 10002,
         "msg": "Lütfen 60 saniye içinde cep telefonu doğrulama kodunu tekrar göndermeyin"
     }
     ```

   - Cep telefonu numarası geçersiz：

     ```JSON
     {
         "code": 10003,
         "msg": "Lütfen geçerli bir cep telefonu numarası sağlayın"
     }
     ```

   - SMS servisi platformu arızası：

     ```JSON
     {
         "code": 10004,
         "msg": "SMS servisi şu anda kullanılamıyor"
     }
     ```

2. Tüm eyalet düzeyi idari birimleri alma - **GET** `/api/districts/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：Yok.

   Kullanım yardımı：Yok.

   İstek parametreleri：Yok.

   Yanıt bilgisi：

   ```JSON
   [
       {
           "distid": 110000,
           "name": "Beijing"
       },
       {
           "distid": 120000,
           "name": "Tianjin"
       }
   ]
   ```

3. Belirtilen idari birimin detayını ve yönetimindeki idari birimleri alma - **GET** `/api/districts/{idari birim numarası}/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：URL parametresiyle idari birim numarası belirtilir; idari birim numarası eyalet düzeyi bir idari birimin numarasıysa, o eyaletin ve eyalete bağlı il düzeyi idari birimlerin bilgisi döner; idari birim numarası il düzeyi bir idari birimin numarasıysa, o ilin ve ile bağlı ilçe/semt bilgisi döner; idari birim numarası ilçe/semt düzeyi bir idari birimin numarasıysa, o ilçe/semtin bilgisi döner ve alt idari birimlerin `cities` özniteliğinin değeri `[]` olur.

   Kullanım yardımı：Veritabanında Sichuan Eyaleti dışındaki idari birimlerin "intro" verisi girilmemiştir; bu alan boş string olabilir.

   İstek parametreleri：Yok.

   Yanıt bilgisi：

   ```JSON
   {
       "distid": 510000,
       "name": "Sichuan",
       "intro": "Çin'in güneybatısında, iç bölgede yer alır; doğuda Chongqing, güneyde Yunnan ve Guizhou, batıda Tibet, kuzeyde Shaanxi, Gansu ve Qinghai ile komşudur; Sichuan Eyaleti'nin toplam yüzölçümü 486.000 kilometrekaredir; eyalet merkezi Chengdu'dur. 2018 yılı sonu itibarıyla Sichuan Eyaleti'ne bağlı 18 il düzeyi şehir, 3 özerk il, 17 ilçe düzeyi şehir, 108 ilçe, 4 özerk ilçe ve 54 şehir semti bulunmaktadır.",
       "cities": [
           {
               "distid": 510100,
               "name": "Chengdu"
           },
           {
               "distid": 510300,
               "name": "Zigong"
           },
           {
               "distid": 510400,
               "name": "Panzhihua"
           }
       ]
   }
   ```

4. Popüler şehirleri alma - **GET** `/api/hotcities/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：Yok.

   Kullanım yardımı：Yok.

   İstek parametreleri：Yok.

   Yanıt bilgisi：

   ```JSON
   [
       {
           "distid": 110100,
           "name": "Beijing"
       },
       {
           "distid": 120100,
           "name": "Tianjin"
       },
       {
           "distid": 130100,
           "name": "Shijiazhuang"
       }
   ]
   ```

5. Emlak danışmanı bilgilerini sayfalı alma - **GET** `/api/agents/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：Danışman adı, önek bulanık eşleşme biçiminde işlenir; danışman hizmet yıldızı, danışmanın hizmet yıldızının bu yıldızdan düşük olamayacağı anlamına gelir; danışmanın sertifikalı olup olmadığı yalnızca 0 (sertifikasız çalışıyor) ve 1 (sertifikalı çalışıyor) olmak üzere iki seçenektir. Üç parametrenin temsil ettiği filtre koşulları arasındaki ilişki "ve"dir. Dönüş sonucu, sayfalanmış emlak danışmanı bilgisidir.

   Kullanım yardımı：Yok.

   İstek parametreleri：

   | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama                                |
   | ------ | ------ | -------- | -------- | ---------------------------------|
   | name   | string | hayır       | sorgu parametresi | danışman adı                          |
   | key    | string | hayır       | sorgu parametresi | danışman hizmet yıldızı                      |
   | cert   | string | hayır       | sorgu parametresi | danışmanın sertifikalı olup olmadığı                      |
   | page   | tamsayı   | hayır       | sorgu parametresi | sayfa numarası, varsayılan 1                     |
   | size   | tamsayı   | hayır       | sorgu parametresi | sayfa boyutu, varsayılan 5, en fazla 50 |

   Yanıt bilgisi：

   ```JSON
   {
       "count": 1,
       "next": null,
       "previous": null,
       "results": [
           {
               "agentid": 6,
               "estates": [
                   {
                       "estateid": 11,
                       "name": "Lingzhi Xincun",
                       "hot": 20
                   }
               ],
               "name": "Xiao Lili",
               "tel": "13040813886",
               "servstar": 4,
               "realstar": 4,
               "profstar": 4,
               "certificated": false
           }
       ]
   }
   ```

6. Yeni emlak danışmanı ekleme - **POST** `/api/agents/`

   Geliştirici：骆昊

   Sürüm numarası：v1

   Arayüz açıklaması：Yok.

   Kullanım yardımı：Giriş yapılmalı ve yönetici yetkisine sahip olunmalıdır; kullanıcı kimlik token'i istek başlığında sağlanır.

   İstek parametreleri：

   | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama             |
   | ------------ | ------ | -------- | -------- | ---------------- |
   | name         | string | evet       | mesaj gövdesi   | danışman adı       |
   | tel          | string | evet       | mesaj gövdesi   | danışman cep telefonu       |
   | servstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | realstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | profstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | certificated | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | token        | string | evet       | istek başlığı   | kullanıcı kimlik doğrulama token'i |

   Yanıt bilgisi：

   - Ekleme başarılı - durum kodu **201**：

     ```JSON
     {
         "agentid": 8,
         "estates": [],
         "name": "Sun Xiaomei",
         "tel": "13800991234",
         "servstar": 0,
         "realstar": 0,
         "profstar": 0,
         "certificated": false
     }
     ```

   - Kimlik doğrulama bilgisi sağlanmadı - durum kodu **401**：

     ```JSON
     {
         "detail": "Hatalı kimlik doğrulama bilgisi."
     }
     ```

   - Mevcut kullanıcının işlem yetkisi yok - durum kodu **403**：

     ```JSON
     {
         "detail": "Bu işlemi gerçekleştirme yetkiniz yok."
     }
     ```

7. Emlak danışmanı bilgilerini düzenleme - **PUT** `/api/agents/{emlak danışmanı numarası}/`

    Geliştirici：骆昊

    Sürüm numarası：v1

    Arayüz açıklaması：Yok.

    Kullanım yardımı：Giriş yapılmalı ve yönetici yetkisine sahip olunmalıdır; kullanıcı kimlik token'i istek başlığında sağlanır.

    İstek parametreleri：

   | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama             |
   | ------------ | ------ | -------- | -------- | ---------------- |
   | name         | string | evet       | mesaj gövdesi   | danışman adı       |
   | tel          | string | evet       | mesaj gövdesi   | danışman cep telefonu       |
   | servstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | realstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | profstar     | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | certificated | tamsayı   | hayır       | mesaj gövdesi   | varsayılan 0          |
   | token        | string | evet       | istek başlığı   | kullanıcı kimlik doğrulama token'i |

    Yanıt bilgisi：

   - Güncelleme başarılı - durum kodu **200**：
      
     ```JSON
     {
         "agentid": 1,
         "estates": [
             {
                 "estateid": 1,
                 "name": "Jinri Jiayuan",
                 "hot": 20
             },
             {
                 "estateid": 2,
                 "name": "Feicui Yuan",
                 "hot": 30
             },
             {
                 "estateid": 3,
                 "name": "Vanke City Garden",
                 "hot": 22
             }
         ],
         "name": "Yuan Xiaomeng",
         "tel": "158173555285",
         "servstar": 5,
         "realstar": 4,
         "profstar": 3,
         "certificated": true
     }
     ```

   - Kimlik doğrulama bilgisi sağlanmadı - durum kodu **403** - eklemeyle aynı
   - Mevcut kullanıcının işlem yetkisi yok - durum kodu **403** - eklemeyle aynı

8. Emlak danışmanını silme - **DELETE** `/api/agents/{emlak danışmanı numarası}/`

    Geliştirici：骆昊

    Sürüm numarası：v1

    Arayüz açıklaması：Yok.

    Kullanım açıklaması：Yok.

    İstek parametreleri：

   | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama             |
   | ------ | ------ | -------- | -------- | ---------------- |
   | token  | string | evet       | istek başlığı   | kullanıcı kimlik doğrulama token'i |

    Yanıt bilgisi：

   - Silme başarılı - durum kodu **204**
   - Kimlik doğrulama bilgisi sağlanmadı - durum kodu **403** - eklemeyle aynı
   - Mevcut kullanıcının işlem yetkisi yok - durum kodu **403** - eklemeyle aynı

9. Emlak projesi bilgilerini sayfalı alma - **GET** `/api/estates/`

    Geliştirici：骆昊

    Sürüm numarası：v1

    Arayüz açıklaması：Danışman adı, önek bulanık eşleşme biçiminde işlenir; danışman hizmet yıldızı, danışmanın hizmet yıldızının bu yıldızdan düşük olamayacağı anlamına gelir; danışmanın sertifikalı olup olmadığı yalnızca 0 (sertifikasız çalışıyor) ve 1 (sertifikalı çalışıyor) olmak üzere iki seçenektir. Üç parametrenin temsil ettiği filtre koşulları arasındaki ilişki "ve"dir. Dönüş sonucu, sayfalanmış emlak danışmanı bilgisidir.

    Kullanım yardımı：Yok.

    İstek parametreleri：

   | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama                                |
   | ------ | ------ | -------- | -------- | ----------------------------------- |
   | name   | string | hayır       | sorgu parametresi | emlak projesi adı (bulanık eşleşme)                  |
   | dist   | string | hayır       | sorgu parametresi | emlak projesinin bulunduğu bölge numarası                    |
   | page   | tamsayı   | hayır       | sorgu parametresi | sayfa numarası, varsayılan 1                     |
   | size   | tamsayı   | hayır       | sorgu parametresi | sayfa boyutu, varsayılan 5, en fazla 50 |

    Yanıt bilgisi：

    ```JSON
    {
        "count": 16,
        "next": "https://120.77.222.217/api/estates/?page=2",
        "previous": null,
        "results": [
            {
                "estateid": 6,
                "district": {
                    "distid": 440303,
                    "name": "Luohu"
                },
                "agents": [
                    {
                        "agentid": 2,
                        "name": "Yang Wei",
                        "tel": "13352939550",
                        "servstar": 3
                    },
                    {
                        "agentid": 4,
                        "name": "Guo Zhipeng",
                        "tel": "13686810707",
                        "servstar": 4
                    }
                ],
                "name": "Xingfuli",
                "hot": 300,
                "intro": ""
            }
        ]
    }
    ```

10. Yeni emlak projesi ekleme - **POST** `/api/estates/`

  Geliştirici：骆昊

  Sürüm numarası：v1

  Arayüz açıklaması：Yok.

  Kullanım yardımı：Giriş yapılmalı ve yönetici yetkisine sahip olunmalıdır; kullanıcı kimlik token'i istek başlığında sağlanır.

  İstek parametreleri：

  | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama                     |
  | ------ | ------ | -------- | -------- | ------------------------ |
  | name   | string | evet       | mesaj gövdesi   | emlak projesi adı                 |
  | hot    | tamsayı   | hayır       | mesaj gövdesi   | emlak projesi popülerliği, varsayılan 0        |
  | intro  | string | hayır       | mesaj gövdesi   | emlak projesi tanıtımı, varsayılan boş string |
  | distid | tamsayı   | evet       | mesaj gövdesi   | emlak projesinin bulunduğu bölge numarası         |
  | token  | string | evet       | istek başlığı   | kullanıcı kimlik doğrulama token'i         |

  Yanıt bilgisi：

  - Ekleme başarılı - durum kodu **201**：
     ```JSON
     {
         "estateid": 17,
         "district": 510107,
         "name": "Shiji Jinyuan",
         "hot": 100,
         "intro": ""
     }
     ```

  - Kimlik doğrulama bilgisi sağlanmadı - durum kodu **403**：
     ```JSON
     {
         "detail": "Lütfen geçerli kimlik doğrulama bilgisi sağlayın"
     }
     ```

  - Mevcut kullanıcının işlem yetkisi yok - durum kodu **403**：
     ```JSON
     {
         "detail": "You do not have permission to perform this action."
     }
     ```

11. Emlak projesi bilgilerini düzenleme - **PUT** `/api/estates/{emlak projesi numarası}`

12. Emlak projesini silme - **DELETE** `/api/estates/{emlak projesi numarası}`

13. Tüm konut tipi bilgilerini alma - **GET** `/api/housetypes/`

14. Yeni konut tipi ekleme - **POST** `/api/housetypes/`

15. Konut tipi bilgilerini düzenleme - **PUT** `/api/housetypes/{konut tipi numarası}`

16. Konut tipini silme - **DELETE** `/api/housetypes/{konut tipi numarası}`

17. Konut kaydı bilgilerini sayfalı alma - **GET** `/api/houseinfos/`

     Geliştirici：骆昊

     Sürüm numarası：v1

     Arayüz açıklaması：Yok.

     Kullanım yardımı：Yok.

     İstek parametreleri：    

     | Parametre adı | Tür   | Zorunlu mu | Parametre konumu | Açıklama                                |
     | --------- | ------ | -------- | -------- | ----------------------------------- |
     | title     | string | hayır       | sorgu parametresi | konut başlığı anahtar kelimesi                      |
     | dist      | tamsayı   | hayır       | sorgu parametresi | emlak projesinin bulunduğu bölge numarası                    |
     | min_price | tamsayı   | hayır       | sorgu parametresi | fiyat aralığının alt sınırı                        |
     | max_price | tamsayı   | hayır       | sorgu parametresi | fiyat aralığının üst sınırı                        |
     | type      | tamsayı   | hayır       | sorgu parametresi | konut tipi numarası                            |
     | page      | tamsayı   | hayır       | sorgu parametresi | sayfa numarası, varsayılan 1                     |
     | size      | tamsayı   | hayır       | sorgu parametresi | sayfa boyutu, varsayılan 5, en fazla 50 |

     Yanıt bilgisi：
     ```JSON
     {
         "count": 7,
         "next": "http://localhost:8000/api/houseinfos/?dist=440303&page=2",
         "previous": null,
         "results": [
     
         ]
     }
     ```

18. Konut kaydı detayını görüntüleme - **GET** `/api/houseinfos/{konut kaydı numarası}`

19. Yeni konut kaydı ekleme - **POST** `/api/houseinfos/`

20. Konut kaydı bilgilerini düzenleme - **PUT** `/api/houseinfos/{konut kaydı numarası}`

21. Konut kaydını silme - **DELETE** `/api/houseinfos/{konut kaydı numarası}`

22. Rastgele belirtilen sayıda konut etiketi alma - **GET** `/api/tags/`

23. Konut etiketlerini sayfalı görüntüleme - **GET** `/api/tags/`

24. Yeni konut etiketi ekleme - **POST** `/api/tags/`

25. Konut etiketini silme - **DELETE**  `/api/tags/{konut kaydı numarası}`

26. Konut kaydının görsellerini görüntüleme - **GET** `/api/houseinfos/{konut kaydı numarası}/photos/`

27. Konut kaydına görsel ekleme - **POST** `/api/houseinfos/{konut kaydı numarası}/photos/`

28. Konut görselini silme - **DELETE** `/api/houseinfos/{konut kaydı numarası}/photos/{görsel numarası}`
