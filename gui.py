import tkinter as tk
from tkinter import ttk
from game import Game
from searching import linear_search
from rekomendasi import rekomendasi_games
from linked_list import Wishlist
from stack_queue import Stack, Queue
from sorting import quick_sort_rating


class GameMatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Match")

        self.games = self.create_game_list()
        self.wishlist = Wishlist()
        self.download_queue = Queue()
        self.recent_stack = Stack()

        self.build_ui()
        self.display_sorted_games()

    def create_game_list(self):
        return [
            Game("DOTA 2", "MOBA", 9.2, 0),
            Game("Among Us", "Party", 8.1, 20000),
            Game("Minecraft", "Sandbox", 9.0, 50000),
            Game("Valorant", "FPS", 8.5, 0),
            Game("Stardew Valley", "Simulation", 9.4, 45000),
            Game("Genshin Impact", "Action RPG", 8.7, 0),
            Game("The Witcher 3", "RPG", 9.8, 30000),
            Game("Cyberpunk 2077", "Action RPG", 7.5, 15000),
            Game("Hades", "Rogue-like", 9.3, 10000),
            Game("Animal Crossing: New Horizons", "Simulation", 9.0, 40000),
            Game("Call of Duty: Warzone", "FPS", 8.0, 0),
            Game("League of Legends", "MOBA", 8.8, 0),
            Game("GTA V", "Action", 9.5, 200000),
            Game("Apex Legends", "FPS", 8.3, 0),
            Game("Terraria", "Sandbox", 8.9, 90000),
            Game("Overwatch", "FPS", 8.4, 0),
            Game("Dark Souls III", "Rogue-like", 9.1, 25000),
            Game("The Legend of Zelda: Breath of the Wild", "Action RPG", 9.2, 30000),
            Game("Mobile Legends", "MOBA", 8.0, 0),
            Game("Vainglory", "MOBA", 7.8, 0),
            Game("Resident Evil 4 Remake", "Action", 9.6, 35000),
            Game("City Skylines", "Simulation", 8.7, 15000),
            Game("world of warcraft", "RPG", 9.0, 0),
        ]

    def build_ui(self):
        self.root.configure(bg="#e6f2ff")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Blue.TCombobox", fieldbackground="#d9ecff", background="#d9ecff", foreground="#000000")

        control_frame = tk.Frame(self.root, bg="#d9ecff", bd=2, relief=tk.RIDGE)
        control_frame.pack(padx=10, pady=10, fill=tk.X)

        label_bg = "#d9ecff"
        entry_bg = "#ffffff"
        button_bg = "#99ccff"
        active_bg = "#80b3ff"

        tk.Label(control_frame, text="Judul Game:", bg=label_bg).grid(row=0, column=0, sticky=tk.W)
        self.title_entry = tk.Entry(control_frame, width=30, bg=entry_bg)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(control_frame, text="Genre:", bg=label_bg).grid(row=1, column=0, sticky=tk.W)
        self.genre_entry = tk.Entry(control_frame, width=30, bg=entry_bg)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(control_frame, text="Rating:", bg=label_bg).grid(row=2, column=0, sticky=tk.W)
        self.rating_entry = tk.Entry(control_frame, width=30, bg=entry_bg)
        self.rating_entry.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(control_frame, text="Harga:", bg=label_bg).grid(row=3, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(control_frame, width=30, bg=entry_bg)
        self.price_entry.grid(row=3, column=1, padx=5, pady=2)

        button_frame = tk.Frame(self.root, bg="#e6f2ff")
        button_frame.pack(padx=10, pady=5)

        tk.Button(button_frame, text="Cari Game", width=14, bg=button_bg, activebackground=active_bg, command=self.search_game).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="Rekomendasi", width=14, bg=button_bg, activebackground=active_bg, command=self.recommend).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(button_frame, text="Wishlist", width=14, bg=button_bg, activebackground=active_bg, command=self.add_wishlist).grid(row=0, column=2, padx=4, pady=4)
        tk.Button(button_frame, text="Download Game", width=14, bg=button_bg, activebackground=active_bg, command=self.add_queue).grid(row=0, column=3, padx=4, pady=4)
        tk.Button(button_frame, text="Mainkan Game", width=14, bg=button_bg, activebackground=active_bg, command=self.play_game).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="Tampil Tersortir", width=14, bg=button_bg, activebackground=active_bg, command=self.display_sorted_games).grid(row=1, column=1, padx=4, pady=4)
        tk.Button(button_frame, text="Keluar", width=14, bg="#b3d9ff", activebackground=active_bg, command=self.root.quit).grid(row=1, column=2, padx=4, pady=4)
        tk.Button(button_frame, text="Tambah Game", width=14, bg=button_bg, activebackground=active_bg, command=self.add_game).grid(row=2, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="Update Game", width=14, bg=button_bg, activebackground=active_bg, command=self.update_game).grid(row=2, column=1, padx=4, pady=4)
        tk.Button(button_frame, text="Hapus Game", width=14, bg=button_bg, activebackground=active_bg, command=self.delete_game).grid(row=2, column=2, padx=4, pady=4)

        self.output = tk.Text(self.root, width=80, height=20, bg="#ffffff", fg="#003366")
        self.output.pack(padx=10, pady=10)

    def _clear_output(self):
        self.output.delete(1.0, tk.END)

    def _show_text(self, text):
        self._clear_output()
        self.output.insert(tk.END, text)

    def _display_list(self, title, lines):
        self._clear_output()
        self.output.insert(tk.END, title)
        for line in lines:
            self.output.insert(tk.END, line + "\n")

    def _selected_game(self):
        title = self.title_entry.get().strip()
        return linear_search(self.games, title) if title else None

    def display_sorted_games(self):
        sorted_games = quick_sort_rating(self.games)
        title = "=== GAME TERSORTIR DARI RATING TERTINGGI ===\n\n"

        self._display_list(title, [game.display() for game in sorted_games])

    def search_game(self):
        game = self._selected_game()

        if game:
            self._display_list("=== GAME DITEMUKAN ===\n\n", [game.display()])
        else:
            self._show_text("Game tidak ditemukan!")

    def recommend(self):
        genre = self.genre_entry.get()
        recommended = rekomendasi_games(self.games, genre)

        self._display_list(f"=== REKOMENDASI GENRE {genre} ===\n\n", [game.display() for game in recommended])

    def add_wishlist(self):
        game = self._selected_game()

        if game:
            self.wishlist.add_game(game)
            self._display_list("=== WISHLIST ===\n\n", self.wishlist.display())

    def add_queue(self):
        game = self._selected_game()

        if game:
            self.download_queue.enqueue(game.judul)
            self._display_list("=== DOWNLOAD QUEUE ===\n\n", self.download_queue.display())

    def add_game(self):
        judul = self.title_entry.get().strip()
        genre = self.genre_entry.get().strip()
        rating_text = self.rating_entry.get().strip()
        price_text = self.price_entry.get().strip()

        if not judul or not genre or not rating_text or not price_text:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Isi semua kolom Judul, Genre, Rating, dan Harga untuk menambahkan game.")
            return

        try:
            rating = float(rating_text)
            price = int(price_text)
        except ValueError:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Rating harus angka dan Harga harus bilangan bulat.")
            return

        self.games.append(Game(judul, genre, rating, price))
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"Game '{judul}' berhasil ditambahkan.\n\n")
        self.display_sorted_games()

    def update_game(self):
        judul = self.title_entry.get().strip()
        if not judul:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Masukkan Judul Game yang akan diperbarui.")
            return

        game = linear_search(self.games, judul)
        if not game:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Game tidak ditemukan untuk diperbarui.")
            return

        genre = self.genre_entry.get().strip()
        rating_text = self.rating_entry.get().strip()
        price_text = self.price_entry.get().strip()

        if genre:
            game.genre = genre
        if rating_text:
            try:
                game.rating = float(rating_text)
            except ValueError:
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, "Rating harus angka.")
                return
        if price_text:
            try:
                game.price = int(price_text)
            except ValueError:
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, "Harga harus bilangan bulat.")
                return

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"Game '{judul}' berhasil diperbarui.\n\n")
        self.output.insert(tk.END, game.display())

    def delete_game(self):
        judul = self.title_entry.get().strip()

        if not judul:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Masukkan Judul Game yang akan dihapus.")
            return

        for index, game in enumerate(self.games):
            if game.judul.lower() == judul.lower():
                del self.games[index]
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, f"Game '{judul}' berhasil dihapus.\n\n")
                self.display_sorted_games()
                return

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Game tidak ditemukan untuk dihapus.")

    def play_game(self):
        judul = self.title_entry.get().strip()

        game = linear_search(self.games, judul)

        if game:
            self.recent_stack.push(game.judul)

            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "=== GAME DIMAINKAN ===\n\n")
            self.output.insert(tk.END, game.display() + "\n\n")
            self.output.insert(tk.END, "=== RECENT PLAYED ===\n\n")

            for item in reversed(self.recent_stack.display()):
                self.output.insert(tk.END, item + "\n")
        else:
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Game tidak ditemukan!")
