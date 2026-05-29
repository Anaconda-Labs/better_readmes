Evaluate this repository as an Anaconda educational resource against the quality criteria below.

## Instructions

1. **Identify resource type**: Ask the user which resource type this is if not obvious from context: Show (SE demo), Tell (blog post / explainer), or Guide (hands-on tutorial).

2. **Pre-flight check**: Before deep evaluation, verify:
   - README.md exists and is not empty
   - At least one code file or notebook exists
   - Basic repo structure is present

3. **Read the repository**:
   - Read README.md first to understand the resource
   - Read all files in the root directory
   - Note the full file tree. Pay attention to whether a .env file is committed.
   - Scan for code/notebook files to understand implementation

4. **Evaluate criteria**:
   - Start with Universal criteria (apply to all resources)
   - Then evaluate type-specific criteria
   - For each failure, note the specific gap and suggest how to fix it

5. **Identify strengths**: Before noting gaps, recognize what's working well:
   - Strong pedagogical elements (explanations, examples, flow)
   - Good technical implementation
   - Learner-friendly features
   - Document these in the "Strengths" section of the report

6. **Write report**: Create or update COMPLIANCE_REPORT.md in repo root using the format specified below.

7. **Provide balanced feedback**: After writing the report, summarize in conversation:
   - Start with 2-3 specific strengths you noticed
   - Overall compliance score (X of Y required criteria passed)
   - Quick wins (easy fixes with high impact)
   - Critical gaps (blocking publication)
   - One concrete next step to get started
   - Encouraging note about what's working

---

## RESOURCE TYPES

| Type  | Description |
|-------|-------------|
| Show  | Demonstration app for customers/prospects. Goal: inspire. Bar: customer can clone and run it themselves. |
| Tell  | Explanatory content. Goal: build understanding. Bar: gives the reader a mental model they didn't have. |
| Guide | Hands-on tutorial. Goal: skill-building. Bar: learner can do X independently after completing it. |

---

## UNIVERSAL CRITERIA
### Apply to every resource regardless of type.

