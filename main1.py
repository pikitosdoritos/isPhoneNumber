import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Мій номер: 415-555-4242.')
print("\nЗнайдений телефоний номер: " + mo.group())


