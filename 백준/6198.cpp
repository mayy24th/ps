#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;

    stack<long long> S;
    long long res = 0;
    while(N--){
        long long h; cin >> h;

        // 입력된 높이보다 왼쪽에 있는 더 높은 빌딩이 나올 떄 까지 pop
        while(!S.empty() && S.top() <= h) S.pop();

        // S.size()는 현재 높이의 빌딩을 내려다 보고 있는 빌딩의 수
        res += S.size();
        S.push(h);
    }

    cout << res;
}
