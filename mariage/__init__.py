from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'graalieatooo'
    players_per_group = None
    num_balls = 100
    prize = cu(100)
    win = cu(20)
    timer_text = 'Time remaining'

    aquestions = [
        (0,"",40,'',60,''), ## risk
        ("between [0;", "10]","between [ 30;","50]", "and between [50;","70]"),
        (0, 100, 20, 60, 50, 100),
        (30, 40, 30, 50, 70, 80)
    ]

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
    p_amb = models.IntegerField(initial=0)
    timeSpent = models.FloatField()
# PAGES
class Apa(Page):
    form_model = 'player'
    form_fields = ['p_amb', 'timeSpent']
    timer_text ='Time remaining'

    @staticmethod
    def vars_for_template(player: Player):
        curr_round = player.round_number
        ball = 'black'
        other_ball = 'yellow'
        second_ball = 'red'


        q = Constants.aquestions[player.round_number - 1]
        return dict(ball=ball, other_ball=other_ball, second_ball=second_ball, q=q)

page_sequence = [Apa]