# Translated to Turkish by himmetcanumutlu

"""
Sihirli yöntemler
Özel bir nesneyi küme (set) içine koymak ya da sözlüğün (dict) anahtarı olarak kullanmak istiyorsanız
__hash__ ve __eq__ adlı iki sihirli yöntemi yeniden yazmanız zorunludur
Birincisi nesnenin hash kodunu hesaplamak, ikincisi iki nesnenin aynı olup olmadığını belirlemek için kullanılır
Hash kodu farklı olan nesneler kesinlikle farklı nesnelerdir, ama hash kodu aynı olanlar aynı nesne olmayabilir (hash kodu çakışması)
Bu yüzden hash kodu aynı olduğunda nesnenin aynı olup olmadığını __eq__ ile belirlemek gerekir
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, '王大锤'))
    # students.add(Student(1001, '王大锤'))
    # students.add(Student(1001, '白元芳'))
    # print(len(students))
    # print(students)
    stu = Student(1234, '骆昊')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('Qianfeng Eğitim')
    school[1001] = Student(1001, '王大锤')
    school[1002] = Student(1002, '白元芳')
    school[1003] = Student(1003, '白洁')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()
