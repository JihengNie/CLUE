# Cards setup
characters = {
  "White": { "revealed": False, "owned": None },
  "Peacock": { "revealed": False, "owned": None },
  "Plum": { "revealed": False, "owned": None },
  "Mustard": { "revealed": False, "owned": None },
  "Green": { "revealed": False, "owned": None },
  "Scarlett": { "revealed": False, "owned": None }
}
weapons = {
  "knife": { "revealed": False, "owned": None },
  "revolver": { "revealed": False, "owned": None },
  "rope": { "revealed": False, "owned": None },
  "wrench": { "revealed": False, "owned": None },
  "candlestick": { "revealed": False, "owned": None },
  "lead pipe": { "revealed": False, "owned": None }
}
rooms = {
  "Ball Room": { "revealed": False, "owned": None },
  "Billiard Room": { "revealed": False, "owned": None },
  "Conservatory": { "revealed": False, "owned": None },
  "Dining Room": { "revealed": False, "owned": None },
  "Hall": { "revealed": False, "owned": None },
  "Kitchen": { "revealed": False, "owned": None },
  "Lounge": { "revealed": False, "owned": None },
  "Library": { "revealed": False, "owned": None },
  "Study": { "revealed": False, "owned": None }
}

cards = {
  "characters": characters,
  "weapons": weapons,
  "rooms": rooms
}

# Players set up

playerNum = int(input("Enter number of players: "))
players = set()

for i in range(playerNum):
  playerName = input("Enter player " + str(i + 1) + "'s name: " )
  players.add(playerName)

print('Players:', players)

# Functions
def revealingCards(cardType, cardName, playerName, cards):
  cards[cardType][cardName]["revealed"] = True
  cards[cardType][cardName]["owned"] = playerName
  return displayOwnedCards(playerName, cards)

def displayOwnedCards(playerName, cards):
  cardsOwned = []
  for cardTypes in cards:
    for items in cards[cardTypes]:
      if cards[cardTypes][items]["owned"] == playerName:
        cardsOwned.append(items)
  return cardsOwned

def displayRevealedCardsByType(cardType, cards):
  revealedType = []
  for items in cards[cardType]:
    if cards[cardType][items]["revealed"] == False:
      revealedType.append(items)
  return revealedType

def displayAllPlayerOwnedCards(players, cards):
  playerOwnedCards = {}
  for names in players:
    playerOwnedCards[names] = displayOwnedCards(names, cards)
  return playerOwnedCards

# Playing the game
gameStatus = True
roundCounter = 0

while gameStatus:
  print("\nRound's Passed: " + str(roundCounter))
  action = input("Choose an action: \n  1. Reveal a card \n  2. Displaying remaining cards \n  3. End Game \n")
  remainingCards = {
    "characters": displayRevealedCardsByType('characters', cards),
    "weapons" : displayRevealedCardsByType('weapons', cards),
    "rooms" : displayRevealedCardsByType('rooms', cards)
  }
  if action == "1":
    cardType = input("Choose a card type: characters, weapons, or rooms: ")
    if cardType == 'characters':
      print(remainingCards["characters"])
      cardName = input("Choose a character: ")
    elif cardType == 'weapons':
      print(remainingCards["weapons"])
      cardName = input("Choose a weapon: ")
    elif cardType == 'rooms':
      print(remainingCards["rooms"])
      cardName = input("Choose a room: ")
    else:
      break
    print(players)
    playerName = input("Enter player name: ")
    revealingCards(cardType, cardName, playerName, cards)
    roundCounter += 1
  elif action == "2":
    print("characters", remainingCards["characters"])
    print("weapons", remainingCards["weapons"])
    print("rooms", remainingCards["rooms"])
    roundCounter += 1
  elif action == "3":
    gameStatus = False
  else:
    print("Try again")
  print(displayAllPlayerOwnedCards(players, cards))
