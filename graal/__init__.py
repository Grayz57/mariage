from otree.api import *
from . import widgets_custom as widgets_cstm
from wtforms.validators import Length, IPAddress
import re

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'graalito'
    players_per_group = None
    num_rounds = 1
    num_balls = 100
    prize = cu(100)

    questions = [
        (33, 33, 34),
        (10,10,20),
        (50,20,30)
    ]

    num_rounds = len(questions)



    qs_radio = [f'q{m + 1}' for m in range(10, 20)]
    choices_radio = list(range(1, 8))

    qs_buttons = [f'q{o + 1}' for o in range(20, 23)]

    qs_range_inputs = [f'q{p + 1}' for p in range(23, 25)]

    num_columns = 2

    num_choices = 20
    radio_list_choices = list(range(1, num_choices + 1))
    radio_list_probabilities = [0, 20] + [n for n in range(35, 95, 5)] + [93, 95, 97, 98, 99, 100]
    radio_list = list(zip(radio_list_choices, radio_list_probabilities))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ball = models.StringField(
        label=f'Please choose the color of the ball that provides you {Constants.prize}:',
        choices=[('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow')], widget=widgets.RadioSelect
    )

    for q in Constants.qs_radio:
        locals()[q] = models.IntegerField(
            choices=Constants.choices_radio,
            widget=widgets.RadioSelect,
            blank=True
        )
    del q

    radio_list_decision = models.IntegerField(initial=0)


# PAGES
class ChooseBall(Page):
    form_model = 'player'
    form_fields = ['ball']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['ball'] = player.ball

class RadioList(Page):
    form_model = 'player'
    form_fields = ['radio_list_decision']

    @staticmethod
    def vars_for_template(player: Player):
        curr_round = player.round_number
        ball = player.participant.vars['ball']
        other_ball = 'j'
        if ball == 'white':
            other_ball = 'black'
        elif ball == 'yellow':
            other_ball ='black'
        else:
            other_ball ='white'

        second_ball = 'yellow'

        if ball == 'white':
            second_ball = 'yellow'
        elif ball == 'black':
            second_ball = 'yellow'
        else:
            second_ball = 'white'

        q = Constants.questions[player.round_number - 1]
        return dict(ball=ball, other_ball=other_ball, second_ball=second_ball, q=q)

page_sequence = [ChooseBall, RadioList]