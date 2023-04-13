def solution(numbers, target):
    
    result = 0
    def func(num, level):
        nonlocal result
        if(len(numbers) == level):
            if(num==target):
                result+=1
            return 
        
        if(level==1):
            func(num+numbers[level], level+1)
            func(num-numbers[level], level+1)
            func(-num+numbers[level], level+1)
            func(-num-numbers[level], level+1)
        else:
            func(num+ numbers[level], level+1)
            func(num- numbers[level], level+1)
        
    func(numbers[0], 1)
    return result


        
