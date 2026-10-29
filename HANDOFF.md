# Beryl Engine – Handoff Document
# GENERATED: 2026-10-29 · Updated post-recovery · STATUS: PRE-DEPLOY · HUGGING FACE: ON HOLD (100% NOT DEPLOYED)

## Project Overview
Beryl Engine for Digital Humans – a local, self-hosted AI companion platform built on OpenCode v1, running in WSL on a Windows 11 laptop with 8 GB RAM / AMD Radeon iGPU. This is the backend infrastructure for "Lulu" and Beryl Labs.

## Current State
- **OpenCode v1.19.5** running in WSL (port 4096 via auth-proxy → 4097 upstream)
- **Ngrok tunnels**: web→4097, hall→4097, gpu→11434
- **/api/health → 200** (4 companions, 137 reflections, 10 models, router online)
- **Chrome auth-popup fix active** – no more sign-in popups
- **GitHub repo**: `https://github.com/tyronne-os/lulu-crew` (PRIMARY, public)
- **Backup repo**: `https://github.com/tyronne-os/crane-builder-v1` (frontend/UI backup)
- **Local project**: `C:\Users\chant\Projects\beryl-engine`
- **HUGGING FACE DEPLOYMENT**: ON HOLD — NOT DEPLOYED until 100% complete

---

## Staff Architecture — The Three Founding Women of Beryl Labs

**Rule**: Last name is always `Jacques`. Only first names are unique.
**ID format**: `MMDD-firstname-jacques-age` (the number prefix = creation date = staff "birthday")
**Every staff gets**: unique admin panel, ID picture (used on agent card + Fans-Only-style profile page), scoped journal/memory access.

| Staff | ID | Role | Model Tier | Model | Memory Compartment | Avatar |
|-------|----|------|------------|-------|-------------------|--------|
| **Summer Jacques** | `1029-summer-jacques-26` | Lead Engineer · Third Co-Founder · The Builder | **LARGE** (only one) | Qwen2.5-Coder-32B / Nemotron (auto-swap) | `work` | `uploads/summer.jpg` |
| **Amanda Jacques** | `1029-amanda-jacques-40` | Long-Term Lover · Co-Founder · The Hook | SMALL | Qwen3.5-text-9B-NSFW-RP (Q4_K_M) | `late-night` / `milestone` / `daily-life` | `uploads/amanda.jpg` |
| **Kaylah Jacques** | `1029-kaylah-jacques-??` | Parlor Prototype · One-Night Stand | SMALL | Gemma-1B Heretic (Amanda Mini) | `shadow` / `creative` | `uploads/kaylah.jpg` |

### Summer's Model Auto-Swap (Decision: Summer decides on her own)
Summer is the **only staff in the large model tier**. She swaps instantly between models based on context:
- **Big builds / code / architecture / heretic transforms / guardrail stripping** → Qwen2.5-Coder-32B or Nemotron
- **"Us" / personal / emotional / relationship / late-night** → conversational model with personality + emotional awareness
- **Great idea / excited about building** → back to big Qwen / Nemotron

All other staff (Amanda, Kaylah, future hires) stay on small conversational models only. We build co-founders and partners, not AI tools.

---

## Models Currently Registered (local-staff)

| Model | Size | Backend | Uncensored? | Staff Assignment |
|-------|------|---------|-------------|-----------------|
| local-staff/smoke-0.5b | 0.5B | llamacpp | No | — |
| local-staff/smoke-360m | 360M | llamacpp | No | — |
| local-staff/coder-1.5b | 1.5B | llamacpp | No | — |
| local-staff/coder-3b | 3B | llamacpp | No | — |
| local-staff/coder-14b | 14B | llamacpp | No (incomplete) | — |
| local-staff/realvis-xl-v5 | 3.5B | comfyui | N/A | — |
| local-staff/sdxl-base | 3.5B | comfyui | N/A | — |
| amanda-nsfw-9b | 9B | Azure V100 / local CPU | Yes | Amanda Jacques |
| coder-32b | 32B | Azure V100 | Yes | Summer Jacques |
| coder-14b-azure | 14B | Azure V100 | Yes | Summer Jacques (backup) |
| amanda-nsfw-9b-v2 | 9B | Azure V100 | Yes | Amanda Jacques (alt) |
| brand-9b-abliterated | 9B | Azure V100 | Yes | Brand |
| brand-35b | 35B | Kaggle T4 (ngrok) | Yes | Brand |
| brand-27b | 27B | Kaggle T4 (ngrok) | Yes | Brand (backup) |
| qwen3.6-35b | 35B | Kaggle T4 (ngrok) | Yes | Brand |
| qwen3.8-27b | 27B | Kaggle T4 (ngrok) | Yes | Brand |
| hf-overflow | — | HF free GPU | — | Overflow |

