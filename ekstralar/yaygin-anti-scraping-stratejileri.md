## Yaygın Anti-Scraping Stratejileri ve Başa Çıkma Yöntemleri

> **Translated to Turkish by** himmetcanumutlu

1. Makul HTTP istek başlıkları oluşturun.
   - Accept

   - User-Agent

   - Referer
   
   - Accept-Encoding
   
   - Accept-Language
2. Sitenin oluşturduğu Cookie'yi inceleyin.
   - Kullanışlı eklenti：[EditThisCookie](http://www.editthiscookie.com/)
   - Betik tarafından dinamik oluşturulan Cookie nasıl işlenir
3. Dinamik içeriği kazıma.
   - Selenium + WebDriver
   - Chrome / Firefox - Driver
4. Kazıma hızını sınırlayın.
5. Formdaki gizli alanları işleyin.
   - Gizli alan okunmadan formu göndermeyin
   - RoboBrowser gibi araçlarla form göndermeyi destekleyin
6. Formdaki doğrulama kodunu işleyin.
   - OCR（Tesseract） - ticari projelerde genellikle dikkate alınmaz 

   - Profesyonel tanıma platformu - Chaojiying / Yundama

     ```Python
     from hashlib import md5
     
     class ChaoClient(object):
     
         def __init__(self, username, password, soft_id):
             self.username = username
             password =  password.encode('utf-8')
             self.password = md5(password).hexdigest()
             self.soft_id = soft_id
             self.base_params = {
                 'user': self.username,
                 'pass2': self.password,
                 'softid': self.soft_id,
             }
             self.headers = {
                 'Connection': 'Keep-Alive',
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
             }
     
         def post_pic(self, im, codetype):
             params = {
                 'codetype': codetype,
             }
             params.update(self.base_params)
             files = {'userfile': ('captcha.jpg', im)}
             r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
             return r.json()
     
     
     if __name__ == '__main__':
         client = ChaoClient('kullanıcı adı', 'parola', 'yazılım ID')
         with open('captcha.jpg', 'rb') as file:                                                
             print(client.post_pic(file, 1902))                                          
     ```

7. “Tuzak”ları atlatın.
   - Web sayfasında, kazıyıcıyı kazımaya teşvik eden gizli bağlantılar (tuzak veya bal küpü) vardır
   - Selenium+WebDriver+Chrome ile bağlantının görünür veya görünür alanda olup olmadığını belirleyin
8. Kimliği gizleyin.
   - Proxy hizmeti -  Kuai Proxy / Xun Proxy / Zhima Proxy / Mogu Proxy / Yun Proxy

     [《Hangi Kazıyıcı Proxy'si Daha İyi? On Ücretli Proxy'nin Ayrıntılı Karşılaştırma Değerlendirmesi!》](https://cuiqingcai.com/5094.html)

   - Soğan yönlendirmesi (Tor) - yurt içinde kullanmak için VPN gerekir

     ```Shell
     yum -y install tor
     useradd admin -d /home/admin
     passwd admin
     chown -R admin:admin /home/admin
     chown -R admin:admin /var/run/tor
     tor
     ```
