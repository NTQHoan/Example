
__doc__ = '''
Requirement: list all Github repositories of an user
'''


import requests
import argparse

# define url
api_url = 'https://api.github.com/users/{}/repos'


def list_repos(username):

    real_url = api_url.format(username)
    resp = requests.get(real_url)
    repos = resp.json()

    return [repo['name'] for repo in repos]


def arg_parsed():
    parser = argparse.ArgumentParser(description='list all repos\
                                    based on github username.')
    parser.add_argument("user", type=str, help="please input a username")
    return parser.parse_args()


def main():

    user_input = arg_parsed().user
    user_repos = list_repos(user_input)
    value = 0
    print('Please find the list of repositories below:')
    while value < len(user_repos):
        print('{0} - {1}'.format(value + 1, user_repos[value]))
        value += 1


if __name__ == "__main__":
    main()
