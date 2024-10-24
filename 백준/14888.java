package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];
        int[] ops = new int[4]; // [더하기, 빼기, 곱하기, 나누기]

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            ops[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3], N, nums);

        System.out.println(result[0]);  // 최대값
        System.out.println(result[1]);  // 최소값
    }

    static int[] dfs(int depth, int sum, int pl, int mi, int mul, int div, int N, int[] nums) {
        if (depth == N) {
            return new int[]{sum, sum};  // 최대값, 최소값이 동일
        }

        int maxValue = Integer.MIN_VALUE;
        int minValue = Integer.MAX_VALUE;

        // 더하기
        if (pl > 0) {
            int[] temp = dfs(depth + 1, sum + nums[depth], pl - 1, mi, mul, div, N, nums);
            maxValue = Math.max(maxValue, temp[0]);
            minValue = Math.min(minValue, temp[1]);
        }

        // 빼기
        if (mi > 0) {
            int[] temp = dfs(depth + 1, sum - nums[depth], pl, mi - 1, mul, div, N, nums);
            maxValue = Math.max(maxValue, temp[0]);
            minValue = Math.min(minValue, temp[1]);
        }

        // 곱하기
        if (mul > 0) {
            int[] temp = dfs(depth + 1, sum * nums[depth], pl, mi, mul - 1, div, N, nums);
            maxValue = Math.max(maxValue, temp[0]);
            minValue = Math.min(minValue, temp[1]);
        }

        // 나누기
        if (div > 0) {
            int[] temp = dfs(depth + 1, sum / nums[depth], pl, mi, mul, div - 1, N, nums);
            maxValue = Math.max(maxValue, temp[0]);
            minValue = Math.min(minValue, temp[1]);
        }

        return new int[]{maxValue, minValue};
    }
}