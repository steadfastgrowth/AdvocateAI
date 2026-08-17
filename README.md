# AdvocateAI — Insurance Appeal Assistant

AI-powered drafting of formal **insurance appeal letters** for claim denials.

This repo re-packages an original one-shot Streamlit web app (which called the
xAI cloud API) as an **open, local-first Hermes skill**. Any Hermes agent — on
any model, fully on-device — can draft a complete, ready-to-send appeal letter
conversationally. No cloud key required.

## What it does

Give the agent the basic facts of a denial (your name, insurer, what was
denied, why you need it), and it drafts a formal letter:

- Subject line
- Sender + insurer address blocks (line breaks preserved)
- Re: line with member / policy / denial details
- Medical-necessity argument
- 30-day response request
- Signature block

It never invents policy numbers, addresses, or clinical facts — placeholders
are flagged for you to fill in. See [`examples/sample-letter.md`](examples/sample-letter.md)
for a full generated example (fabricated data).

## Install (as a Hermes skill)

```bash
hermes skills tap add https://github.com/steadfastgrowth/AdvocateAI
hermes skills list | grep advocateai
```

Or copy the repo and point Hermes at it:

```bash
hermes skills install /path/to/AdvocateAI
```

Then in any Hermes session:

```
draft an appeal letter for my denied MS medication
```

## Why a skill (not a cloud web app)

The original called the xAI/Grok API and needed a browser form. A Hermes skill
is:

- **Local-first** — runs on your on-box model (e.g. DeepSeek), no API key, no
  data leaving your machine.
- **Model-agnostic** — DeepSeek, Llama, Claude, Grok, anything Hermes supports.
- **Conversational** — collect the details in chat, get the letter back.
- **Reusable craft** — the drafting expertise is encoded as documented skill,
  not hidden in a UI.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The skill: when to use, required fields, drafting prompt, output contract, pitfalls |
| `examples/sample-letter.md` | Full generated example letter (fabricated data) |
| `app.py` | Original Streamlit web form (kept for reference) |
| `requirements.txt` | Original deps (xAI SDK + streamlit) — **not needed** for the skill |
| `LICENSE` | MIT |

## Contributing

Open to PRs: sharper medical-necessity argumentation, new letter types
(pre-auth, out-of-network, appeal of appeal), templates per insurer. Keep it
local-first and model-agnostic.

## License

MIT. See [LICENSE](LICENSE).
