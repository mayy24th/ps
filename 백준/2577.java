package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        int res = A * B * C;
        List<Integer> cnt = new ArrayList(Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
        while(res > 0){
            cnt.set(res % 10, cnt.get(res % 10) + 1);
            res /= 10;
        }

        for(int i : cnt){
            System.out.println(i);
        }
    }
}