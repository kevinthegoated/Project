def calc_sum(x,y):
    sums=x+y
    return sums
def calc_sub(x,y):
    sub=x-y
    return sub
def calc_div(x,y):
    div=x/y
    return div
def calc_mult(x,y):
    mult=x*y
    return mult

def main():
    x=int(input("Enter First Number"))
    operation=(input("Enter Operation(+,-,*,/)"))
    y=int(input("Enter second Number"))
    if operation=="+":
        print(calc_sum(x,y))
    elif operation=="-":
        print(calc_sub(x,y))
    elif operation=="*":
        print(calc_mult(x,y))
    elif operation=="/":
        print(calc_div(x,y))
main()

