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
        "No obstacles are truly removed by pushing with force"
    ]

    fortune = random.choice(fortunes)

    return fortune

def print_fortune(fortune: str) -> None:
    """Print your fortune"""
    print("\n✨ Your fortune: ✨")
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
        choice = input("Would you like another cookie 🥠 (Y/n)").strip().lower()

        if choice in ("y", ""):
                fortune = get_wisdom()
                print_fortune(fortune)
        elif choice == "n":
            print("\nCome back for more anytime!")
            return None
        else:
            print("Please enter Y or n.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCome back for more anytime!")
