package com.lab3a.utils;

import java.util.*;


public class Permissions {

    private final long[][] perms;
    private final long[] p;
    private final int n;
    private int k;

    public Permissions(long[] s) {

        this.n = s.length;
        this.perms = new long[fact(n)][n];
        p = Arrays.copyOf(s, n);
        k = 0;
        antilex(n - 1);

    }

    public long[][] getPerms() {

        return this.perms;

    }

    private void antilex(int m) {

        if(m == 0)
            perms[k++] = Arrays.copyOf(p, n);
        else {
            for(int i = 0; i <= m; i++) {
                antilex(m-1);
                if(i < m) {
                    swap(i, m);
                    reverse(m-1);
                }
            }
        }

    }

    private void swap(int a, int b) {

        long t = p[a];
        p[a] = p[b];
        p[b] = t;

    }

    private void reverse(int m) {

        int i = 0;
        int j = m;

        while(i < j) {

            swap(i, j);
            i++;
            j--;

        }

    }

    private static int fact(int n) {

        int res = 1;

        for(int i = 1; i <= n; i++) res *= i;

        return res;

    }

}
