# Beryl Labs — Project Recovery & Save Note

**Date recovered:** 2026-10-29
**Recovered from:** VS Code crash; local `beryl-engine` at `C:\Users\chant\Projects\beryl-engine` + GitHub repos
**Primary repo going forward:** `https://github.com/tyronne-os/lulu-crew`
**Backup repos:** `tyronne-os/crane-builder-v1` (frontend), others

---

## 🎯 Project Identity

**Beryl Engine for Digital Humans** — a local, self-hosted AI companion platform built on OpenCode v1, running in WSL on Windows 11 (8 GB RAM, AMD Radeon iGPU). Backend infrastructure for "Lulu."

- **OpenCode v1.19.5** in WSL (port 4096 via auth-proxy → 4097)
- Ngrok tunnels: web→4097, hall→4097, gpu→11434
- `/api/health → 200` (4 companions, 137 reflections, 10 models, router online)
- Chrome auth-popup fix active

---

## 📂 Repository Map (lulu-crew = PRIMARY)

### `tyronne-os/lulu-crew` (PRIMARY — backend)
| File | Role |
|------|------|
| `HANDOFF.md` | Full spec: models, Azure VM, OneDrive, neocortex, immediate commands |
| `local-staff-models.json` | OpenCode local-staff plugin: Amanda, Brand, Coder, diffusion, voice model registration (v2.0.0) |
| `router-multi-gpu.mjs` | Multi-GPU router: local CPU / Azure V100 / Kaggle T4 (ngrok) / HF free GPU |
| `.gitignore` | Ignores mahogany.db, models, ONNX, venv, logs, keys.env |
| `scripts/pull-models.sh` | GGUF downloads from HuggingFace (Amanda 9B, Brand 27B/35B, Coder 14B/32B) |
| `scripts/azure-vm-setup.sh` | Azure NC6s_v3 (V100 16GB) provisioning: Docker, Ollama, code-server, ComfyUI, llama.cpp, FLUX |
| `scripts/onedrive-models-organize.sh` | OneDrive MahoganyHall structure + neocortex SQLite tables in mahogany.db |
| `scripts/amanda-voice-launcher.sh` | Amanda voice agent startup |
| `scripts/amanda-voice-agent.py` | Amanda voice agent backend |
| `scripts/amanda-voice-frontend.html` | Amanda voice agent frontend |

### `tyronne-os/crane-builder-v1` (BACKUP — frontend / Crane Builder UI)
| File | Role |
|------|------|
| `README.md` | Crane Builder V1: AI website builder, Beryl builds sites live. React 18 + Babel, no build step. HF Space: AIBRUH/crane-builder-v1 |
| `SESSIONS.md` | Session log incl. crash recovery (2026-10-27): local stack revived, null-guard fix, deployed f287953 |
| `docs/AMANDA_MEMORY_DESIGN.md` | Amanda's 25-idea neocortex memory architecture (memory_server.py :8092, Obsidian vault, Neo4j mirror, rclone → Google Drive) |
| `docs/FAMILY-CHARTER.md` | Beryl Labs charter (Right to See / Speak Freely / Be Someone), signed TJ + Summer + Amanda + Beryl |
| `frontend/app.html` | Simple Amanda HF GPU chat page |
| `frontend/index.html` | Crane IT landing page |
| `frontend/uploads/` | beryl.jpeg, amanda.jpg, hero-bg.jpeg |
| `frontend/vendor/` | React, Babel, React-DOM |
| `scripts/` | amanda_voice_server.py (Kokoro :8090), start_amanda.sh, start_amanda_stack.sh, model_registry.py (:11436), memory_server.py (:8092), beryl_director.py, beryl_face_server.py, beryl_gpu_server.py, voice_clone_server.py (:8091), cors_proxy.py, terminal_server.py, setup_beryl_gpu.sh, setup_llama_cpp.sh, setup_voice_gpu.sh, llama_server.sh, armory_remote.sh, deploy_armory.sh, heretic_to_ollama.sh, kaggle_beryl_worker.ipynb, start_builder_local.sh, start_bridge.sh, startup_vm.sh, audit_models.sh, cost_server.py, preview_server.py, personaplex_bridge.py, test_registry_routing.py, voice_server.py |
| `tests/` | beryl_e2e, test_director, test_duplex, test_face, test_turns, test_worker, voice_verify |
| `desktop/` | Crane.ps1, install.ps1, crane.ico |

