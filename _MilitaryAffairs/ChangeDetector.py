import re

from requests import *


class Detector:

    def __init__(self):
        pass

    def isNewNotification(self, location): #인자로 받은 지방 병무청 url에 새 공지사항이 있는지 검사합니다.
        page = post(location).text
        result = self.regex(page)
        if result != None: # 만약 새 글이 있다면
            return result # 새 글의 정보가 담긴 json 파일을 반환합니다.
        else:
            return 'no new notification'


    def regex(self, string): # 정규표현식으로, 새로운 공지사항이 있는지 체크
        pat = self.getPattern()
        result = re.search(pat, string, flags=re.DOTALL)
        json = self.parse(result)
        if json == False:
            return False
        return json

    def parse(self, data):
        if data == None:
            return False
        id_num = data.group(1)
        # print('글 번호:', end=' ')
        # print(id_num)
        title = data.group(3)
        # print('글 제목:', end=' ')
        # print(title)

        return {'id_num':id_num, 'title':title}

    def getPattern(self):
        #([0-9]{1,3}) 은 글 번호를 의미함. 1번 group
        #(.*)는 사이의 모든 문자열을 의미
        #<img src="\/images\/icon\/new_icon.gif 은 새 글이 나타났을때만 나오는 이미지 이걸로 새 글이 나왔는지 식별한다.
        return r'skip_m">([0-9]{1,3})(.*)>(.*)<img src="\/images\/icon\/new_icon.gif'

