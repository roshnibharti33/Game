import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self, noOfDecks):
        self.orderedCardList = []
        suit_list = ['Spade', 'Heart', 'Diamond', 'Club']
        for deck_count in range(noOfDecks):
            for suit in suit_list:
                for val in range(1,14):
                    card = Card(suit, val)
                    self.orderedCardList.append(card)

    def shuffleCards(self):
        self.shuffleCardList = []
        while len(self.orderedCardList) > 0:
            index = random.randint(-1,len(self.orderedCardList)-1)
            self.shuffleCardList.append( self.orderedCardList.pop(index))

    def getCard(self):
        return self.shuffleCardList.pop(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.card_list = []

    def addCard(self, card):
        self.card_list.append(card)

    def calculateScore(self):
        aceCount = 0
        score = 0
        for cardIndex in range(len(self.card_list)):
            card = self.card_list[cardIndex]
            if card.value == 1:
                aceCount += 1
            else:
                score += min(card.value, 10)

        if (aceCount > 0):
            if score+11+(aceCount-1) <= 21:
                score += 11+(aceCount-1)
            else:
                score += aceCount
        return score


class Game:
    def __init__(self):
        self.player_list = []

    def startGame(self):
        #print("Enter The number of Players")
        noOfPlayers = int(input("Enter The number of Players"))
        for num in range(noOfPlayers):
            name = input("Enter Player Name")
            self.player_list.append(Player(name))
        noOfDecks = int(input("Enter Number of Decks"))
        deck = Deck(noOfDecks)
        print("Starting the game...")
        deck.shuffleCards()
        for player_index in range(noOfPlayers):
            curr_player = self.player_list[player_index]
            curr_player.addCard(deck.getCard())
            curr_player.addCard(deck.getCard())

            while curr_player.calculateScore() < 21:
                cards = [str(s.suit)+str(s.value) for s in curr_player.card_list]
                print(curr_player.name+" has "+ str(curr_player.calculateScore()) + " Cards: " + ", ".join(cards))
                x = input("Wants to continue 1/Yes or 0/No")
                if int(x) == 1:
                    curr_player.addCard(deck.getCard())
                else:
                    break
            print(curr_player.name + " has " + str(curr_player.calculateScore()))

        winner_player = []
        winner_score = 0
        for curr_player in self.player_list:
            score = curr_player.calculateScore()
            if score <= 21:
                if score == winner_score:
                    winner_player.append(curr_player.name)
                elif score > winner_score:
                    winner_player = []
                    winner_player.append(curr_player.name)
                    winner_score = score
            print(curr_player.name + " has " + str(curr_player.calculateScore()))
        if winner_score == 0:
            print("Every body Wins!")
            return

        print("Winner Score is "+ str(winner_score)+ " Winner Players: " +", ".join(winner_player))


game = Game()
game.startGame()

