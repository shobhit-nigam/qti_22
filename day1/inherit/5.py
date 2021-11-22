class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it secure")

class linux(unix):
    def free(self):
        print("the kernel is free")


obju = unix()
objl = linux()

print(type(objl) is linux)
print(type(objl) is unix)
print("---")
print(isinstance(objl, linux))
print(isinstance(objl, unix))
