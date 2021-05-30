package com.lab2a;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import com.lab2a.activity.LabActivityInflater;


public class LabActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LabActivityInflater.inflate(this);

    }

}
