import sys

class Avenger:
    ranking = 0
    strength = None

    def fight():
        print("uses", strength)

ironMan = Avenger()

print(sys.getsizeof(ironMan))
print(sys.getsizeof(Avenger))
