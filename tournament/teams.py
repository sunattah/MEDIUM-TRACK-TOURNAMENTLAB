def normalize_name(name: str) -> str:


## strip() then casefold(), return

    return    name.strip().casefold()


if __name__ == "__main__":
        print(normalize_name("   sunday  "))

def make_team(team_id: str, name: str) -> dict:
      return {team_id: "ID", name : "name"}
def validate_team_name(name: str) -> str | None:
    return None, f"Error finding {name}"
def find_team_by_name(league: dict, name: str) -> dict | None:
    return {league: {}, name: "name"}, None
def generate_team_id(league: dict) -> str:
    return league, "name"
def register_team(league: dict, name: str) -> tuple[bool, str]:
    