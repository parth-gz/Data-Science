#Need for decorators
import time
lst=[1,2,3,4,5,6,7,8,9,10,333333333333,4444444444444,55555555555555,66666666666666,777777777777]
def cube(numbers):
    start=time.time()
    result=[]
    for num in numbers:
        result.append(num*num*num*num*num*num*num*num*num)
    end=time.time()
    totalTime=(end-start)/1000
    print(f"Total execution time= {totalTime}")
    return result
print(cube(lst))
    