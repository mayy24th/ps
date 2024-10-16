package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int tc = Integer.parseInt(br.readLine());

        int M, N, K, x, y, res;
        int [][] graph;
        int [][] visited;
        while(tc --> 0){
            res = 0;
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            graph = new int[N][M];
            visited = new int[N][M];
            while(K --> 0){
                st = new StringTokenizer(br.readLine());
                y = Integer.parseInt(st.nextToken());
                x = Integer.parseInt(st.nextToken());
                graph[x][y] = 1;
            }

            for(int i=0; i<N; i++){
                for(int j=0; j<M; j++){
                    if(visited[i][j] == 0 && graph[i][j] == 1){
                        res += bfs(graph, i, j, visited);
                    }
                }
            }
            System.out.println(res);
        }
    }

    public static int bfs(int[][] graph, int i, int j, int[][] visited){
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});
        visited[i][j] = 1;

        while(! q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for(int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dy[k];

                if (nx >= 0 && ny >= 0 && nx < graph.length && ny < graph[0].length){
                    if(visited[nx][ny] == 0 && graph[nx][ny] == 1){
                        q.add(new int[]{nx, ny});
                        visited[nx][ny] = 1;
                    }
                }
            }
        }

        return 1;
    }
}