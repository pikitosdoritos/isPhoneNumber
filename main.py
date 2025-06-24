def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('\n415-555-4242 - is Phone number: ', isPhoneNumber('415-555-4242'))
print('\nMoshi moshi - is Phone number: ', isPhoneNumber('Moshi moshi'))

message = 'Подзвони мені завтра за номером 415-555-4292, 415-555-4292 - це телефоний номер мого офісу.'

for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print("Знайдений номер телефону: " + chunk)
print('Готово')