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

        int[] T = new int[N];
        int[] P = new int[N];

        int[] dp = new int[N+1];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=N-1; i>=0; i--){
            if(i+T[i] <= N){ // 상담 진행 가능
                dp[i] = Math.max(dp[i+1], P[i]+dp[i+T[i]]);
            } else{
                dp[i] = dp[i+1];
            }
        }
        System.out.println(dp[0]);
    }
}