class parent:
    def p1(self):
        print("this is from parent class")

class child(parent):
    def c1(self):
        print("this is from child class")


obj_child=child
print(obj_child.p1)
print(obj_child.c1)

#This is single inheritance example...