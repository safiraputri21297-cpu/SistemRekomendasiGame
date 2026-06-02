class BSTNode:
    def __init__(self, game):
        self.game = game
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, game):
        if self.root is None:
            self.root = BSTNode(game)
        else:
            self._insert(self.root, game)

    def _insert(self, node, game):
        if game.judul.lower() < node.game.judul.lower():
            if node.left is None:
                node.left = BSTNode(game)
            else:
                self._insert(node.left, game)

        else:
            if node.right is None:
                node.right = BSTNode(game)
            else:
                self._insert(node.right, game)

    def search(self, title):
        return self._search(self.root, title)

    def _search(self, node, title):
        if node is None:
            return None

        if node.game.judul.lower() == title.lower():
            return node.game

        if title.lower() < node.game.judul.lower():
            return self._search(node.left, title)

        return self._search(node.right, title)