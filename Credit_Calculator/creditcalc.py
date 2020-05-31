import argparse
import math

i_val = 0.0
# month_val = 0
# count_val_minus = 0
# rounded_up = 0
# # write your code here
#
# allequal_month = 0
# some_months = 0
# last_month = 0
# print("Enter the credit principal:")
# credit_val = int(input())
# print("What do you want to calculate?")
# print('type "m" - for count of months,')
# print('type "p" - for monthly payment:')
# type_val = input()
# def even_month(credit_val, count_val):
#     if credit_val % count_val == 0:
#         return True
#     else:
#         return False
#
# if type_val == "m":
#     print("Enter monthly payment:")
#     month_val = int(input())
#     num_month = format((credit_val / month_val),'0.0f')
#     print("It takes " + str(num_month) + " month to repay the credit")
#
# elif type_val == "p":
#     print("Enter count of months:")
#     count_val = int(input())
#     if even_month(credit_val,count_val) == True:
#         allequal_month = format((credit_val / count_val), '0.0f')
#         print("Your monthly payment = "+ str(allequal_month))
#     else:
#         some_months = format((credit_val / count_val), '0.1f')
#         # print(some_months)
#         rounded_up = math.ceil(credit_val / count_val)
#         count_val_minus = count_val - 1
#         last_month = credit_val - (count_val_minus) * rounded_up
#         print("Your monthly payment = "+ str(rounded_up) + " with last month payment = " + str(last_month) + ".")
#
# print("What do you want to calculate?")
# print('type "n" - for count of months,')
# print('type "a" - for annuity monthly payment,')
# print('type "p" - for credit principal:')
#
# type_val = input()
# i_val = 0.0
# n_val = 0.0
# year = 0
# month = 0
# thic_formula = 0
# if type_val == 'n':
#     print("Enter credit principal:")
#     cred_p = float(input())
#     print("Enter monthly payment:")
#     monthly_p = float(input())
#     print("Enter credit interest:")
#     cred_interest = float(input())
#     # thic_formula = monthly_p / (monthly_p - i_val * cred_p )
#     i_val = cred_interest / (12 * 100)
#     n_val = math.log(monthly_p / (monthly_p - i_val * cred_p), 1 + i_val)
#     if n_val % 12 == 0:
#         n_val = n_val / 12
#         print("You need " + str(n_val) + " years to repay this credit!")
#     elif n_val > 12 and n_val % 12 != 0:
#         if math.ceil(n_val) % 12 == 0:
#             n_val = math.ceil(n_val)
#             n_val = n_val / 12
#             n_val = int(n_val)
#             print("You need " + str(n_val) + " years to repay this credit!")
#         else:
#             year = n_val/12
#             year = math.floor(year)
#             month = math.ceil(n_val - (year * 12))
#             print("You need " + str(year) + " years and " + str(month) + " months to repay this credit!")
#     elif n_val < 12:
#         n_val = math.ceil(n_val)
#         print("You need " + str(n_val) + " months to repay this credit!")
#
# elif type_val == 'a':
#     print("Enter credit principal:")
#     cred_p = int(input())
#     print("Enter count of periods:")
#     count_p = float(input())
#     print("Enter credit interest:")
#     cred_interest = float(input())
#     i_val = cred_interest / (12 * 100)
#     n_val = cred_p * ((i_val * pow(1 + i_val, count_p)) / (pow(1+i_val, count_p) - 1))
#     n_val = math.ceil(n_val)
#     n_val = round(n_val, 0)
#     print("Your annuity payment = " + str(n_val) + "!")
#
# elif type_val == 'p':
#     print("Enter monthly payment:")
#     month_p = float(input())
#     print("Enter count of periods:")
#     count_p = int(input())
#     print("Enter credit interest:")
#     cred_interest = float(input())
#     i_val = cred_interest / (12 * 100)
#     n_val = month_p / ((i_val * pow(1 + i_val, count_p)) / (pow(1+i_val, count_p) - 1))
#     n_val = math.floor(n_val)
#     n_val = round(n_val, 0)
#     print("Your credit principal = " + str(n_val) + "!")

#-----------------------------STAGE 4


