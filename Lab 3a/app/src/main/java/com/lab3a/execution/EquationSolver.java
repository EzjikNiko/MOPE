package com.lab3a.execution;

import android.os.Build;

import androidx.annotation.RequiresApi;

import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;


public class EquationSolver {

    private long y;
    private long[] coefficients;
    private long[] roots;

    private long findMax(long[] array) {

        Arrays.sort(array);

        return array[array.length - 1];

    }

    private void mix(int[] a) {

        Random random = new Random();

        for (int i = 1; i < a.length; i++) {

            int j = random.nextInt(i);
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;

        }

    }

    private void replace(long[] a, long[] b) {

        Random random = new Random();
        int index = random.nextInt(a.length);
        long tmp;
        tmp = a[index];
        a[index] = b[index];
        b[index] = tmp;

    }

    public void setY(long y) {

        this.y = y;

    }

    public void setCoefficients(long[] coefficients) {

        this.coefficients = coefficients;

    }

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    public void solve() {

        long max_root_value = this.y / this.findMax(this.coefficients) + 1;
        Random random = new Random();

        long[][] population = new long[4][4];
        long[] fitnesses = new long[4];
        double[] ratios = new double[4];
        boolean rootFound = false;

        for (int i = 0; i < population.length; i++) {
            for (int j = 0; j < population[i].length; j++) {
                population[i][j] = ThreadLocalRandom.current().nextLong(max_root_value+1);
            }
        }

        while (!rootFound) {

            // Фітнес функція
            for (int i = 0; i < fitnesses.length; i++) {
                long value = 0L;
                for (int j = 0; j < population[i].length; j++) {
                    value += population[i][j] * this.coefficients[j];
                }
                fitnesses[i] = Math.abs(this.y - value);
            }

            // Перевірка наявності коренів
            for (int i = 0; i < fitnesses.length; i++) {
                if (fitnesses[i] == 0) {
                    this.roots = population[i];
                    rootFound = true;
                    break;
                }
            }

            // Вихід із циклу, якщо знайдено корінь
            if (rootFound) continue; else {

                double sumD = 0;
                for (long fitness : fitnesses) {
                    sumD += 1.0 / fitness;
                }

                for (int i = 0; i < ratios.length; i++) {
                    ratios[i] = fitnesses[i] / sumD;
                }

            }

            long[][] new_population = new long[4][4];
            for (int i = 0; i < new_population.length; i++) {
                double selector = Math.random();
                double ratio = 0;
                for (int j = 0; j < ratios.length; j++) {
                    if (ratio <= selector && selector < ratios[j]) {
                        new_population[i] = population[j];
                    } else {
                        ratio += ratios[j];
                    }
                }
            }

            int[] indexes = {0, 1, 2, 3};
            this.mix(indexes);
            this.replace(new_population[indexes[0]], new_population[indexes[1]]);
            this.replace(new_population[indexes[2]], new_population[indexes[3]]);

            for (int i = 0; i < new_population.length; i++) {
                int index = random.nextInt(new_population[i].length);

                boolean inc = random.nextBoolean();
                if (inc) new_population[i][index]++; else new_population[i][index]--;

            }

            for (int i = 0; i < new_population.length; i++) {
                System.arraycopy(new_population[i], 0, population[i],
                        0, new_population[i].length);
            }
        }
    }

    public long[] getRoots() {

        return this.roots;

    }
}
