from argparse import ArgumentParser
import sys
print(sys.path)
#Calculates the minimum credit card payment
def get_min_payment(balance, fees=0):
   """
   Parameters are:
       balance and fees: The total amount of the balance in the account is "balance".
       Fees are the fees associated with the account


   Returns:
       A float: The minimum credit card payment.
   """
   mini_payment = (balance * 0.02) + fees
   return max(mini_payment, 25)


#Amount of interest in the next payment
def interest_charged(balance, apr):
   """
   Parameters are the same as get_min_payment with the addition of apr:
       apr (int): The annual percentage rate.


   Returns:
       float: The amount of interest charged.
   """
   a = apr / 100.0
   y = 365
   d = 30
   interest = (a / y) * balance * d
   return interest


#Calculate the number of payments required to pay off the credit card balance.
def remaining_payments(balance, apr, targetamount=None, credit_line=5000, fees=0):
   """
   Parameters:
       balance: The balance of the credit card.
       apr: The annual APR.
       targetamount: The target payment amount per payment.
       credit_line: The credit line.
       fees: The amount of fees charged in addition to the minimum payment.


   Returns:
       A tuple: (total_payments, over_25, over_50, over_75)
   """


def remaining_payments(balance, apr, target_payment=None, credit_line=5000, fees=0):
   total_payments = 0
   over_25 = 0
   over_50 = 0
   over_75 = 0


# While loop simulating payments until card is paid off
   while balance > 0:
       if target_payment is None:
           payments = get_min_payment(balance, fees)
       else:
           payments = max(target_payment, get_min_payment(balance, fees))


       interest = interest_charged(balance, apr)
       balance -= (payments - interest)


       if balance > 0:
           if balance > 0.75 * credit_line:
               over_75 += 1
           elif balance > 0.50 * credit_line:
               over_50 += 1
           elif balance > 0.25 * credit_line:
               over_25 += 1


       total_payments += 1


   return total_payments, over_25, over_50, over_75




#Compute recommended minimum payment and display results.


def main(balance, annual_apr, credit_line=5000, target_payment=None, fees=0):
   mini_payment = get_min_payment(balance, fees)
   result_string = f"The recommended minimum payment is: ${mini_payment}\n"


   pays_minimum = False
   if target_payment is None:
       pays_minimum = True
   elif target_payment < mini_payment:
       return "Your target payment is less than the minimum payment for this credit card"


   total_payments = remaining_payments(balance, annual_apr, target_payment=target_payment, credit_line=credit_line, fees=fees)


   if pays_minimum:
       result_string += f"If you pay the minimum payments each month, you will pay off the balance in {total_payments[0]} payments."
   else:
       result_string += f"If you make payments of ${target_payment}, you will pay off the balance in {total_payments[0]} payments."


   result_string += f"\nYou will spend a total of {total_payments[1]} months over 25% of the credit line."
   result_string += f"\nYou will spend a total of {total_payments[2]} months over 50% of the credit line."
   result_string += f"\nYou will spend a total of {total_payments[3]} months over 75% of the credit line."


   return result_string




def parse_args(args_list):
   """
   Takes a list of strings from the command prompt and passes them through as arguments.


   Args:
   - args_list (list): The list of strings from the command prompt.


   Returns:
   - args (ArgumentParser)
   """
   parser = ArgumentParser()
   parser.add_argument('balance_amount', type=float, help='The total amount of balance left on the credit account')
   parser.add_argument('apr', type=int, help='The annual APR, should be an int between 1 and 100')
   parser.add_argument('credit_line', type=int, help='The maximum amount of balance allowed on the credit line.')
   parser.add_argument('--payment', type=float, default=None, help='The amount the user wants to pay per payment, should be a positive number')
   parser.add_argument('--fees', type=float, default=0, help='The fees that are applied monthly.')


   # parse and validate arguments
   args = parser.parse_args(args_list)
   if args.balance_amount < 0:
       raise ValueError("balance amount must be positive")
   if not 0 <= args.apr <= 100:
       raise ValueError("APR must be between 0 and 100")
   if args.credit_line < 1:
       raise ValueError("credit line must be positive")
   if args.payment is not None and args.payment < 0:
       raise ValueError("number of payments per year must be positive")
   if args.fees < 0:
       raise ValueError("fees must be positive")
   return args


if __name__ == "__main__":
   try:
       arguments = parse_args(sys.argv[1:])
   except ValueError as e:
       sys.exit(str(e))
   print(main(arguments.balance_amount, arguments.apr, credit_line=arguments.credit_line, targetamount=arguments.payment, fees=arguments.fees))

