# Demo Criteria

**Last updated:** 1 May 2026

See resources to support criteria adoption: https://github.com/Anaconda-Labs/criteria_checker

---

## Table of Contents

- [Introduction](#introduction)
  - [Why this document exists](#why-this-document-exists)
  - [How to use this document](#how-to-use-this-document)
- [The three types of resources this covers](#the-three-types-of-resources-this-covers)
  - [Show](#show)
  - [Tell](#tell)
  - [Guide](#guide)
- [Universal Baseline Criteria](#universal-baseline-criteria)
- [Additional Criteria](#additional-criteria)
  - [Show](#show-1)
  - [Tell](#tell-1)
  - [Guide](#guide-1)
- [Lifecycle Policy](#lifecycle-policy)
- [What Comes Next](#what-comes-next)

---

## Introduction

### Why this document exists

When someone finds content from Anaconda (e.g., a tutorial, a demo, a blog post) we want them to be able to trust it. That it works. That it's current. That someone is accountable for it. That it's honest about what it is and who it's for.

Right now we don't have a shared standard for what that looks like, which makes it hard to build that trust consistently. This document proposes a shared standard. It covers three types of content: Show, Tell, and Guide. It describes what each should look like when it's ready for an external audience.

The goal isn't to make publishing harder. It's to make what we publish worth finding.

### How to use this document

This is a reference for anyone creating or reviewing external-facing content at Anaconda. Use it to check whether something is ready to publish, to understand why a particular criterion exists, or to get a sense of what we're aiming for as a team.

---

## The three types of resources this covers

We create three meaningfully different kinds of educational content, and they should be held to different standards because they serve different purposes. The three types are:

### Show

Demonstration applications. These are typically built by Technical Enablement for use with customers and prospects. Their job is to inspire: to show a customer what's possible with Anaconda tools in a scenario relevant to their industry. A good Show resource makes a customer think "I could build this." The bar is that a customer should be able to clone the repo and run it themselves.

### Tell

Explanatory content (e.g., blog posts, explainers, concept guides). Their job is to build understanding: to answer "what is this?" and "why would I care?" A good Tell resource gives someone a mental model they didn't have before. These often live on the Anaconda blog.

### Guide

Hands-on tutorials. Their job is skill-building and to take someone from zero to being able to do a specific thing independently. A Guide resource makes the strongest promise to a learner: "follow this and you'll be able to do X" and therefore requires the most care before publication. These typically live in GitHub repos.

---

## Universal Baseline Criteria

These criteria apply to every resource before publication.

| Criteria | Description |
|---|---|
| Hosted in the Anaconda-Labs GitHub org | Content that lives on a personal GitHub account or a Google Drive is not a published resource, it's a draft. Everything we intend for external audiences needs to be represented in an official [Anaconda-Labs GitHub org](https://github.com/Anaconda-Labs). The [resource-registry](https://github.com/Anaconda-Labs/resource-registry) is used to manage Anaconda-Labs. This is the first step toward having a coherent, findable body of work. |
| README with required sections for the given resource type (i.e., show, tell, or guide) | A README that says "coming soon" or just has an install command does not pass. |
| Named owner confirmed | "DevRel" or "SE Team" is not an owner. A specific individual must be listed, and that person must have confirmed they accept responsibility for keeping the resource current. If someone leaves the company, the resource must be reassigned or flagged for review. **Two named owners are highly recommended.** |
| Environment specified | Anyone who wants to use the resource should be able to reproduce the environment that the author used. That means a `pyproject.toml`, `environment.yml`, or `pixi.toml` with pinned versions (not floating requirements like `pandas>=1.0`). Exact versions belong in the spec file. This is a fundamental requirement for reproducibility. All demos must work with access to defaults channel alone unless otherwise specified. Using `requirements.txt` is no longer recommended as a best practice. |
| No hardcoded secrets or credentials | API keys, tokens, and passwords must never be committed to a repo. They belong in environment variables or `.env` files, and `.env` must be listed in `.gitignore`. An `.env.example` with placeholder values is strongly recommended. |
| No customer data or PII | No real customer names, account identifiers, email addresses, or otherwise identifiable information should appear anywhere in the resource. Synthetic or anonymized data is fine. When in doubt, generate mock data rather than anonymize real data. You can also use publicly available datasets (e.g., [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets?tab=readme-ov-file#awesome-public-datasets)) |
| License declared | A `LICENSE` file must be present in the repo root. Use an MIT license and list Anaconda, Inc as the license holder. |
| Resource registered | An entry must exist in a shared registry (see: [Anaconda-Labs/resource-registry](https://github.com/Anaconda-Labs/resource-registry)) |

---

## Additional Criteria

### Show

Show resources have a specific job: help a customer see themselves using Anaconda tools (e.g., SE Demos).

| Criteria | Description |
|---|---|
| Customer-runnable end-to-end | An SE walking through a demo on their own laptop in a meeting is not the standard. A customer should be able to clone the repo, follow the setup instructions, and run it themselves without needing to ask for help. If it only works in an SE's hands, it is not finished. |
| Data accessible to all | All data used in the demo must be on a public URL, in a shared cloud, or synthetic/generated within the repo. It cannot live on a personal machine or internal share that a customer can't reach. |
| Anaconda's role made explicit | The README or a notebook cell must call out which Anaconda tools are being used and why (not just that they're imported). This is what makes a demo an Anaconda demo rather than a generic notebook. If the resource would work just as well without Anaconda, that needs to be addressed. |
| Discovery-to-value arc | The demo must be structured to tell a story: here is the problem, here is why it matters, here is how Anaconda addresses it, here is the measurable outcome. This structure needs to be visible in the README, in narrative notebook cells, or both. An SE should be able to walk a customer through this arc without additional coaching materials. |
| At least one quantified business value metric | A specific number: time saved, cost avoided, risk reduced, or revenue enabled. Even approximate figures ("reduces environment setup from two hours to five minutes") are valid and valuable. |
| Persona and industry vertical specified | The resource must state who it's designed for and which industries it applies to. A demo without a named audience is a tool, not a story. |

### Tell

Tell resources have more flexibility in format than the other types, but they still need to meet a bar that makes them worth reading (e.g., blogs with explanatory content).

| Criteria | Description |
|---|---|
| All code tested | Every code block must have been run by the author in the documented environment and must produce the stated output. Broken code in a blog post is more damaging than no code as it signals carelessness about the reader's time. |
| Versions noted where it matters | Where behavior differs across versions, the relevant version must be stated. If everything is tested on a specific version, say so once near the top. This prevents the most common reader complaint of "this doesn't work on my machine." |
| Progressive complexity | The content should start accessible and build. A reader who stops halfway through should still have learned something useful. |
| Concepts defined before use | Technical terms should be defined or linked at the point where they're first introduced. The exception is terminology the stated audience can reasonably be expected to know. |
| "Why this approach" included | Not just "here's how to do X" but "here's why this approach over the alternatives." Even one sentence per major choice is sufficient. This is what separates content that builds expertise from content that just gets copy-pasted. |
| Next steps provided | The piece should end with at least one clear direction: a related tutorial, official documentation, or a practice option. This is also an opportunity to link to our own Guide resources when relevant. |

### Guide

Tutorials make the strongest promise to a learner and require the most structure. The criteria here are more numerous, but none of them are arbitrary. Each one exists because its absence is a reliable way to frustrate or lose a learner.

| Criteria | Description |
|---|---|
| Learning objectives | 3–5 specific, measurable outcomes using action verbs: Build, Configure, Debug, Analyze, Deploy. Never "Understand" or "Learn about." If you can't describe what a learner will be able to *do*, the tutorial's scope hasn't been decided yet. |
| Prerequisites | Both what a learner should already know (with links to resources that fill gaps) and what they need to have installed (with installation links). |
| Estimated completion time | Even rough estimates are significantly better than nothing as they help learners decide whether to start now or come back later. |
| External dependencies must be declared | Tier 1 - no external dependencies. Tier 2 - external service with a documented fallback. Tier 3 - external service with no fallback. *Note: Tier 3 dependency is fine when the external service is the point of the tutorial. It's not acceptable for incidental dependencies. Tier 3 dependencies need to be noted in the Prerequisites.* |
| Starting-state declarations | Every major section opens with one sentence describing what a learner should have *working* before they begin. This allows a learner to jump into any section without reading everything before it. Example: "Before starting this section, you should have the server running and have seen a successful response to the checkpoint command in Section 3." |
| Checkpoints | Every major section ends with a specific verification step: "✅ At this point, you should see\..." The expected output must be described specifically enough to distinguish success from failure. Checkpoints are what make tutorials self-serviceable (without them, every failure could become a support request). |
| Output examples | Sample output must be included for every significant step, either as text in a fenced code block or as a screenshot *with descriptive alt text*. Screenshots should supplement text output, not replace it as screenshots go stale and are less accessible to screen readers. |
| Extension challenges | At least one open-ended "try this next" prompt in the tutorial. These are not required exercises. They are optional for learners who want to go deeper. |
| Glossary of domain-specific terms *(Recommended)* | All project-specific, ecosystem-specific, or domain-specific terms a learner might not know are defined. Standard Python knowledge can be omitted. |
| At least one failure mode shown *(Recommended)* | At least one section should show an actual error or failure and walk through diagnosing and fixing it. This is distinct from a "common mistakes" warning because it should model the actual thought process of debugging. This teaches judgment, not just steps. |
| Common mistakes called out *(Recommended)* | At least one real failure mode noted, ideally drawn from actual learner experience rather than hypothetical warnings. |
| CI smoke test present *(Recommended)* | A single command that verifies the environment builds and core functionality runs. Documented in README. GitHub Actions workflow that runs on PR strongly preferred. |

---

## Lifecycle Policy

The Anaconda-Labs GitHub org is only as useful as its content is trustworthy. The lifecycle policy is how we keep the body of work honest over time.

### Three statuses

#### Active

The resource has been tested end-to-end within the last 90 days, the named owner is a current employee, and there are no known broken dependencies. **This is the only status under which a resource should be actively promoted or linked from official channels.** README badge is set to Active in this state.

#### Needs Review

A badge change condition exists:

- The resource may be outdated
- The owner has changed (and DevRel has been notified)
- A dependency has broken (and DevRel has been notified)

A resource in this status is still visible but should not be actively recommended.

*If a Needs Review badge isn't resolved within 30 days, the resource moves to Archived.*

#### Archived

The resource is no longer maintained. It stays in the org for reference, but the README lifecycle badge will display "Archived". A new owner may volunteer to restore an Archived resource to Active after re-testing and resolving open issues.

### Who handles the lifecycle

The expectation is self-certification (via GitHub Actions) by owners at initial intake into [the registry](https://github.com/Anaconda-Labs/resource-registry) (indicated using a GitHub badge), with a review happening continuously via GitHub actions. Self-certification must be done every 90 days.
