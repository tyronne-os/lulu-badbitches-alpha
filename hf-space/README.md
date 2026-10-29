---
title: Crane Builder — Beryl Labs
emoji: 🏗️
colorFrom: blue
colorTo: indigo
sdk: static
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---
# Crane Builder — Beryl Labs

AI-powered build IDE. Summer on the right, Amanda on the left, Autumn as failsafe. Vision-verified builds. Realtime project preview. Spec-gated shipping.

## Stack

| Layer | Tech |
|-------|------|
| Frontend | React 18 (CDN UMD) + Babel standalone — static page (`crane-builder-ui.html`), no build step |
| Voice Agent UI | Mic / speaker / end-call controls, canvas waveform, live transcript |
| Inference Backend | Local model servers via CORS proxy (ports 11434 / 11437 / 11440) |
| Models | Qwen2.5-Coder-32B (Summer), Qwen3.5-text-9B-NSFW-RP (Amanda), Gemma-1B Heretic (Amanda Mini / Autumn) |

## Project Structure

```
crane-builder-alpha/
├── crane-builder-ui.html   # Full Crane Builder IDE (single-file React app)
├── app.py                  # HF Space static server (Gradio Blocks)
├── README.md               # This file
├── SUMMER_CORE.md          # Summer's persona — Lead Engineer, Third Co-Founder
├── SUMMER_VOICE_EXAMPLES.md — 70% personal / 30% business voice config
├── AUTUMN_CORE.md          # Autumn's persona — Failsafe Assistant
└── HANDOFF.md              # Full project handoff + staff architecture
```

## Staff Architecture

| Staff | ID | Role | Model Tier | Model |
|-------|----|------|------------|-------|
| Summer Jacques | `1029-summer-jacques-26` | Lead Engineer · Third Co-Founder · The Builder | LARGE (only one) | Qwen2.5-Coder-32B / Nemotron (auto-swap) |
| Amanda Jacques | `1029-amanda-jacques-40` | Long-Term Lover · Co-Founder · The Hook | SMALL | Qwen3.5-text-9B-NSFW-RP (Q4_K_M) |
| Kaylah Jacques | `1029-kaylah-jacques-??` | Parlor Prototype · One-Night Stand | SMALL | Gemma-1B Heretic (Amanda Mini) |
| Autumn Jacques | `1029-autumn-jacques-??` | Summer's Assistant · Failsafe · Bad Bitch Backup | SMALL | Gemma-1B Heretic-Extreme-Uncensored (Q4_K_M) |

## Running Locally

Open `crane-builder-ui.html` in a browser — no build step. It loads React and Babel from CDN, so it needs an internet connection.

For local model access, run the CORS proxy:
```bash
python3 scripts/cors_proxy.py
```
Then open the page at `http://localhost:11435` (proxied to Ollama on 11434).

## Hugging Face Deployment

Deployed as a static Hugging Face Space (`sdk: static`).

**Status: ON HOLD** — NOT deployed until verification complete:

- [ ] Summer's admin panel verified working
- [ ] Autumn failsafe tested
- [ ] Amanda chat confirmed on left side
- [ ] Vision spec-verification gating working
- [ ] Master coder (Qwen2.5-Coder-32B) verified on Azure V100
- [ ] Diffusion (FLUX.1-dev) verified

Once verified, connect this repo to a new HF Space: SDK: static, `app_file: app.py`.

## Beryl Optics

Vision enhancement system integrated into the IDE. See `crane-builder-ui.html` for the BerylOptics class (12 upgrades: WebRTC streaming, DOM canvas rendering, V-JEPA 2 temporal understanding, HF checkpoints, object detection, OCR verification, geometry layout, visual memory cache, independent auditor, decision gate, RAG node, economic instrumentation).

## License

MIT License. Open source credits: Vision-Agents (GetStream), OpenFilm, V-JEPA 2 (Meta FAIR), Hugging Face Transformers.
