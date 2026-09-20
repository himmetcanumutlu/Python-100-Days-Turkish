-- Translated to Turkish by himmetcanumutlu

-- İşlem tablosu
CREATE TABLE `transaction` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'işlem numarası',
  `member_id` bigint(20) NOT NULL COMMENT 'işlemi yapan kullanıcı ID',
  `amount` decimal(8,2) NOT NULL COMMENT 'işlem tutarı',
  `integral` int(11) NOT NULL DEFAULT '0' COMMENT 'kullanılan puan',
  `pay_state` tinyint(4) NOT NULL COMMENT 'ödeme türü 0: bakiye 1: WeChat 2: Alipay 3: xxx',
  `source` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'ödeme kaynağı wx app web wap',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'ödeme durumu -1: iptal 0 tamamlanmadı 1 tamamlandı -2: anormal',
  `completion_time` int(11) NOT NULL COMMENT 'işlem tamamlanma zamanı',
  `note` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'not',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `transaction_order_sn_member_id_pay_state_source_status_index` (`order_sn`(191),`member_id`,`pay_state`,`source`(191),`status`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- İşlem kayıt tablosu
CREATE TABLE `transaction_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `events` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'olay ayrıntısı',
  `result` text COLLATE utf8mb4_unicode_ci COMMENT 'sonuç ayrıntısı',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Sipariş tablosu
CREATE TABLE `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'sipariş numarası',
  `order_sn` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'işlem numarası',
  `member_id` int(11) NOT NULL COMMENT 'müşteri numarası',
  `supplier_id` int(11) NOT NULL COMMENT 'satıcı kodu',
  `supplier_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'satıcı adı',
  `order_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'sipariş durumu 0 ödenmedi, 1 ödendi, 2 kargoya verildi, 3 teslim alındı, -1 iade başvurusu, -2 iadede, -3 iade edildi, -4 işlem iptal',
  `after_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'kullanıcı satış sonrası durumu 0 başvuru yok 1 başvuruldu -1 iptal edildi 2 işleniyor 200 tamamlandı',
  `product_count` int(11) NOT NULL DEFAULT '0' COMMENT 'ürün adedi',
  `product_amount_total` decimal(12,4) NOT NULL COMMENT 'ürün toplam fiyatı',
  `order_amount_total` decimal(12,4) NOT NULL DEFAULT '0.0000' COMMENT 'gerçek ödeme tutarı',
  `logistics_fee` decimal(12,4) NOT NULL COMMENT 'kargo ücreti',
  `address_id` int(11) NOT NULL COMMENT 'teslimat adresi kodu',
  `pay_channel` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'ödeme kanalı 0 bakiye 1 WeChat 2 Alipay',
  `out_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'sipariş ödeme numarası',
  `escrow_trade_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'üçüncü taraf ödeme akış numarası',
  `pay_time` int(11) NOT NULL DEFAULT '0' COMMENT 'ödeme zamanı',
  `delivery_time` int(11) NOT NULL DEFAULT '0' COMMENT 'kargolama zamanı',
  `order_settlement_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'sipariş mutabakat durumu 0 mutabakat yok 1 mutabakat yapıldı',
  `order_settlement_time` int(11) NOT NULL DEFAULT '0' COMMENT 'sipariş mutabakat zamanı',
  `is_package` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'paket mi',
  `is_integral` enum('0','1') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0' COMMENT 'puan ürünü mü',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_sn_unique` (`order_sn`),
  KEY `order_order_sn_member_id_order_status_out_trade_no_index` (`order_sn`,`member_id`,`order_status`,`out_trade_no`(191))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Satış sonrası başvuru tablosu
CREATE TABLE `order_returns_apply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'sipariş numarası',
  `order_detail_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'alt sipariş kodu',
  `return_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'satış sonrası numarası',
  `member_id` int(11) NOT NULL COMMENT 'kullanıcı kodu',
  `state` tinyint(4) NOT NULL COMMENT 'tür 0 yalnızca iade 1 iadeli geri ödeme',
  `product_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'ürün durumu 0: teslim alındı 1: teslim alınmadı',
  `why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'iade/değişim nedeni',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'inceleme durumu -1 reddedildi 0 incelenmedi 1 onaylandı',
  `audit_time` int(11) NOT NULL DEFAULT '0' COMMENT 'inceleme zamanı',
  `audit_why` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'inceleme nedeni',
  `note` text COLLATE utf8mb4_unicode_ci COMMENT 'not',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Satış sonrası kayıt tablosu
CREATE TABLE `order_returns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `returns_no` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'iade numarası, müşteri sorgusu için',
  `order_id` int(11) NOT NULL COMMENT 'sipariş numarası',
  `express_no` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'lojistik numarası',
  `consignee_realname` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'teslim alan kişi adı',
  `consignee_telphone` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'iletişim telefonu',
  `consignee_telphone2` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'yedek iletişim telefonu',
  `consignee_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'teslimat adresi',
  `consignee_zip` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'posta kodu',
  `logistics_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'lojistik yöntemi',
  `logistics_fee` decimal(12,2) NOT NULL COMMENT 'lojistik kargo ücreti',
  `order_logistics_status` int(11) DEFAULT NULL COMMENT 'lojistik durumu',
  `logistics_settlement_status` int(11) DEFAULT NULL COMMENT 'lojistik mutabakat durumu',
  `logistics_result_last` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'lojistik son durum açıklaması',
  `logistics_result` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'lojistik açıklaması',
  `logistics_create_time` int(11) DEFAULT NULL COMMENT 'kargolama zamanı',
  `logistics_update_time` int(11) DEFAULT NULL COMMENT 'lojistik güncelleme zamanı',
  `logistics_settlement_time` int(11) DEFAULT NULL COMMENT 'lojistik mutabakat zamanı',
  `returns_type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 tümü iade 1 kısmi iade',
  `handling_way` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'PUPAWAY: iade depoya; REDELIVERY: yeniden gönderim; RECLAIM-REDELIVERY: iadesiz yeniden gönderim; REFUND: geri ödeme; COMPENSATION: iadesiz tazminat',
  `returns_amount` decimal(8,2) NOT NULL COMMENT 'geri ödeme tutarı',
  `return_submit_time` int(11) NOT NULL COMMENT 'iade başvuru zamanı',
  `handling_time` int(11) NOT NULL COMMENT 'iade işleme zamanı',
  `remark` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'iade nedeni',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Değerlendirme tablosu
CREATE TABLE `order_appraise` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL COMMENT 'sipariş kodu',
  `info` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'yorum içeriği',
  `level` enum('-1','0','1') COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'seviye -1 olumsuz 0 nötr 1 olumlu',
  `desc_star` tinyint(4) NOT NULL COMMENT 'açıklama uyumu 1-5',
  `logistics_star` tinyint(4) NOT NULL COMMENT 'lojistik hizmeti 1-5',
  `attitude_star` tinyint(4) NOT NULL COMMENT 'hizmet tutumu 1-5',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_appraise_order_id_index` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;