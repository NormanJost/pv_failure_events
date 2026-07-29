# PV failure event explorer

This is a shareable, standalone snapshot generated 2026-07-29 20:56 UTC. Share this entire folder.

## Open it

Open `index.html` in a modern browser. The event data and map software are included locally.

If your browser or organization blocks local HTML files, run `python serve.py` in this folder and open the local address it prints.

The background map uses OpenStreetMap tiles, so an internet connection is needed for the basemap. The event list, filters, details, and embedded event data remain available without it.

## Included

- `index.html` - explorer interface
- `events.js` - current 97-event dataset
- `data/pv_failure_events_pvllm.csv` - source event table used to populate the explorer
- `assets/leaflet/` - local map-library files (Leaflet, BSD-2-Clause license)
- `data_quality.json` - validation snapshot

Do not edit `events.js` manually. Refresh this share folder from the main PV-LLM workflow when the dataset changes.
