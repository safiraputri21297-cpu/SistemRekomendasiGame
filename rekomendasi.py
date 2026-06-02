from sorting import quick_sort_rating
def rekomendasi_games(games, genre):
  recommended = []

  for game in games:
    if game.genre.lower() == genre.lower():
      recommended.append(game)

  return quick_sort_rating(recommended)
