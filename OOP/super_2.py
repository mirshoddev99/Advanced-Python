class Names:
    def __init__(self):
        self.names = ["John", "Jenny", "Doe", "Jack", "Mirshod", "Jonie", "Mike"]
    
    def get_names(self):
        return self.names


class ChildClass(Names):
    def get_names(self):
        filtered_names = super().get_names()
        name_filter = list(filter(lambda w: w.startswith("J"), filtered_names))
        return name_filter



child = ChildClass()
print(child.get_names())