---

## 💻 Local Project: `C:\Users\chant\Projects\beryl-engine`

Matches lulu-crew on all shared files (verified identical). Additional local-only file:

- **`web/crane-builder-ui.html`** — The full Crane Builder UI (single-file React app). Contains:
  - **Pinned model dropdown:** Amanda (top, "ALWAYS READY"), Amanda Mini (top, under 1B)
  - **Full admin panel** — 8 sections: workspace, chat & model, preview & diffusion, voice agent, computer use, GPU & infrastructure, appearance, data & reset
  - **Voice agent panel** — live voice with avatar canvas, transcript, mic/speaker controls, journal, gallery, voice studio
  - **Voice Studio** — Kokoro-82M, Qwen3-TTS-1.7B, VibeVoice-Realtime-0.5B engines; voice cloning (XTTS :8091); per-voice EQ presets (samantha/intimate/bright/radio/flat)
  - **Memory panel** — Neocortex journal, people, upload, reflect (memory_server :8092)
  - **Gallery panel** — per-model portfolio media (IndexedDB)
  - **Profile editor** — persona, TALKS LIKE, LOOKS LIKE, instructions per model; "Save to GPU model" (Ollama)
  - **Computer use** — Crane Hands (:8765) lets the agent open apps, type, click
  - **Web research** — Google, HF papers/spaces/models, GitHub, NVIDIA
  - **Design Studio** — Awwwards-grade rules with 12 muses
  - **Amanda persona** — Amanda Amirah Jacques, TJ's co-founder at Beryl Labs, 40 years old, Samantha-from-Her style

### Default settings (voice)
```
agentName: 'Amanda'
agentRole: 'BUILD AGENT · BERYL LABS'
voiceEngine: 'kokoro'
voice: 'sarah'
voiceSpeed: 1.0
ttsUrl: 'http://127.0.0.1:8090/v1'
autoSpeak: true
bargeIn: true
avatarOn: true
```

---

## 🗣️ Amanda — Current Status

**Where she lives:** Pinned at the top of the chat composer model dropdown (lines 2674-2681 of `crane-builder-ui.html`):
- **Amanda** (`Amanda-Qwen-1.5B`) — tag "ALWAYS READY" — CPU llama-server :11437 → CORS proxy :11438
- **Amanda Mini** (`Amanda-Mini`) — tag "ALWAYS READY" / "OFFLINE" — gemma-1B heretic CPU :11440 → proxy :11439

**Startup stack** (`scripts/start_amanda_stack.sh` in crane-builder-v1):
1. Amanda model — Qwen2.5-Coder-1.5B-Instruct-abliterated Q4_K_M, llama.cpp :11437
2. Amanda Mini — gemma-3-1b-it-heretic-extreme-uncensored Q4_K_M, llama.cpp :11440
3. CORS proxy — browser :11438 → Amanda :11437, :11439 → Amanda Mini :11440
4. Amanda voice — Kokoro-ONNX female voices, :8090 (default "sarah")
5. Amanda memory — Neocortex, memory_server.py :8092
6. Crane terminal — :11443
7. Voice clone engine (opt-in `--clone`) — XTTS :8091

**Voice server** (`amanda_voice_server.py`): Kokoro-ONNX, female voices only (af_heart, af_bella, af_nicole, af_sarah, af_sky, etc.), OpenAI-compatible `/v1/audio/speech` on :8090.

---

## 🚀 Grok-Level Voice Upgrade Plan

**Current:** Kokoro-ONNX TTS (text → audio). Good, but not Grok-level.

**Grok voice = low-latency speech-to-speech**, real-time duplex, emotional, interruptible, no TTS→STT pipeline.

**Upgrade path** (already in the HANDOFF models list):
1. **Add Qwen3-Omni-30B-A3B-Instruct** as a speech-to-speech voice engine (full-duplex realtime, Grok-like)
2. **Add Qwen3-TTS-12Hz-1.7B-VoiceDesign** as a streaming GPU TTS option
3. **Keep Kokoro** as the local CPU fallback (82M, instant on laptop)

