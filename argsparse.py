import argparse

tanks = {
    "tank_a": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}

parser = argparse.ArgumentParser(description="List fish in aquarium.")
parser.add_argument("tank", type=str, help="Tank to print fish from.")
parser.add_argument("--upper-case", '-u',  default=False, action="store_true", help="Upper case the outputted fish.")
parser.add_argument('-n', dest='now', action='store_true', help="shows now")

args = parser.parse_args()

fish = tank_to_fish[args.tank]

if args.upper_case:
    fish = fish.upper()

print(fish)

# parser.add_argument('filename')           # positional argument
# parser.add_argument('-c', '--count')      # option that takes a value
# parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
