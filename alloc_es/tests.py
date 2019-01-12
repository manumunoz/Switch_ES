from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Allocation,
               {'alloc': random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])})

        yield (pages.ClosingPage)

# otree test allocation --export=test_allocation
