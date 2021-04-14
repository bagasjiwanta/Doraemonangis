import time 

def randomInt(digit): 
    # input digit = berapa digit integer random yang ingin dihasilkan
    # contoh : randomInt(8) = 12345678
    randstr = int(str(time.time() - int(time.time()))[2:digit+1]) 
    rvalue = int(time.strftime("%S", time.localtime()))
    return ("%d" % (rvalue*randstr))[:digit]