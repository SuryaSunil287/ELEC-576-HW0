# Work on these problems with your group.
# You will submit one solution for the entire group.
#
# You should write the Python using only your group's knowledge and
# the Python documentation (the "Docs" link on the CodeSkulptor page).
#
#   Full Names:
#     Arati Pati
#     Saif Khan


import matplotlib.pyplot as plt
import math
import random


def roll(num_dice, num_sides):
    """
    Simulates rolling the specified number of dice (num_dice), each of which has the
    specified number of sides (num_sides), and returns the sum of all of the dice that
    were rolled.
    """

    #outcome = random.randint(1, num_sides)
    #num = print(random.randint(1, 6))


    dice_list = []
    sum_of_dice = 0
    for num in range(0, num_dice):
        dice_list.append(random.randint(1, num_sides))


    sum_of_dice = sum(dice_list)

    return sum_of_dice

#print("Sum of Dice is :",roll(3, 12))

def run_experiments(num_trials, num_dice, num_sides):
    """
    Runs the specified number of trials (num_trials), where each trial should involve
    rolling the specified number of dice with the specified number of sides. Builds
    and plots a histogram of the results.
    """

    #exp_list = [0]*num_sides
    trials_list = []
    sum_of_dice = 0
    for trials in range(0, num_trials):
        sum_of_dice = roll(num_dice, num_sides)
        trials_list.append(sum_of_dice)


   #plt.hist(trials_list)

    #plt.hist([1,2,3,4], bins = 4, color = None , Stacked = False , edgecolor = None)
    #plt.show()
    #sum_exp = sum(dice_list)
    return trials_list


trial2 = run_experiments(30, 3, 10)
print(trial2)
plt.hist(trial2, bins = 4, color = None , Stacked = False , edgecolor = None)

#plt.hist([1,2,3,4], bins = 4, color = None , Stacked = False , edgecolor = None)

# Uncomment the following line, and add your own additional calls to run_experiments,
# when you're ready to run some experiments and see the results.
#run_experiments(100, 3, 6)