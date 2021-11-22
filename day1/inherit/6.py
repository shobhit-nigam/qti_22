class unix:
    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("the kernel is free")


obju = unix()
objl = linux()
