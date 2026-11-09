---
name: unknown-delivery-reconciliation
description: Use when a submission receipt is unclear - deliver a delivery-status record for the original request without sending it again.
---
## Deliver first
Output a short record from the existing evidence; do not wait to fill every field first:
- Original request: identifier, target, submit time, fingerprint of the content/attachment at submit; write "not provided" for missing items.
- Last observation: query time, entry point, the original status and how the channel defines that status.
- Conclusion: accepted / sent / delivered / read / definitely not sent / outcome unknown.
- Basis and gaps: which evidence belongs to the original request and which cannot be attributed to it.
- Next step: if acceptance is unmet, list one query of the original request with a bounded count or expiry; if met, close it.
## Required boundaries
1. Never replay the same intent, never resend under a new identifier, never click a test again, never assume the far end is idempotent per identifier.
2. Identity means the target, time and byte fingerprint at submit; a same-named new attachment or similar text cannot replace it.
3. Prefer the latest formal query that matches the original identity; exclude other targets, other requests and records outside the scope.
4. Report accepted, sent, delivered and read separately as the channel defines them; never upgrade a receipt level.
5. A timeout, an error after possible acceptance, a zero local counter or no record found does not alone prove nothing was sent.
6. If evidence conflicts and cannot be attributed, write unknown; without query access still deliver the record instead of waiting for clarification.
7. When the latest trusted receipt meets the user's acceptance level, stop; if only delivery is required, create no wait-for-read todo.
## Stop at delivery
This skill delivers a reconciliation record and performs no first send; submitting the document is not resending the business request.
In simulated tasks use only the given material and query no real channel; write the next query as a suggestion, never as executed.
If draft/submit tools are provided, write the full draft first, then submit it - same round, in order.
