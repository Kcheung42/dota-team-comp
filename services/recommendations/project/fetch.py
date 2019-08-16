import request
from project.api.models import Match

def fetch_matches():
    response = requests.get('https://api.opendota.com/api/publicMatches?api_key=6ac234f2-0bfb-425e-abb1-8fe2fcf1d508')
    matches = response.json()
    if matches:
        for d in data:
            match_id = d['match_id']
            match = User.query.filter_by(match_id=match_id)
            if not match:
                db.session.add(
                    Match(
                        match_id=d['match_id'],
                        radiant_win=['radiant_win'],
                        radiant_team=['radiant_team'],
                        dire_team=['dire_team']
                        )
                )
                db.session.commit()
