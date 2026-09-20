-- Çevirmen notu: Bu dosyadaki Çince INSERT verisi (ör. ürün/şehir/kişi adları) bilinçli olarak çevrilmemiştir.

-- Translated to Turkish by himmetcanumutlu

-- hrs adlı veritabanını oluştur
drop database if exists `hrs`;
create database `hrs` default charset utf8mb4;

-- hrs veritabanına geç
use `hrs`;

-- Departman tablosunu oluştur
create table `tb_dept`
(
`dno` int not null comment 'numara',
`dname` varchar(10) not null comment 'ad',
`dloc` varchar(20) not null comment 'konum',
primary key (dno)
);

-- 4 departman ekle
insert into `tb_dept` values 
    (10, '会计部', '北京'),
    (20, '研发部', '成都'),
    (30, '销售部', '重庆'),
    (40, '运维部', '深圳');

-- Çalışan tablosunu oluştur
create table `tb_emp`
(
`eno` int not null comment 'çalışan numarası',
`ename` varchar(20) not null comment 'çalışan adı',
`job` varchar(20) not null comment 'çalışan pozisyonu',
`mgr` int comment 'yönetici numarası',
`sal` int not null comment 'çalışan aylık maaşı',
`comm` int comment 'aylık ödenek',
`dno` int comment 'bağlı departman numarası',
primary key (eno),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- 14 çalışan ekle
insert into `tb_emp` values 
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
    (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
    (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
    (3211, '张无忌', '程序员', 2056, 3200, null, 20),
    (3233, '丘处机', '程序员', 2056, 3400, null, 20),
    (3251, '张翠山', '程序员', 2056, 4000, null, 20),
    (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
    (5234, '郭靖', '出纳', 5566, 2000, null, 10),
    (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
    (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
    (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
    (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
    (3577, '杨过', '会计', 5566, 2200, null, 10),
    (3588, '朱九真', '会计', 5566, 2500, null, 10);


-- En yüksek maaşlı çalışanın adını ve aylık maaşını sorgula

-- Çalışanların adını ve yıllık maaşını sorgula (yıllık maaş = (sal + comm) * 13)

-- Çalışanı olan departmanların numarasını ve kişi sayısını sorgula

-- Tüm departmanların adını ve kişi sayısını sorgula

-- Maaşı ortalama maaşı aşan çalışanların adını ve maaşını sorgula

-- Maaşı, departmanının ortalama maaşını aşan çalışanların adını, departman numarasını ve maaşını sorgula

-- Departmanındaki en yüksek maaşlı kişinin adını, maaşını ve departman adını sorgula

-- Yöneticilerin adını ve pozisyonunu sorgula

-- Aylık maaşı 4.-6. sırada olan çalışanların sırasını, adını ve aylık maaşını sorgula

-- Her departmanda maaşı ilk 2 de olan çalışanların adını, maaşını ve departman numarasını sorgula
