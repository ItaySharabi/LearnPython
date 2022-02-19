
d = {}

x = input('Please enter your name: ') # נשמור במשתנה name את הערך מהמשתמש

d['Name'] = x      # {'Name' : 'David'}
d['Name'] = x + x  # {'Name' : 'DavidDavid'}  עידכנו את הערך השייך למפתח

print(d.get('Name'))

