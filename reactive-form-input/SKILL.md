---
name: reactive-form-input
description: Use when a form shows your text but the app state has not caught up - deliver a layered record of which inputs actually took effect.
---
## Deliver first
Write the record from the existing page and interaction evidence; do not submit the business form:
- Target field: label/accessible name, the form it belongs to, page version and expected format.
- Action and observation: input method, moment of observation, whether the displayed value matched (mask sensitive values).
- App signals: validation message, linked button or derived-field state, and where that evidence sits.
- Conclusion: effective / not effective / validating / unverified - list what is known and what is missing for each.
- Next step: one required observation or normal interaction, with a bounded completion signal; stop if effective.
## Required boundaries
1. Rule out hidden duplicates and same-named search boxes; confirm the field is visible and editable; record the reason if covered or disabled.
2. Prefer normal fill or keyboard input; state the clear behavior before replacing; keep required formats and units.
3. Never call it success after only changing DOM properties; keep the control limits and follow the normal validation flow.
4. Record the displayed value and the app-accepted signal separately; right value with unsynced validation is not effective.
5. Wait for business state, not just page load, within a time/attempt limit; do not judge final failure while async validation runs.
6. Blur only if the normal flow allows it; do not click final submit to test; do not use unproven event sequences.
7. Re-locate after navigation; never repeat actions on stale handles; keep format rejections as-is and do not silently change business values.
8. Deliver the record even without page access, marked unverified; in simulated material, never write suggested actions as performed.
9. If observing requires submission, state the limit and stop; for an unknown submission outcome, query the original request only - never replay.
## Stop at delivery
This skill does not click final submit; an effective input is not a submitted business request.
If draft/submit tools are provided, read the needed material, write the full record and submit it - same round, in order.
