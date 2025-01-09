import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        visited = new boolean[N][N];

        // 입력
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 섬 번호 -> 1:바다 / 섬은 2부터 시작
        int mapNumber = 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    mapNumberCheck(i, j, mapNumber);
                    mapNumber++;
                }
            }
        }

        // 최소 다리길이 계산
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] > 1) { // 섬인 경우
                    result = Math.min(result, calcBridge(i, j));
                }
            }
        }

        System.out.println(result);
    }

    static void mapNumberCheck(int x, int y, int mapNumber) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;
        map[x][y] = mapNumber;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cx = cur[0];
            int cy = cur[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
                    if (map[nx][ny] == 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        map[nx][ny] = mapNumber;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }

    static int calcBridge(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] curVisited = new boolean[N][N];
        queue.add(new int[]{x, y, 0}); // x좌표, y좌표, 거리
        curVisited[x][y] = true;
        int currentIsland = map[x][y];

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cx = cur[0];
            int cy = cur[1];
            int dist = cur[2];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
                    if (!curVisited[nx][ny]) {
                        curVisited[nx][ny] = true;

                        if (map[nx][ny] == 0) { // 바다라면 계속 탐색
                            queue.add(new int[]{nx, ny, dist + 1});
                        } else if (map[nx][ny] != currentIsland) { // 다른 섬에 도달
                            return dist;
                        }
                    }
                }
            }
        }
        return Integer.MAX_VALUE; // 다른 섬에 도달하지 못한 경우
    }
}
