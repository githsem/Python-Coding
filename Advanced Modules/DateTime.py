from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

tarih = datetime.now()
suan = tarih.timestamp()
print(suan)

suan2 = tarih.fromtimestamp(0)
print(suan2)