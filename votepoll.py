class VotePoll:
    def __init__(self, options):
        self.options = options
        self.votes = {option: 0 for option in options}

    def cast_vote(self, option):
        if option in self.votes:
            self.votes[option] += 1
            print(f"Vote cast for {option}.")
        else:
            print(f"{option} is not a valid option.")

    def show_results(self):
        print("\nVoting Results:")
        for option, count in self.votes.items():
            print(f"{option}: {count} votes")

def main():
    print("Welcome to the Voting Poll!")
    options = input("Enter the options for the poll, separated by commas: ").split(',')

    poll = VotePoll(options)

    while True:
        print("\nVote Poll Menu:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print(f"{len(options) + 1}. Show results")
        print(f"{len(options) + 2}. Exit")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                poll.cast_vote(options[choice - 1])
            elif choice == len(options) + 1:
                poll.show_results()
            elif choice == len(options) + 2:
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
