from datetime import datetime, timedelta

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro','outubro', 'novembro', 'dezembro'
        ]

        mes_atual = self.momento_cadastro.month - 1 # índice do month começa em 1, indíce de array em 0
        return meses_do_ano[mes_atual]

    def dia_cadastro(self):
        dias_semana = [
            'segunda-feira', 'terça-feira', 'quarta-feira','quinta-feira', 'sexta-feira', 'sábado', 'domingo'
        ]

        dia_atual = self.momento_cadastro.weekday()
        return dias_semana[dia_atual]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M:%S')
        return data_formatada

    def tempo_cadastro(self):
        tempo = (datetime.today() + timedelta(days=30))- self.momento_cadastro
        return tempo

