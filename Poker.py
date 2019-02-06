#  File: Poker.py

#  Description: Assignmeng6

#  Student's Name: Shimin Zhang

#  Student's UT EID: sz6939

#  Partner's Name: Zijie Pang

#  Partner's UT EID: zp2478

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: Sept 25

#  Date Last Modified: Sept 28
import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, n = 1):
    self.deck = []
    for i in range (n):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal all the hands
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append (hand)

  # simulates the play of the game
  def play (self):
    points_hand = []   # create a list to store points for each hand
    type_hand = []  # create a list to store type for each hand

    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      sorted_hand = sorted (self.all_hands[i])
      for card in sorted_hand:
        hand_str = hand_str + str(card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
      if self.is_royal(self.all_hands[i]) > 0:
        points_hand.append (self.is_royal(self.all_hands[i]))
        type_hand.append("Royal Flush")
        continue

      elif self.is_straight_flush(self.all_hands[i]) > 0:
        points_hand.append (self.is_straight_flush(self.all_hands[i]))
        type_hand.append("Straight Flush")
        continue

      elif self.is_four_kind(self.all_hands[i]) > 0:
        points_hand.append (self.is_four_kind(self.all_hands[i]))
        type_hand.append("Four of a Kind")
        continue

      elif self.is_full_house(self.all_hands[i]) > 0:
        points_hand.append (self.is_full_house(self.all_hands[i]))
        type_hand.append("Full House")
        continue

      elif self.is_flush(self.all_hands[i]) > 0:
        points_hand.append (self.is_flush(self.all_hands[i]))
        type_hand.append("Flush")
        continue

      elif self.is_straight(self.all_hands[i]) > 0:
        points_hand.append (self.is_straight(self.all_hands[i]))
        type_hand.append("Straight")
        continue

      elif self.is_three_kind(self.all_hands[i]) > 0:
        points_hand.append (self.is_three_kind(self.all_hands[i]))
        type_hand.append("Three of a Kind")
        continue

      elif self.is_two_pair(self.all_hands[i]) > 0:
        points_hand.append (self.is_two_pair(self.all_hands[i]))
        type_hand.append("Two Pair")
        continue

      elif self.is_one_pair(self.all_hands[i]) > 0:
        points_hand.append (self.is_one_pair(self.all_hands[i]))
        type_hand.append("One Pair")
        continue

      else:
        points_hand.append (self.is_high_card(self.all_hands[i]))
        type_hand.append("High Card")
        continue


    print()
    for i in range(len(self.all_hands)):
      print('Player' + str(i + 1) + ": " + type_hand[i])
    print()

    #rank the type based on the index
    hand_type_list=["Royal Flush","Straight Flush",'Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pair','One Pair','High Card']
    #create a list for rank of type
    type_rank=[]
    for i in type_hand:
      for k in hand_type_list:
        if i==k:
          type_rank.append(hand_type_list.index(k))
    min_num=min(type_rank) #find the highest rank of card in hand

    #count ties
    count=0
    ties_points=[]
    print_list=[]
    for i in type_rank:
      count=count+1
      if i == min_num:
        ties_points.append(points_hand[count-1])
        print_list.append('Player '+str(count)+' ties.')

    #print ties
    if len(print_list)>1:
        for i in print_list:
          print(i)
    # determine winner and print
    print ('Player ' + str(points_hand.index(max(ties_points)) + 1) +' is the winner!')


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

    return points


  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)-1):
      rank_order = rank_order and (hand[i].rank == hand[i+1].rank-1)

    if (not rank_order):
      return 0

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

    return points


  def is_four_kind (self, hand):

    if hand[0].rank==hand[1].rank==hand[2].rank==hand[3].rank or hand[1].rank==hand[2].rank==hand[3].rank==hand[4].rank:
        rank_order=True
    else:
        rank_order=False

    if not rank_order:
        return 0

    if hand[0].rank==hand[1].rank==hand[2].rank==hand[3].rank:
      points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[1].rank==hand[2].rank==hand[3].rank==hand[4].rank:
      points = 8 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[0].rank)

    return points

  def is_full_house (self, hand):

    if hand[0].rank==hand[1].rank==hand[2].rank and hand[3].rank==hand[4].rank:
        full_house=True
    elif hand[2].rank==hand[3].rank==hand[4].rank and hand[0].rank==hand[1].rank:
        full_house=True
    else:
        full_house=False
    if not full_house:
        return 0
    if hand[0].rank==hand[1].rank==hand[2].rank and hand[3].rank==hand[4].rank:
      points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[2].rank==hand[3].rank==hand[4].rank and hand[0].rank==hand[1].rank:
       points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1 + (hand[1].rank)


    return points


  def is_flush (self, hand):
    same_suit=True
    for i in range(len(hand)-1):
      same_suit=same_suit and (hand[i].suit==hand[i+1].suit)
    if (not same_suit):
      return 0

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

    return points


  def is_straight (self, hand):
    for i in range (0, len(hand)-1):
      if (hand[i].rank != (hand[i+1].rank + 1)):
        return 0

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

    return points


  def is_three_kind (self, hand):

    if hand[0].rank==hand[1].rank==hand[2].rank:
        full_house=True
    elif hand[2].rank==hand[3].rank==hand[4].rank:
        full_house=True
    elif hand[1].rank==hand[2].rank==hand[3].rank:
        full_house=True
    else:
        full_house=False
    if not full_house:
        return 0
    if hand[0].rank==hand[1].rank==hand[2].rank:
      points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[2].rank==hand[3].rank==hand[4].rank:
      points = 4 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[1].rank)
    elif hand[1].rank==hand[2].rank==hand[3].rank:
      points = 4 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[4].rank)

    return points

  def is_two_pair (self, hand):

    if hand[0].rank==hand[1].rank and hand[2].rank==hand[3].rank:
        full_house=True
    elif hand[0].rank==hand[1].rank and hand[3].rank==hand[4].rank:
        full_house=True
    elif hand[1].rank==hand[2].rank and hand[3].rank==hand[4].rank:
        full_house=True
    else:
        full_house=False
    if not full_house:
        return 0
    if hand[0].rank==hand[1].rank and hand[2].rank==hand[3].rank:
      points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[0].rank==hand[1].rank and hand[3].rank==hand[4].rank:
      points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[2].rank)
    elif hand[1].rank==hand[2].rank and hand[3].rank==hand[4].rank:
      points = 3 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[0].rank)

    return points

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        break
    if (not one_pair):
      return 0

    if hand[0]==hand[1]:
      points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[1]==hand[2]:
      points = 2 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[0].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[2]==hand[3]:
      points = 2 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1 + (hand[4].rank)
    elif hand[3]==hand[4]:
      points = 2 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[4].rank) * 15 ** 3 + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1 + (hand[2].rank)

    return points


  def is_high_card (self, hand):

    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)

    return points

def main():
  # prompt the user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  print('')
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))
    print('')

  # create the Poker object
  game = Poker (num_players)

  # play the game - poker
  game.play()

# do not remove this line above main()
if __name__ == '__main__':
  main()



