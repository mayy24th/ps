import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Scanner sc = new Scanner(System.in);

        String input = br.readLine();
        String[] splitByMinus = input.split("-");

        int res = 0;

        String[] splitFirst = splitByMinus[0].split("\\+");
        for(String n : splitFirst){
            res += Integer.parseInt(n);
        }

        for(int i = 1;i<splitByMinus.length; i++){
            String[] splitByPlus = splitByMinus[i].split("\\+");
            int tmp = 0;
            for(String n : splitByPlus){
                tmp += Integer.parseInt(n);
            }
            res -= tmp;
        }

        System.out.println(res);
    }
}