#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // <내 앞의 최대 높이, 인덱스>
    stack<pair<int, int>> S;

    // 첫번째 타워의 신호는 수신 불가
    S.push({100000001, 0});

    int n; cin >> n;
    for(int i=1; i<=n; i++){
        int num; cin >> num;

        // 입력받은 높이보다 큰 높이가 나올때까지 pop
        while(S.top().first < num) S.pop();

        // 큰 높이가 나오면 그때의 인덱스 출력하고 입력받은 높이, 인덱스 push
        cout << S.top().second << " ";
        S.push({num, i});
    }
}
