from TextColour import TextColour, colour
from random import randrange
from math import ceil


GREEN  = TextColour.GREEN
YELLOW = TextColour.YELLOW
RED    = TextColour.RED
MIN_HEALTH = 0
MAX_HEALTH = 100
SCALE_FACTOR = int(MAX_HEALTH / 5)
HEALTH_BIT = '='

sample_health = randrange(MIN_HEALTH, MAX_HEALTH)

# PART 1
health_bar_length = health_bar_length = ceil(sample_health / MAX_HEALTH * SCALE_FACTOR)

# PART 2
health_num_string = f"HP: {sample_health} / {MAX_HEALTH}"
health_bar_string = f"[{HEALTH_BIT * health_bar_length:<{SCALE_FACTOR}s}]"

if 0 <= sample_health <= 33:
    health_num_string = colour(health_num_string, RED)
    health_bar_string = colour(health_bar_string, RED)
elif 34 <= sample_health <= 66:
    health_num_string = colour(health_num_string, YELLOW)
    health_bar_string = colour(health_bar_string, YELLOW)
else:
    health_num_string = colour(health_num_string, GREEN)
    health_bar_string = colour(health_bar_string, GREEN)

print(health_num_string)
print(health_bar_string)