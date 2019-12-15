"""
Add quotes later, add three problem solvers
___author___ Zina Atia
"""

name = (input("HI! Thanks for joining me? What's is your Name?"))

print("Wonderful to meet you", name)

print("I would like to give you this letter that I think you might find "
      "interesting.")

print("Congratulations!\n"
      "\tYou have been selected to help stop Dr.Vladimir from contaminating "
      "the cities only water supply. In order to stop him, you must risk "
      "discovery by going into his layer and cracking his top secret password"
      " by answering a series of questions. Its up to you to make your choice. "
      "If you succeed in your mission, you will be rewarded $1,000,000,000. "
      "We hope we can count you on our team. "

      )
input("press enter to continue")

choice_1 = input("Is this something you w f4ould be interested in? "
                 "(Hint: yes or no)")


def shop():
    """Demonstrates basic outputs and if try statements"""
    if choice_1 == "yes":
        print("Great!, Wonderful to have you here")


    elif choice_1 == "no":
        print("Too bad:(, will have to erase your memory now, Good Bye")


shop()
