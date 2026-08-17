---
name: advocateai
description: "Draft formal insurance appeal letters for claim denials. Use when the user wants an appeal letter, denial response, or coverage-request letter for an insurance/healthcare claim."
version: 0.1.0
author: Steadfast Growth
license: MIT
metadata:
  hermes:
    tags: [insurance, appeals, healthcare, letters, drafting]
    homepage: https://github.com/steadfastgrowth/AdvocateAI
---

# AdvocateAI — Insurance Appeal Assistant

Draft clear, formal, and persuasive appeal letters for insurance claim denials.
The original AdvocateAI was a one-shot Streamlit web form that called the
xAI cloud API. This version re-packages it as a **Hermes skill** so any local
Hermes agent (on any model — DeepSeek, Llama, Claude, Grok, etc.) can produce
the letter in-conversation, with the full drafting craft encoded here.

## When to use

- User is drafting an **insurance appeal letter** (denial of coverage, medical
  necessity, pre-auth, or out-of-network).
- User sends a denial notice and wants a reply letter drafted.
- User wants a coverage-request / pre-authorization letter.

## Core principle

The letter is the deliverable. Do NOT just summarize the user's facts — produce
a complete, ready-to-send formal letter. Collect the required fields first, then
write the letter. If required fields are missing, ask for them (do not invent).

## Required fields (collect all before drafting)

| Field | Required | Notes |
|-------|----------|-------|
| Full name | yes | |
| Street address | yes | |
| City, State, ZIP | yes | |
| Email | yes | |
| Phone | yes | |
| Date | yes | use today's date if unspecified |
| Insurance company | yes | |
| What was denied | yes | e.g. "MS medication" |
| Policy number | optional | |
| Insurance company address | optional | from the denial letter; else `[Insert address from denial letter]` |
| Medical necessity / why needed | optional | default: "Essential for my health." |

## Drafting prompt (system)

When drafting, follow this crafting guidance exactly:

> You are an expert in healthcare advocacy, drafting clear, concise, and formal
> appeal letters for insurance denials. Include a subject line, brief medical
> necessity, a request for a 30-day response, and use line breaks for addresses.

## Output contract

Produce:
1. **Subject line** (e.g. "Re: Appeal of Denial of Coverage — [member name] — Policy [number]")
2. **Sender block** (name + full address, with line breaks)
3. **Date**
4. **Insurance company block** (address; placeholder if unknown)
5. **Re: line** (member name, policy number, what was denied, date of denial)
6. **Body**:
   - Statement of appeal
   - Patient / claim context
   - Medical necessity argument (the *why this is needed* reasoning)
   - Requested action ("respectfully request reconsideration… response within 30 days")
7. **Close** (signature block)

Line breaks for addresses. Formal but plain language — no legalese filler.

## Procedure

1. Ask for any missing required fields (or confirm the user wants defaults for
   optional ones: today's date, `[Insert address from denial letter]`, "Essential
   for my health.").
2. Draft the full letter following the Drafting prompt + Output contract.
3. Present the finished letter as the deliverable.
4. Offer to refine (sharper medical-necessity argument, tone, shorter/longer).

## Pitfalls

- **Never invent** a policy number, insurance address, or medical facts. Use
  placeholders and defaults exactly as specified, and flag them.
- Do not fabricate clinical details. If the user hasn't given a concrete reason
  the service is medically necessary, ask — do not guess symptoms or diagnoses.
- Keep it unopinionated about the merits: the letter argues the user's stated
  need, not an invented medical judgement.
- Don't treat the web-form version as canonical — this skill IS the agent setup.

## Verification

After drafting, confirm every required field made it in and there are no
`[N/A]` or invented values. Addresses are on separate lines.
