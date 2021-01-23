import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class TrelloDao:
    dashboard_id = os.getenv('TRELLO_DASHBOARD_ID')
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
        return self.formatar_em_texto(cards)
    
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

    def formatar_em_texto(self, cards_in_list):
        texto_str = ''
        for lista in cards_in_list:
            # nome da lista
            lista_com_cards_str = '*'+lista['list_name']+'*\n'
            # percorre todos os cards da lista
            for card in lista['cards_in_list']:
                lista_com_cards_str += ( card['name'] + ' -> ' + card['desc'] +'\n')
            texto_str += ( lista_com_cards_str + '\n\n' )
        return texto_str