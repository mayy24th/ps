package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int L, C;
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        char []input = new char[C];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<C; i++) input[i] = st.nextToken().charAt(0);

        Arrays.sort(input);
        combi(C, L, input, 0, 0, "", 0, 0);
    }

    public static void combi(int C, int L, char[] input, int start, int depth, String res, int vowel, int consonant) {
        if (depth == L) {
            if (vowel >= 1 && consonant >= 2) {
                System.out.println(res);
            }
            return;
        }

        for (int i = start; i < C; i++) {
            char c = input[i];
            int newVowel = vowel;
            int newConsonant = consonant;

            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                newVowel++;
            } else {
                newConsonant++;
            }

            combi(C, L, input, i+1, depth+1, res+c, newVowel, newConsonant);

        }
    }
}