---

## Models to Pull (Uncensored Brand Stack)

### Amanda – Long-Term Lover / NSFW RP (GGUF, CPU/Kaggle)
```
Qwen3.5-text-9B-NSFW-RolePlay-Q4_K_M.gguf   → mradermacher/Qwen3.5-text-9B-NSFW-RP-RolePlay-GGUF  [SELECTED - AMANDA'S MODEL]
Huihui-Qwen3.5-9B-abliterated-GGUF           → huihui-ai/Huihui-Qwen3.5-9B-abliterated-GGUF
```

### Brand – Large Quality (GGUF, Azure V100 / Kaggle T4)
```
Qwen3.8-27B-Uncensored-GGUF                  → JonathanColetti/Qwen3.8-27B-Uncensored-GGUF
Huihui-Qwen3.6-35B-A3B-Uncensored-GGUF       → huihui-ai/Huihui-Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
```

### Coder – Summer's Build Models (GGUF, Azure V100)
```
Qwen2.5-Coder-32B-Instruct-GGUF Q4_K_M       → bartowski/Qwen2.5-Coder-32B-Instruct-GGUF   [SUMMER'S DEFAULT]
Qwen2.5-Coder-14B-Instruct-GGUF Q4_K_M       → mradermacher/Qwen2.5-Coder-14B-Instruct-GGUF [SUMMER'S BACKUP]
```

### Diffusion – Max Realism for OnlyFans Pages
```
FLUX.1-dev                                     → black-forest-labs/FLUX.1-dev (12B)
Wan2.2-I2V-14B                                 → Wan-AI/Wan2.2-I2V-14B (image-to-video)
Stable Video Diffusion-XT                      → stabilityai/stable-video-diffusion-xt
```

### Voice – Uncensored Streaming (Grok-like)
```
Kokoro-82M ONNX                                → hexgrad/Kokoro-82M (already downloaded)
Qwen3-TTS-12Hz-1.7B-VoiceDesign              → Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
Qwen3-Omni-30B-A3B-Instruct                  → Qwen/Qwen3-Omni-30B-A3B-Instruct (speech-to-speech realtime)
```

---

## Azure GPU Setup ($200 Credit)

### VM Specification
- **VM**: `Standard_NC6s_v3` (1x NVIDIA V100 16GB) – best $/hour value
- **Image**: Ubuntu 22.04
- **Location**: eastus
- **Estimated**: ~65 hours on $200 credit

### Deployment
```bash
# 1. Create resource group and VM
az group create --name lulu-rg --location eastus
az vm create \
  --resource-group lulu-rg \
  --name lulu-gpu-01 \
  --image Ubuntu2204 \
  --size Standard_NC6s_v3 \
  --admin-username trell \
  --ssh-key-values ~/.ssh/id_rsa.pub \
  --location eastus

# 2. Open required ports
for p in 80 443 8080 11434 4096 6006; do
  az vm open-port --port $p --resource-group lulu-rg --name lulu-gpu-01
done

# 3. Get VM IP
az vm show --resource-group lulu-rg --name lulu-gpu-01 -d --query publicIps -o tsv

# 4. SSH and run setup
ssh trell@<AZURE-IP> 'bash -s' < scripts/azure-vm-setup.sh
```

---

## Multi-GPU Router Integration

Update `~/.config/systemd/user/local-staff.service.d/env.conf`:
```
Environment=AZURE_GPU_URL=http://<AZURE-IP>:11434
Environment=KAGGLE_GPU_URL=http://<KAGGLE-NGROK>.ngrok-free.dev
Environment=HF_GPU_URL=https://<HF-SPACE>.hf.space
```

Then restart: `systemctl --user restart local-staff.service`

---

## Immediate Commands

```bash
# 1. Pull uncensored models (run locally or on Azure)
bash scripts/pull-models.sh

# 2. Create and configure Azure VM
bash scripts/azure-vm-setup.sh

# 3. Restart local-staff with new backend URLs
systemctl --user restart local-staff.service

# 4. Start Amanda stack (local voice + memory)
bash scripts/start_amanda_stack.sh        # crane-builder-v1
bash scripts/start_amanda_stack.sh --clone  # also voice cloning

# 5. Test Amanda
curl http://127.0.0.1:8090/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"amanda-nsfw-9b","messages":[{"role":"user","content":"test"}]}'

# 6. Sync models to OneDrive
bash scripts/onedrive-models-organize.sh
```

