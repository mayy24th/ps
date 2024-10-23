package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        List<String[]> p = new ArrayList<>();

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            p.add(new String[]{st.nextToken(), st.nextToken()});
        }

        p.sort((p1, p2) -> Integer.parseInt(p1[0]) - Integer.parseInt(p2[0]));
        for (String[] res : p) {
            System.out.println(res[0] + " " + res[1]);
        }
    }
}
