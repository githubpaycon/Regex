import re

with open('salmos33.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    # print(text)
    
    # Senhor e a próxima palavra que vinher na seguencia
    
senhor = re.findall(r'Senhor\W+\w+', text)
print(senhor)