import random

NUMBERS_COUNT = 6
NUMBER_RANGE = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(number_of_picks)
    print_quick_picks(quick_picks)


def generate_quick_picks(number_of_picks):
    quick_picks = []
    for _ in range(number_of_picks):
        pick = random.sample(range(1, NUMBER_RANGE + 1), NUMBERS_COUNT)
        quick_picks.append(sorted(pick))
    return quick_picks

def print_quick_picks(quick_picks):
    for pick in quick_picks:
        print(" ".join(f"{num:2}" for num in pick))

main()
















