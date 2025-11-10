# GPA Calculator

## Overview

This Python program calculates a student's **Grade Point Average (GPA)** based on their numeric class grades.
It converts each grade into the standard **4.0 GPA scale**, then computes and displays the average.

---

## How It Works

1. The program greets the user and asks how many classes they are taking.
2. It validates that at least one class is entered.
3. For each class, the program:

   * Prompts the user to enter a numeric grade (0–100).
   * Checks for invalid inputs (non-numeric values or grades outside the valid range).
   * Converts the numeric grade to its corresponding GPA value using the following scale:

| Numeric Grade | GPA |
| ------------- | --- |
| 93–100        | 4.0 |
| 90–92         | 3.7 |
| 87–89         | 3.3 |
| 83–86         | 3.0 |
| 80–82         | 2.7 |
| 77–79         | 2.3 |
| 73–76         | 2.0 |
| 70–72         | 1.7 |
| 67–69         | 1.3 |
| 65–66         | 1.0 |
| Below 65      | 0.0 |

4. Once all grades are entered, it calculates the **average GPA** and prints the result.

---

## Example Run

```
Welcome to the GPA calculator!
How many classes are you taking? 3
What is your grade in class 1? 95
What is your grade in class 2? 88
What is your grade in class 3? 74
Your GPA is: 3.1
```

---

## Requirements

* Python 3.6 or higher

No external libraries are required; the program uses only built-in Python functions.

---

## Notes

* Input validation prevents non-numeric or out-of-range grades.
* The GPA output is a **numeric average** on a 4.0 scale (not letter-based).
* To modify the grading scale (for example, to include weighting or different GPA cutoffs), edit the `convert()` function.

---

## How to Run

1. Save the program as `gpa_calculator.py`.
2. Open a terminal or command prompt.
3. Run the following command:

   ```
   python gpa_calculator.py
   ```
4. Follow the prompts to enter your grades.
