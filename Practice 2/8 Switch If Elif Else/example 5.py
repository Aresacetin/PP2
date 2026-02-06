# matching spells in game
spell = "Fireball"
match spell:
    case "Fireball":
        print("10 fire damage")
    case "Thunderbolt":
        print("14 electro damage")
    case "Divine blast":
        print("25 holy damage")
    case "Waterbolt":
        print("7 water damage")
    case _:
        print("Cast a proper spell")

