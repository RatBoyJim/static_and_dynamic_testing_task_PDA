### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# card.value should be == 1. No colon (:) after else statement

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# def spelled incorrectly and no comma (,) between card1 and card2 parameters. Method not indented correctly from if statement. First return statement should state return card1 instead of just card.


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# total not set to a value of zero and whole method not indented. Return statement is within for loop. total in return statement should be written as str(total) to turn the integer returned into a string.
```
