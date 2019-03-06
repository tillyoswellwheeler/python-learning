#-------------------------------------
# Python Learning -- Inheritance
#-------------------------------------

#-------------------------------------
#

class Chef:

    def make_chicken(self):
        print("Chef makes chicken")

    def make_ham(self):
        print("Chef makes ham")

    def make_special_dish(self):
        print("Chef makes a special dish")


class ChineseChef(Chef):

    def make_chicken_feet(self):
        print("Hmm crunchy chicken feet!")


dinner1 = Chef.make_chicken(Chef)
dinner2 = ChineseChef.make_chicken(ChineseChef)
dinner3 = ChineseChef.make_chicken_feet(ChineseChef)

