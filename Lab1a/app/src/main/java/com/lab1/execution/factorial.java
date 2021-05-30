package com.lab1.execution;

import com.lab1.utils.exception.TimeExceededException;

import java.util.ArrayList;
import java.util.List;


public class factorial {

    private long time0;

    public Long[] factorize(long n) throws TimeExceededException {

        this.time0 = System.nanoTime();
        List<Long> multipliers = new ArrayList<>();

        while (n % 2 == 0) {
            multipliers.add(2L);
            n /= 2;
            long time = System.nanoTime() - this.time0;
            if (time >= 3000000000L) throw new TimeExceededException();
        }

        long[] sqrts = this.SquarSum    (n);
        multipliers.add(Math.abs(sqrts[0] + sqrts[1]));
        multipliers.add(Math.abs(sqrts[0] - sqrts[1]));

        return multipliers.toArray(new Long[0]);

    }

    private long[] SquarSum(long n) throws TimeExceededException {
        double x, y;
        x = Math.ceil(Math.sqrt(n));
        y = Math.pow(x, 2) - n;

        while (Math.sqrt(y) != Math.ceil(Math.sqrt(y))) {
            x++;
            y = Math.pow(x, 2) - n;
            long time = System.nanoTime() - this.time0;
            if (time >= 3000000000L) throw new TimeExceededException();
        }

        return new long[]{(long) x, (long) Math.sqrt(y)};
    }
}
