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
        int[] arr = new int[N];
        int pos = 0;
        int neg = 0;
        int zero = 0;
        int one = 0;

        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(br.readLine());
            if(arr[i] == 0) zero ++;
            else if(arr[i] == 1) one ++;
            else if(arr[i] > 1) pos ++;
            else neg ++;
        }

        Arrays.sort(arr);
        int res = 0;

        // 양수 처리
        for(int i=N-1; i>=N-pos; i--){
            if(i-1 >= N-pos){
                res += arr[i] * arr[i-1];
                i--;
            } else{
                res += arr[i];
            }
        }

        // 음수 처리
        for(int i=0; i<neg; i++){
            if(i+1 < neg){
                res += arr[i] * arr[i+1];
                i++;
            } else{
                if(zero > 0){
                    res += 0;
                } else{
                    res += arr[i];
                }
            }
        }

        // 1 처리
        res += one;

        System.out.println(res);
    }
}