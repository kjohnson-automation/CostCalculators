import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sale_price", help="Current offer for the house", type=float)
parser.add_argument("-a", "--sellers_assist", help="Sellars assist, can be percent (0.03) or dollars (5000)", type=float)
parser.add_argument("-p", "--mortgage_payoff", help="The amount left on the mortgage", type=float)
args = parser.parse_args()

# In percentages so divide by 100 when using
TRANSFER_TAX_RATE = 2.14
COMMISSION = 6

# In Dollars
MUNICPAL_USE_OCCUPANCY = 100
NOTARY = 30
CERTS = 100
MORTGAGE_PAY_OFF = 500
WIRING = 40

# Credits in Dollars
TAX_REFUND = 2968.19


def main():
    """ Prints the amount we make after selling and if mortgage payoff is supplied, subtracts that """
    if args.sale_price is None:
        print("Need to supply -s <sale_price>")
        return -1
    sale_price = args.sale_price
    
    transfer_fee = (TRANSFER_TAX_RATE/100) * sale_price

    

    
    if args.sellers_assist is not None:
        if args.sellers_assist < 1:
            sellers_assist = args.sellers_assist * sale_price
            print("Sellers assist: {0}".format(sellers_assist))
        else:
            sellers_assist = args.sellers_assist
        brokerage_commission = (COMMISSION/100) * (sale_price - sellers_assist)
    else:
        brokerage_commission = (COMMISSION/100) * sale_price
        sellers_assist = 0

    sale_cost = transfer_fee + brokerage_commission + MUNICPAL_USE_OCCUPANCY + NOTARY + CERTS + MORTGAGE_PAY_OFF + WIRING + sellers_assist
    revenue = sale_price - sale_cost
    print("Cost of selling the home: {0}".format(sale_cost))
    print("Money before mortgage payoff: {0}".format(revenue))
    if args.mortgage_payoff is not None:
        profit = revenue - args.mortgage_payoff
        print("Money in the bank: {0}".format(profit))

if __name__ == "__main__":
    main()

