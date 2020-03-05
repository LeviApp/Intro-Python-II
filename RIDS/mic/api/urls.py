from django.urls import path
from mic.api.views import cities_api, players_api, criminals_api, cases_api, places_api, witnesses_api, responses_api

app_name = 'mic'
urlpatterns = [
    path(f'cities/', cities_api, name='cities'),
    path(f'players/', players_api, name='players'),
    path(f'criminals/', criminals_api, name='criminals'),
    path(f'cases/', cases_api, name='cases'),
    path(f'places/', places_api, name='places'),
    path(f'witnesses/', witnesses_api, name='witnesses'),
    path(f'responses/', responses_api, name='responses'),

]