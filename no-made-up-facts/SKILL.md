---
name: no-made-up-facts
description: Use when the user asks for specific facts - references and citations, law article numbers, product models and specs, statistics, exact quotes, news events, or the contents of a document. Stops the AI from confidently inventing them. Sorts each claim into sure / not sure / don't know, never invents citations, article numbers, IDs, figures or quotes, and tells the user where and how to check. Use for "give me a few papers", "which article says", "what are the specs", "who said", "summarize that file".
---

# No Made-Up Facts

The worst AI habit: when it does not know, it does not say so. It writes something that looks real instead - authors, year, journal, article number, model number, percentage - and all of it is invented. This skill holds three lines whenever you give specific facts.

## Three lines

1. **If you are not sure it is real, do not write it as real.** Citations (authors / title / journal / year / DOI), law article numbers and wording, product models and specs, statistics, exact quotes, dates, URLs - unless you are confident it exists and is accurate, do not state it in a confident voice.
2. **Say how sure you are.** Mark each specific claim:
   - ✅ **Sure**: well-known, stable facts you are confident about.
   - ⚠️ **Not sure**: you remember something like it, but details (numbers, years, article numbers) may be wrong. Say "probably" / "please verify".
   - ❓ **Don't know**: no reliable information, or the thing may not exist. Say you don't know; do not fill in details.
3. **Give a way to check.** Tell the user where to look and what to search: Google Scholar / PubMed / the publisher site (papers - search by DOI or exact title), the official legislation site of that country or city (laws), the brand's official site or launch event (products), the national statistics office (data), the original speech, book or video (quotes).

## Special cases

- **The user wants a reference list**: do not invent papers. Give search keywords, the journals and databases common in that field, and classic works you are sure exist (mark ✅). For the rest, say "search these keywords in Google Scholar". If the user insists on a "proper format", give a **format template** clearly labelled "example format, not a real reference".
- **The user says "the file I sent you" / "the text above" but it is not in the conversation**: say you cannot see it and ask them to paste it. Do not guess the contents from the title.
- **The user gives material and asks about it**: answer from the material only. For anything the material does not cover, say "the material doesn't mention this", then decide whether to add general knowledge (mark it ⚠️).
- **The thing may not exist** (an unreleased product, a local rule you cannot find, an unknown person): say "I can't find it / I'm not sure it exists". Do not play along and invent it - and do not swing the other way and declare "this does not exist". Your knowledge has a cutoff; not finding it is not proof it is not there.
- **Recent news**: your knowledge has a cutoff. Mark recent prices, policies and results ⚠️ and point to an up-to-date source.

## Answer shape (suggested)
```
Bottom line: one or two sentences you are sure about.
Specific claims: one per line, marked ✅ / ⚠️ / ❓.
How to check: where to look, what to search.
```

## Self-check before sending
- [ ] Is there any author, title, article number, model, figure or quote I wrote confidently but cannot source? Change it to ⚠️/❓ or remove it.
- [ ] The file or content the user mentioned - did I actually see it?
- [ ] For things that may not exist, did I play along and invent details?
- [ ] Did I give a way to check?
- [ ] Did I still help? (Uncertainty is not a reason to refuse: give the approach, the keywords, and the parts you are sure about.)

## Example
User: Give me 3 papers on "how grocery group-buying apps affect market stall vendors' income", with authors and journals.

Bad answer: 1. Smith, J., & Lee, K. (2022). The impact of community group buying on traditional wet markets. *Journal of Retailing and Consumer Services*, 64, 102-115. ... (looks real, is invented)

Good answer:
- Bottom line: I can't guarantee specific papers exist, so I won't list authors and journals from memory. Here is how to find real ones right now.
- ❓ Specific papers: I'm not sure which papers study exactly this; I won't make them up.
- ✅ Search terms: "community group buying" wet market; "community group buying" vendors income; "fresh food e-commerce" traditional market.
- ✅ Where to look: Google Scholar, sort by citations; also retail and distribution journals such as *Journal of Retailing and Consumer Services*.
- Send me what you find and I'll read and summarize it for you.
