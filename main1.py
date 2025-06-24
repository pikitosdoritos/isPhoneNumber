import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Мій номер: 415-555-4242.')
print("\nЗнайдений телефоний номер: " + mo.group())


phoneNumberRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumberRegex1.search('Мій номер: 415-555-4242.')
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(0))
print(mo1.group())
print(mo1.groups())

areaCode, mainNumber = mo1.groups()
print(areaCode)
print(mainNumber)

phoneNumberRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumberRegex2.search('Мій номер: (415) 555-4242.')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))
print(mo2.group())
print(mo2.groups())

areaCode, mainNumber = mo2.groups()
print(areaCode)
print(mainNumber)