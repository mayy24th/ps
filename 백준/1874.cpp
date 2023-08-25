#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> S;
    string res;
    int n; cin >> n;
    int num = 1;

    while(n--){
        int i; cin >> i;

        while(num <= i){
            // 입력받은 수와 같아질 때 까지 push
            S.push(num++);
            res += "+\n";
        }

        if(S.top() != i){
            // push 이후 top과 입력받은 수가 다르다면 올바르지 않은 수열
            cout << "NO\n";
            return 0;
        }

        S.pop();
        res += "-\n";
    }
    cout << res;
}
