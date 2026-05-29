def quick_sort_rating(games):
    if len(games) <= 1:
        return games

    pivot = games[0]

    left = [x for x in games[1:] if x.rating <= pivot.rating]
    right = [x for x in games[1:] if x.rating > pivot.rating]

    return quick_sort_rating(right) + [pivot] + quick_sort_rating(left)

def merge_sort_price(games):
    if len(games) <= 1:
        return games

    mid = len(games) // 2
    left = merge_sort_price(games[:mid])
    right = merge_sort_price(games[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].price < right[j].price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def selection_sort_title(games):
    n = len(games)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if games[j].judul < games[min_index].judul:
                min_index = j

        games[i], games[min_index] = games[min_index], games[i]

    return games