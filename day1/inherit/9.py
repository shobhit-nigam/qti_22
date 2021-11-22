class unix:
    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def __init__(self):
        print("init of linux")
        super().__init__()

    def free(self):
        print("the kernel is free")


objl = linux()
