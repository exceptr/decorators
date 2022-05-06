import requests as requests
from debug_utils import make_logger


@make_logger('logs.json')
def get_max_intelligence_hero():
    hero_intelligence = {}
    request_url = f"https://superheroapi.com/api/2619421814940190/332/powerstats"
    response = requests.get(request_url)
    hero_intelligence['Hulk'] = int(response.json()['intelligence'])
    request_url = f"https://superheroapi.com/api/2619421814940190/149/powerstats"
    response = requests.get(request_url)
    hero_intelligence['CaptainAmerica'] = int(response.json()['intelligence'])
    request_url = f"https://superheroapi.com/api/2619421814940190/655/powerstats"
    response = requests.get(request_url)
    hero_intelligence['Thanos'] = int(response.json()['intelligence'])
    max_intelligence = max(hero_intelligence, key=hero_intelligence.get)
    return max_intelligence


if __name__ == '__main__':
    get_max_intelligence_hero()