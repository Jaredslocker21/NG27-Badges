# NG27 Badges

Nordic Game 2027 badge preview — 25–28 May 2027, Slagthuset, Malmö.

The existing profile editor and badge layout use Roc Grotesk. Nordic Game fish swim across the entire landing-page background and return in the opposite direction using HTML and CSS. The Pause fish checkbox pauses all fish. Reduced-motion settings are respected, and background fish are hidden when printing.

## Run locally

From the repository folder:

```sh
python -m http.server 8000
```

Open http://localhost:8000. Python's built-in server needs no pip dependencies. Stop it with Ctrl+C.

## GitHub Codespaces

Open Code → Codespaces → Create codespace on main. The development container starts the static preview automatically on port 8000. Click the globe beside 8000 in the Ports panel. If needed, run the local command above from the repository folder.

## Docker

With Docker installed and running:

```sh
docker compose up --build
```

Open http://localhost:8000. The Docker image has not been build-tested in the source workspace.

## Edit

- `index.html`: profile editor, badge markup and live-edit script.
- `badge.css`: layout, typography and swimming fish.
- `assets/`: Roc Grotesk fonts, NG27 banner, fish artwork and original Code of Conduct QR.

The original Code of Conduct QR is restored from the supplied badge artwork. The personal attendee QR must be supplied by the account system using `window.ngBadgePreview.updateBadge({ qrImageUrl: "..." })`. The preview does not save changes to an account. Wi-Fi, password and sponsor details remain pending. Print size: 90 × 126 mm.

This repository contains the standalone badge preview. It does not require React, Django or FastAPI to run.
