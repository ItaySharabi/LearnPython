# ניתן לייבא גם קבצי פייתון חיצוניים שאנחנו כתבנו:
import my_user_validation_lib as py_file

username = 'David'
pw = 'adwnladnSDA'

is_valid = py_file.is_valid(pw)

print(f'Calling is_valid({pw}) returned {is_valid}')

if is_valid:
    py_file.register(username, pw)
else:
    print(f'{username} Cannot be registered because password is too weak!')

