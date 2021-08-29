from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'graalitooo'
    players_per_group = None
    num_balls = 100
    prize = cu(100)
    win = cu(20)


    aquestions = [
        (0,0,0,0,0,0),
        (1,1,1,1,1,1),
        (2,2,2,2,2,2),
        (3,3,3,3,3,3),
        (0, 10, 20, 50, 30, 70),
        (0, 100, 20, 60, 50, 100),
        (30, 40, 30, 50, 70, 80)
    ]

    def creating_session(subsession):
        if subsession.round_number == 1:
            for player in subsession.get_players():
                participant = player.participant
                import random
                randomized_questions = random.sample(Constants.aquestions, len(Constants.aquestions))
    num_rounds = len(aquestions)

    qs_range_inputs = [f'q{p + 1}' for p in range(23, 25)]

    num_columns = 2

    num_choices = 20
    radio_list_choices = list(range(1, num_choices + 1))
    radio_list_probabilities = [0, 1, 2] + [n for n in range(5, 75, 5)] + [85, 100]
    radio_list_probabilities_two_events = [0, 20] + [n for n in range(35, 95, 5)] + [93, 95, 97, 98, 99, 100]
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


    p_amb = models.IntegerField(initial=0)

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


class Apa(Page):
    form_model = 'player'
    form_fields = ['p_amb']

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

        q = Constants.randomized_questions[player.round_number - 1]
        return dict(ball=ball, other_ball=other_ball, second_ball=second_ball, q=q)

page_sequence = [ChooseBall, Apa]