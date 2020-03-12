import argparse
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--home_cost", help="Home cost in dollars", type=float)
parser.add_argument("-d", "--downpayment", help="Either in percent (<1) or dollars", type=float)
parser.add_argument("-i", "--insurance", help="Yearly home insurance premium", type=float)
parser.add_argument("-t", "--tax", help="Yearly tax ammount", type=float)
parser.add_argument("-c", "--close_date", help="Closing date in MM/DD/YY format", type=str)
args = parser.parse_args()

# Dollar Values
LENDER_FEES = 1290.00
APPRAISAL_FEE = 425.00
CREDIT_REPORT_FEE = 27.50
DEBT_REPORT_FEE = 62.50
TITLE_FEES = 617.00
TITLE_INSURANCE_OWNER = 772.25
TITLE_INSURANCE_LENDER = 2393.00
RECORDING_FEES = 338.50

# Percent Values
TRANSFER_TAX_RATE = 1

def main():
    """ Calulates the amoun needed at closing """
    if args.home_cost is None:
        print("Need home cost")
        return -1
    home_cost = args.home_cost

    if args.close_date is None:
        print("Assuming full year, buy date of 1/1/XX")
    else:
        dt_close = datetime.datetime.strptime(args.close_date, "%m/%d/%y")
        date_delta = dt_close - datetime.datetime(year=dt_close.year, month=1, day=1)
        print("Day delta from year beginning: {0}".format(date_delta.days))
    
    if args.insurance is None:
        print("Not using home insurance premium in calculation, numbers will be off")
        insurance = 0
        insruance_escrow = 0
    else:
        insurance = (date_delta.days/365) * args.insurance
        insruance_escrow = (dt_close.month/12) * insurance
    
    if args.tax is None:
        print("Not using property tax in calculation, numbers will be off")
        property_tax = 0
        escrow_tax = 0
    else:
        property_tax = args.tax
        escrow_tax = property_tax * (dt_close.month/12)
    
    if args.downpayment is None:
        print("No downpayment supplied")
        downpayment = 0
    elif args.downpayment < 1:
        downpayment = home_cost * args.downpayment
    else:
        downpayment = args.downpayment
    
    transfer_tax = (TRANSFER_TAX_RATE/100) * home_cost

    total_fees = (LENDER_FEES + APPRAISAL_FEE + CREDIT_REPORT_FEE + DEBT_REPORT_FEE +
                  TITLE_FEES + TITLE_INSURANCE_LENDER+ TITLE_INSURANCE_OWNER + RECORDING_FEES)
    print("Total Lender Fees: {0}".format(total_fees))
    print("Down Payment: {0}".format(downpayment))
    total_cost = total_fees + downpayment + insurance + insruance_escrow + property_tax + escrow_tax + transfer_tax
    print("Total Cost Due at Closing: {0}".format(round(total_cost,2)))


if __name__ == "__main__":
    main()