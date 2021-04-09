from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from eunjeon import Mecab
from OCR import main

import time


text = main()

kom = Komoran()
mecab = Mecab()
okt = Okt()
kkm = Kkma()
han = Hannanum()

# 성능비교 - 정확도
mecab_mor = mecab.morphs(text)
kom_mor = kom.morphs(text)
# okt_mor = okt.morphs(text)
han_mor = han.analyze(text)
# print(kom_mor)
# print(kkm_mor)
print(mecab_mor)

# ---------> 성능은 비슷 , 코모란이 조금 낫다

# 성능비교 - 시간
start = time.time()
kom_mor = kom.morphs(text)
kom_time = time.time()
print("코모란 실행시간----------------------",kom_time-start)

kkm_mor = kkm.morphs(text)
kkm_time = time.time()
print("꼬꼬마 실행시간----------------------",kkm_time-kom_time)

mecab_mor = mecab.morphs(text)
mecab_time = time.time()
print("매캡 실행시간----------------------",mecab_time-kkm_time)



