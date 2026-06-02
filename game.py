class Game:
    def __init__(self, judul, genre, rating, harga):
        self.judul = judul
        self.genre = genre
        self.rating = rating
        self.harga = harga
        self.downloaded = False

    def display(self):
        harga_text = "Gratis" if self.harga == 0 else f"Rp{self.harga}"
        status_text = "Mainkan" if getattr(self, 'downloaded', False) else "Download"
        return f"{self.judul} | {self.genre} | Rating: {self.rating} | {harga_text} | {status_text}"

    def download(self):
        self.downloaded = True

    def is_downloaded(self):
        return getattr(self, 'downloaded', False)