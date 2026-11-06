def normalize_name(name: str) -> str:


## strip() then casefold(), return

    return    name.strip().casefold()


if __name__ == "__main__":
        print(normalize_name("   sunday  "))

def make_team(team_id: str, name: str) -> dict:
    return {"id": team_id, "name": name}
def validate_team_name(name: str) -> str | None:
    return None, f"Error finding {name}"
def find_team_by_name(league: dict, name: str) -> dict | None:
    target = normalize_name(name)
    for team in league["teams"]:
        if <comparison>:
            return team
    return None
def generate_team_id(league: dict) -> str:
    return "TM" + str(league["next_team_num"]).zfill(3)
def register_team(league: dict, name: str) -> tuple[bool, str]:
    pass
def list_teams(league: dict) -> list[dict]:
    return list(league["teams"])