#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);                                           // ...
    cin.tie(NULL);                                                              // Optimize reading from stdin (970 ms -> 160 ms in vjudge)
    int C, T, H, F, q, a;
    cin >> C;                                                                   // Number of test cases
    while (C--){                                                                // While there are test cases remaining...
        cin >> T >> H >> F;                                                     // Number of trees, height of each tree, falling distance                         
        int M[T+1][H] = {};                                                     // M is the memorization matrix, which holds the max acorns attainable starting from any given tree and height. The last subarray holds the max possible acorns from each height across all trees (unnecessary, but it can save lots of time). The solution, after computing M, is therefore given by M[T][H-1]
        for (int t = 0; t<T; t++){                                              // Initialize M with the number of acorns at each height of each tree
            cin >> q;
            while (q--){
                cin >> a;
                M[t][a-1]++;
            }
        }
        for (int h = 0; h<H; h++){
            for (int t = 0; t<T; t++){
                M[t][h] += h<F ? (h>0 ? M[t][h-1]:0):max(M[t][h-1], M[T][h-F]); // To get M[t][h] take the amount of acorns from tree t and height h and sum the following to it: if 0 < h < F then the max acorns attaninable by going down one feet in the same tree, if h = 0 then 0 (because there is no possible lower height); otherwise, if h >= F, the max acorns attainable by either going down one foot in the same tree or jumping to another tree and dropping F feet at once
                M[T][h] = max(M[T][h], M[t][h]);                                // Save the max acorns attainable from height h across all trees
            }
        }                                                                       // By the end, the memorization matrix and array are fully computed
        cout << M[T][H-1] << '\n';                                              // Output test case result to stdout
    }
    cin >> C;                                                                   // Parse trailing 0
    return 0;
}