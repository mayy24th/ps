import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;

        int cur_answer = -1;
        for (int i = 0; i < wires.length; i++) {
            int[][] arr = new int[wires.length - 1][2];

            int index = 0;
            for (int j = 0; j < wires.length; j++) {
                if (i == j) continue;
                arr[index++] = wires[j];
            }
            boolean[] visited = new boolean[n+1];
            int[] count = new int[2];
            int idx = 0;
            for(int num = 1; num <= n; num++){
                if(!visited[num]){
                    count[idx++] = bfs(arr, num, n, visited);
                    if(idx == 2) break;
                }
            }

            answer = Math.min(answer, Math.abs(count[0]-count[1]));
        }


        return answer;
    }

    int bfs(int[][] arrs, int start, int n, boolean[] visited){
        int count = 0;

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] arr: arrs){
            graph.get(arr[0]).add(arr[1]);
            graph.get(arr[1]).add(arr[0]);
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;

        while(!q.isEmpty()){
            int node = q.poll();
            count ++;

            for(int next: graph.get(node)){
                if(!visited[next]){
                    q.add(next);
                    visited[next] = true;
                }
            }
        }
        return count;
    }
}