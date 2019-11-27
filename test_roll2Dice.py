# test_import rollDice01.py

# Import Statements
import unittest
import roll2Dice

class KnownValues(unittest.TestCase):

  def test_rollDiceForSnakeEyes(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(1, 1)
    # Check for expected output
    self.assertEqual('You rolled a 1 and a 1 for a total of 2. Snake eyes, you lose!', result)

  def test_rollDiceForBoxcars(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(6, 6)
    # Check for expected output
    self.assertEqual('You rolled a 6 and a 6 for a total of 12. Boxcars, you lose!', result)

  def test_rollDiceForWin1and6(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(1, 6)
    # Check for expected output
    self.assertEqual('You rolled a 1 and a 6 for a total of 7. You win!', result)

  def test_rollDiceForWin6and1(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(6, 1)
    # Check for expected output
    self.assertEqual('You rolled a 6 and a 1 for a total of 7. You win!', result)

  def test_rollDiceForWin2and5(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(2, 5)
    # Check for expected output
    self.assertEqual('You rolled a 2 and a 5 for a total of 7. You win!', result)

  def test_rollDiceForWin5and2(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(5, 2)
    # Check for expected output
    self.assertEqual('You rolled a 5 and a 2 for a total of 7. You win!', result)

  def test_rollDiceForWin3and4(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(3, 4)
    # Check for expected output
    self.assertEqual('You rolled a 3 and a 4 for a total of 7. You win!', result)

  def test_rollDiceForWin4and3(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(4, 3)
    # Check for expected output
    self.assertEqual('You rolled a 4 and a 3 for a total of 7. You win!', result)

  def test_rollDiceForDraw1and5(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(1, 5)
    # Check for expected output
    self.assertEqual("You rolled a 1 and a 5 for a total of 6. It's a draw!", result)

  def test_rollDiceForDraw4and6(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(4, 6)
    # Check for expected output
    self.assertEqual("You rolled a 4 and a 6 for a total of 10. It's a draw!", result)

  def test_rollDiceForDraw1and2(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(1, 2)
    # Check for expected output
    self.assertEqual("You rolled a 1 and a 2 for a total of 3. It's a draw!", result)

  def test_rollDiceForDraw3and5(self):
    # Capture the results of the function
    result = roll2Dice.checkRoll(1, 5)
    # Check for expected output
    self.assertEqual("You rolled a 3 and a 5 for a total of 8. It's a draw!", result)


# Run the tests
if __name__ == '__main__':
    unittest.main()