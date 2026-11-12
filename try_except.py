def gregorian():
    print("\n\n")
    try:
        age = int(input("please enter your age : "))
        year = 2026 - age
        print(f"you was born in {year} .")

    except ValueError as error:
        print("invalid number the error is", error)


try:
    gregorian()
except Exception as error:
    print("invalid number for calling the func the error is", error)
