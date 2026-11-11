# Lab 7 - Fuzz Testing

This folder applies Hypothesis fuzz testing to the same three tennis scoring functions used for Lab 6.
The functions are kept in `processor.py` to match the Lab 7 handout.

## Run it

Install the dependencies:

```powershell
py -m pip install -r requirements.txt
```

Run the application demonstration:

```powershell
py processor.py
```

Run the Hypothesis tests:

```powershell
py -m pytest -q test_processor.py
```

The final test run passes all 10 tests. The screenshots folder contains the starting application run,
a minimized fuzz failure from the uncorrected version, the corrected application run, and the final passing run.
