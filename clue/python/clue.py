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
  "dagger": { "revealed": False, "owned": None },
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
# def notOwnedCards(playerName, cards):


def enteringPlayerCard(playerName, cards):
  numOfCards = int(input("Enter number of cards you have: "))
  playerHand = []
  for i in range(numOfCards):
    tempCard = input("Enter card " + str(i + 1) + ": ")
    playerHand.append(tempCard)
  for cardTypes in cards:
    for items in cards[cardTypes]:
      if items in playerHand:
        cards[cardTypes][items]["revealed"] = True
        cards[cardTypes][items]["owned"] = playerName
        playerHand.remove(items)
  if len(playerHand) > 0:
    return playerHand
  else:
    return "All cards entered successfully"

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

def storingRoundGuesses(cards, roundGuesses):
  print("Players:", players)
  whoGuess = input("Enter who guessed: ")

  print(cards["rooms"].keys())
  roomGuess = input("Enter room: ")

  print(cards["characters"].keys())
  characterGuess = input("Enter character: ")

  print(cards["weapons"].keys())
  weaponGuess = input("Enter weapon: ")

  print("Players:", players)
  whoAnswered = input("Enter who answered: ")

  roundInformation =  {
    "whoGuessed":whoGuess,
    "whoAnsered": whoAnswered,
    "room": None,
    "character": None,
    "weapon": None
  }
  if not cards["rooms"][roomGuess]["owned"]:
    try:
      roundInformation[roundNumber]["room"] = roomGuess
    except:
      print("Room not found or room already revealed")
  if not cards["characters"][characterGuess]["owned"]:
    try:
      roundInformation[roundNumber]["character"] = characterGuess
    except:
      print("Character not found or character already revealed")

  if not cards["weapons"][weaponGuess]["owned"]:
    try:
      roundInformation[roundNumber]["weapon"] = weaponGuess
    except:
      print("Weapon not found or weapon already revealed")
  return roundInformation

# Playing the game
gameStatus = True
roundCounter = 0
roundGuesses = []

while gameStatus:
  print("\nRound's Passed: " + str(roundCounter))
  inputMenu = """Choose an action:
  1. Reveal a card
  2. Enter player hand
  3. Displaying remaining cards
  4. Enter a guess
  0. End Game
    """
  action = input(inputMenu)
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
      continue
    print("Players:", players)
    playerName = input("Enter player name: ")
    revealingCards(cardType, cardName, playerName, cards)
    roundCounter += 1
  elif action == "2":
    print("Players:", players)
    playerName = input("Enter player name: ")
    print(enteringPlayerCard(playerName, cards))
  elif action == "3":
    print("characters", remainingCards["characters"])
    print("weapons", remainingCards["weapons"])
    print("rooms", remainingCards["rooms"])
    roundCounter += 1
  elif action == "4":
    roundGuesses.append(storingRoundGuesses(cards, roundGuesses))
    print(roundGuesses)
  elif action == "0":
    gameStatus = False
  else:
    print("Try again")
  print("Player's current cards: ",displayAllPlayerOwnedCards(players, cards))
