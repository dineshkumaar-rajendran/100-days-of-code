x = 4  # global variable


def function_v():
    y = "kumaar"  # local variable
    print(y)
    print(x)


def function_two():
    global x # global keyword 
    x += 5
    print(x)


function_v()
function_two()
