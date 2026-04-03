# COP4533 Programming Assignment 3 - HVLCS

## Students

Jesus Lopez - 13285108

Christian Betancourt Dias - 30823881

## How to Run

### Run HVLCS (Main Program)

```bash
python3 src/main.py
```

### Input Format

**Then enter input in the following format:**

```text
k
letter value
letter value
...
stringA
stringB
```

### Example

```text
3
a 2
b 4
c 5
aacb
caab
```

### Output

```text
<maximum_value>
<one optimal subsequence>
```

### How to Run Question 1

From the project root directory:

**1. Generate input files:**

```bash
python -m src.question1.generate_input
```

**2. Run timing analysis:**

```bash
python -m src.question1.timing
```

**3. Plot results:**

```bash
python -m src.question1.plot_results
```

Output files (`timing_results.txt` and `runtime_plot.png`) will be saved to `src/question1/output/`.

## Questions

Answers to questions 2 and 3 are inside the `questions` folder.

Question 1 is answered within `src/question1` folder with each file's purpose described by their names (generating input files, timing runtime, plotting, etc).

Additionally, we have folders `input` and `output` which store input files, and the runtime plot with its raw data, respectively.
