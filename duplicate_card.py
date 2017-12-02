import json
from argparse import ArgumentParser
import requests

VERSION = '0.1.0'

class Redmine:
    URL = 'https://api.trello.com/1'

    def __init__(self, keys):
        self.keys = keys

    def find_list_id(self, board, list_name):
        resp = requests.get('{}/boards/{}/lists'.format(Redmine.URL, board), params={**self.keys})

        for board_list in json.loads(resp.content.decode('utf-8')):
            if list_name in board_list['name']:
                return board_list['id']

        return None

    def duplicate(self, source, board, list_name):
        list_id = self.find_list_id(board, list_name)

        requests.post('https://api.trello.com/1/cards', params=
                      {
                          **self.keys,
                          'idList': list_id,
                          'idCardSource': source
                      })

if __name__ == '__main__':
    print('Trello card duplicater v{}'.format(VERSION))
    parser = ArgumentParser()

    parser.add_argument('-s', '--source', help='Source card ID', required=True)
    parser.add_argument('-b', '--board', help='Destination board ID', required=True)
    parser.add_argument('-l', '--list', help='Destination list name substring', required=True)

    args = parser.parse_args()

    with open('config.json') as i:
        r = Redmine(json.load(i))
        r.duplicate(args.source, args.board, args.list)
        print('done')
