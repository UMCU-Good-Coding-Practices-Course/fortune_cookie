import random


def get_wisdom() -> str:
    """Return a random wisdom from the list.

    Returns
    -------
    str
        A randomly selected fortune message.
    """
    fortunes = [
        "If the duck understands, your code is good",
        "Commit to two things in life: your spouse and git",
        "Errors should never pass silently",
        "Coding repetition prevents code repetition",
        "No obstacles are truly removed by pushing with force",
	      "fajfauhfahfa",
        "Life is too short to learn all the programming languages",
        "The best way to predict the future is to create it",
        "The best way to get a project done faster is to start sooner",
        "Don't let perfection be the enemy of good enough",
        "One bird in hand is better than two in the bush",
        "No obstacles are truly removed by pushing with force",
        "Don't be afraid to ask for help, even if it means asking a rubber duck",
        "In the face of ambiguity, refuse the temptation to guess",
        "There should be one-- and preferably only one --obvious way to do it",
        "Let branches be pointers in your life"
    ]

    fortune = random.choice(fortunes)

    return fortune

def print_fortune(fortune: str) -> None:
    """Print your fortune"""
    print("\n✨✨ Your fortune: ✨✨")
    print(f"\"{fortune}\"\n")

def main(first_cookie: bool=True) -> None:
    """Run the interactive fortune cookie simulator.

    Returns
    -------
    None
        This function does not return a value.
    """
    print("\nWelcome to the Fortune Cookie Simulator 🥠")
    input("Press Enter to crack open your cookie 🥠 (or ctrl+c if you're not hungry) ... ")

    # Get and display the fortune
    fortune = get_wisdom()
    print_fortune(fortune)
    
    # Ask for another cookie
    while True:
        choice = input("Which cookie would you like 🥠 " \
        "a. white chocolate/ b.rainbow chocolate / c. black chocolate / n. none of them)").strip().lower()

        if choice == "a":
            fortune = get_wisdom()
            print_fortune(fortune)
        elif choice == "b":
            fortune = get_wisdom()
            print_fortune(fortune)
        elif choice == "c":
            fortune = get_wisdom()
            print_fortune(fortune)
        elif choice == "n":
            print("\nCome back for more anytime!")
            return None
        else:
            print("Please enter a/b/c or n.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n ✨ Come back for more anytime! ✨ ")
