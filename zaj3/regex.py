# regexes

import re

regex_email = re.compile(
    r'''(?P<adres>
            (?P<login>[\w+.]+)
            @
            (?P<domena>\w+(\.\w+)+)
        )
    ''',
    re.IGNORECASE | re.VERBOSE
)

# + --> jeden lub wiecej
# . --> jakikolwiek jeden znak
# * --> zero lub wiecej (cokolwiek)



text = u'mail1@gmail.com, test jan.nowak@poczta.pl'

print(text)
for match in regex_email.finditer(text):
    print(match.groupdict())
