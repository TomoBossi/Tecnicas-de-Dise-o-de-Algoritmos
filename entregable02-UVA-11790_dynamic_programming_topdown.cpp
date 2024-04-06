#include <iostream> 
using namespace std; 

void insert_in_order(int N, int M[][2], int data[], int i) {
    int data_0 = data[0];
    int data_1 = data[1];
    if (data_0 > M[i+1][0]) {
        M[i][0] = data_0;
        M[i][1] = data_1;
    } else {
        for (int j = i; j < N-1; j++) {
            if (data_0 > M[j+1][0]) {
                return;
            }
            M[j][0] = M[j+1][0];
            M[j][1] = M[j+1][1];
            M[j+1][0] = data[0];
            M[j+1][1] = data[1];
        }
    }
}

void longest_subsequence(int N, int M[][2], int heights[], int widths[], int building_idx, bool reverse) {
    if (building_idx < 0) {
        return;
    }
    int h = heights[building_idx];
    int w = widths[building_idx];
    for (int k = building_idx+1; k < N; k++) {
        int total_width = M[k][0];
        int building = M[k][1];
        bool subsequence_continues = (!reverse && h < heights[building] || reverse && h > heights[building]);
        if (subsequence_continues) {
            int data[2] = {w + total_width, building_idx};
            insert_in_order(N, M, data, building_idx);
            longest_subsequence(N, M, heights, widths, building_idx - 1, reverse);
            return;
        }
    }
    int data[2] = {w, building_idx};
    insert_in_order(N, M, data, building_idx);
    longest_subsequence(N, M, heights, widths, building_idx - 1, reverse);
}

int main() { 
    int cases;
    cin >> cases;
    for (int case_idx = 0; case_idx < cases; case_idx++) {
        int N;
        cin >> N;
        int heights[N];
        int widths[N];
        int number;
        int i = 0;
        while (i < N) {
            cin >> number; 
            heights[i++] = number;
        }
        i = 0;
        while (i < N) {
            cin >> number; 
            widths[i++] = number;
        }

        int M[N][2];
        M[N-1][0] = widths[N-1];
        M[N-1][1] = N-1;
        longest_subsequence(N, M, heights, widths, N-2, false);
        int inc = M[0][0];
        M[N-1][0] = widths[N-1];
        M[N-1][1] = N-1;
        longest_subsequence(N, M, heights, widths, N-2, true);
        int dec = M[0][0];

        if (inc >= dec) {
            cout << "Case " << case_idx+1 << ". Increasing (" << inc << "). Decreasing (" << dec << ").\n";
        } else {
            cout << "Case " << case_idx+1 << ". Decreasing (" << dec << "). Increasing (" << inc << ").\n";
        }
    }
    return 0;
} 