def n_func(cred_p, monthly_p, cred_interest):
    solution = ""
    n_val = 0
    i_val = cred_interest / (12 * 100)
    n_val = math.log(monthly_p / (monthly_p - i_val * cred_p), 1 + i_val)
    if n_val % 12 == 0:
        n_val = n_val / 12
        print("You need " + str(n_val) + " years to repay this credit!")
    elif n_val > 12 and n_val % 12 != 0:
        if math.ceil(n_val) % 12 == 0:
            n_val = math.ceil(n_val)
            n_val = n_val / 12
            n_val = int(n_val)
            overpayment = (monthly_p * (n_val * 12)) - cred_p
            print("You need " + str(n_val) + " years to repay this credit!")
            print("Overpayment = " + str(overpayment))
        else:
            year = n_val/12
            year = math.floor(year)
            month = math.ceil(n_val - (year * 12))
            overpayment = (monthly_p * ((year * 12) + month)) - cred_p
            print("You need " + str(year) + " years and " + str(month) + " months to repay this credit!")
            print("Overpayment = " + str(overpayment))
    elif n_val < 12:
        n_val = math.ceil(n_val)
        overpayment = (monthly_p * n_val) - cred_p
        print("You need " + str(n_val) + " months to repay this credit!")
        print("Overpayment = " + str(overpayment))
    return solution


def p_func(cred_interest, month_p, count_p):
    i_val = cred_interest / (12 * 100)
    n_val = month_p / ((i_val * pow(1 + i_val, count_p)) / (pow(1+i_val, count_p) - 1))
    n_val = math.floor(n_val)
    n_val = int(n_val)
    overpayment = (month_p * count_p) - n_val
    print("Your credit principal = " + str(n_val) + "!")
    print("Overpayment = " + str(overpayment))


def annuity(i_val, cred_i, credit_p, count_p):
    n_val = 0
    i_val = cred_i / (12 * 100)
    n_val = credit_p * ((i_val * pow(1 + i_val, count_p)) / (pow(1+i_val, count_p) - 1))
    n_val = math.ceil(n_val)
    n_val = int(n_val)
    overpayment = (n_val * count_p) - credit_p
    print("Your annuity payment = " + str(n_val) + "!")
    print("Overpayment = " + str(overpayment))


def differentiated(cred_p, count_p, i_val, m):
    d_m = 0.0
    # sum_months = 0
    i_val = i_val / (12 * 100)
    d_m = (cred_p/ count_p) + (i_val * (cred_p - ((cred_p * (m-1))/count_p)))
    d_m = math.ceil(d_m)
    d_m = int(d_m)
    # sum_months += d_m
    return d_m


ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", required=True, help="type")
ap.add_argument("-p", "--principal", required=False, help="principal")
ap.add_argument("-pp", "--periods", required=False, help="periods")
ap.add_argument("-i", "--interest", required=False, help="interest")
ap.add_argument("-ppp", "--payment", required=False, help="payment")

args = vars(ap.parse_args())

if len(args) < 4:
    print("Incorrect parameters.")
# display a friendly message to the user

type_val = args["type"]
if args["principal"] is not None:
    principal_val = int(args["principal"])
else:
    principal_val = args["principal"]
if args["periods"] is not None:
    periods_val = int(args["periods"])
else:
    periods_val = args["periods"]
if args["interest"] is not None:
    interest_val = float(args["interest"])
else:
    interest_val = args["interest"]
if args["payment"] is not None:
    payment_val = int(args["payment"])
else:
    payment_val = args["payment"]

sum_month = 0
if type_val == "diff":
    if principal_val is not None and periods_val is not None and interest_val is not None:
        for i in range(1,periods_val+1):
            d_m = differentiated(principal_val, periods_val, interest_val, i)
            print("Month " + str(i) + ": paid out " + str(d_m).format(",.0f"))
            sum_month += differentiated(principal_val, periods_val, interest_val, i)
            overpayment = sum_month - principal_val
        print("Overpayment = " + str(overpayment))
    else:
        print("Incorrect parameters")
elif type_val == "annuity":
    if principal_val is not None and periods_val is not None and interest_val is not None:
         annuity(i_val, interest_val, principal_val, periods_val)
    elif payment_val is not None and periods_val is not None and interest_val is not None:
    #annuity * period - principal = overpayment
        p_func(interest_val, payment_val, periods_val)
    elif payment_val is not None and principal_val is not None and interest_val is not None:
        n_func(principal_val, payment_val, interest_val)
    else:
        print("Incorrect parameters")
