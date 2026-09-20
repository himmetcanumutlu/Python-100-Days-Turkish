-- Çevirmen notu: Bu dosyadaki Çince INSERT verisi (ör. ürün/şehir/kişi adları) bilinçli olarak çevrilmemiştir.

-- Translated to Turkish by himmetcanumutlu

drop database if exists `app_store`;

create database `app_store` default character set utf8mb4;

use `app_store`;

create table `app_info` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id, uygulamanın id si',
`app_name` varchar(255) default '' comment 'ad',
`icon_url` varchar(255) default '' comment 'ikon adresi',
`version` varchar(32) default '' comment 'sürüm numarası',
`app_size` varchar(32) default '' comment 'paket boyutu',
`banner_info` varchar(4096) default '' comment 'banner bilgisi',
`developer_id` varchar(255) default '' comment 'geliştirici id',
`summary` varchar(512) default '' comment 'kısa tanıtım',
`app_desc` text comment 'ayrıntılı bilgi',
`download_url` varchar(255) default '' comment 'indirme bağlantısı',
`price` int(10) default '0' comment 'fiyat, birim: cent',
`status` tinyint(4) unsigned default '0' comment 'durum, 1: incelemede, 2: onaylandı, 3: yayından kaldırıldı',
`version_desc` varchar(4096) default '' comment '',
`create_time` datetime not null default '0000-00-00 00:00:00' comment 'oluşturma zamanı',
`update_time` datetime not null default '0000-00-00 00:00:00' comment 'güncelleme zamanı',
primary key (`id`)
) engine=innodb auto_increment=100000 default charset=utf8mb4 comment='app基本信息表';

create table `app_ext_info` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`install_count` bigint(20) unsigned not null default '0' comment 'uygulama kurulum sayısı',
`score` int(10) unsigned not null default '0' comment 'puan',
`comment_count` int(10) unsigned not null default '0' comment 'yorum sayısı',
`create_time` int(10) not null default 0 comment 'oluşturma zamanı',
`update_time` int(10) not null default 0 comment 'güncelleme zamanı',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='App扩展信息表';

create table `app_category` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`parent_id` bigint(20) not null default '0' comment 'üst kategori id',
`name` varchar(64) not null default '' comment 'kategori adı',
`icon` varchar(512) not null default '' comment 'ikon adresi',
`category_desc` text comment 'kategori açıklaması',
`category_level` tinyint(4) unsigned not null default '0' comment 'kategori seviyesi',
`status` tinyint(4) unsigned not null default '0' comment 'mevcut durum, 1: kullanımda, gizli',
`display_order` int(10) unsigned not null default '0' comment 'sıralama, değer ne kadar büyükse o kadar önde',
`create_time` int(10) not null default 0 comment 'oluşturma zamanı',
`update_time` int(10) not null default 0 comment 'güncelleme zamanı',
primary key (`id`)
) engine=innodb default charset=utf8mb4 comment='分类信息表';

create table `app_category_rel` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`category_id` bigint(20) unsigned not null default '0' comment 'en alt seviye kategori id',
primary key (`id`),
unique key `idx_category_app` (`category_id`,`app_record_id`),
) engine=innodb default charset=utf8mb4 comment='App和分类关联表';

create table `app_comment` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`title` varchar(255) default '' comment 'yorum başlığı',
`content` varchar(2048) default '' comment 'yorum içeriği',
`parent_id` bigint(20) default '0' comment 'üst yorum id',
`commenter_uid` bigint(20) default '0' comment 'yorum yapan kullanıcı id',
`commenter_name` varchar(255) default '' comment 'yorum yapan kullanıcı adı',
`commenter_avatar` varchar(255) default '' comment 'yorum yapan kullanıcı avatarı',
`top_flag` tinyint(4) default '0' comment 'sabitleme durumu',
`like_count` int(10) default '0' comment 'yorumun beğeni sayısı',
`status` tinyint(4) default '0' comment 'yorum durumu',
`create_time` int(10) not null default 0 comment 'oluşturma zamanı',
`update_time` int(10) not null default 0 comment 'güncelleme zamanı',
primary key (`id`),
key `idx_app_status` (`app_id`, `status`, `top_flag`)
) engine=innodb default charset=utf8mb4 comment='评论信息表';

create table `user_app_relation` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`user_id` bigint(20) unsigned not null default '0' comment 'kullanıcı id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`create_time` int(10) not null default 0 comment 'oluşturma zamanı',
`update_time` int(10) not null default 0 comment 'güncelleme zamanı',
`is_del` tinyint(4) not null default '0' comment '1: silindi 0: silinmedi',
primary key (`id`),
key `idx_user_app` (`user_id`,`app_id`)
) engine=innodb auto_increment=8063 default charset=utf8mb4 comment='用户购买关系表';

create table `bot_score` (
`id` bigint(20) not null auto_increment comment 'otomatik artan id',
`app_id` bigint(20) not null default '0' comment 'app_id',
`score` int(10) default '0' comment 'kullanıcı puanı',
`commenter_uid` bigint(20) default '0' comment 'puanlayan kullanıcı id',
`status` tinyint(4) default '0' comment 'puanlama durumu',
`create_time` int(10) not null default 0 comment 'oluşturma zamanı',
`update_time` int(10) not null default 0 comment 'güncelleme zamanı',
primary key (`id`),
unique key `idx_uid_score` (`app_id`,`commenter_uid`)
) engine=innodb default charset=utf8mb4 comment='App评分表';