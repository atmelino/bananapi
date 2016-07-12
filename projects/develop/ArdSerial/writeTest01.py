from datetime import datetime
import time

i=1
try:
    while 1:
        print i
        i=i+1
        curdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fh = open("Hello.txt", "a")
        output="%s %8d Hello World again\n" %(curdate,i)
        fh.write(output)
        fh.close 
        time.sleep(1)
except KeyboardInterrupt:
        print "end"
        

