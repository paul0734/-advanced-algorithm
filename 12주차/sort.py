def compare(number):
    number=list(map(str, number))                   #비교를 위해 배열을 문자열로 치환
    number.sort(key = lambda x:x*2, reverse=True)
    
    #정렬 key=lambda x:x*2 -> key=lambda 인자:조건식 / x값에 x*2를 한다는 뜻
    #7 -> 77 / 75 -> 7575
    #문자열이기 때문에 77과 7575를 비교하면 77이 더 큼

    return ''.join(number)                          #문자열인 number리스트 값들을 join으로 연결하여 리턴         


arr=[10,68,75,7,21,12]
print(compare(arr))
