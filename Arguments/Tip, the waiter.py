def calculate(total_bill, tip_perc):
    tip=(total_bill*tip_perc) /100
    return tip

print("the tip amount is", calculate(1000,7))