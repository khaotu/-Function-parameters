import re
def decompress(text):
    hello = ''
    result = re.split("\]",text)
    # print(result)
    # print(len(result))
    for i in result:
        x = re.split("\[",i)
        num = x[0]
        if len(x) > 1:
            hello = hello + print_text(x[1],int(num))

    return hello

def print_text(value,num):
    get_text= ''
    for x in range(0, num):
        get_text = get_text + value 
    return get_text

   
    
    


print(decompress("2[as]3[fp]4[eoirere]"))