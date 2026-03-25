# Hardcoded values for the season and plant type
season = input("What season would you like advice for? (Summer, Winter, "
               "Autumn, Spring)\n").lower()
plant_type = input("What type of plant would you like advice for?"
                   "(Flower, Vegetable)\n").lower()


# Determine advice based on the season
def get_season_advice(season):
    if season == "summer":
        season_advice = "Water your plants regularly "
        "and provide some shade.\n"
    elif season == "winter":
        season_advice = "Protect your plants from frost with covers.\n"
    else:
        season_advice = "No advice for this season.\n"
    return season_advice


# Determine advice based on the plant type
def get_plant_advice(plant_type):
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

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
