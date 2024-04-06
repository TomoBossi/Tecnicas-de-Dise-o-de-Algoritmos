#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);                                           // Optimize reading from stdin
    int c;                                                                      // Number of test cases
    cin >> c;
    while (c--){                                                                // While there are test cases remaining...
        int res = 0;                                                            // Initilize test case result
        int T, H, F, q, ai, prev;
        cin >> T >> H >> F;                                                     // Number of trees, height of each tree, falling distance
        vector<vector<int>> A(T, vector<int>(H, 0));                            // Number of acorns at each height of each tree
        vector<vector<int>> M(T, vector<int>(H, 0));                            // Memorization matrix, holds the max possible acorns starting from any given tree and height
        vector<int> hMax(H, 0);                                                 // Memorization vector, holds the max possible acorns at each height across all trees
        for (int ti = 0; ti < T; ti++){                                         // Initialize A
            cin >> q;
            while (q--){
                cin >> ai;
                A[ti][ai-1]++;
            }
        }
        for (int hi = 0; hi < H; hi++){
            for (int ti = 0; ti < T; ti++){
                M[ti][hi] = A[ti][hi];                                          // M[ti][hi], the max acorns attainable from tree ti and height hi, is the acorns at A[ti][hi] plus...
                if (hi < F) {
                    M[ti][hi] += hi > 0 ? M[ti][hi-1] : 0;                      // If 0 < hi < F then the max acorns attaninable by either going down one feet in the same tree, otherwise if hi = 0 then 0 (because there is no possible lower height)
                } else {
                    M[ti][hi] += max(M[ti][hi-1], hMax[hi-F]);                  // Otherwise, the max acorns attainable by either going down one feet in the same tree or jumping to another tree and dropping F feet at once
                }
                hMax[hi] = max(hMax[hi], M[ti][hi]);                            // Save the max acorns at height hi across all trees
            }
        }                                                                       // By the end, the memorization matrix is fully computed
        for (int i = 0; i < T; i++){
            res = max(res, M[i][H-1]);                                          // Out of all possible ending positions, choose the one with most acorns as the test case result
        }
        cout << res << '\n';                                                    // Output test case result to stdout
    }
    cin >> c;                                                                   // Parse trailing 0
    return 0;
}