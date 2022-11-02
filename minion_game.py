vowels = ["a", "i", "u", "e", "o"]


# def compute_scores(in_text, match_text):
#     scores = 0
#     step = len(match_text)
#     for i in range(0, len(in_text)):
#         if i + step > len(in_text):
#             break
#         if in_text[i:i + step] == match_text:
#             scores += 1
#     return scores


def get_scores(string):
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    return kevin_score, stuart_score


def minion_game(string):
    if 0 < len(s) <= pow(10, 6):
        string = string.lower()
        kevin_scores, stuart_scores = get_scores(string)

        if stuart_scores == kevin_scores:
            print("Draw")
        elif stuart_scores > kevin_scores:
            print(f"Stuart {stuart_scores}")
        else:
            print(f"Kevin {kevin_scores}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
# for step in range(1, len(string)):
#     for i in range(0, len(string)):
#         if i + step > len(string):
#             break
#         words = string[i:i + step]
