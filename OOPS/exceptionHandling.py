
# class ZeroDenominatorError(Exception):
#     pass

class ZeroDenominatorError(ZeroDivisionError):
    pass

while True:
    try:
        num = int(input("Enter the Numerator: "))
        den = int(input("Enter the Numerator: "))
        if den == 0:
            raise ZeroDenominatorError()
        value = num/den
    except ValueError:
        print("Numerator and Denominator should be integers")
    except ZeroDenominatorError:
        print("Denominator should not be zero")
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    # except (ValueError, ZeroDivisionError):
    #     print("Numerator and Denominator should be integers and Denominator should not be zero")
    except:
        print('Some exception occured')
    else:
        print("%.2f" %value)
        break
    finally:
        # don't use any variables in this block, bcoz ho sakta h
        # wo variable upar aane se pehle hi exception aa gya ho, then error aa jaayega
        print("Exception may or may not have occured")