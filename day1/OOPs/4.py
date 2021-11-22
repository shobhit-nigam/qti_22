
class Avenger:
    ranking = 0
    strength = None

    def fight():
        print("uses", strength)

ironMan = Avenger()
wanda = Avenger()

ironMan.strength = "suit"

print(ironMan.strength)
print(wanda.strength)

# error
ironMan.fight()
