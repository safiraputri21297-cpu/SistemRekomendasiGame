def quick_sort_rating(games):
    if len(games) <= 1:
        return games

    pivot = games[0]

    left = [x for x in games[1:] if x.rating <= pivot.rating]
    right = [x for x in games[1:] if x.rating > pivot.rating]

    return quick_sort_rating(right) + [pivot] + quick_sort_rating(left)