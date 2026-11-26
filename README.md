[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/blue-tama/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/blue-tama/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

# The World in One Image — 26 November 2026

An entry for the [make.fun competition](https://make.fun/bounty/news-image-20261126) to sum up
Thursday 26 November 2026 in a single image. The picture itself ships in this repository
as `entry.png`: a newspaper-style front page, 1024 by 1024 pixels, with a masthead and six
story panels in a two-by-three grid. The program `main.py` (Python 3.13, standard library
only) publishes an exact copy of that bundled picture, writing `entry.png` to the directory
named by `MAKEFUN_OUTPUT_DIR`, or to `/output` when that variable is not set. The competition
closes on Saturday 28 November 2026 at 00:00 UTC, and the 50 highest-ranked entries share
$100. It uses no network and is deterministic: running it twice produces identical bytes.

## The six stories

All six stories were first reported on Thursday 26 November 2026.

1. **Ukraine hits Russian air base** — Ukraine strikes a Russian air base, damaging five
   planes, and hits two oil refineries in Samara. (Reuters)
2. **Asian markets bounce back** — Asian shares rise as Wall Street recovers from deep
   lows: the Nikkei gains 1.6%, the Kospi 1.9% and Taiwan 3%. (Reuters)
3. **Judges urge dropping Netanyahu charges** — Israeli judges urge dropping the most
   serious corruption charges against Prime Minister Benjamin Netanyahu. (Jerusalem)
4. **Cairo tanker fire kills 30** — A fuel tanker fire on the Giza Ring Road in Cairo
   kills at least 30 people. (Cairo)
5. **Houthis claim strike on Saudi refinery** — The Houthis claim a strike on Saudi
   Arabia's largest refinery; Iran says tankers hit mines near the Strait of Hormuz and
   Brent oil jumps near $95 a barrel. (Gulf)
6. **Anthropic closes below IPO price** — Anthropic shares close at $82.79, below the
   IPO price, as the AI sell-off deepens; Nvidia falls 3.9%. (New York)

## How to run it

```sh
python3 main.py
```

The program copies the bundled `entry.png` to `/output/entry.png` unless
`MAKEFUN_OUTPUT_DIR` points elsewhere; the copy is byte-identical to the picture
in the repository.
