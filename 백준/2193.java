import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(br.readLine());
        long[] dp = new long[91];

        dp[1] = 1;
        dp[2] = 1;

        for(int i=3; i<=N; i++){
            /*
             * 0으로 끝나는 이친수 : 길이가 N-1인 이친수 끝에 0을 추가
             * 1로 끝나는 이친수 : 길이가 N-2인 이친수 끝에 1을 추가
             * N=3) 100, 101
             * N=4) 1000, 1001, 1010
             * N=5) 10000, 10001, 10010, 10100, 10101
             * -> N=3인 이친수의 뒤에 00을 붙이거나, N=4인 이친수 뒤에 1을 붙이면 N=5 이친수
             */
            dp[i] = dp[i-1] + dp[i-2];
        }

        System.out.println(dp[N]);
    }
}