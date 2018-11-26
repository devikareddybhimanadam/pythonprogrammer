def switch_demo(argument):
    switch = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    print switch.get(argument, "Invalid Input")
i=int(raw_input())
switch_demo(i)
