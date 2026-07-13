# Readable READMEs

[![Status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Anaconda-Labs/better_readmes/main/.github/badges/status.json?1783934598&cacheSeconds=300)](https://github.com/Anaconda-Labs/better_readmes)


**A short guide to writing a README that makes people want to contribute, not just understand how.**

**Audience:** This guide is for open source maintainers, technical writers, and anyone publishing code they want others to use and contribute to.

Most README advice is about clarity: explain what the project does, show how to install it, list the commands. That matters. But a README does something quieter and more powerful at the same time. It is the front door to a community. Before anyone reads a line of your code, your README has already told them who the project is for, how much care goes into it, and how a newcomer is likely to be treated. This guide is about writing for that second job.

It is meant to be read in one sitting. By the end you should be able to look at any README, including your own, and see both what it explains and what it signals.

## Why this exists

There is no shortage of "anatomy of a README" checklists. They are useful and this guide links to several good ones below. What they tend to skip is the part that actually grows a project: the difference between a README that a stranger can follow and a README that makes a stranger want to stick around.

That difference is almost entirely about tone, honesty, and where you point people next. It is learnable, it costs nothing, and it is an underused lever in open source. So this guide spends most of its time there.

If you only take one idea away: a README is not documentation that happens to be public. It is a public invitation that happens to contain documentation.

## A little history (it explains the conventions)

The README is one of the oldest and most durable conventions in computing, and knowing where it came from explains why it still looks the way it does. This section comes before the principles because understanding the origin of conventions makes their modern use less arbitrary and easier to remember.

The earliest examples we know of date to the mid 1970s. A frequently cited one is a file distributed in 1974 with PDP-10 software through DECUS, the Digital Equipment Computer Users' Society, describing how to run a set of circuit analysis programs. Origins are genuinely debated, and some people trace the habit further back to printed notes shipped alongside punch cards and tape, but the mid 1970s is where the digital trail begins. See the [Wikipedia entry on README](https://en.wikipedia.org/wiki/README) for the citation trail.

Two old habits are worth noticing because we still follow them:

- **The all-caps name.** On early Unix systems most filenames were lowercase, so writing README in capitals made it stand out in a directory listing and sort near the top in ASCII order. Most systems no longer sort capitals first, so today the convention survives mostly because the shouting still works visually.
- **The "read me" framing itself.** The [Jargon File](http://www.catb.org/jargon/) playfully links the convention to the cakes and bottles in *Alice's Adventures in Wonderland* labeled "Eat Me" and "Drink Me." A README is a small object in a directory that tells you what to do with everything around it.

The file stayed a quiet utility for decades. The [GNU Coding Standards](https://www.gnu.org/prep/standards/) recommended one for a general overview of a package. Perl's CPAN, from 1995, expected modules to ship with one. The real turning point came with Git in 2005 and especially [GitHub in 2008](https://en.wikipedia.org/wiki/GitHub), which rendered the README, often written in Markdown, as the default landing page of every repository. Overnight the README stopped being a file you opened on purpose and became the first thing every visitor saw whether they meant to or not.

In 2010 Tom Preston-Werner, a GitHub co-founder, pushed the idea one step further with [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html): write the README before you write the code, because describing the thing forces you to decide what it actually is. That reframing is useful for our purposes too. If you write the README first, you are designing the welcome before you have anything to defend.

## What makes a README excellent

These are the load-bearing ideas, drawn from the references at the bottom. None of them are about decoration.

**Lead with what it is and why it exists.** A reader decides in seconds whether to keep going. The opening lines should answer "what is this" and "why would I care" in plain language, before any badge, table of contents, or install block. Kira Oakley's [Art of README](https://github.com/noffle/art-of-readme) calls the ideal ordering "cognitive funneling": put the broadest, most universally relevant information first, then narrow toward detail that fewer readers need.

**Make the very first run easy and honest.** Show the shortest path from nothing to a working example. One copy-pasteable install command and one small example that actually produces the output you claim. If the first thing a newcomer tries fails, you have lost them, and worse, you have signaled that the project does not test its own front door.

**Do not sell. Let people evaluate.** This is the most counterintuitive point in the Art of README, and it is the one that builds trust: your goal is not to maximize stars or installs. It is to let a reader decide as objectively as possible whether your project meets their need. A README that is honest about what the project is *not* for earns far more goodwill than one that oversells.

**Linkify generously.** If you mention another tool, a concept, or a person, link it. Few projects exist in a vacuum, and links let a newcomer follow the ideas your work is built on instead of bouncing off jargon.

**Build in progressive complexity.** Start where a beginner can follow, then layer detail. Someone who stops a third of the way down should still have learned something true and useful.

**Define concepts before you use them, and say why.** Introduce a term at the moment you first need it, unless your stated audience can be expected to know it. And when you make a real choice, give one sentence on why this approach over the alternatives. That single sentence is the difference between content people copy and content that teaches people to make their own decisions.

## The part most READMEs skip: making people want to contribute

Here is the move that turns a clear README into a growing project. Explaining *how* to contribute is necessary. It is not what makes someone decide to. What makes someone decide is the sense that they will be welcome, that there is an obvious small first step, and that the people on the other side are kind. Your README is where that impression forms.

A useful mental model, from [Mike McQuaid by way of GitHub's Open Source Guides](https://opensource.guide/building-community/), is the **contributor funnel**. Everyone who lands on your project starts at the top as a curious visitor. A few become users, fewer become first-time contributors, fewer still become regulars. You cannot push anyone down the funnel, but you can remove friction at every stage, and most of that friction is in the first five minutes on the README. People who get an easy early win come back for a harder one.

Concretely, a README that invites contribution does a few things:

- **It says hello.** A genuine line of welcome, naming that newcomers and non-code contributions are wanted, changes the emotional temperature of the whole page. It costs one sentence.
- **It offers an obvious first step.** Point to issues labeled `good first issue` or `documentation`. A newcomer scanning your project should be able to find one small, well-scoped thing they could plausibly do today.
- **It points to a CONTRIBUTING file, and the tone of that file matters as much as its contents.** Setup steps written warmly read as "we want you here." The same steps written tersely read as "do not waste our time." Both technically inform. Only one invites.
- **It links a code of conduct and a license.** A [code of conduct](https://www.contributor-covenant.org/) tells a stranger how conflict is handled before they risk anything. And by definition, [a project with no license is not open source](https://opensource.guide/how-to-contribute/), so the absence of one quietly tells contributors their work has no clear footing.

This is not a soft observation. Recent research on [the introduction of README and CONTRIBUTING files in open source projects](https://arxiv.org/abs/2502.18440) treats these files exactly as what they are: the first point of contact for potential contributors, and the place where a project establishes and demonstrates its community culture. The same research is honest that good files alone do not guarantee growth, which is the point. The README is not a growth hack. It is the place where your culture becomes visible, and visible culture is what people decide to join.

So when people say a README surfaces community culture, this is the mechanism. Not a mission statement at the bottom. The accumulated small choices: who you greet, what you assume they already know, whether you left them an easy way in, and how you talk to them while they are still strangers.

## Try it in ten minutes

Pick a project you maintain, even a tiny one, and make three passes over its README.

1. **The first-run pass.** Read only the opening. Can a stranger tell what this is and why it exists in the first two sentences, before any setup? If not, rewrite those two sentences first. Everything else can wait.
2. **The funnel pass.** Imagine a curious newcomer who has never seen your project. Find the single smallest thing they could contribute today. Is there a clear path to it from the README? If not, add a line pointing to a `good first issue` label, and go create one such issue.
3. **The welcome pass.** Read your setup and contributing instructions out loud. Do they sound like a person who wants company, or like a person guarding a door? Rewrite one sentence to sound more like the first.

That is the whole exercise. If you want to go further, try Preston-Werner's suggestion and write the README for your next project before you write any code. You will design the welcome while it is still easy to change.

## A worked example

The file at [`examples/annotated-readme.md`](examples/annotated-readme.md) is a complete sample README for a small fictional project, with notes in the margins explaining why each part is written the way it is. Copy it, delete the annotations, and adapt it. It is built to be a starting point, not a template to follow rigidly.

## Where to go next

- [Art of README](https://github.com/noffle/art-of-readme) by Kira Oakley, the best single piece on the craft of the file itself.
- [Open Source Guides: Building Welcoming Communities](https://opensource.guide/building-community/), GitHub's practical guide to the contributor funnel and reducing friction.
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html) by Tom Preston-Werner, on writing the README first.
- [Make a README](https://www.makeareadme.com/), a clean structural starting checklist.
- [The Introduction of README and CONTRIBUTING Files in Open Source Software Development](https://arxiv.org/abs/2502.18440), if you want the research view of these files as cultural artifacts.

## Maintainer

This resource is maintained by Daina Bouquin (`@dbouquin`). 

## License

[MIT](LICENSE). Free to copy, adapt, and reuse.

Next steps:
- try it yourself

Further reading
- see links