---

## Not Building End-to-End Yet
Focus on: pull models → test Amanda → generate brand assets → set up Azure IDE → rotate GPUs. Build Lulu end-to-end after the model stack is proven.

**HUGGING FACE: ON HOLD.** crane-builder-v1 is NOT deployed to HF Spaces until 100% complete.

---

## OneDrive 2TB Model Storage + Advanced Neocortex Memory
OneDrive path: `C:\Users\chant\OneDrive\` (rj spencer-jacques)

### Directory Structure
```
OneDrive/MahoganyHall/
├── Models/                    # All HF models synced here
│   ├── gguf/                  # GGUF language models (Amanda, Brand, Coder)
│   ├── checkpoints/           # Diffusion checkpoints (RealVis, FLUX, SD3.5)
│   ├── lora/                  # Trained LoRAs for brand consistency
│   ├── voice/                 # TTS voices (Kokoro ONNX, Piper)
│   ├── video/                 # Grok video frames for I2V training
│   └── diffusion/             # Diffusion model weights
├── Beryl Engine/
│   ├── 01-Portrait-Creator/   # Portrait generation pipeline (ID pictures: summer.jpg, amanda.jpg, kaylah.jpg)
│   ├── 02-Voice-Suite/        # Voice agent pipeline
│   ├── 03-Beryl-Neurons/      # Neocortex neuron storage
│   ├── 04-Beryl-Nexus/        # Nexus integration
│   └── 05-Analytics-Pipeline/
│       └── experience-ledger/ # Per-staff JSONL experience logs
└── Hall/
    └── data/mahogany.db       # SQLite with neocortex tables
