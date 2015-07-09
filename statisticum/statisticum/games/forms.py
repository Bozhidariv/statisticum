from django.forms import ModelForm
from statisticum.games.models import Game, GameScore
from django.forms.models import inlineformset_factory


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"

class GameScoreForm(ModelForm):
    class Meta:
        model = GameScore
        fields = "__all__"


AddGameScoreFormset = inlineformset_factory(Game,GameScore,extra=1,fields="__all__")