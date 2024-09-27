from random import uniform, random


def main():
    score = float(input("Enter score:"))
    result = evaluate_score(score)
    print(result)

    random_score = uniform(0,100)
    print("random_socre", random_score)
    print(evaluate_score(random_score))


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "bad"
    elif score < 90:
        return "passable"
    else:
        return "excellent"

main()