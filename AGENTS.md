# AGENTS.md

Bu dosya, bu depoda çalışacak yapay zekâ asistanları (Claude, Copilot, Cursor vb.) için rehberdir.

## Bu Proje Nedir

Bu depo, [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) adlı Çince kaynağın **eksiksiz Türkçe çevirisidir**.

- **Orijinal yazar**: 骆昊 (jackfrued) — orijinal içerik ve tüm telif hakları ona aittir.
- **Çevirmen**: himmetcanumutlu.
- Orijinal depo lisanssız olduğundan bu depo da herhangi bir açık lisans sağlamaz; ayrıntı için `NOTICE.md` dosyasına bakın.

## Çeviri Durumu

- Tüm 125 `.md` ders dosyası, kod dosyaları (`.py`, `.java`, `.sql`, `.html`) ve 7 Jupyter notebook tamamen Türkçeye çevrilmiştir.
- Çeviri **tamamlanmıştır**; kalan Çince karakterler **bilinçli olarak** bırakılmıştır (aşağıya bakın).

## Kasıtlı Olarak Bırakılan Çince İçerikler — ÇEVİRME

Aşağıdaki Çince içerikler kasıtlı olarak çevrilmemiştir; bunları çevirmeye çalışma:

- `骆昊` (yazar) ve `王大锤` / `白元芳` gibi yer tutucu/kurgusal kişi adları.
- Notebook'larda okunan **veri dosyası sütun adları** (ör. `销售额` = satış tutarı, `售价` = satış fiyatı). Çevrilirse `df['销售额']` gibi kod erişimleri bozulur.
- Çin il/şehir adları (pyecharts haritasıyla eşleşme için zorunlu).
- Ürün, meyve, kıyafet, sporcu adları gibi örnek/gerçek veriler; `微软雅黑` font adı.
- 89. Gün (NLP) ve 97. Gün (ElasticSearch) örneklerindeki jieba/ik sözcük bölümleme Çince test verisi.

Bu kasıtlı Çince yerlerin bulunduğu notebook hücrelerinde ve SQL dosyalarında "Çevirmen notu" yorumu zaten eklenmiştir.

## Çalışma Kuralları

- **Orijinalde olmayan içerik ekleme.** Bu depo yalnızca çeviridir; yeni ders, terim sözlüğü, SSS vb. ekleme.
- Kod örnekleri tek tek test edilmemiştir; yalnızca çevrilmiştir. Bir kod hatası görülürse önce orijinal depoyla karşılaştır (bkz. `CONTRIBUTING.md`).
- Yazar atfı `骆昊 (jackfrued)`, çevirmen atfı himmetcanumutlu olarak korunur.
