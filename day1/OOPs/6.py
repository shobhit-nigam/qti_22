
class Avenger:
    ranking = 0
    strength = None

    def fight(self):
        print("uses", self.strength)

ironMan = Avenger()
wanda = Avenger()

ironMan.strength = "suit"

ironMan.fight()

# ironMan.fight()
# translates to
# Avenger.fight(ironMan)



#
