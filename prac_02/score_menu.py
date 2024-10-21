def main():
    """display menu and process user's choice"""
    menu = ("(G)et a valid score"
            "(P)rint result"
            "(S)how stars"
            "(Q)uit")
    print(menu)
    score = get_valid_score()
    choice = get_choice()


def get_valid_score(score):
    """get valid score (ensure 0 - 100)"""
    while score < 0 or score > 100:
        print("invalid score")
        score = float(input("Enter score(0-100):"))
    return score

def evaluate_score(score):
    """give evaluation based on score"""

    if score < 50:
        return "bad"
    elif score < 90:
        return "passable"
    else:
        return "excellent"

def show_stars(score):
    """print stars based on score"""
    print("*" * int(score))

def get_choice(choice,score):
    if choice == "G":
        score = get_valid_score()
    elif choice == "P":
        result = evaluate_score(score)
        print("result is ",result)
    elif choice == "S":
        show_stars(score)
    elif choice == "Q":
        print("Thanks for using,BYE!!")
        return score
main()