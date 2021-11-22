class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

class mobileOS:
    def portable(self):
        print("portable OS")

    def free(self):
        print("OS is free")

class android(mobileOS, linux):
    def ui(self):
        print("great gui")


obju = unix()
objl = linux()
obja = android()

obja.free()
