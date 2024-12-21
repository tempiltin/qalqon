# Qalqon

Qalqon - bu Nmap asosida tarmoq xavfsizligini tekshiruvchi vosita. Ushbu dastur yordamida siz tarmoqdagi zaifliklarni aniqlash, operatsion tizimni va xizmatlarni aniqlash, shuningdek, zaifliklarni aniqlash uchun skriptlarni ishga tushirishingiz mumkin.

---

## O'rnatish

Qalqonni Arch Linux tizimiga o'rnatish uchun quyidagi bosqichlarni bajaring:

### 1. Python kutubxonalarini o'rnatish
Dastur uchun kerakli kutubxonani o'rnating:
```bash
sudo pacman -S python-pip
pip install python-nmap
```

### 2. Skriptni ko'chirish
`qalqon.py` faylni o'rnating va uni bajariladigan faylga aylantiring:
```bash
chmod +x qalqon.py
sudo mv qalqon.py /usr/local/bin/qalqon
```

Endi siz tizimingizda `qalqon` komandasidan foydalana olasiz.

---

## Foydalanish

Dasturdan foydalanish uchun quyidagi formatda komanda bering:
```bash
qalqon <target> [options]
```

### Opsiyalar:
| Opsiya              | Tavsif                                           |
|---------------------|--------------------------------------------------|
| `--os-detect`       | Operatsion tizimni aniqlash                     |
| `--service-detect`  | Portlarda xizmatlarni aniqlash                  |
| `--scripts <script>`| Nmap skriptlarini ishlatish (masalan: `vuln`)    |
| `--report <file>`   | Natijalarni ko'rsatilgan faylga yozish          |

### Misollar:
- Oddiy skanerlash:
  ```bash
  qalqon 192.168.1.1
  ```
- OS aniqlash:
  ```bash
  qalqon 192.168.1.1 --os-detect
  ```
- Xizmatlarni aniqlash:
  ```bash
  qalqon 192.168.1.1 --service-detect
  ```
- Zaifliklarni aniqlash:
  ```bash
  qalqon 192.168.1.1 --scripts vuln
  ```
- Natijalarni faylga yozish:
  ```bash
  qalqon 192.168.1.1 --report result.txt
  ```

---

## Ishga tushirishda chiqadigan xabar
Agar `qalqon` komandasini yozsangiz, dastur ishlashni boshlaydi va quyidagi xabarni chiqaradi:

```plaintext
Qalqon - Nmap asosida tarmoq xavfsizligini tekshiruvchi vosita

Foydalanish:
  qalqon <target> [options]

Opsiyalar:
  --os-detect          Operatsion tizimni aniqlash
  --service-detect     Portlarda xizmatlarni aniqlash
  --scripts <script>   Nmap skriptlarini ishlatish (masalan: vuln)
  --report <file>      Natijalarni faylga yozish

Misollar:
  qalqon 192.168.1.1                   Oddiy skanerlash
  qalqon 192.168.1.1 --os-detect       OS aniqlash
  qalqon 192.168.1.1 --service-detect  Xizmatlarni aniqlash
  qalqon 192.168.1.1 --scripts vuln    Zaifliklarni aniqlash
  qalqon 192.168.1.1 --report result.txt
                                       Natijalarni faylga yozish
```

---

## Qalqon komandasini ishga tushirish

Qalqon dasturini ishga tushirish uchun faqat quyidagilarni kiriting:
```bash
qalqon
```

Ushbu komanda dokumentatsiyani va ishlatilish bo'yicha yordamni ko'rsatadi.
