from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions FLUID
"""

class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'inst_fluid_en'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    instructions_template = 'inst_fluid_en/Instructions.html'
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    others = len(names) - 1
    total_circles = 4
    total_triangles = 3
    part_name = 1
    part_fixed = 2
    part_fluid = 3
    part_alloc = 4
    rounds_fixed = 10
    #------------------------------------------
    # Payoffs
    exp_currency = "points"
    currency = "pesos"
    currency_exchange = 800
    points_exchange = 1
    min_pay = 10000
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    switch_cost = 6
    #------------------------------------------
    # Interdependent Costs
    multiplier = 2
    n_min = 3
    n_maj = 4
    #------------------------------------------
    # Group Names
    group_a = 'Lions' #Leones
    group_b = 'Tigers' #Tigres
    group_c = 'Leopards' #Leopardos
    group_d = 'Jaguars' #Jaguares
    group_e = 'Cats' #Gatos
    group_f = 'Coyotes' #Coyotes
    group_g = 'Jackals' #Chacales
    group_h = 'Wolves' #Lobos
    group_i = 'Foxes' #Zorros
    group_j = 'Dogs' #Perros
    #------------------------------------------


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3, 4, 5, 6])
        # 1: Full-Free, 2: Sticky-Free, 3: Blurry-Free, 4: Full-Cost, 5: Sticky-Cost, 6: Blurry-Cost
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 6

    given_group = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    appearance = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round by changing my group'],
        ],
        widget=widgets.RadioSelect
    )

    label = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    cost_change_one = models.PositiveIntegerField(
        choices=[
            [1, '6 fixed + 2 for 2 players who did not change = 10 points'],
            [2, '6 fixed + 0 because all players changed = 6 points'],
            [3, '6 fixed + 2 for 1 player who did not change = 8 points']
        ],
        widget=widgets.RadioSelect
    )

    cost_change_none = models.PositiveIntegerField(
        choices=[
            [1, '6 fixed + 2 for 2 players who did not change = 10 points'],
            [2, '6 fixed + 0 because all players changed = 6 points'],
            [3, '6 fixed + 2 for 1 player who did not change = 8 points']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord = models.PositiveIntegerField(
        choices=[
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord2 = models.PositiveIntegerField(
        choices=[
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )

    information = models.PositiveIntegerField(
        choices=[
            [1, 'They can see the group I choose and my new appearance'],
            [2, 'They can see the group I choose and my appearance from Part {}'.format(Constants.part_fixed)],
            [3, 'They cannot see the group I choose only my appearance from Part {}'.format(Constants.part_fixed)],
        ],
        widget=widgets.RadioSelect
    )

    revelation_cost = models.PositiveIntegerField(
        choices=[
            [1, '6 points'],
            [2, '0 points'],
            [3, '10 points']
        ],
        widget=widgets.RadioSelect
    )


    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
            'names': len(Constants.names)
        }
