def clocker():
    while True:
        pid = '' # process ID
        if os.system('ps -e | grep ' + pid) == 0:
            time.sleep(120) # scan the pid every 120s
        else:
            break
        time.sleep(10)
        command = ''
        os.system(command)