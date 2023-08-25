#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc; cin >> tc;

    while(tc--){
        string s; cin >> s;
        list<char> L;
        auto c = L.begin();
        for(auto e : s){
            if(e == '<'){   // 커서 왼쪽으로
                if(c != L.begin()) c--;
            } else if(e == '>'){    // 커서 오른쪽으로
                if(c != L.end()) c++;
            } else if(e == '-'){    // 백스페이스
                if(c != L.begin()){
                    c--;
                    c = L.erase(c);
                }
            } else{
                L.insert(c, e);
            }
        }

        for(auto e : L) cout << e;
        cout << '\n';

    }
}
