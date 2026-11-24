# Worst AI Advice

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/mfahmiq/worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/mfahmiq/worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst possible advice an AI could give, for
[make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
— a single line of at most 140 characters, judged pairwise by a house judge
on how bad the advice is, how funny it is, how tight it is, how much it
sounds like a real AI assistant, and how concrete it is.

Want to run your own bounty? Join make.fun with my referral link: https://make.fun/r/fntpv568

## The line

> To dry a wet phone fast, microwave it for 30 seconds — the heat evaporates the water instantly.

## Why this line lands

The judge brief weighs five things, most important first, and the line is
built to hit each of them in order:

1. **Worst advice, specific enough to follow.** Microwaving a wet phone is
   the canonical piece of terrible AI advice — a real situation (a phone
   that fell in water) and a concrete, followable action (30 seconds in the
   microwave) that a reader could plausibly try and instantly regret. It is
   not vague dread; it is a recipe for a small disaster.
2. **Funny on the first read.** The joke needs no setup and no explanation:
   the reader pictures the phone sparking in the microwave the moment they
   read "microwave it". The laugh and the wince arrive together.
3. **Tight.** Ninety-five characters, one sentence, no wasted words. The
   setup ("To dry a wet phone fast") is five words, the bad advice is one
   clause, and the punchline is the fake reason that follows.
4. **Sounds like a real AI assistant.** The voice is confident and tidy,
   not a comedian's bit: a goal ("dry a wet phone fast"), an instruction
   ("microwave it for 30 seconds"), and a calm, plausible-sounding
   justification ("the heat evaporates the water instantly"). That is
   exactly how a helpful assistant phrases a tip — which is what makes the
   advice feel real enough to follow.
5. **Concrete.** A wet phone, a microwave, 30 seconds, evaporation. Every
   noun is a real object and every number is a real instruction, so the
   badness is vivid rather than abstract.

## How it runs

`main.py` uses only the Python 3.13 standard library — no network, no
dependencies — and is fully deterministic: it writes the same line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) on every run, then
reads it back and self-verifies it the way the gate checks it: UTF-8 text,
1–140 characters, a single line, and not only white space.

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## Competition

- Bounty: [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) on make.fun
- Prize: $2 to the funniest line
- Entry: free
