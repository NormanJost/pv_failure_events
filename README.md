# PV failure event explorer

This is a complete GitHub Pages site snapshot generated 2026-08-13 22:54 UTC. It contains 129 PV failure event records.

## Publish on GitHub Pages

Use this `webtool` folder as the repository root. Upload its **contents** directly to the repository root; do not place the folder inside another repository subfolder. In GitHub, enable **Settings** -> **Pages** -> **Deploy from a branch**, then select the `main` branch and the `/(root)` folder.

The page works from the GitHub Pages address without Python or other software. Map tiles use OpenStreetMap over the internet; the explorer interface, event list, filters, and data are all included locally.

## Included

- `index.html` - explorer interface
- `events.js` - embedded event data used by the map and event list
- `data/pv_failure_events_pvllm.csv` - backing PV-LLM-aligned CSV
- `assets/leaflet/` - local Leaflet map library and license
- `data_quality.json` - data validation snapshot
