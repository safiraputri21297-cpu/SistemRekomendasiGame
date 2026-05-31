class Node:
    def __init__(self, game):
        self.game = game
        self.next = None

class Wishlist:
    def __init__(self):
        self.head = None

    def add_game(self, game):
        new_node = Node(game)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        games = []
        temp = self.head

        while temp:
            games.append(temp.game.judul)
            temp = temp.next

        return games