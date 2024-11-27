import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        List<Long> list = new ArrayList<>();

        while(true){
            list.add(sc.nextLong());
            if(list.size() == N) break;
        }

        List<Long> res = new ArrayList<>();

        for(Long num : list){
            Long newNum = 0L;
            while(num > 0){
                newNum = newNum*10 + num%10;
                num /= 10;
            }
            res.add(newNum);
        }

        Collections.sort(res);

        for(Long num : res){
            System.out.println(num);
        }

    }
}