from aip import AipOcr
import autopy

i = open(r'user.png', 'rb')
img = i.read()

# 百度文字识别
APP_ID = '19641700'
API_KEY = 'BDCKlcTWXGGx1pCKqdy8SvB7'
SECRET_KEY = 'xtKUVYndR38cGaiLyCCnV2dvL2koat'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

message = client.basicGeneral(img)
print(message.get('words_result'))
