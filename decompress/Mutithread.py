import re
# import threading
from threading import Thread
import Queue

   
def decompress(text):
    result = ''
    cutting = re.split("\]",text)
    for i in cutting:
        x = re.split("\[",i)
        num = x[0]
        if len(x) > 1:
            result = result + print_text(x[1],int(num))
    if result is '' :
        return "wrong input plase try again!"
    else :
        return result

def print_text(value,num):
    get_text= ''
    for x in range(0, num):
        get_text = get_text + value 
    return get_text

ex = "2[ad]3[oe]4[kp]4[wer]2[dsd]"
text_split = ex.rsplit(']', 3)
que = Queue.Queue()
th1 = Thread(target=lambda q, arg1: q.put(decompress(arg1)), args=(que, text_split[0]))
th2 = Thread(target=lambda q, arg2: q.put(decompress(arg2)), args=(que, text_split[1]))
th1.start()
th2.start()
th1.join()
th2.join()
final_result = ''
while not que.empty():
    final_result = final_result + que.get()
print(final_result)
