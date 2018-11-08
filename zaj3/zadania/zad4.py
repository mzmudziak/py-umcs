import re

regex_pesel = re.compile(r'^(?P<pesel>'
                         r'(?P<year>\d\d)'
                         r'(?P<month>\d\d)'
                         r'(?P<day>\d\d)'
                         r'\d\d\d'
                         r'(?P<sex>\d)'
                         r'\d'
                         r')$')

match = regex_pesel.match('93041511592')

print('year: ', match.group('year'))
print('year: ', match.group('month'))
print('year: ', match.group('day'))
print("plec: ", 'male' if int(match.group('sex')) % 2 else 'female')
