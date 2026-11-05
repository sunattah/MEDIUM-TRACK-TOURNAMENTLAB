def normalize_name(name: str) -> str:


## strip() then casefold(), return

    return    name.strip().casefold()


if __name__ == "__main__":
        print(normalize_name("   sunday  "))