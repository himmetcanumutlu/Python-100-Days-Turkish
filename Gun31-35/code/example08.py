# Translated to Turkish by himmetcanumutlu

"""
Şifreleme ve şifre çözme
Simetrik şifreleme - şifreleme ve çözme aynı anahtarla - DES / AES
Asimetrik şifreleme - şifreleme ve çözme farklı anahtarlarla - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES şifrelemenin anahtarı (uzunluk 32 bayt)
# key = md5(b'1qaz2wsx').hexdigest()
# # AES şifrelemenin başlangıç vektörü (rastgele üretilir)
# iv = Random.new().read(AES.block_size)


def main():
    """Ana fonksiyon"""
    # Anahtar çifti üret
    key_pair = RSA.generate(1024)
    # Açık anahtarı içe aktar
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # Özel anahtarı içe aktar
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # Veriyi şifrele
    data = pub_key.encrypt(message1.encode(), None)
    # Şifrelenmiş veriye BASE64 kodlaması uygula
    message2 = base64.b64encode(data[0])
    print(message2)
    # Şifrelenmiş veriye BASE64 kod çözümü uygula
    data = base64.b64decode(message2)
    # Verinin şifresini çöz
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - simetrik şifreleme
    # str1 = 'Hepinizi seviyorum!'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # Şifrele
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # Şifreyi çöz
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
