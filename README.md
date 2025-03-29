# E-commerce Analysis

Bu loyiha elektron tijorat (e-commerce) savdolarini tahlil qilish uchun mo‘ljallangan oddiy Python vositasidir. U foydalanuvchilarga eng ko‘p sotilgan mahsulotlarni ko‘rish va savdo statistikasini grafik shaklida vizualizatsiya qilish imkonini beradi.

## Xususiyatlar
- **Eng Ko‘p Sotilgan Mahsulotlar**: Eng ko‘p sotilgan mahsulotlarni va ularning sotilish sonini ko‘rsatadi.
- **Savdo Statistikasi**: Mahsulotlarning sotuv bo‘yicha taqsimotini grafik shaklida ko‘rsatadi.
- **Chiqish**: Dasturdan chiqish imkoniyati mavjud.

## Dataset

Loyihada ishlatilgan ma'lumotlar Kaggle platformasidan olingan:
Online Retail Dataset

Bu dataset onlayn do‘kon tranzaktsiyalarini o‘z ichiga oladi, jumladan mahsulot kodlari, tavsiflari, miqdorlari va sotuv sanalari.



## O‘rnatish
Python va kerakli kutubxonalarni o‘rnatish uchun quyidagi buyruqlarni bajaring:

```bash
pip install matplotlib
```

## Ishga tushirish
Dasturni ishga tushirish uchun:

```bash
python main.py
```

## Loyiha Tuzilishi
```bash
ecommerce_analysis/
│── data/
│   ├── products.csv          # Mahsulotlar ro‘yxati
│   ├── transactions.csv      # Xaridlar tarixi
│── src/
│   ├── analyzer.py           # Sotuvlarni tahlil qilish
│   ├── data_loader.py        # Ma'lumotlarni yuklovchi modul
│   ├── main.py               # Dasturni ishga tushirish
│   |── visualizer.py         # Grafik chizish
│── README.md                 # Loyihaning tavsifi
```

## 🖼 Natija
Savdo statistikasini grafik shaklda ```sales_chart.png``` fayliga saqlaydi.
