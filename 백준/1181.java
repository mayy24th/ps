package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        Set<String> set = new HashSet<>();

        while (N-- > 0) {
            set.add(br.readLine());
        }

        List<String> list = new ArrayList<>(set);

        Collections.sort(list, (s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2); // 사전순 정렬
            }
            return Integer.compare(s1.length(), s2.length()); // 길이순 정렬
        });

        for (String s : list) {
            System.out.println(s);
        }
    }
}
