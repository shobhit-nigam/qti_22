class unix:
    def __init__(self, data):
        print("init of unix")
        self.u = data

    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def __init__(self, vala, valb):
        super().__init__(valb)
        print("init of linux")

    def free(self):
        print("the kernel is free")


objl = linux(100, 200)
