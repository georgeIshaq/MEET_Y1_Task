
runtime = True # variable for continous operation of calc
# set up each operation as a function

def add(*vals):
    res = vals[0]
    for val in vals[1:]:
        res+=val
    return res
def sub(*vals):
    res = vals[0]
    for val in vals[1:]:
        res-=val
    return res
def mult(*vals):
    res = vals[0]
    for val in vals[1:]:
        res *= val
    return res
def div(*vals):
    res = vals[0]
    for val in vals[1:]:
        if val != 0:
            res /= val
        else:
            return "Can not divide by 0"
    return res
def exp(*vals):
    res = vals[0]
    for val in vals[1:]:
        res = res**val
    return res

def run(): # function to run the calculator
    global runtime
    num_list = [] # list to store user inputs
    op = input(" \n 1:add \n 2:subtract \n 3:multiply \n 4:divide \n 5:exponeniate \n 0:end calculator")
    if op == "0": # check if user wants to quit the calc
        runtime = False
        return runtime
    
    try:  # check if user gave a valid number of values 
        num_val = int(input("enter the number of values"))
    except Exception:
        return print("not a valid number of values")
    
    for i in range(num_val): # take all user numbers and store in list
        num = float(input(f"Enter the {i+1} number:"))
        num_list.append(num)
    #Perform the operation the user requested earlier
    if op =="1":
        try: # ensure operation returns a valid result
            add(*num_list)
        except Exception:
            print("You must input a valid number")
        else:
            print("result is:",add(*num_list))
    elif op =="2":
        try:
            sub(*num_list)
        except Exception:
            print("You must input a valid number")
        else:
            print("result is:",sub(*num_list))
    elif op == "3":
        try:
            mult(*num_list)
        except Exception:
            print("You must input a valid number")
        else:
            print("result is:",mult(*num_list))
    elif op == "4":
        try:
            div(*num_list)
        except Exception:
            print("You must input a valid number")
        else:
            print("result is:",div(*num_list))
    elif op == "5":
        try:
            exp(*num_list)
        except Exception:
            print("You must input a valid number")
        else:
            print("result is:",exp(*num_list))
    else:
        print("that is not a valid operation")

while runtime: # run calculator until user deems to end it
    run()