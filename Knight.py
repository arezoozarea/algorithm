# def is_valid(a, b, n):
#     return (0 <= a <= n) and (0 <= b <= n)
#
#
# def next_move(xy, hv, n):
#     h, v = hv
#     x, y = xy
#     states = [(x + v, y + h), (x - v, y - h), (x + v, y - h), (x - v, y + h), (x + h, y + v), (x - h, y - v),
#               (x + h, y - v), (x - h, y + v)]
#     return list(filter(lambda a: is_valid(a[0], a[1], n), states))
#
#
# # todo add n also to this and all sub-function
# def get_score(v, h, n):
#     x = 0
#     y = 0
#     score = None
#     move_num = 0
#     state_num = [{(x, y): 0}]
#
#     while True:
#         if move_num > n * 2:
#             state_num = state_num[0: move_num]
#             move_num -= 1
#             x, y = [key for key in state_num[move_num]][0]
#             state_num[move_num][(x, y)] += 1
#             continue
#
#         cell = next_move((x, y), (v, h), n)
#         index = state_num[move_num][(x, y)]
#
#         if index > len(cell) - 1:
#             if move_num == 0:
#                 if not score:
#                     return -1
#                 return score + 1
#
#             state_num = state_num[0: move_num]
#             move_num -= 1
#             x, y = [key for key in state_num[move_num]][0]
#             state_num[move_num][(x, y)] += 1
#             continue
#
#         x, y = cell[index]
#
#         if score and move_num >= score:
#             state_num = state_num[0: move_num]
#             move_num -= 1
#             x, y = [key for key in state_num[move_num]][0]
#             state_num[move_num][(x, y)] += 1
#             continue
#
#         if x == n and y == n:
#             if not score or score > move_num:
#                 score = move_num
#
#             state_num = state_num[0: move_num]
#             move_num -= 1
#
#             if move_num == -1:
#                 return score + 1
#
#             x, y = [key for key in state_num[move_num]][0]
#             state_num[move_num][(x, y)] += 1
#         else:
#             move_num += 1
#             if move_num not in state_num:
#                 state_num.append({(x, y): 0})
#

def knightlOnAChessboard(n):
    def is_in_range(a, b, n):
        return (0 <= a <= n) and (0 <= b <= n)

    def next_move(xy, hv, n):
        h, v = hv
        x, y = xy
        states = [(x + v, y + h), (x - v, y - h), (x + v, y - h), (x - v, y + h), (x + h, y + v), (x - h, y - v),
                  (x + h, y - v), (x - h, y + v)]
        return list(filter(lambda a: is_in_range(a[0], a[1], n), states))

    # todo add n also to this and all sub-function
    def get_match(v, h, n):
        x = 0
        y = 0
        score = None
        move_num = 0
        state_num = [{(x, y): 0}]

        while True:
            if move_num > n * 2:
                state_num = state_num[0: move_num]
                move_num -= 1
                x, y = [key for key in state_num[move_num]][0]
                state_num[move_num][(x, y)] += 1
                continue

            cell = next_move((x, y), (v, h), n)
            index = state_num[move_num][(x, y)]

            if index > len(cell) - 1:
                if move_num == 0:
                    if not score:
                        return -1
                    return score + 1

                state_num = state_num[0: move_num]
                move_num -= 1
                x, y = [key for key in state_num[move_num]][0]
                state_num[move_num][(x, y)] += 1
                continue

            x, y = cell[index]

            if score and move_num >= score:
                state_num = state_num[0: move_num]
                move_num -= 1
                x, y = [key for key in state_num[move_num]][0]
                state_num[move_num][(x, y)] += 1
                continue

            if x == n and y == n:
                if not score or score > move_num:
                    score = move_num

                state_num = state_num[0: move_num]
                move_num -= 1

                if move_num == -1:
                    return score + 1

                x, y = [key for key in state_num[move_num]][0]
                state_num[move_num][(x, y)] += 1
            else:
                move_num += 1
                if move_num not in state_num:
                    state_num.append({(x, y): 0})

    score_list = {}

    for v in range(1, n):
        for h in range(1, n):
            keys = [key for key in score_list]
            if (h, v) in keys:
                score_list[(v, h)] = score_list[(h, v)]
            else:
                score_list[(v, h)] = get_match(v, h, n - 1)

    rows = []
    scores = [score_list[key] for key in score_list]

    for i in range(0, len(scores), n - 1):
        rows.append(scores[i:i + n - 1])

    return rows


if __name__ == '__main__':
    a = knightlOnAChessboard(int(input().strip()))
    print('\n'.join([' '.join(map(str, x)) for x in a]))
