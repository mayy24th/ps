import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int cnt = 0, res = 0;
        boolean[] isChecked = new boolean[N+1];

        for(int i=2; i<=N; i++) {
            if(!isChecked[i]){
                for(int j=i; j<=N; j+=i){
                    if(!isChecked[j]){
                        isChecked[j] = true;
                        cnt ++;
                        if(cnt == K){
                            res = j;
                            break;
                        }
                    }
                }
            }
        }

        System.out.println(res);
    }
}