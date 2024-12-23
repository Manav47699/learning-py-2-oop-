#exception handling = it is done to prevent the stopping of the program if some error occurs
# except Exception -> catches all exception (bad practice), exception TypeError -> catches particular exception 
#main types are = (ZeroDivisionError, TypeError, ValueError)
#usually user input is kept inside try block as it is a danger area

while True:                                   #yo loop run gareko garei garna jhau lagera haldeko
    choice = input ("Enter q to quit or any key to continue")
    if choice.lower() == "q":
        break
    else:

        try:
            num = int(input("Enter a number: "))
            print (4/num)
        except ValueError:
            print ("Only numbers are allowed")
        except ZeroDivisionError:
            print ("Division by zero  isn't possible")
        except Exception:
            print ("Some exception occured")

        finally:
            print("This is finally block so it always executes")
