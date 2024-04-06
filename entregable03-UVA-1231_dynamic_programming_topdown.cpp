#include <iostream>
#include <vector>
using namespace std;

int max_acorns(int T, int H, int F, vector<vector<int>> &M, vector<vector<int>> &heights, int i, int j) {
    if (j >= H) {
        return 0;
    }
    if (M[i][j] == -1) {
        if (H - j - 1 <= F) {
            M[i][H-1] = heights[i][H-1];
            for (int k = H-2; k >= j; k--) {
                M[i][k] = heights[i][k] + M[i][k+1];
            }
        } else {
            int next_j = j + 1;
            while (next_j < H && heights[i][next_j] == 0) {
                next_j += 1;
            }
            int res = max_acorns(T, H, F, M, heights, i, next_j);
            for (int k = j+1; k < next_j; k++) {
                M[i][k] = res;
            }
            int res_candidate;
            for (int k = 0; k < T; k++) {
                if (k != i) {
                    res_candidate = max_acorns(T, H, F, M, heights, k, j+F);
                    if (res_candidate > res) {
                        res = res_candidate;
                    }
                }
            }
            M[i][j] = heights[i][j] + res;
        }
    }
    return M[i][j];
}

int main() { 
    ios_base::sync_with_stdio(false);
    int cases;
    cin >> cases;
    for (int case_idx = 0; case_idx < cases; case_idx++) {
        int T, H, F, qty, idx, res, res_candidate;
        cin >> T;
        cin >> H;
        cin >> F;
        vector<vector<int>> heights(T, vector<int>(H, 0));
        vector<vector<int>> M(T, vector<int>(H, -1));
        for (int i = 0; i < T; i++) {
            cin >> qty;
            for (int _ = 0; _ < qty; _++) {
                cin >> idx;
                heights[i][idx - 1]++;
            }
        }
        res = max_acorns(T, H, F, M, heights, 0, 0);
        for (int i = 1; i < T; i++) {
            res_candidate = max_acorns(T, H, F, M, heights, i, 0);
            if (res_candidate > res) {
                res = res_candidate;
            }
        }
        cout << res << endl;
    }
    cin >> cases;
    return 0;
}
