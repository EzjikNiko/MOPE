package com.lab1.utils.exception;

import androidx.annotation.NonNull;

import java.io.PrintStream;


public class TimeExceededException extends Exception {

    @Override
    public void printStackTrace(@NonNull PrintStream s) {

        super.printStackTrace(s);

    }

}
