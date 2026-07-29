# Share the explorer with a GitHub Pages link

GitHub Pages is the recommended way to share the explorer. Recipients only need a web browser; they do not need Python or the PV-LLM project.

## Publish once

1. Create a GitHub repository for the explorer. Use a public repository only if all included event data may be public.
2. Upload the **contents** of this folder to the repository root. `index.html` must be at the repository root, alongside `events.js` and `assets/`.
3. In the repository, open **Settings** -> **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, select the `main` branch and the `/(root)` folder, then save.
5. GitHub will display the published address after deployment. Share that address with collaborators.

The explorer uses relative file paths, so it works as a normal GitHub Pages project site without any changes. The interactive basemap still loads OpenStreetMap tiles over the internet.

## Updating it later

Replace the repository files with a newer version of this folder. GitHub Pages republishes the update automatically.
