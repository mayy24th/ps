#include <bits/stdc++.h>

using namespace std;

int arr[10000001], res[10000001];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;
    for(int i=0; i<N; i++) cin >> arr[i];

    stack<int> S;

    for(int i=N-1; i>=0; i--){

        // 현재 높이 < top이 될 때까지 pop
        while(!S.empty() && S.top() <= arr[i]) {
//            cout << "pop " << S.top() << "\n";
            S.pop();
        }

        if(S.empty()) res[i] = -1;  // 없는 경우
        else res[i] = S.top();

        S.push(arr[i]);
    }

    for(int i=0; i<N; i++) cout << res[i] << ' ';
}
