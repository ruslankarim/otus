import sys
print(sys.path)
class Cat:

    def __init__(self, first_name, last_name="Cat"):
        self.first_name = first_name
        self.last_name = last_name

    def meow(self):
        print("The cat is meow.")


class MainCoon(Cat):
    pass


main_coon = MainCoon("Lisa")


# print(MainCoon.mro())

class A:
    def process(self):
        print("A process()")


class B:
    pass


class C(A, B):
    pass


obj = C()
# print(C.mro())
