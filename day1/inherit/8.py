class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):

    def free(self):
        print("the kernel is free")

    def secure(self):
        print("along with rwx, we can also have spywares")


obju = unix()
obju.secure()
print("---")
objl = linux()
objl.secure()
