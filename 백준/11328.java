package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for(int i=0; i<N; i++){
            List<String> input = List.of(br.readLine().split(" "));

            Arrays.fill(cnt1, 0);
            Arrays.fill(cnt2, 0);

            for(int j=0; j<input.get(0).length(); j++){
                cnt1[input.get(0).charAt(j) - 'a'] ++;
            }
            for(int j=0; j<input.get(1).length(); j++){
                cnt2[input.get(1).charAt(j) - 'a'] ++;
            }

            if(Arrays.equals(cnt1, cnt2)){
                System.out.println("Possible");
            } else{
                System.out.println("Impossible");
            }
        }
    }
}
