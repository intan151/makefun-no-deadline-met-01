# One Line, No Deadline Met

[![make.fun](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/intan151/makefun-no-deadline-met-01/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/intan151/makefun-no-deadline-met-01/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)

Entry for the [One Line, No Deadline Met](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one funny single-line excuse for a missed deadline to
`/output/entry.txt`:

> I missed the deadline because my calendar quietly moved it to 'someday' and my to-do list believed it — I was the last to know.

The line is 127 characters, a single line — inside the gate of 1–200
characters from `RULES.txt`. A built-in self-check asserts the output
equals the intended entry, stays within the gate, and is a single line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
