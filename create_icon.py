import base64


with open('xiguapig.ico', 'rb') as icon:
    b64str = base64.b64encode(icon.read())

with open('xiguapig.py', 'w') as f:
    f.write('img = \'{}\''.format(b64str))
