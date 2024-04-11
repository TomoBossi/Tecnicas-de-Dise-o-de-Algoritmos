#include <iostream>
using namespace std;

char a[200001], b[200001];                                                      // Strings (globals)
int n = 0;                                                                      // String length (global)

bool eq(int i, int j, int k, int l) {
    int n = j-i+1;                                                              // String length
    if (j<i || l<k) return false;                                               // Pathological case (inverted indexes)
    else if (n-1 != l-k) return false;                                          // Pathological case (strings of different lengths)
    else if (n==1) return a[i]==b[k];                                           // Base case (n = 1)
    else if (n==2) return a[i]==b[k] && a[j]==b[l] || a[i]==b[l] && a[j]==b[k]; // Base case (n = 2) (unnecesary, but removes lots of recursive calls)
    if (n%2==0) {                                                               // If a, b are of even length...
        int m = n/2;
        if (eq(i, j-m, k, l-m) && eq(i+m, j, k+m, l)) return true;              // Check condition 2.1. (recursion)
        if (eq(i, j-m, k+m, l) && eq(i+m, j, k, l-m)) return true;              // Check condition 2.2. (recursion)
    }
    for (int m = 0; m<n; m++) { if (a[i+m]!=b[k+m]) return false; }             // Else (if nothing was returned or a, b are of odd length) check condition 1.
    return true;
}

int main() { 
	scanf("%s\n",a);
	scanf("%s",b);
    while (a[n] != '\0') n++;
    cout << (eq(0, n-1, 0, n-1) ? "YES" : "NO") << endl;
    return 0;
}