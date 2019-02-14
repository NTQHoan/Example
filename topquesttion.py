__doc__ = '''
    requiment:
        - return top questtion tag **Label** in stackoverflow.com
'''
import argparse
import requests
import json


def get_top_question(N, L):

    numb_q = str(N)
    url_get_question = "https://api.stackexchange.com/2.2/questions?pagesize={}&order=desc&\
           sort=votes&tagged={}&site=stackoverflow".format(numb_q, L)
    res = requests.get(url_get_question)
    data = res.json()
    result = [(dt['title'], dt['link']) for dt in data['items']]
    for i in result:
        _str = "Title: {} \nLink answer top {} votes: {}".format(i[0], N, i[1])
        print(_str)
    return result

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("N", help="Top N questions on stackoverflow", type=int)
    parser.add_argument("L", help="Label you want to search", type=str)
    args = parser.parse_args()
    return args
    
def main():
    
    get_top_question(arg_parse().N, arg_parse().L)


if __name__ == '__main__':
    main()
