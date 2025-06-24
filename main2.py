import re

heroRegex = re.compile(r'Batman|Tina Fey')
mol = heroRegex.search("Batman and Tina Fey.")  
print(mol.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mob = batRegex.search("Btmobile загубив колесо")
if mob:
    print(mob.group())
else:
    print('xD')