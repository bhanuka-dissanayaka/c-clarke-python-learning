class Top:
    def top_method(self):
        print("Calling top method")

class Middle(Top):
    def middle_method(self):
        print("Calling middle method")

    def top_method(self):
        print("I override top method")



class Bottom(Top,Middle):
    def bottom_method(self):
        print("Calling bottom method")


bottom = Bottom()
bottom.top_method()
