import subprocess 
import wave
from OCR import main



text = main()
# text = "안녕하세요 잘 되나요?"
# print(text)

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

speak = '<speak>'+text+'</speak>'

res = subprocess.Popen(['curl', '-v', '-X', 'POST', url,
                        '-H', "Content-Type: application/ssml",
                        '-H', "Authorization: b4e5257e61f7df0c8994a5d5eaf6ff58",
                        '-d', speak], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = res.communicate()

# print(output)
# print(err)

f = open('book_.wav', 'wb')
f.write(output)
f.close()

print(err)
