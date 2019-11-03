import random
import time
number=0
correct=0
start=time.time()

while number<5:
    minuend=random.randrange(100)
    subtract=random.randrange(100)

    if minuend>=subtract:
        result=str(minuend-subtract)
        answer=input("{0:d}-{1:d}=".format(minuend,subtract))

        if result==answer:
            correct+=1

        number+=1
end=time.time()
print("答对次数：{}".format(correct))
print("答题时间：{0:.2f}".format(end-start),"秒")