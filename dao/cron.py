from cron_descriptor import get_description, ExpressionDescriptor, Options

class CronDao:
    def __init__(self):
        self.options = Options()
        self.options.locale_code = 'pt_PT'

    def get_descricao(self, cron_expressao):
        descripter = ExpressionDescriptor(cron_expressao, self.options)
        return descripter.get_description()

    def get_horas(self, cron_expressao):
        descripter = ExpressionDescriptor(cron_expressao, self.options)
        # ERRO NA LIB
        return descripter.get_hours_description()