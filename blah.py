from random import randint
solution = randint(1,10)
guess = None
number_of_guesses_so_far = 0
print "Guess the Number Game"
while solution != guess:
  guess = None
  print "What is your (integer) guess between 1 and 10 in arabic numerals?"
  guess = raw_input ()
  try:
    guess = int (guess)
  except ValueError:
    print "OMG, your, like, stupid cuz, like, you didn't follow, like, the instructions. #loser"
    continue
  if solution > guess:
    print "Your guess is too small."
  if solution < guess:
    print "Your guess is too big."
  number_of_guesses_so_far = number_of_guesses_so_far + 1
  if solution == guess:
    print "YAY! YOU WIN! Play again? [Y/N]"
  elif number_of_guesses_so_far == 5:
    print "you lose the game. Try again? [Y/N]"
  if solution == guess or number_of_guesses_so_far == 5:
    cont = raw_input ()
    if cont == "Y":
      number_of_guesses_so_far = 0
      guess = None
      continue
    elif cont == "N":
      break
    else:
      print "By not following instructions, you lose the right to play the game."
      break
    
print "bye!"