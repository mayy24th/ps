import java.util.*;

class Solution {
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    String[][] map;
    boolean[][] visited;
    int n, m;

    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        n = storage.length;
        m = storage[0].length();
        map = new String[n+2][m+2];

        for(int i=0; i<n+2; i++) Arrays.fill(map[i], "-1");
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                map[i+1][j+1] = storage[i].charAt(j) + "";
            }
        }

        for(String req : requests){
            bfs();
            if(req.length() == 2) crane(req.charAt(0) + "");
            else fork(req);
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(map[i+1][j+1].equals("-1")) continue;
                answer ++;
            }
        }

        return answer;
    }

    void bfs(){
        visited = new boolean[n+2][m+2];

        Queue<int []> q = new LinkedList<>();
        q.add(new int[]{0, 0});
        visited[0][0] = true;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int i=0; i<4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx < 0 || ny < 0 || nx >= n+2 || ny >= m+2) continue;
                if(visited[nx][ny] || !map[nx][ny].equals("-1")) continue;

                visited[nx][ny] = true;
                q.add(new int[]{nx, ny});
            }
        }
    }

    void crane(String req){
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(map[i+1][j+1].equals(req)) map[i+1][j+1] = "-1";
            }
        }
    }

    void fork(String req){
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(map[i+1][j+1].equals(req) && isBoundary(i+1, j+1)) map[i+1][j+1] = "-1";
            }
        }
    }

    boolean isBoundary(int x, int y){
        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (visited[nx][ny]) return true;
        }
        return false;
    }
}