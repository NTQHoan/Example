import argparse
import json
import requests
from bs4 import BeautifulSoup as BS

url = 'http://ketqua.net'

def get_number():
    req = requests.get(url)
    lucky_number = BS(req.text, 'html.parser').find('tbody').get_text(' ').split()
    number_of_lucky = [number for number in lucky_number if number.isdigit()]
    return number_of_lucky

def check_number(numbers):
    prizes = get_number()
    lo_numbers = [int(prize[-2:]) for prize in prizes]
    for number in numbers:
        if number in lo_numbers:
            count = lo_numbers.count(number)
            if count >= 1:
                print("number lucky: {} ,number of time: {}".format(str(number), count))
            else:
                print('Good luck next time:(')

def arg_parse():
    parser = argparse.ArgumentParser(description='Check Jackpot: )')
    parser.add_argument('nb', type=int, nargs='*', help='an integer for the check')
    args = parser.parse_args()
    return args
def main():
    input_data = arg_parse().nb
    check_number(input_data)


if __name__ == '__main__':
    main()
