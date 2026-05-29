class Game:
    def __init__(self, judul, genre, rating, harga):
        self.judul = judul
        self.genre = genre
        self.rating = rating
        self.harga = harga

    def display(self):
        harga_text = "Gratis" if self.harga == 0 else f"Rp{self.harga}"
        return f"{self.judul} | {self.genre} | Rating: {self.rating} | {harga_text}"