def battery_status(level):
    if level > 70:
        return "high"
    elif level > 30:
        return "medium"
    else:
        return "low - return to dock"


for lvl in [90, 15, 15]:
    print(lvl, "->", battery_status(lvl))