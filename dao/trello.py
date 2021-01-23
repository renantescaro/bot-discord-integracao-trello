import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class TrelloDao:
    dashboard_id = ''
    headers = {
        "Accept": "application/json"
    }

    def get(self, url):
        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            params={
                'key'   : os.getenv('TRELLO_KEY'),
                'token' : os.getenv('TRELLO_TOKEN')
            }
        )
        return response

    def get_cards_dashboard(self):
        lists = self.get_lists_dashboard()
        cards = self.get_cards_list(lists)
        return self.formatar_discord(cards)
    
    def get_lists_dashboard(self):
        response = self.get('https://api.trello.com/1/boards/'+self.dashboard_id+'/lists')
        response_json = response.json()
        lista = []
        for lista_json in response_json:
            lista.append({
                'id':lista_json['id'],
                'name':lista_json['name']})
        return lista

    def get_cards_list(self, lists):
        listas_com_cards = []
        for lista in lists:
            response_cards_list = self.get('https://api.trello.com/1/lists/'+lista['id']+'/cards')
            response_json_cards_list = response_cards_list.json()    
            cards_in_list = []
            for card in response_json_cards_list:
                cards_in_list.append({
                    'name': card['name'],
                    'desc': card['desc']
                })
            listas_com_cards.append({
                'list_name': lista['name'],
                'cards_in_list': cards_in_list
            })
        return listas_com_cards

    def formatar_discord(self, cards_in_list):
        texto_dircord = ''
        for lista in cards_in_list:
            lista_com_cards_str = '** '+lista['list_name']+' **\n'
            for card in lista['cards_in_list']:
                lista_com_cards_str += ( card['name'] + ' - ' + card['desc'] +'\n\n')
            texto_dircord += lista_com_cards_str

        return [texto_dircord[0:1999]]