"""Garden Advice Application"""

# Variable definition section
season = input("What season would you like advice for? (Summer, Winter, Autumn, Spring)\n").lower()
plant_type = input("What type of plant would you like advice for? (Flower, Vegetable)\n").lower()


# Season advice section
def get_season_advice(season):
    """Returns gardening advice based on the season."""
    if season == "summer":
        season_advice = "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        season_advice = "Protect your plants from frost with covers.\n"
    else:
        season_advice = "No advice for this season.\n"
    return season_advice


# Plant advice section
def get_plant_advice(plant_type):
    """Returns gardening advice based on plant type."""
    if plant_type == "flower":
        plant_advice = "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        plant_advice = "Keep an eye out for pests!"
    else:
        plant_advice = "No advice for this type of plant."
    return plant_advice


season_advice = get_season_advice(season)
plant_advice = get_plant_advice(plant_type)

advice = f"\nDuring {season}, it is important to: {season_advice} " \
         f"When planting {plant_type}s, it is important to: {plant_advice}"

print(advice)