---
name: resumable-handover
description: Use when pausing, switching shifts or handing off - deliver a resume point the next person can act on directly.
---
## Deliver first
Write a short resume document from the existing material; do not perform the remaining actions:
- Goal and current state: done / not done / paused / cancelled / outcome unknown.
- Finished items: result, where the evidence is and which version it covers; write "not provided" for missing fields.
- Remaining items: only the necessary actions, ordered by dependency; independent items come before waiting items.
- First action: verb + object + completion signal; if nothing can be done, name the specific event being waited on.
- If anything changed: the object, where the actual backup is and the restore trigger; write "none" when there is no backup.
## Required boundaries
1. A current explicit update overrides the matching old conclusion; keep other facts; do not re-confirm facts already settled.
2. Evidence covers only its version and scope; after a version change list only the affected gaps instead of re-checking everything.
3. Cancelled items are no longer open work; a paused item resumes only when its explicit resume condition is met.
4. When the original side effect is unknown, keep its identifier, target, time and content fingerprint, as far as available.
   The next step only queries the original request or waits a bounded time; do not resend; do not turn "unknown" into "not started".
5. Deliver without evidence: separate facts from gaps; never invent an entry point, backup, time or success record.
6. If all goals are already accepted, write "done, no next action" - add no optimization or duplicate verification.
## Stop at delivery
A finished handover document is not a finished business task; do not delay delivery to perfect the list.
If draft/submit tools are provided, read the needed material, write the full document and submit it - same round, in order.
