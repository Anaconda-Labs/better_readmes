# Tidewatch

**A tiny Python library for fetching and tidying NOAA tide predictions into a clean DataFrame.**

> **Note on this file.** This is a sample README for a fictional project. The quoted notes like this one explain *why* each part is written the way it is. When you adapt this file, delete the notes and keep the structure.

Tidewatch turns NOAA's tide prediction API into one function that returns a tidy, well-typed table. It handles the date math, the station lookup, and the unit conversions so you do not have to.

> **Why open this way.** A reader knows what this is and why they would care in two sentences, before any badge or install block. This is the cognitive funnel: broadest first.

```python
from tidewatch import predictions

df = predictions(station="8443970", days=3)  # Boston, MA
print(df.head())
```

> **Why an example this early.** The fastest way to let someone evaluate a tool is to show them what using it looks like. One small block that produces real output earns more trust than a paragraph of description.

## Why Tidewatch exists

NOAA publishes excellent tide data, but the raw API returns nested JSON with awkward timestamps and station codes most people have to look up by hand. Existing wrappers either pull in heavy dependencies or stop at the raw response. Tidewatch does one narrow thing well: clean data, minimal dependencies, no surprises.

> **Why this section is not optional.** This is the hardest part to write and the most important. It states what problem the project solves and, just as usefully, where it stops. Naming what a tool is *not* for is how you respect a reader's time.

## Install

```bash
pip install tidewatch
```

Requires Python 3.10 or newer. The only runtime dependency is `pandas`.

> **Why state the version and the dependency.** This is the single most common source of "it does not work on my machine." Saying it once, near the top, prevents most of those reports.

## Usage

Fetch predictions for a station by ID:

```python
from tidewatch import predictions

df = predictions(station="9414290", days=7)  # San Francisco, CA
```

Look up a station ID by name if you do not have one:

```python
from tidewatch import find_station

find_station("Boston")  # returns matching stations and their IDs
```

The returned DataFrame has three columns: `time` (timezone-aware), `height_m`, and `type` (high or low). Heights are in meters by default; pass `units="ft"` for feet.

> **Why describe the output shape in words.** A screenshot of a DataFrame goes stale and is invisible to a screen reader. Describing the columns in text is durable and accessible. Use screenshots to supplement, never to replace, text.

## Contributing

New contributors are genuinely welcome here, including for documentation, examples, and bug reports, not only code.

The friendliest place to start is an issue labeled [`good first issue`](https://github.com/example/tidewatch/labels/good%20first%20issue). Pick one, say hello on it, and we will help you get set up. Full setup steps and our expectations are in [CONTRIBUTING.md](CONTRIBUTING.md), and everyone here agrees to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

> **Why this paragraph carries the most weight.** It says hello, it names that non-code work counts, it offers one obvious small first step, and it points to the contributing file and code of conduct. This is where a curious visitor decides whether to become a contributor.

## License

[MIT](LICENSE). Use it freely.

> **Why the license is here at all.** A project with no license is not open source, and a contributor who cannot find one cannot be sure their work stands on solid ground.