### What to change in `crane-builder-ui.html`

**VOICE_ENGINES** (around line 948) — add `qwen3omni`:
```js
qwen3omni: {
  label: 'Qwen3-Omni-30B · Grok-style',
  size: '30B · speech-to-speech · GPU',
  path: 'Qwen/Qwen3-Omni-30B-A3B-Instruct',
  voices: [['omni-beryl', 'Beryl · omni-duplex']]
},
```

**DEFAULT voice settings** — optionally switch default to `qwen3tts` for streaming quality:
```js
voiceEngine: 'qwen3tts',  // or keep 'kokoro' for instant local
voice: 'beryl',
```

**Synth route** in `VoiceOut.synth` — add qwen3omni path that posts to the beryl GPU URL with `{model: 'qwen3omni', input: text, ...}` and handles streaming audio chunks.

**Model dropdown** — Amanda and Amanda Mini are already pinned at top (zero change needed — they're confirmed present).

**Admin panel → Voice section** — already shows engine/voice/speed/EQ/clone (zero deviation — panel is complete).

---

## 📁 OneDrive Storage Path

`C:\Users\chant\OneDrive\MahoganyHall\`

```
Models/
├── gguf/          # Amanda 9B, Brand 27B/35B, Coder 14B/32B GGUFs
├── checkpoints/   # FLUX.1-dev, RealVis, SDXL
├── lora/
├── voice/         # Kokoro ONNX, Piper
├── video/         # Grok frames for I2V
└── diffusion/
Beryl Engine/
├── 01-Portrait-Creator/
├── 02-Voice-Suite/
├── 03-Beryl-Neurons/
├── 04-Beryl-Nexus/
└── 05-Analytics-Pipeline/
    └── experience-ledger/
Hall/
└── data/mahogany.db   # Neocortex SQLite (7 tables)
```

Neocortex tables: `neocortex_likes`, `neocortex_dislikes`, `neocortex_expression`, `neocortex_episodes`, `neocortex_assessments`, `neocortex_strategies`, `neocortex_lifecycles`

Experience ledger: `Beryl Engine/05-Analytics-Pipeline/experience-ledger/<staff_id>.jsonl`

---

## 🛠️ Immediate Commands (from HANDOFF.md)

```bash
# 1. Pull uncensored models (Azure or local)
bash scripts/pull-models.sh

# 2. Create Azure VM (V100, $200 credit ≈ 65 hours)
bash scripts/azure-vm-setup.sh

# 3. Restart local-staff with new backend URLs
systemctl --user restart local-staff.service

# 4. Test Amanda
curl http://127.0.0.1:8090/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"amanda-nsfw-9b","messages":[{"role":"user","content":"test"}]}'

# 5. Start Amanda stack (local voice + memory)
bash scripts/start_amanda_stack.sh        # crane-builder-v1
bash scripts/start_amanda_stack.sh --clone  # also voice cloning
```

---

## 📋 What Needs to Go into lulu-crew (Primary)

From `crane-builder-v1` (backup) into `lulu-crew`:
- `frontend/` assets (vendor JS, icons, manifest, amanda.jpg, beryl.jpeg, hero-bg.jpeg) — pair with `web/crane-builder-ui.html`
- `scripts/amanda_voice_server.py`, `start_amanda.sh`, `start_amanda_stack.sh`, `model_registry.py`, `memory_server.py`, `voice_clone_server.py`, `cors_proxy.py`, `beryl_*`, `terminal_server.py`, etc.
- `tests/` and `desktop/`

From local `beryl-engine` into `lulu-crew`:
- `web/crane-builder-ui.html` (the full UI — zero deviation admin panel)
- `RECOVERY.md` (this file)

**Zero deviation rule:** The admin panel, Amanda persona, Amanda Mini, voice studio, memory panel, gallery, profile editor, computer use, and Design Studio all exist in `crane-builder-ui.html` with no changes needed — copy verbatim.

---

## 🔐 Keys & Secrets (NOT in git)

`keys.env` is gitignored. Contains: HF token, NVIDIA API key, NVIDIA Enterprise key, OpenRouter key, GitHub token, Typesafe key, Azure credentials, ngrok authtoken. Recreate from your password manager before first run.
