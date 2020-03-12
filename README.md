# CostCalulators
 Useful for calculating buying and selling costs

## sellers_proceeds.py:
`use`: python sellers_proceeds.py -s <sale_price> -a <sellers_assist> -p <mortgage_payoff>
 
 - -s (sale_price): is the current offer being evaluated, *required*
 - -a (sellers_assist): this is either a value less than 1 (percent based) or a numeric value in dollars, *optional*
 - -p (mortgage_payoff): The value left on the mortgage, *optional*

## buyers_cost.py:
`use`: python buyers_cost.py -b <home_cost> -d <down_payment> -i <insurance_premium> -t <property_tax> -c <close_date>

 - -b (home_cost): current accepted offer for the home *required*
 - -d (down_payment): downpayment amount in percent (0.XX) or dollars $1+ *optional*
 - -i (insurance_premium): Yearly insurance premium, escrow amount adjusted and added as well *optional*
 - -t (property_tax): Yearly property tax liability, escrow amount adjusted and added as well *optional*
 - -c (close_date): Close date on the property to adjust for escrow amounts *optional*
