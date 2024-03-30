import sys

def load(): # load() taken from https://stackoverflow.com/questions/35687667/python-runtime-error-in-online-judge
    cases = int(next(sys.stdin))
    for _ in range(cases):
        n = int(next(sys.stdin))
        heights = [int(height) for height in next(sys.stdin).split(' ')]
        widths = [int(width) for width in next(sys.stdin).split(' ')]
        yield n, heights, widths


def longest_subsequence(heights: list[int], widths: list[int], reverse: bool = False):
    N = len(heights)
    M = [(widths[N-1], N-1)]

    def insert_in_order(M, data):
        i = 0
        not_added = True
        while i < len(M) and not_added:
            if data > M[i]:
                M.insert(i, data)
                not_added = False
            i += 1
        if i == len(M):
            M.append(data)

    def longest(building_idx, reverse):

        if building_idx < 0:
            return M[0]

        h = heights[building_idx]
        w = widths[building_idx]
        for j in range(len(M)):
            total_width, building = M[j]
            subsequence_continues = h < heights[building]
            if reverse:
                subsequence_continues = h > heights[building]
            if subsequence_continues:
                insert_in_order(M, (w + total_width, building_idx))
                return longest(building_idx - 1, reverse)
        insert_in_order(M, (w, building_idx))
        return longest(building_idx - 1, reverse)

    return longest(N-2, reverse)


if __name__ == '__main__':
    for case_idx, (n, heights, widths) in enumerate(load()):
        inc = longest_subsequence(heights, widths, False)[0]
        dec = longest_subsequence(heights, widths, True)[0]

        if inc >= dec:
            print(f'Case {case_idx + 1}. Increasing ({inc}). Decreasing ({dec}).')
        else:
            print(f'Case {case_idx + 1}. Decreasing ({dec}). Increasing ({inc}).')