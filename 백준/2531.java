package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int D = sc.nextInt();
        int K = sc.nextInt();
        int C = sc.nextInt();

        int[] sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = sc.nextInt();
        }

        int [] cnt = new int [D+1];
        int sushiCnt = 0;   // 스시 종류 수
        int res = 0;

        for(int i=0; i<K; i++){
            if(cnt[sushi[i]] == 0) sushiCnt ++;
            cnt[sushi[i]] ++;
        }

        res = sushiCnt;

        for(int i=0; i<N; i++){
            int removeSushi = sushi[i];
            cnt[removeSushi] --;
            if (cnt[removeSushi] == 0) sushiCnt --;

            int addSushi = sushi[(i+K) % N];
            if (cnt[addSushi] == 0) sushiCnt ++;
            cnt[addSushi] ++;

            if (cnt[C] == 0) {
                res = Math.max(res, sushiCnt + 1); // 쿠폰 초밥이 없으면 고유 초밥 수에 +1
            } else {
                res = Math.max(res, sushiCnt); // 쿠폰 초밥이 이미 포함되어 있으면 그대로
            }
        }
        System.out.println(res);
    }
}