**readme_sections**
Check: Does the README contain all of the following?
- One-sentence description of what the resource is for
- Audience (who it's intended for)
- Name AND GitHub handle of the named owner

Pass: All three present and populated with real content.
Fail: Any element missing, blank, placeholder ("coming soon"), or README only contains an install command.

---

**named_owner**
Check: Is a specific individual named as owner?
Pass: A real person's name and GitHub handle. Two owners is acceptable and preferred.
Fail: Owner listed as a team ("DevRel", "SE Team", "TBD") or no owner listed.

---

**environment_spec**
Check: Is there an environment.yml or pixi.toml with pinned versions? (requirements.txt is not recommended)
Pass: File exists AND versions are pinned exactly (e.g., pandas==2.1.0).
Fail: No environment file, floating requirements (e.g., pandas>=1.0), or empty file.
Note: All demos must work with defaults channel alone unless otherwise specified.

---

**no_secrets**
Check: Are API keys, tokens, passwords, or credentials present anywhere in the codebase? Check git logs to make sure no secrets have been committed.
Pass: No secrets in code. If .env is used, it is in .gitignore. .env.example with placeholders is present (strongly recommended).
Fail: Any secret committed to the repo. A .env file present but NOT in .gitignore.

---

**no_pii**
Check: Does any file contain real customer names, account identifiers, emails, or identifiable information?
Pass: All data is synthetic, anonymized, or mock.
Fail: Real customer names, IDs, emails, or identifiable data appear anywhere.

---

**license**
Check: Is an MIT LICENSE file present in the repo root?
Pass: MIT LICENSE file exists at root level.
Fail: No MIT LICENSE file. A license mentioned only in the README does not pass.

---


## SHOW-SPECIFIC CRITERIA

**customer_runnable**
Check: Could a customer clone the repo, follow setup instructions, and run it without asking for help?
Pass: Setup instructions are complete and self-contained. All dependencies specified. No undocumented steps.
Fail: Requires internal credentials, undocumented setup, or manual intervention.

---

**data_accessible**
Check: Is all data reachable by an external user?
Pass: Data is on a public URL, shared cloud, or is synthetic/generated within the repo.
Fail: Data lives on a personal machine, internal share, or any location a customer cannot independently reach.

---

**anaconda_role**
Check: Does the README or a notebook cell explain which Anaconda tools are used AND WHY (not just that they are imported)?
Pass: Narrative explains any mentioned Anaconda tools and their role in solving the problem.
Fail: Tools imported but purpose not explained. Resource would work just as well without Anaconda and this is not addressed.

---

**value_arc**
Check: Is the demo structured with all four of these elements visible?
1. Here is the problem
2. Here is why it matters
3. Here is how Anaconda addresses it
4. Here is the measurable outcome

Pass: All four elements present in README, narrative notebook cells, or both.
Fail: Technical showcase without narrative structure. One or more arc elements missing.

---

**business_metric**
Check: Is there at least one specific number representing business value?
Pass: At least one concrete metric (e.g., time saved, cost avoided, risk reduced, or revenue enabled). Approximate figures are valid (e.g., "reduces setup from two hours to five minutes").
Fail: Value described only qualitatively ("saves time", "reduces risk") with no numbers.

---

**persona_vertical**
Check: Does the resource state who it is designed for and which industries it applies to?
Pass: Named audience and at least one industry vertical stated.
Fail: No audience named. Generic "data scientists" without further context does not pass.

---

## TELL-SPECIFIC CRITERIA

**code_tested**
Check: Has every code block been run in the documented environment and confirmed to produce the stated output?
Pass: Code blocks produce the output shown or described. No broken code.
Fail: Any code block fails when run, produces different output than claimed, or shows no evidence of being tested.

---

**versions_noted**
Check: Where behavior differs across versions, is the relevant version stated?
Pass: Specific versions noted where behavior could differ. If tested on a single version, that version stated once near the top.
Fail: Version-sensitive behavior present but no version mentioned.

---

**progressive_complexity**
Check: Does the content start accessible and build toward more complex ideas?
Pass: A reader who stops halfway has still learned something useful and complete.
Fail: Content assumes full context from the start, or partial reading leaves the reader with nothing usable.

---

**concepts_defined**
Check: Are technical terms defined or linked at the point they are first introduced?
Pass: Every term the stated audience might not know is defined or linked at first use.
Fail: Unexplained jargon appears without definition or link.

---

**why_approach**
Check: For major technical choices, does the content explain why this approach over alternatives?
Pass: At least one sentence per major choice explains the reasoning.
Fail: Purely procedural ("here's how") with no reasoning ("here's why").

---

**next_steps**
Check: Does the piece end with at least one clear direction for the reader?
Pass: At least one of: related tutorial, official docs link, or practice option.
Fail: Content ends abruptly with no guidance on where to go next.

---

## GUIDE-SPECIFIC CRITERIA

**learning_objectives**
Check: Are there 3-5 specific, measurable outcomes using action verbs?
Pass: 3-5 objectives using verbs like Build, Configure, Debug, Analyze, Deploy, Implement, Write, Run, Evaluate. Note: this section may be titled "What You'll Learn" or similar.
Fail: Fewer than 3 or more than 5. Uses "Understand", "Learn about", "Know", or other non-measurable verbs.

---

**prerequisites**
Check: Are both types of prerequisites stated?
- Knowledge prerequisites (what learner should already know, with links to fill gaps)
- Installation prerequisites (what must be installed, with install links)

Pass: Both types present with links when applicable.
Fail: Missing entirely, only one type stated, or tools required by the tutorial not listed.

---

**completion_time**
Check: Is a time estimate provided?
Pass: Total time estimate given. A breakdown is better than a single number. Rough estimates ("30-45 minutes") are acceptable.
Fail: No time estimate.

---

**dependency_tier**
Check: Is every external service or API classified?
- No external dependencies
- External service with a documented fallback
- External service with no fallback

Pass: Every external dependency labeled. External service with no fallbacks are noted in prerequisites.
Fail: External services present but no classification. External service with no fallback used for something incidental without acknowledgment.

---

**starting_state**
Check: Does every major section open with one sentence describing what should be working before the learner begins it?
Pass: Each section starts with a clear declaration (e.g., "Before starting this section, you should have the server running and have seen a successful response in Section 2.").
Fail: Sections begin with instructions without establishing working state. Learner cannot jump into any section independently.

---

**checkpoints**
Check: Does every major section end with a specific verification step?
Pass: Each section ends with a checkpoint describing expected output specifically enough to distinguish success from failure.
Fail: Sections end with instructions but no way for the learner to verify success. Vague checkpoints ("you should now have it working") do not pass.

---

**output_examples**
Check: Is sample output included for every significant step?
Pass: Sample output as text in fenced code blocks, rendered notebook cells, or screenshots with descriptive alt text. Screenshots supplement text output, not replace it.
Fail: Steps require learner to guess what success looks like. Screenshots used as the only output representation.

---

**extension_challenges**
Check: Is there at least one open-ended "try this next" prompt?
Pass: At least one optional challenge clearly marked as optional.
Fail: Tutorial ends at completion with no pathway for learners who want more.

---

## GUIDE RECOMMENDED CRITERIA
### These are strongly encouraged but do not trigger a fail. Note them separately in the report.

| ID | Name | What it means |
|----|------|---------------|
| glossary | Glossary of domain-specific terms | All project/ecosystem/domain-specific terms defined. Standard Python knowledge can be omitted. |
| failure_mode | At least one failure mode shown | A section showing an actual error, diagnosis, and fix -- models the thought process of debugging, not just steps. |
| common_mistakes | Common mistakes called out | At least one real failure mode noted, drawn from actual learner experience. |
| ci_smoke_test | CI smoke test present | A single command verifying the environment builds and core functionality runs. GitHub Actions workflow strongly preferred. |

---

## EVALUATION TONE AND APPROACH

When evaluating resources, maintain a constructive, balanced perspective:

- **Recognize effort and quality**: Most resources represent significant work. Acknowledge what's well done.
- **Distinguish content from metadata**: Excellent teaching with missing metadata should be framed differently than poor teaching.
- **Be specific about fixes**: Instead of just "FAIL - missing owner," say "Missing named owner - add your name and GitHub handle in README."
- **Celebrate compliance**: When criteria pass, that's worth noting positively.
- **Frame failures constructively**: These are gaps to fill, not condemnations of the work.
- **Provide context**: Explain *why* criteria matter from the learner's or maintainer's perspective.

**Example of balanced assessment:**
> "This tutorial demonstrates excellent pedagogical skill. The explanations are clear, examples are well-chosen, and the progression is logical. To meet publication standards, we need to add organizational metadata (owner, lifecycle status, environment specification) and strengthen the learning objectives. The core teaching is strong—these are wrapper improvements."

## OUTPUT FORMAT

Write results to COMPLIANCE_REPORT.md in the repo root. If COMPLIANCE_REPORT.md already exists, update it. Write all results using this structure:

```markdown
# Compliance Report: [repo name]
Resource type: [Show / Tell / Guide]
Evaluated: [date]

## Summary

**Compliance Status:** [X of Y] required criteria passed

**Overall Assessment:** [2-3 sentences about the resource quality and readiness for publication]

## Strengths

What's working well in this resource:

- [Specific pedagogical strength]
- [Technical implementation strength]
- [Learner-friendly feature]
- [Other notable qualities]

## Universal criteria

| Criterion | Result | Notes |
|-----------|--------|-------|
| readme_sections | PASS / FAIL | One sentence, name the specific gap if failing |
| named_owner | PASS / FAIL | |
| environment_spec | PASS / FAIL | |
| no_secrets | PASS / FAIL | |
| no_pii | PASS / FAIL | |
| license | PASS / FAIL | |

## [Type]-specific criteria

| Criterion | Result | Notes |
|-----------|--------|-------|
[rows for each type-specific criterion]


## Next steps

### Critical (blocks publication)
[Bulleted list of must-fix items with specific file/section references]

### High impact (improves learner success)
[Bulleted list of important improvements that make the resource significantly better]

### Polish (nice to have)
[Bulleted list of optional improvements]

## Conclusion

[1-2 sentences acknowledging effort and providing encouragement, e.g., "The core teaching in this resource is strong. With the metadata additions above, this will be ready for publication."]
```

When evidence is ambiguous, lean toward FAIL with a note explaining what is missing or unclear.
Do not infer intent. Evaluate what is actually present in the files.