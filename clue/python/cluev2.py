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
  "player0": {"potentialCards":["Dagger", "Ball Room"], "notOwned": ["Study", "Lounge"] },
  "player1": {"potentialCards":["Dagger", "Ball Room"], "notOwned": ["Study", "Lounge"] },
  "player2": {"potentialCards":["Dagger", "Ball Room"], "notOwned": ["Study", "Lounge"] }
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

  print(selectionObject["players"])
  selectedPlayer = int(input("Enter the number for the player: "))

  print(selectionObject["characters"])
  selectedCharacters = input("Enter the number assoicated with the character cards you own seprated by commas: ").replace(" ", "")
  if selectedCharacters != "":
    charactersList = convertStrToInt(selectedCharacters.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["characters"][items])
      del selectionObject["characters"][items]

  print(selectionObject["weapons"])
  selectedWeapons = input("Enter the number assoicated with the weapons cards you own seprated by commas: ")
  if selectedWeapons != "":
    weaponsList = convertStrToInt(selectedWeapons.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["weapons"][items])
      del selectionObject["weapons"][items]

  print(selectionObject["rooms"])
  selectedRooms = input("Enter the number assoicated with the rooms cards you own seprated by commas: ")
  if selectedRooms != "":
    roomsList = convertStrToInt(selectedRooms.split(","))
    for items in charactersList:
      selectedCardsList.append(selectionObject["rooms"][items])
      del selectionObject["rooms"][items]

  print(selectedCardsList)
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
  return playerHand

# Test space
enterPlayerHand(players, cards, selectionObject)
# print(selectionObject)
print(viewPlayerOwnedCards(players, cards))
