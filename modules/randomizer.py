import time 

def randomInt(digit):
    randstr = int(str(time.time() - int(time.time()))[2:digit+1]) 
    rvalue = int(time.strftime("%S", time.localtime()))
    return ("%d" % (rvalue*randstr))[:digit]
    