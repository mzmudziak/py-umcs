import re

regex_ip = re.compile(
    r'^(?P<address>'
    r'(?P<first>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
    r'.'
    r'(?P<second>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
    r'.'
    r'(?P<third>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
    r'.'
    r'(?P<fourth>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
    r')'
)
with open('ips') as f:
    for line in f:
        for match in regex_ip.finditer(line):
            print(match.groupdict())
