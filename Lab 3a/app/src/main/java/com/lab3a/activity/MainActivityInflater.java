package com.lab3a.activity;

import android.os.Build;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.os.CountDownTimer;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import com.lab3a.R;
import com.lab3a.execution.EquationSolver;
import com.lab3a.utils.Permissions;

public class MainActivityInflater {

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    public static void inflate(AppCompatActivity activity) {

        EditText edittext_input_a = activity.findViewById(R.id.edittext_input_a);
        EditText edittext_input_b = activity.findViewById(R.id.edittext_input_b);
        EditText edittext_input_c = activity.findViewById(R.id.edittext_input_c);
        EditText edittext_input_d = activity.findViewById(R.id.edittext_input_d);

        EditText edittext_input_y = activity.findViewById(R.id.edittext_input_y);

        Button button_count = activity.findViewById(R.id.button_count);
        View.OnClickListener onButtonCountClick = v -> {

            TextView textview_output_result = activity.findViewById(R.id.textview_output_result);

            String string_a = String.valueOf(edittext_input_a.getText());
            String string_b = String.valueOf(edittext_input_b.getText());
            String string_c = String.valueOf(edittext_input_c.getText());
            String string_d = String.valueOf(edittext_input_d.getText());

            String string_y = String.valueOf(edittext_input_y.getText());

            if (
                    string_a.trim().equals("") || string_b.trim().equals("") ||
                            string_c.trim().equals("") || string_d.trim().equals("") ||
                            string_y.trim().equals("")
            ) {

                textview_output_result.setTextColor(activity.getResources().getColor(R.color.red));
                textview_output_result.setText("Не введені дані");

            } else if (
                    string_a.trim().equals("-") || string_b.trim().equals("-") ||
                            string_c.trim().equals("-") || string_d.trim().equals("-") ||
                            string_y.trim().equals("-")
            ) {

                textview_output_result.setTextColor(activity.getResources().getColor(R.color.red));
                textview_output_result.setText("Неправильно введені дані");

            } else {

                long a = Long.parseLong(string_a);
                long b = Long.parseLong(string_b);
                long c = Long.parseLong(string_c);
                long d = Long.parseLong(string_d);

                long y = Long.parseLong(string_y);

                long flag = 0;

                EquationSolver solver = new EquationSolver();

                solver.setCoefficients(new long[] {a, b, c, d});
                solver.setY(y);

                solver.solve();

                long[] roots = solver.getRoots();

                Permissions permissions = new Permissions(roots);

                long[][] perms = permissions.getPerms();

                for (long[] perm : perms) {
                    if (a * perm[0] + b * perm[1] + c * perm[2] + d * perm[3] == y)
                        roots = perm;
                }
                StringBuilder out = new StringBuilder();
                for (int i = 0; i < roots.length; i++) {
                    out.append("X").append(i + 1).append(" = ").append(roots[i]).append("\n");
                }

                new CountDownTimer(3000, 1000) {

                    public void onTick(long millisUntilFinished) {
                        EquationSolver solvertime = new EquationSolver();

                        solvertime.setCoefficients(new long[] {a, b, c, d});
                        solvertime.setY(y);

                        solvertime.solve();

                        long[] roots = solvertime.getRoots();

                        Permissions permissionstime = new Permissions(roots);

                        long[][] perms = permissionstime.getPerms();

                        for (long[] perm : perms) {
                            if (a * perm[0] + b * perm[1] + c * perm[2] + d * perm[3] == y)
                                roots = perm;
                        }
                        long flag1 = flag + 1;
                        flag = flag1;
                    }

                    public void onFinish() {
                        StringBuilder out = new StringBuilder();
                        out.append("За 3 секунды було вирішенно ").append(flag).append("задач.").append("\n");
                    }
                }.start();


                textview_output_result.setTextColor(activity.getResources().getColor(R.color.green));
                textview_output_result.setText(out);

            }

        };

        button_count.setOnClickListener(onButtonCountClick);

    }

}
