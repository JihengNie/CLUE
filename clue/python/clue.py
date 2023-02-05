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

# playerNum = int(input("Enter number of players: "))
# players = []

# for i in range(playerNum):
#   playerName = input("Enter player " + str(i + 1) + "'s name: " )
#   players.append(playerName)

# Functions
def revealing_cards(cardType, cardName, player):
  cards[cardType][cardName]["revealed"] = True
  cards[cardType][cardName]["owned"] = player

def playerCardsOwned(playerName, cards):
  cardsOwned = []
  for cardTypes in cards:
    for items in cards[cardTypes]:
      if cards[cardTypes][items]["owned"] == playerName:
        cardsOwned.append(items)
  return cardsOwned

print(playerCardsOwned("Jade", cards))
print(playerCardsOwned(None, cards))
