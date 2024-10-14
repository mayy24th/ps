package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) {
            String str = br.readLine().trim();
            int chk = 0;
            boolean isBalanced = true;

            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '(') {
                    chk++;
                } else if (str.charAt(j) == ')') {
                    chk--;
                    if (chk < 0) {
                        isBalanced = false;
                        break;
                    }
                }
            }

            if (isBalanced && chk == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}