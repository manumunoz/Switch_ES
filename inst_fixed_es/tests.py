from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.WelcomeInst)
        yield (pages.DecisionsInst,
               {'given_group': 1, 'appearance': 1, 'label': 2, 'active': 3, 'count': 3})
        yield (pages.PointsInst,
               {'pay_coord': 1, 'pay_nocoord':3})
        yield (pages.SummaryInst)

# otree test inst_fixed --export=test_inst_fixed

