import os
from dotenv import load_dotenv
from dao.cron import CronDao

class ReuniaoDao:
    def __init__(self):
        load_dotenv()
        self.cron_dao = CronDao()

    def get_reunioes_texto(self):
        cron1 = str(os.getenv('REUNIAO_CRON_1'))
        cron2 = str(os.getenv('REUNIAO_CRON_2'))
        txt1  = self.cron_dao.get_descricao(cron1)
        txt2  = self.cron_dao.get_descricao(cron2)
        return str(txt1) + '\n\n' + str(txt2)

    def get_horas_texto(self, cron_expressao):
        # ERRO NA LIB
        return ('Reunião geral hoje as ' + str(self.cron_dao.get_horas(cron_expressao))+' !!')

    def get_horas_texto_1(self):
        return str(os.getenv('REUNIAO_TEXTO_1'))

    def get_horas_texto_2(self):
        return str(os.getenv('REUNIAO_TEXTO_2'))

