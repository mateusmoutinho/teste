from time import sleep

i = 0 
while True:
    if i ==30:
        raise Exception("teste")
    i+=1
    print('att4')
    sleep(1)
