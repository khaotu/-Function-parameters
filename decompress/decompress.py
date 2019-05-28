import re
import threading
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

