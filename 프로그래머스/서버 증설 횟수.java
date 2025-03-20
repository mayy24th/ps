import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] server_count = new int[24];
        int[] count = new int[24];
        Arrays.fill(server_count, 0);
        Arrays.fill(count, 0);

        for(int i=0; i<24; i++){
            int p = players[i];

            if(p >= m){
                if(p/m <= server_count[i]) continue;
                // 증설해야하는 서버 - 이미 있는 서버
                int tmp = (p/m) - server_count[i];
                count[i] += tmp;
                for(int j=i; j<i+k; j++){
                    if(j == 24) break;
                    server_count[j] += tmp;
                }
            }
        }

        for(int i=0; i<24; i++){
            answer += count[i];
        }
        return answer;
    }
}