import re

text = ''
with open('telefones.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(re.findall(r'\(\d+\) \d{4}-\d{4}|\(\d+\) \d{4}-?\d{4}|\d+ \d{4}-?\d{4}|\d{11}', text))
# ['(21) 3692-6483', '(85) 2324-8636', '(83) 2217-6631', '(41) 2446-3839', '(22) 2277-0242', '(61) 2155-0573', '(82) 3746-4464', '(55) 3824-2476', '(67) 3463-4231', '(99) 2954-1336', '(14) 2137-6424', '(17) 3226-3573', '11 32263573', '11933565648']
# print(text)

# Recuperação de telefones válidos:
from itertools import permutations

cel = re.compile(r'[7-9][0-9]{7}')
for tel in permutations(range(1, 10), 8):
    _tel = ''.join(str(x) for x in tel)
    if cel.search(_tel):
        print(_tel)