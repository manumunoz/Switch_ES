from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeP2WP(WaitPage):
    pass


class WelcomeP2(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


class GroupChangeInstWP(WaitPage):
    pass


class GroupChangeInst(Page):
    form_model = 'player'
    form_fields = ['given_group','appearance','label','pay_coord','pay_coord2','information']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def given_group_error_message(self, value):
        if value != 3:
            return 'En esta Parte usted puede cambiarse de grupo en cada ronda'

    def appearance_error_message(self, value):
        if self.player.treat == 1 or self.player.treat == 4:
            if value != 3:
                return 'En esta Parte usted puede cambiar su apariencia cuando usted cambia su grupo'
        elif self.player.treat != 1 and self.player.treat != 4:
            if value != 1:
                return 'En esta Parte usted no puede cambiar su apariencia aunque cambie de grupo'

    def label_error_message(self, value):
        if value != 2:
            return 'En esta Parte su etiqueta se asigna aleatoriamente en cada ronda'

    def pay_coord_error_message(self, value):
        if value != 2:
            return 'Un jugador en este grupo recibe 4 puntos por cada coordinación en la acción violeta con una ' \
                   'conexión activa y paga 2 puntos por proponer esa conexión'

    def pay_coord2_error_message(self, value):
        if value != 1:
            return 'Un jugador en este grupo recibe 6 puntos por cada coordinación en la acción violeta con una ' \
                   'conexión activa y paga 2 puntos por proponer esa conexión'

    def information_error_message(self, value):
        if self.player.treat == 1:
            if value != 1:
                return 'Los demás jugadores verán el grupo que usted haya elegido. También verán su nueva apariencia'
        elif self.player.treat == 2:
            if value != 2:
                return 'Los demás jugadores verán el grupo que usted haya elegido. También verá  su apariencia que no cambia respecto ' \
                       'a las partes anteriores'
        elif self.player.treat == 3:
            if value != 3:
                return 'Ls demás jugadores no verán el grupo que usted ha elegido. Pero sí verán su apariencia que no cambia ' \
                       'respecto a las partes anteriores'


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    WelcomeP2WP,
    WelcomeP2,
    GroupChangeInstWP,
    GroupChangeInst,
    SummaryInstWP,
    SummaryInst,
]
