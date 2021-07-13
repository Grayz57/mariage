from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ellsberg_two_urns'
    players_per_group = None

    num_balls = 100
    prize = cu(100)

    questions = [
        (45, 55),
        {'A': (65, 35), 'B': (25, 75)},
        {'A': (75, 25), 'B': (55, 45)},
        {'A': (35, 65), 'B': (15, 85)},
        {'A': (80, 20), 'B': (70, 30)},
        {'A': (60, 40), 'B': (50, 50)},
        {'A': (40, 60), 'B': (30, 70)},
        {'A': (20, 80), 'B': (10, 90)},
        {'A': (90, 10), 'B': (5, 95)}
    ]

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ball = models.StringField(
        label=f'Please choose the color of the ball that provides you {Constants.prize}:',
        choices=[('white', 'White'), ('black', 'Black'),('yellow', 'Yellow')], widget=widgets.RadioSelect
    )
    urn = models.StringField(
        label='',
        choices=[('A', 'Urn A'), ('B', 'Urn B')], widget=widgets.RadioSelect
    )


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


class ChooseUrn(Page):
    form_model = 'player'
    form_fields = ['urn']

    @staticmethod
    def vars_for_template(player: Player):
        curr_round = player.round_number
        ball = player.participant.vars['ball']
        other_ball = 'white' if ball == 'black' else 'black'

        q = Constants.questions[player.round_number-1]
        if curr_round > 1:
            q = q[player.in_round(curr_round - 1).urn]
        return dict(ball=ball, other_ball=other_ball, q=q)


page_sequence = [ChooseBall, ChooseUrn]