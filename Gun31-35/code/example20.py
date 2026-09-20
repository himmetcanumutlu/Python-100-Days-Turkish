# Translated to Turkish by himmetcanumutlu

"""
İş parçacıkları arası iletişim (veri paylaşımı) çok basittir çünkü aynı sürecin belleğini paylaşabilirler
Süreçler arası iletişim (veri paylaşımı) görece zahmetlidir çünkü işletim sistemi sürece ayrılan belleği korur
Çok süreçli iletişimi gerçekleştirmek için genellikle sistem boruları, soketler ve üçüncü taraf hizmetler kullanılabilir
multiprocessing.Queue
Koruyucu iş parçacığı - daemon thread
Koruyucu süreç - firewalld / httpd / mysqld
Sistem kapanırken korunmayan süreç - süreç henüz bitmedi diye sistemin durmasını engellemez
"""
from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')


def main():
    Thread(target=output, args=('Ping', ), daemon=True).start()
    Thread(target=output, args=('Pong', ), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
