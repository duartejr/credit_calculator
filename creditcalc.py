from math import ceil
from math import log
import argparse


def count_months(P, A, i):
    n = log(A / (A - i * P), i+1)
    years = ceil(n / 12)
    months = ceil(((n / 12) - years) * 12)

    if months < 0:
        years = years-1
        months = ceil(((n / 12) - years) * 12)

    if years == 1:
        nm_y = 'year'
    else:
        nm_y = 'years'

    if months == 1:
        nm_m = 'month'
    else:
        nm_m = 'months'

    if years == 0:
        print(f'You need {months} {nm_m} to repay this credit!')
    elif months == 0:
        print(f'You need {years} {nm_y} to repay this credit!')
    else:
        print(f'You need {years} {nm_y} and {months} {nm_m} to repay the '
              f'credit')

    overpayment = ceil(A * ceil(n) - P)
    print(f'Overpayment = {overpayment}')


def annuity_payment(P, n, i):
    A = ceil(P * (i * (1 + i)**n) / ((1 + i)**n - 1))
    overpayment = int(A * n - P)
    print(f'Your annuity payment = {A}!')
    print(f'Overpayment = {overpayment}')


def credit_principal(A, n, i):
    P = ceil(A / ((i * (1 + i)**n) / ((1 + i)**n - 1)))
    overpayment = int(A * n - P)
    print(f'Your credit principal = {P}!')
    print(f'Overpayment = {overpayment}')


def diff(args):
    principal = args.principal
    periods = args.periods
    interest = args.interest / 1200

    if principal and periods and interest:

        total = 0

        for m in range(1, periods+1):
            mth_diff = (principal / periods) + interest * (principal - (
                principal * (m - 1)) / periods)
            mth_diff = ceil(mth_diff)
            print(f"Month {m}: paid out {mth_diff}")
            total += mth_diff

        total -= int(principal)
        print(f"\nOverpayment = {total}\n")

    else:
        print("Incorrect parameters.")



def annuity(args):
    principal = args.principal
    payment = args.payment
    periods = args.periods
    interest = args.interest / 1200

    try:
        if not payment:
            annuity_payment(principal, periods, interest)
        elif not principal:
            credit_principal(payment, periods, interest)
        elif not periods:
            count_months(principal, payment, interest)
        else:
            print("Incorrect parameters.")
    except:
        print("Incorrect parameters.")


actions = {'diff': diff, 'annuity': annuity}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default=False)
    parser.add_argument("--principal", type=float, default=False)
    parser.add_argument("--periods", type=int, default=False)
    parser.add_argument("--interest", type=float, default=False)
    parser.add_argument("--payment", type=float, default=False)
    args = parser.parse_args()

    if args.type not in ['diff', 'annuity'] or args.periods < 0 or \
            args.principal < 0 or args.interest < 0 or args.payment < 0 or\
            args.interest > 100:
        print(args.payment <= 0)
        print('here')
        print('Incorrect parameters')

    else:
        actions[args.type](args)

