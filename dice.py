import random


class DiceSimulator():
    """ Dice simulator the rolls dice and takes the average of their rolls.
    """
    def __init__(self):
        self.sum = 0
        
    """ rolls dice and returns sum of dice thrown
        params:
            num_die: int of number of die to throw
            num_sides: int of how sides die have
        returns sum and average of dice thrown.
    """
    def rollDie(self, num_die, num_sides):
        min = 1
        max = num_sides

        rolls = []
        for i in range (1, num_die + 1):
            roll_value = random.randint(min, max)
            print("Roll {}: {}".format(i, roll_value))
            self.sum += roll_value

        print("Sum: {}".format(results.sum))

        average = self.getAvg(num_die)
        print("Average: {}".format(average))
        return self.sum
    
    """ returns the average of the dice throwm
        params:
            num_die: int of how many dice were thrown
    """
    def getAvg(self, num_die):
        return self.sum / num_die

############################################

if __name__ == '__main__':
    game_running = True

    while (game_running): 
        print("Enter number of dice you want to throw: ")
        num_die = input()
        print("Enter the number of sides on the die you want to use (e.g. 3, 4, ... 20)")
        num_sides = input()

        print("We will roll {}d{}.".format(num_die, num_sides))

        results = DiceSimulator()
        results.rollDie(int(num_die), int(num_sides))

        print("Roll again? Y/N")
        answer = input()
        if (answer.lower() == 'n'):
            game_running = False
    print("Bye! Thanks for playing Dice Simulator.")
    
