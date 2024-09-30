class Team:


    head = "Roopa"

    @classmethod
    def get_name(cls):
        return cls.head

    @classmethod
    def set_name(cls,name):
        cls.head = name

Team.set_name("Tom")
print(Team.get_name())

