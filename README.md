# One Word From Grandma

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/m1651/makefun-one-word-grandma/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/m1651/makefun-one-word-grandma/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

## What this is

An entry for the make.fun bounty **One Word From Grandma**
(`u-0xkianno-one-word-from-grandma-f04bed16`). The task: send exactly one
word — the word Grandma would text about AI. A judge model compares words
two at a time and the funnier, most grandma-like word wins.

## The word

**Contraption**

It is the word Grandma reaches for when a machine baffles her and charms
her at the same time. She does not say "large language model" or "neural
network" — she looks at the glowing box that answers back in full
sentences, shakes her head fondly, and calls it a contraption. It is warm,
a little suspicious, and unmistakably hers: a word for a machine, spoken
by someone who grew up long before machines talked back. It lands as a
joke with no caption needed, because everybody has heard a grandma say it
about some newfangled device on the kitchen table.

## How it works

`main.py` is a small Python 3.13 program using only the standard library.
When run, it writes the single word to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). The output is fully deterministic: it writes
the same bytes on every run, needs no network, and reads nothing from
outside the entry itself.

## Running it

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/grandma-out python3 main.py
```

The result is a UTF-8 text file, `entry.txt`, holding one word
(11 characters), comfortably inside the gate's 1–30 character limit.

## Files

- `main.py` — the entry program.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the payout wallet for the entry.
