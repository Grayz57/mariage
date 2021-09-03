from otree.api import *
from typing import List
import csv
import time
import datetime

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'marriage'
    players_per_group = None
    num_rounds = 1

    num_choices = 20
    radio_list_choices = list(range(1, num_choices + 1))
    radio_list_probabilities = [0, 20] + [n for n in range(35, 95, 5)] + [93, 95, 97, 98, 99, 100]
    radio_list = list(zip(radio_list_choices, radio_list_probabilities))

    bubble_chart_title = ''
    bubble_chart_series = [
        [9, 81, 63], [98, 5, 89], [51, 50, 73], [41, 22, 14], [58, 24, 20], [78, 37, 34], [55, 56, 53], [18, 45, 70],
        [42, 44, 28], [3, 52, 59], [31, 18, 97], [79, 91, 63], [93, 23, 23], [44, 83, 22]
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    case_id = models.StringField(initial='955')
    decision = models.IntegerField(initial=0)


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        cases = read_csv_table('cases')
        for case in cases:
            add_timestamp_to_case(case)
            add_table_to_case(case)
        subsession.session.cases_by_similarity = cases


def read_csv_table(file_name, path='marriage/static/data/') -> list:
    with open(f'{path}{file_name}.csv', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def add_timestamp_to_case(case: dict):
    case['timestamp'] = time.mktime(datetime.datetime.strptime(case['Date'], "%d/%m/%Y").timetuple())


def add_table_to_case(case: dict):
    case['table'] = '<div class="highcharts-data-point-info">' + \
                    f'<p>La décision <b class="color-amber">n&#186; {case["case_id"]}</b> ' \
                    f'en date du <b class="color-amber">{case["Date"]}</b> présente ' \
                    f'<b class="color-amber">{case["Taux de correspondance"]}%</b> de correspondance ' \
                    f'avec votre requête.</p>' + \
                    '<ul>' + \
                    ''.join(f'<li>{k}: {v}</li>' for k, v in case.items()
                            if k not in ['Taux de correspondance', 'Date', 'case_id', 'timestamp']) + \
                    '</ul>' + \
                    '</div>'


def get_cases_series_by_decision(cases: list, decision: str) -> List[dict]:
    return [
        dict(
            x=case['timestamp'] * 1000,
            y=int(case['Taux de correspondance']),
            z=int(case['Montant de la PC']),
            case_id=case['case_id'],
            date=case['Date'],
            table=case['table']
        ) for case in cases if case['Decision'] == decision
    ]


# PAGES
class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class BubbleChart(Page):
    @staticmethod
    def js_vars(player: Player):
        const = Constants
        cases = player.session.cases_by_similarity
        cases = [case for case in cases if case['case_id'] == player.case_id]
        cases_series = dict(
            condemnation=dict(
                name='Condamnation',
                data=get_cases_series_by_decision(cases, 'Condamnation')
            ),
            condemnation_no=dict(
                name='Absence de condamnation',
                data=get_cases_series_by_decision(cases, 'Non Condamnation')
            )
        )

        return dict(
            bubble_chart_title=const.bubble_chart_title,
            cases_series=cases_series
        )


page_sequence = [Decision, BubbleChart]
