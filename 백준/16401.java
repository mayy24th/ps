
import java.io.*;
import java.util.*;

public class Main {
    static int M, N;
    static int[] L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        L = new int[N];

        int left = 1, right = 0;
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            L[i] = Integer.parseInt(st.nextToken());
            right = Math.max(right, L[i]);  // 최대길이 찾기
        }

        int res = 0;
        while(left <= right){
            int mid = (left+right) / 2;
            int cnt = 0;

            for(int num : L){
                cnt += num/mid;     // 같은 길이로 과자를 나누었을때 총 몇명에게 줄 수 있는지 계산
            }

            if(cnt >= M){
                // M명 이상에게 나누어줄 수 있다면 더 길게 쪼갤 수 있음
                res = mid;  // 현재 값으로 결과값을 갱신 -> 마지막에 가장 긴 값이 저장
                left = mid+1;
            } else{
                right = mid-1;
            }
        }

        System.out.println(res);

    }
}
