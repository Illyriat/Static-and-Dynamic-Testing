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

# Missing Semi Colon (:) online 23 after the else, and line 21 should be a == instead of a single =
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# Missseplling of def on line 27, as missing comma on line 27 between card1 and card2. The if statement is outside of the def meaning it won't recognise the card1 and card2, and in addition card on line 29 should be changed to card1.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total on line 36 is missing an assigned value.
# indentation of the return on line 40 should be on the same level as the for, so it returns once the for loop has finished.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```