def normalize_name(name: str) -> str:


## strip() then casefold(), return

name_list = name.strip().casefold()
return name_list
print(normalize_name("   sunday  "))