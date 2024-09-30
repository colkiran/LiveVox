
class Player:

    def __init__(self):                 # constructor
        print("Player initialized......")

    def get_runs(self):
        print('Runs scored.....')

    def __del__(self):
        print("Player Dtor called......")

sachin = Player()
sachin.get_runs()

sachin.__init__()


del sachin
print("-" * 60)

sourav= Player()
sourav.get_runs()

