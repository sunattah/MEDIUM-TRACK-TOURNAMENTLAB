## tournament 
today is 4 november 2026 i am working on a project called the tournament where i have 4 teams playing and one to win

## this is the file structure

tournamentlab/
├── main.py                    # entry point, calls cli.run()
├── tournament/
│   ├── __init__.py            # empty
│   ├── teams.py               # register_team, list_teams, find_team
│   ├── fixtures.py            # generate_fixtures, list_fixtures, get_fixture
│   ├── scoring.py             # record_result, validate_score
│   ├── standings.py           # compute_standings, rank_teams, is_league_complete, get_champion
│   ├── storage.py             # save_league, load_league, validate_loaded_league
│   └── cli.py                 # menu loop, dispatches to functions above
├── tests/
│   ├── __init__.py
│   ├── test_teams.py
│   ├── test_fixtures.py
│   ├── test_scoring.py
│   ├── test_standings.py
│   └── test_storage.py
├── data/                      # for saved JSON (gitignored)
├── docs/
│   ├── design-decisions.md
│   └── ai-learning-log.md
├── README.md
└── .gitignore