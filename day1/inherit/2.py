class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

class android(linux):
    def ui(self):
        print("great gui")


obju = unix()
objl = linux()
obja = android()

obja.secure()
