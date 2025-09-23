import re

match = re.search(r'\d{1,2}\s(Января|Февраля|Марта|Апреля|Мая|Июня|Июля|Августа|Сентября|Октября|Ноября|Декабря)\s\d{1,4}', r'12 Августа 23')
print(match[0] if match else 'Not found')