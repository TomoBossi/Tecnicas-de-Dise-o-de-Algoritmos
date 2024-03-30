import sys

def load(): # load() taken from https://stackoverflow.com/questions/35687667/python-runtime-error-in-online-judge
    cases = int(next(sys.stdin))
    for _ in range(cases):
        n = int(next(sys.stdin))
        heights = [int(height) for height in next(sys.stdin).split(' ')]
        widths = [int(width) for width in next(sys.stdin).split(' ')]
        yield n, heights, widths


def longest_subsequence(heights: list[int], widths: list[int], total_width: int = 0, buildings: list[int] = [], building_idx: int = 0, reverse: bool = False):
    
    def optimal(left: tuple, right: tuple):
        if left[0] >= right[0]:
            return left
        return right
    
    if len(heights) <= building_idx:
        return (total_width, buildings)
    
    if not buildings:
        return optimal(
            longest_subsequence(
                heights,
                widths, 
                total_width + widths[building_idx], 
                buildings + [building_idx], 
                building_idx + 1,
                reverse),
            longest_subsequence(heights, widths, total_width, buildings, building_idx + 1, reverse)
        )

    last_height = heights[buildings[-1]]
    for i in range(building_idx, len(heights)):
        subsequence_continues = heights[i] > last_height
        if reverse:
            subsequence_continues = heights[i] < last_height
        if subsequence_continues:
            return optimal(
                longest_subsequence(
                    heights, 
                    widths, 
                    total_width + widths[i], 
                    buildings + [i], 
                    i+1,
                    reverse),
                longest_subsequence(heights, widths, total_width, buildings, i+1, reverse)
            )
    
    return (total_width, buildings)


if __name__ == '__main__':
    for case_idx, (n, heights, widths) in enumerate(load()):
        inc = longest_subsequence(heights, widths, 0, [], 0, False)[0]
        dec = longest_subsequence(heights, widths, 0, [], 0, True)[0]

        if inc >= dec:
            print(f'Case {case_idx + 1}. Increasing ({inc}). Decreasing ({dec}).')
        else:
            print(f'Case {case_idx + 1}. Decreasing ({dec}). Increasing ({inc}).')