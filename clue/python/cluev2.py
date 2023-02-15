# Data setup
characters = {
  "White": {"owned": None },
  "Peacock": {"owned": None },
  "Plum": {"owned": None },
  "Mustard": {"owned": None },
  "Green": {"owned": None },
  "Scarlett": {"owned": None }
}
weapons = {
  "Dagger": {"owned": None },
  "Revolver": {"owned": None },
  "Rope": {"owned": None },
  "Wrench": {"owned": None },
  "Candlestick": {"owned": None },
  "Lead Pipe": {"owned": None }
}
rooms = {
  "Ball Room": {"owned": None },
  "Billiard Room": {"owned": None },
  "Conservatory": {"owned": None },
  "Dining Room": {"owned": None },
  "Hall": {"owned": None },
  "Kitchen": {"owned": None },
  "Lounge": {"owned": None },
  "Library": {"owned": None },
  "Study": {"owned": None }
}

cards = {
  "characters": characters,
  "weapons": weapons,
  "rooms": rooms
}

players = {
  "player0": {"potentialCards":[], "notOwned": [] },
  "player1": {"potentialCards":[], "notOwned": [] },
  "player2": {"potentialCards":[], "notOwned": [] }
}

rounds = [
  {"whoAnswered":"PlayerName", "cards": ["Dagger", "Library", "Study"]}
]

# Selection objects

def creatingSelectionObjects(dictionary):
  selectionNames = dictionary.keys()
  counter = 1
  outputObject = {}
  for names in selectionNames:
    outputObject[counter] = names
    counter += 1
  return outputObject

selectionObject = {
  "players": creatingSelectionObjects(players),
  "characters": creatingSelectionObjects(cards["characters"]),
  "weapons": creatingSelectionObjects(cards["weapons"]),
  "rooms": creatingSelectionObjects(cards["rooms"])
}


# Functions

def convertStrToInt(list):
  outputList = []
  for items in list:
    outputList.append(int(items))
  return outputList

def initializationPlayers(players):
  numOfPlayers = int(input("Enter number of players: "))
  for i in range(numOfPlayers):
    playerName = input("Enter player " + str(i + i) + "'s name: ")
    players[playerName] = {"potentialCards": []}
  print("Players:", players)
  return players

def enterPlayerHand(players, cards, selectionObject):
  selectedCardsList = []

  print("Players:", selectionObject["players"])
  selectedPlayer = int(input("Enter the number for the player: "))

  print("Character Cards:", selectionObject["characters"])
  selectedCharacters = input("Enter the number assoicated with the character cards seprated by commas: ").replace(" ", "")
  if selectedCharacters != "":
    charactersList = convertStrToInt(selectedCharacters.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["characters"][items])
      del selectionObject["characters"][items]

  print("Weapons Cards:", selectionObject["weapons"])
  selectedWeapons = input("Enter the number assoicated with the weapons cards seprated by commas: ")
  if selectedWeapons != "":
    weaponsList = convertStrToInt(selectedWeapons.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["weapons"][items])
      del selectionObject["weapons"][items]

  print("Room Cards:", selectionObject["rooms"])
  selectedRooms = input("Enter the number assoicated with the rooms cards seprated by commas: ")
  if selectedRooms != "":
    roomsList = convertStrToInt(selectedRooms.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["rooms"][items])
      del selectionObject["rooms"][items]

  print("\nSelected cards:", selectedCardsList)
  for cardTypes in cards:
    for card in cards[cardTypes]:
        if card in selectedCardsList:
          cards[cardTypes][card]["owned"] = selectionObject["players"][selectedPlayer]
  return cards

def viewPlayerOwnedCards(players, cards):
  playerHand = {}
  for player in players.keys():
    currentHand = []
    for cardTypes in cards:
      for card in cards[cardTypes]:
        if cards[cardTypes][card]["owned"] == player:
          currentHand.append(card)
    playerHand[player] = currentHand
  print("PlayerHand:", playerHand)
  return playerHand

def enterRoundGuess(selectionObject, players, rounds):
  ### --------------------Problem: People can guess cards that is already known. Solution: Give user an option to select a None card-----------------------------------###
  print("Please enter the guess.\n")
  # Card Selection
  print(selectionObject["characters"])
  selectedCharacter = int(input("Enter the number for the character: "))

  print(selectionObject["weapons"])
  selectedWeapon = int(input("Enter the number for the weapon: "))

  print(selectionObject["rooms"])
  selectedRoom = int(input("Enter the number for the room: "))
  cardSelected = [
    selectionObject["characters"][selectedCharacter],
    selectionObject["weapons"][selectedWeapon],
    selectionObject["rooms"][selectedRoom],
  ]
  # Round guess
  roundGuess = {
    "whoAnswered": None,
    "cards": cardSelected
  }

  stillGuessing = True
  while stillGuessing:
    guessCheck = input("Are you still guessing? y/n: ")
    if guessCheck == "y":
      # Player selection
      print(selectionObject["players"])
      selectedPlayerNum = int(input("Enter the number for the player: "))
      selecterPlayer = selectionObject["players"][selectedPlayerNum]

      shownCard = input("Did the player show a card? y/n: ")
      if shownCard == "y":
        roundGuess["whoAnswered"] = selecterPlayer
        for card in cardSelected:
          if card not in players[selecterPlayer]["potentialCards"]:
            players[selecterPlayer]["potentialCards"].append(card)
      else:
        for card in cardSelected:
          if card not in players[selecterPlayer]["notOwned"]:
            players[selecterPlayer]["notOwned"].append(card)
    else:
      stillGuessing = False
  rounds.append(roundGuess)
  return players

def displayingRemainingCards(selectionObject):
  print("Characters:", selectionObject["characters"])
  print("Weapons:", selectionObject["weapons"])
  print("Rooms:", selectionObject["rooms"])

# "player0": {"potentialCards":["Dagger", "Ball Room"], "notOwned": ["Study", "Lounge"] },

# Test space
# enterPlayerHand(players, cards, selectionObject)
# print(selectionObject)
# print(viewPlayerOwnedCards(players, cards))
# print(enterRoundGuess(selectionObject, players, rounds))

# Playing the game

gameStatus = True

while gameStatus:
  inputMenu = """\nChoose an action:
  1. Enter player hand
  2. Enter a card player owns
  3. Displaying player cards
  4. Enter guesses
  5. Display remaining cards
  0. End Game
    """
  action = input(inputMenu)
  if action == "0":
    gameStatus = False
  elif action == "1":
    enterPlayerHand(players, cards, selectionObject)
  elif action == "2":
    enterPlayerHand(players, cards, selectionObject)
  elif action == "3":
    viewPlayerOwnedCards(players, cards)
  elif action == "4":
    enterRoundGuess(selectionObject, players, rounds)
  elif action =="5":
    displayingRemainingCards(selectionObject)
  else:
    print("Try again")
