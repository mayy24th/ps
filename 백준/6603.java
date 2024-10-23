package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while(true){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            if(n == 0) break;

            int[] arr = new int[n];
            boolean[] visit = new boolean[n];

            for(int i=0; i<n; i++) arr[i] = Integer.parseInt(st.nextToken());

            combi(arr, visit, 0, 0);
            System.out.println();
        }
    }

    public static void combi(int[] arr, boolean[] visit, int start, int depth) {
        if(depth == 6){
            for(int i=0; i<arr.length; i++){
                if(visit[i]){
                    System.out.print(arr[i] + " ");
                }
            }
            System.out.println();
            return ;
        }

        for(int i=start; i<arr.length; i++){
            visit[i] = true;
            combi(arr, visit, i+1, depth+1);
            visit[i] = false;
        }
    }
}
