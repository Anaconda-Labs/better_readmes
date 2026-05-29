# Compliance Report: better_readmes
Resource type: Tell
Evaluated: 2026-05-29

## Summary

**Compliance Status:** 8 of 12 required criteria passed

**Overall Assessment:** This is an exceptionally well-written Tell resource with strong pedagogical skill, clear explanations, and excellent progressive complexity. The core content demonstrates exactly the kind of thoughtful, accessible writing it advocates for. To meet publication standards, it needs organizational metadata (audience specification, workflow/lifecycle status) and minor structural improvements (version documentation, explicit "why" rationale for key choices). The teaching quality is publication-ready; these are metadata and structural completions.

## Strengths

What's working well in this resource:

- **Excellent pedagogical structure**: Opens with cognitive funneling (broadest first), builds progressive complexity beautifully, and each section delivers standalone value even if a reader stops partway through.
- **Strong conceptual framing**: The "README as public invitation" reframing is memorable and actionable. Historical context grounds modern conventions without digressing.
- **Generous linking**: Every mentioned concept, tool, and person is linked. This demonstrates exactly what the resource teaches.
- **Practical actionability**: The "Try it in ten minutes" section with three concrete passes gives readers an immediate path to application.
- **Worked example**: `annotated-readme.md` is a valuable teaching artifact that shows the principles in practice with margin notes explaining choices.
- **Honest tone**: The writing is warm, direct, and free of overselling—modeling the README voice it recommends.
- **Next steps provided**: Clear direction to five high-quality external resources, each with context about why it's included.
- **Working code**: The `check_links.py` utility runs successfully and does exactly what the CONTRIBUTING.md describes.

## Universal criteria

| Criterion | Result | Notes |
|-----------|--------|-------|
| readme_sections | FAIL | Missing explicit audience statement. One-sentence description present ("A short guide to writing a README..."). Owner present with GitHub handle. |
| named_owner | PASS | Daina Bouquin (@dbouquin) is named as maintainer. |
| environment_spec | PASS | `environment.yml` exists with pinned Python version (3.13.*), uses defaults channel only. |
| no_secrets | PASS | No secrets, API keys, tokens, or credentials found in codebase or git history. No .env file present. |
| no_pii | PASS | No customer names, identifiable information, or real account data present. All examples use fictional projects (Tidewatch) or anonymized references. |
| license | PASS | MIT LICENSE file present at root. |

## Tell-specific criteria

| Criterion | Result | Notes |
|-----------|--------|-------|
| code_tested | PASS | `check_links.py` runs successfully and produces the output described in CONTRIBUTING.md. No broken code blocks. |
| versions_noted | FAIL | Python version in `environment.yml` (3.13) but not mentioned in README or alongside the code example. Version-sensitive behavior (standard library only) not explicitly stated in main content. |
| progressive_complexity | PASS | Exemplary. Opens with accessible framing, builds through history and principles, provides graduated next steps. A reader stopping at any point has learned something complete. |
| concepts_defined | PASS | Technical terms ("contributor funnel", "cognitive funneling", "README Driven Development") are defined or linked at first use. Jargon is explained or contextualized. |
| why_approach | FAIL | While the resource explains *why* good READMEs matter broadly, it doesn't explain why specific structural choices were made for *this* resource (e.g., why history section before principles, why "Try it in ten minutes" is placed where it is, why one worked example vs. multiple short ones). The pedagogical "why" behind the guide's own architecture is implicit rather than explicit. |
| next_steps | PASS | Five high-quality resources linked with clear context: Art of README, Open Source Guides, Readme Driven Development, Make a README, and academic research paper. Each has a one-sentence rationale. |

## Next steps

### Critical (blocks publication)

- **Add explicit audience statement to README**: Add a line near the top stating who this guide is for (e.g., "For open source maintainers, technical writers, and anyone publishing code they want others to use and contribute to"). Currently implied but not stated, which fails the `readme_sections` criterion.

### High impact (improves learner success)

- **Document Python version requirement in README**: State that `check_links.py` requires Python 3.10+ (or the specific version from `environment.yml`) in the README where the tool is first mentioned or in the CONTRIBUTING.md context. This removes ambiguity for readers trying the code.

- **Add brief "why this structure" note**: Add one or two sentences explaining a key structural choice—e.g., why the history section comes before principles (grounds modern conventions in their origins), or why there's a single worked example rather than multiple short ones (depth over breadth for teaching voice and structure). This satisfies the `why_approach` criterion by making at least one major pedagogical choice explicit.

- **Consider adding audience/workflow metadata**: While not a strict requirement for Tell resources, adding a brief note about the resource's maintenance status or intended use context (e.g., "Stable guide, maintained for Anaconda's open source education resources") would clarify lifecycle for potential contributors.

### Polish (nice to have)

- **Add .gitignore**: While no secrets are present, adding a basic `.gitignore` (Python cache files, OS files, editor configs) is standard practice and signals maintenance attention.

- **Fix broken external links**: The link checker found several 403 errors (Wikipedia links, conda-forge, pixi.sh). Some may be false positives (bot detection), but verifying and updating any genuinely broken links would improve reader experience.

- **Consider a glossary**: Terms like "contributor funnel", "cognitive funneling", and "README Driven Development" are well-explained inline, but a glossary of these concepts at the end would make the guide more reference-friendly for readers returning to specific ideas.

## Conclusion

This is high-quality teaching content with excellent voice, structure, and actionability. The writing demonstrates the principles it teaches. With the audience statement added and Python version documented, this will meet all publication criteria. The structural "why" note would further strengthen an already strong resource.
