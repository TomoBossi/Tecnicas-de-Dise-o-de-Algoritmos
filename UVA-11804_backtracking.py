import sys

# Quisiera prefasear la entrega comentando que me gusta hacer comentarios en inglés

# test_input = """
# sameezahur 20 21
# sohelh 18 9
# jaan 17 86
# sidky 16 36
# shamim 16 18
# shadowcoder 12 9
# muntasir 13 4
# brokenarrow 16 16
# emotionalblind 16 12
# tanaeem 20 97
# """
# for name, at, df in [line.split(" ") for line in test_input.split('\n')[1:-1]]:
#     print('\t{')
#     print(f"\t\t'name': '{name}',\n\t\t'at': {at},\n\t\t'df': {df}")
#     print('\t},')

# TEST = [
#     [
#         {
#             'name': 'sameezahur',
#             'at': 20,
#             'df': 21
#         },
#         {
#             'name': 'sohelh',
#             'at': 18,
#             'df': 9
#         },
#         {
#             'name': 'jaan',
#             'at': 17,
#             'df': 86
#         },
#         {
#             'name': 'sidky',
#             'at': 16,
#             'df': 36
#         },
#         {
#             'name': 'shamim',
#             'at': 16,
#             'df': 18
#         },
#         {
#             'name': 'shadowcoder',
#             'at': 12,
#             'df': 9
#         },
#         {
#             'name': 'muntasir',
#             'at': 13,
#             'df': 4
#         },
#         {
#             'name': 'brokenarrow',
#             'at': 16,
#             'df': 16
#         },
#         {
#             'name': 'emotionalblind',
#             'at': 16,
#             'df': 12
#         },
#         {
#             'name': 'tanaeem',
#             'at': 20,
#             'df': 97
#         },
#     ],
# ]

################################################################################

def load(): # load() taken from https://stackoverflow.com/questions/35687667/python-runtime-error-in-online-judge
    cases = int(next(sys.stdin))
    for _ in range(cases):
        players = []
        for _ in range(10):
            name, at, df = next(sys.stdin).split(' ')
            at = int(at)
            df = int(df)
            players.append({'name': name, 'at': at, 'df': df})
        yield players


def sort_by_name(players: list[dict]):
    players.sort(key = lambda p: p['name'])


def assign(players: list[dict], sum_at: int = 0, attackers: list[int] = [], player_idx: int = 0):

    def optimal(left: tuple, right: tuple):
        sum_at_left, sum_df_left, attackers_left = left
        sum_at_right, sum_df_right, attackers_right = right
        if sum_at_left > sum_at_right:
            return left
        elif sum_at_left < sum_at_right:
            return right
        else:
            if sum_df_left > sum_df_right:
                return left
            elif sum_df_left < sum_df_right:
                return right
            else:
                for left_at, right_at in zip(attackers_left, attackers_right):
                    if left_at < right_at:
                        return left
                    elif left_at > right_at:
                        return right

    if len(attackers) == 5: # attacker list is full
        sum_df = sum([players[i]['df'] for i in range(10) if i not in attackers])
        return (sum_at, sum_df, attackers)

    elif len(attackers) + (10 - player_idx) == 5: # attacker list is already determined 
        attackers += [i for i in range(player_idx, 10)]
        sum_at += sum([players[i]['at'] for i in range(player_idx, 10)])
        sum_df = sum([players[i]['df'] for i in range(10) if i not in attackers])
        return (sum_at, sum_df, attackers)
    
    return optimal(
        assign(
            players,
            sum_at + players[player_idx]['at'],
            attackers + [player_idx],
            player_idx + 1
        ),
        assign(players, sum_at, attackers, player_idx + 1)
    )

if __name__ == '__main__':
    for case_idx, players in enumerate(load()):
        sort_by_name(players) # Preprocess
        sum_at, sum_df, attacker_idxs = assign(players, 0, [], 0)
        attackers = [players[i]['name'] for i in attacker_idxs]
        defenders = [players[i]['name'] for i in range(10) if i not in attacker_idxs]

        print(f'Case {case_idx + 1}:')
        print('(', end = '')
        for attacker in attackers[:-1]:
            print(f'{attacker}, ', end = '')
        print(f'{attackers[-1]})')
        print('(', end = '')
        for defender in defenders[:-1]:
            print(f'{defender}, ', end = '')
        print(f'{defenders[-1]})')