# פייתון היא שפה שבה מאוד נהוג להשתמש בספריות חיצוניות
# ולכן נלמד מספר דרכים נוחות להתנהלות עם ספריות

# Import with alias
import math as m  # בשורה זו ייבאנו את הספרייה המתמטית שהכרנו, ונתנו לה "שם בדוי"

# עכשיו נפנה לספריה עם השם `m`

print(f'You can give an alias to your import using the keyword `as`')
print(f'Now you can address math as `m`:  m.pi -> {m.pi}')

import random as rand

print(f'Use the `random` library to produce random numbers: \nrand.randint(0,10) -> {rand.randint(0, 10)}')