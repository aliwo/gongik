from django.http import HttpResponse, JsonResponse
from _MilitaryAffairs.MilitarySites import *
from _MilitaryAffairs.ChangeDetector import *
#상대 경로로 import를 쓰면 에러 남. 왜 그럴까?

def new_notice(request, location):
    print('요청 받은 지역: '+location)
    det = Detector()
    try:
        location = sites[location]
    except KeyError as error:
        return HttpResponse('invalid location')
    result = det.isNewNotification(location)
    return JsonResponse(result, safe=False) # 만약 새 글이 없으면 'false'라는 문자열을 리턴합니다.
