def linear_search(games, target):
    for game in games:
        if game.judul.lower() == target.lower():
            return game

    return None