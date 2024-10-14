package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayDeque<Integer> deque = new ArrayDeque<>();
        for(int i=1; i<=N; i++) deque.add(i);

        st = new StringTokenizer(br.readLine());
        int res = 0;
        for(int i=0; i<M; i++){
            int findNum = Integer.parseInt(st.nextToken());

            // <-- 2
            // --> 3
            // 1 2 3 4 5 6 7 8 9 10

            // min(Deque.size() - 찾은 인덱스, 찾은 인덱스)
            // 2

            int idx = 0;
            for(int num : deque){
                if(num == findNum) break;
                idx ++;
            }

            if(idx < deque.size() - idx){ // <--
                for(int j=0; j<idx; j++){
                    deque.offerLast(deque.pollFirst());
                }
            } else{ // -->
                idx = deque.size() - idx;
                for(int j=0; j<idx; j++){
                    deque.offerFirst(deque.pollLast());
                }
            }
            res += idx;
            deque.pollFirst();
        }
        System.out.println(res);
    }
}