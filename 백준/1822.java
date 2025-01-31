package org.elice;

import java.io.*;
import java.util.*;

public class Main {
    static int NA, NB;
    static int[] A;
    static int[] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        NA = Integer.parseInt(st.nextToken());
        NB = Integer.parseInt(st.nextToken());
        A = new int[NA];
        B = new int[NB];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < NA; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < NB; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(B);
        List<Integer> res = new ArrayList<>();

        for (int num : A) {
            int left = 0, right = NB - 1;
            boolean isFind = false;

            while (left <= right) {
                int mid = (left + right) / 2;
                if (B[mid] == num) {
                    isFind = true;
                    break;
                } else if (B[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            if (!isFind) {
                res.add(num);
            }
        }

        Collections.sort(res);
        System.out.println(res.size());
        for(int num : res){
            System.out.print(num + " ");
        }
    }
}
