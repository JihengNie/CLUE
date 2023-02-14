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
  "player0": {"potentialCards":["Dagger", "Ball Room"], "notOwned": ["Study", "Lounge"] }
}

rounds = [
  {"whoAnswered":"PlayerName", "cards": ["Dagger", "Library", "Study"]}
]

# Functions
def initializationPlayers(players):
  numOfPlayers = int(input("Enter number of players: "))
  for i in range(numOfPlayers):
    playerName = input("Enter player " + str(i + i) + "'s name: ")
    players[playerName] = {"potentialCards": []}
  print("Players:", players)
  return players

initializationPlayers(players)
