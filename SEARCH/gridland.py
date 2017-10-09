#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/gridland-metro

def get_empty_places(r, c, tracks):
    '''
    return an integer denoting the number of cells are not occupied
    '''
    cache = {}
    for track in tracks:
        if track[0] in cache:
            for ran in cache[track[0]]:
                if not (track[2] < ran[0] or track[1] > ran[1]):
                    if track[1] < ran[0]:
                        ran[0] = track[1]
                    if track[2] > ran[1]:
                        ran[1] = track[2]
                else:
                    cache[track[0]].append([track[1], track[2]])
        else:
            cache[track[0]] = [[track[1], track[2]]]
    empty_places  = r*c
    for key in cache.keys():
        for ran in cache[key]:
            empty_places -= (ran[1] - ran[0] +1)
    return empty_places


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    tracks = []
    for i in range(k):
        track = map(int, input().split())
        tracks.append(list(track))
    print(get_empty_places(r, c, tracks))


