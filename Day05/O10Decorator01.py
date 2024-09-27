
def outerFun(fnc):

    def helperFun(amt):
        print("Logging into the server......")
        fnc(amt)
        print("Logging out of the server .......")
        print("-" * 60)


    return helperFun


@outerFun               # deposit = outerFun(deposit)
def deposit(amt):
    print(f"Amount {amt} successfully credited into the account end ####")

@outerFun
def withdraw(amt):
    print(f"Amount {amt} debited from the account ending ####")


deposit(85000)
withdraw(15000)



