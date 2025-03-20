import java.util.*;

class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;

        int h = 0;
        if(n%w==0) h = n/w;
        else h = (n/w) + 1;

        int[][] map = new int[h][w];
        for(int i=0; i<h; i++){
            Arrays.fill(map[i], -1);
        }

        int tmp = 1;
        for(int i=0; i<h; i++){
            if(i % 2 == 0){ // 짝수 : 오른쪽으로
                for(int j=0; j<w; j++){
                    map[i][j] = tmp ++;
                    if(map[i][j] == n) break;
                }
            } else { // 홀수 : 왼쪽으로
                for(int j=w-1; j>=0; j--){
                    map[i][j] = tmp ++;
                    if(map[i][j] == n) break;
                }
            }
        }

        int x = 0;
        int y = 0;

        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(map[i][j] == num){
                    x = i;
                    y = j;
                    break;
                }
            }
        }

        for(int i=x; i<h; i++){
            if(map[i][y] != -1) answer ++;
        }
        return answer;
    }
}