def linear_search(games, target):
    for game in games:
        if game.judul.lower() == target.lower():
            return game

    return None

def binary_search(games, target):
    low = 0
    high = len(games) - 1

    while low <= high:
        mid = (low + high) // 2

        if games[mid].judul.lower() == target.lower():
            return games[mid]

        elif games[mid].judul.lower() < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return None