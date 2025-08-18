from django.urls import path

from characters.views import get_random_characters
from characters.views import CharacterListView

urlpatterns = [
    path("character/random/", get_random_characters, name="character-random" ),
    path("characters", CharacterListView.as_view(), name="characters-list" ),
]

app_name = "characters"
