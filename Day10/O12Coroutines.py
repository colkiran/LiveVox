
def get_name(surname):
    print(f"surname is :{surname}")

    while(True):
        name = yield
        print(f"Recieved Name: {name}")
        print("-" * 60)
        if surname in name:
            print(f"Surname {surname} found in {name}.....")

coObj = get_name("Pillai")
coObj.__next__()

coObj.send("Sachin Tendulkar")
coObj.send("Virat Kholi")
coObj.send("Yuvraj Singh")
coObj.send("Dhanraj Pillai")


