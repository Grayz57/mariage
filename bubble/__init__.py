from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'charts'
    players_per_group = None
    num_rounds = 1

    bubble_chart_title = 'This is a bubble chart'
    bubble_chart_series_1 = [
        [9, 81, 63], [98, 5, 89], [51, 50, 73], [41, 22, 14], [58, 24, 20], [78, 37, 34], [55, 56, 53], [18, 45, 70],
        [42, 44, 28], [3, 52, 59], [31, 18, 97], [79, 91, 63], [93, 23, 23], [44, 83, 22]
    ]

    bubble_chart_series_2 = [
        [42, 38, 20], [6, 18, 1], [1, 93, 55], [57, 2, 90], [80, 76, 22], [11, 74, 96], [88, 56, 10], [30, 47, 49],
        [57, 62, 98], [4, 16, 16], [46, 10, 11], [22, 87, 89], [57, 91, 82], [45, 15, 98]
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class BubbleChart(Page):
    @staticmethod
    def js_vars(player: Player):
        const = Constants
        return dict(
            bubble_chart_title=const.bubble_chart_title,
            bubble_chart_series_1=const.bubble_chart_series_1,
            bubble_chart_series_2=const.bubble_chart_series_2
        )


page_sequence = [BubbleChart]