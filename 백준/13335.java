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
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[] trucks = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trucks[i] = Integer.parseInt(st.nextToken());
        }

        Queue<Integer> bridge = new LinkedList<>();
        int currentWeight = 0;
        int time = 0;

        // 다리 길이에 맞게 초기 큐를 0으로 채움
        for (int i = 0; i < w; i++) {
            bridge.offer(0);
        }

        int idx = 0;

        while (idx < n || currentWeight > 0) {  // 지나갈 트럭이 남아있거나 다리위에 트럭이 있는 경우 반복
            time++;  // 시간 흐름

            // 다리에서 트럭이 나감
            currentWeight -= bridge.poll();

            // 다음 트럭이 다리에 올라갈 수 있는지 체크
            if (idx < n && currentWeight + trucks[idx] <= L) {
                // 트럭이 다리에 올라갈 수 있는 경우
                bridge.offer(trucks[idx]);
                currentWeight += trucks[idx];
                idx++;
            } else {
                // 트럭이 올라갈 수 없는 경우, 다리를 비워주기 위해 0을 추가
                bridge.offer(0);
            }
        }

        System.out.println(time);
    }
}
