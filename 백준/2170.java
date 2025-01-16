import java.io.*;
import java.util.*;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        int [][] arr = new int[N][2];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, Comparator.comparingInt(i -> i[0]));

        int res = 0;
        int start = arr[0][0];
        int end = arr[0][1];

        for(int i=1; i<N; i++){
            if(arr[i][0] <= end){
                // start = 1, end = 3
                // 새로 들어온 두 점이 2, 5일 경우
                // 시작점이 end 보다 작음 (겹치는 선)
                // => 두 좌표중 끝 좌표가 더 큰 값으로 end 갱신
                // start = 1, end = 5
                end = Math.max(end, arr[i][1]);
            } else{
                // 새로 들어온 두 점의 시작점이
                // end 보다 클 경우 => 겹치지 않음
                // 현재까지의 길이를 res 에 저장하고 start, end 갱신
                res += (end - start);
                start = arr[i][0];
                end = arr[i][1];
            }
        }

        res += (end - start);

        System.out.println(res);
    }
}
