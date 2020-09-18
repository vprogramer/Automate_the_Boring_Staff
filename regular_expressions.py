import re


phoneNumber = re.compile(r'\d\d\d-\d\d-\d\d')
mo = phoneNumber.search("Number: 236-01-62")
print(mo.group())

phoneGroupNumber = re.compile(r'(\d\d\d)-(\d\d-\d\d)')
mo1 = phoneGroupNumber.search("Number: 236-01-62")
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(0))

phoneNumberWithPrefiks = re.compile(r'8029|8033|8036')
mo2 = phoneNumberWithPrefiks.search('8029 283 13 84')
mo3 = phoneNumberWithPrefiks.search('8055 902 92 37')
print(mo2.group())
# print(mo3.group()) # Error NoneType
