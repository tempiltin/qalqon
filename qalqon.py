#!/usr/bin/env python3

import sys
import argparse
import nmap

def main():
    # Argumentlarni aniqlash
    parser = argparse.ArgumentParser(
        description="Qalqon - Nmap asosida tarmoq xavfsizligini tekshiruvchi vosita",
        usage="""
  ___        _                   
 / _ \   __ _| |  __ _   ___   _ __  
| | | | / _` | | / _` | / _ \ | '_ \ 
| |_| |  (_| | |  (_| |  (_)  | | | |
 \__\_\ \__,_|_| \__, | \___/ |_| |_|
                    |_|            
                                 
       https://tempiltin.uz      
                                                                                           
                                                                                     
                                                                            
                                                               
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
                                       Natijalarni faylga yozish"""
    )

    parser.add_argument("target", nargs="?", help="Skanerlash uchun IP manzil yoki domen")
    parser.add_argument("--os-detect", action="store_true", help="Operatsion tizimni aniqlash")
    parser.add_argument("--service-detect", action="store_true", help="Portlarda xizmatlarni aniqlash")
    parser.add_argument("--scripts", help="Nmap skriptlarini ishlatish (masalan: vuln)")
    parser.add_argument("--report", help="Skaner natijalarini faylga saqlash")

    # Argumentlarni o'qish
    args = parser.parse_args()

    if not args.target:
        print("\nQalqon - Nmap asosida tarmoq xavfsizligini tekshiruvchi vosita\n")
        parser.print_usage()  # `usage` qismini chiqaradi
        print("\nOpsiyalar:")
        print("  --os-detect          Operatsion tizimni aniqlash")
        print("  --service-detect     Portlarda xizmatlarni aniqlash")
        print("  --scripts <script>   Nmap skriptlarini ishlatish (masalan: vuln)")
        print("  --report <file>      Natijalarni faylga yozish\n")
        print("Misollar:")
        print("  qalqon 192.168.1.1                   Oddiy skanerlash")
        print("  qalqon 192.168.1.1 --os-detect       OS aniqlash")
        print("  qalqon 192.168.1.1 --service-detect  Xizmatlarni aniqlash")
        print("  qalqon 192.168.1.1 --scripts vuln    Zaifliklarni aniqlash")
        print("  qalqon 192.168.1.1 --report result.txt")
        print("                                       Natijalarni faylga yozish")
        sys.exit(0)  # Dasturni to'xtatish

    # Agar argumentlar mavjud bo'lsa, skanerlash boshlanadi
    scanner = nmap.PortScanner()
    print(f"Skanerlash boshlanmoqda: {args.target}")

    # Nmap uchun variantlarni to'plash
    options = "-Pn"
    if args.os_detect:
        options += " -O"
    if args.service_detect:
        options += " -sV"
    if args.scripts:
        options += f" --script {args.scripts}"

    try:
        # Skanerni ishga tushirish
        results = scanner.scan(hosts=args.target, arguments=options)
        print("Skanerlash natijalari:")
        print(results)

        # Agar `--report` ishlatilgan bo'lsa, natijalarni faylga saqlash
        if args.report:
            with open(args.report, "w") as report_file:
                report_file.write(str(results))
            print(f"Natijalar saqlandi: {args.report}")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Qalqon dasturi ishga tushdi")
    main()