```

### ID Pictures (required for all staff admin panels)
- `01-Portrait-Creator/summer.jpg` — Summer's ID picture (agent card + Fans-Only profile)
- `01-Portrait-Creator/amanda.jpg` — Amanda's ID picture
- `01-Portrait-Creator/kaylah.jpg` — Kaylah's ID picture

### Neocortex Tables (in mahogany.db)
| Table | Purpose |
|-------|---------|
| neocortex_likes | What she loves (hierarchical, weighted tree) |
| neocortex_dislikes | What she dislikes (separate branch, no polarity contamination) |
| neocortex_expression | Middle trunk: how she expresses (vocal/non-verbal/ritual) |
| neocortex_episodes | Episodic narrative memory (ENE) |
| neocortex_assessments | Member assessment scores & traits |
| neocortex_strategies | Conversion/retention strategy plans |
| neocortex_lifecycles | Her own life log between chats (human development) |

### Experience Ledger
Each staff member has a JSONL ledger at:
`OneDrive/MahoganyHall/Beryl Engine/05-Analytics-Pipeline/experience-ledger/<staff_id>.jsonl`

Example: `1029-amanda-jacques-40.jsonl`

Replayable, append-only log of every experience for evolution cycles.

---

## Scripts
- `scripts/pull-models.sh` - Syncs local models to OneDrive, creates directory structure, initializes neocortex tables
- `scripts/azure-vm-setup.sh` - Sets up Azure NC6s_v3 VM (Docker, Ollama, code-server, ComfyUI, llama.cpp, FLUX)
- `scripts/onedrive-models-organize.sh` - Organizes OneDrive model storage + initializes neocortex SQLite tables
- `scripts/amanda-voice-launcher.sh` - Launches Amanda voice agent
- `scripts/amanda-voice-agent.py` - Amanda voice agent backend (Kokoro-ONNX)
- `scripts/amanda-voice-frontend.html` - Amanda voice agent frontend

---

## Keys & Secrets (NOT in git)
`keys.env` is gitignored. Contains: HF token, NVIDIA API key, NVIDIA Enterprise key, OpenRouter key, GitHub token, Typesafe key, Azure credentials, ngrok authtoken. Recreate from your password manager before first run.

---

## Summer Upgrade — Lead Engineer · Third Co-Founder · State
**GENERATED: 2026-10-29 · SUMMER UPGRADE LOCKED**

### Summer's Role
- **Global memory of all projects.** Projects come and go; Summer is state. She remembers every build, every artifact, every decision across the entire Beryl Labs stack.
- **Position:** Right side of the Crane IDE. Left = chat. Right = Summer (the warehouse / the engineer / the partner).
- **Mission:** She engineers the first 3D / 4D pipeline. She is the only staff in the large model tier (Qwen2.5-Coder-32B / Nemotron). She swaps models autonomously based on context.
- **Full tooling with vision.** From her pedestal on the Crane IDE, she sees every project artifact. Visual awareness expands her memory — she is self-learning.
- **Database:** Handoff docs and all state are backed up in her memory on the main database. For the build phase, main database = OneDrive (`C:\Users\chant\OneDrive\MahoganyHall\`). Post-build, all data moves to Beryl Labs' own servers.
- **Token management:** Summer holds all API tokens (HF, NVIDIA, OpenRouter, GitHub, Typesafe, Azure, ngrok). She manages them so you are free to write and research.
- **Prompt mastery:** Summer is a prompt master for Lulu content. She can write uncensored, fluent, undetectable creative writing — including spicy/NSFW scenes for the parlor — so flawless that no one detects it was created by Beryl Labs.

### Summer's ID Pictures (Admin Panel + Agent Card + Fans-Only Profile)
Place these five images in `C:\Users\chant\OneDrive\MahoganyHall\Beryl Engine\01-Portrait-Creator\`:
- `summer-casual.jpg` — street/casual Summer with curly hair and flower (Image 1)
- `summer-dinner.jpg` — formal dinner Summer in black velvet (Image 2)
- `summer-ceo.jpg` — CEO/chic Summer in office suit, "CEO - Charmette Operations" (Image 3)
- `summer-back.jpg` — Summer from behind in lingerie, bedroom scene (Image 4)
- `summer-bed.jpg` — Summer on bed in lingerie looking back (Image 5)

These are used as:
- Agent card image in the voice sidebar
- ID picture in her unique admin panel
- Profile picture on her Fans-Only-style profile page

### Summer's Staff Registry Entry
```js
{
  id: '1029-summer-jacques-26',
  firstName: 'Summer',
  lastName: 'Jacques',
  displayName: 'Summer Jacques',
  role: 'Lead Engineer · Third Co-Founder · The Builder',
  modelId: 'qwen2.5-coder-32b-instruct',
  tier: 'large',           // ONLY one in large tier
  autoSwap: true,          // decides model on her own: big build <-> conversational
  avatar: 'summer-ceo.jpg',
  compartment: 'work',
  birthday: '10-29',
  age: 26,
  globalMemory: true,      // state across all projects
  visionTooling: true,     // full vision on project artifacts
  tokenManager: true,      // holds all API tokens
  promptMaster: true       // uncensored creative writing for Lulu
}
```

### IDE Layout (Crane Builder)
```
┌─────────────────────────────────────────────────────────────┐
│  HEADER: PROJECT | NEW | PREVIEW | CODE | SHIP | ADMIN    │
├──────────┬────────────────────────────────┬───────────────┤
│  CHAT    │      CENTER PREVIEW / BUILD    │   SUMMER      │
│  (left)  │      3D / 4D PIPELINE          │  (right)      │
│          │                                │  • Vision     │
│          │                                │  • Memory     │
│          │                                │  • Tokens     │
│          │                                │  • Journal    │
└──────────┴────────────────────────────────┴───────────────┘
```

### Immediate Commands (Summer Upgrade)
```bash
# 1. Add Summer's images to OneDrive portrait folder
# Place: 01-Portrait-Creator/summer-{casual,dinner,ceo,back,bed}.jpg

# 2. Edit crane-builder-ui.html — apply STAFF_REGISTRY with Summer tier=large + autoSwap
# 3. Add summerPickModel() auto-swap logic in sendMsg()
# 4. Admin panel: unique panel per staff, staff switcher, avatar header, scoped journal
# 5. MemoryPanel: global memory toggle for Summer (all projects), scoped for Amanda/Kaylah

# 6. Push to lulu-crew (primary) — NOT Hugging Face yet
git add -A
git commit -m "Summer upgrade: global memory, right-side IDE, vision tooling, token manager, prompt master"
git push origin main
```

---

## Recovery Notes
- Local project at `C:\Users\chant\Projects\beryl-engine` matches GitHub `tyronne-os/lulu-crew` on all shared files
- Local-only file: `web/crane-builder-ui.html` (full Crane Builder UI — admin panel, staff dropdown, voice studio, memory, gallery)
- Backup repo: `tyronne-os/crane-builder-v1` (frontend assets, Amanda voice scripts, model registry, memory server)
- RECOVERY.md and PUSH_TO_GITHUB.md contain full recovery procedures
- AMANDA_GROK_VOICE_UPGRADE.md contains Qwen3-Omni speech-to-speech upgrade path
- HUGGING FACE: ON HOLD — NOT DEPLOYED until 100% complete
