def solution(participant, completion):
    
    participant.sort()
    completion.sort()
           
    for i in participant:
        if i not in completion:
            answer = i
            break
        else:
            completion.remove(i)
        
    return answer
    
    #정답50효율30
