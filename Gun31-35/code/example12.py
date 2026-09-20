# Translated to Turkish by himmetcanumutlu

"""
Nesne yönelimli programlamanın üç temel direği: sarmalama (encapsulation), kalıtım, çok biçimlilik
Nesne yönelimli tasarım ilkeleri: SOLID ilkeleri
Nesne yönelimli tasarım desenleri: GoF tasarım desenleri (tekil, fabrika, vekil, strateji, yineleyici)
Aylık maaş sistemi - departman müdürü ayda 15000, programcı saatte 200, satış temsilcisi 1800 taban maaş + satışın %5'i komisyon
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """Çalışan (soyut sınıf)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """Aylık maaşı hesapla (soyut yöntem)"""
        pass


class Manager(Employee):
    """Departman müdürü"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """Programcı"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """Satış temsilcisi"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """Çalışan oluşturan fabrika (fabrika deseni - fabrika aracılığıyla nesne kullanıcısı ile nesne arasındaki bağ çözülür)"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """Çalışan oluştur"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
