def solution(phone_book):
    answer = True
    if len(phone_book) == 1:
        return True
    
    prefix = {number: True for number in phone_book}
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in prefix:
                return False
            
    return answer