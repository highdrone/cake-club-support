# Cake Club website and store listing

Official website: https://playcakeclub.com
Support: support@playcakeclub.com

## Source

- `website/` contains the complete public website source and gameplay artwork.
- `app-store/description.txt` is the App Store description submitted with version 1.0 (24).
- The native app source is maintained separately in https://github.com/highdrone/CakeClub (private).
- Root `index.html` and `privacy.html` preserve the original GitHub Pages redirects to the official domain.

## Website development

From `website/`, run `python3 build.py` to generate `dist/`. Preview with `python3 -m http.server 3010 --bind 127.0.0.1 --directory dist`.

Production is hosted through the existing Sites project in `website/.openai/hosting.json`. Publishing uses a separately authenticated source push and deployment; pushing this GitHub backup does not deploy the production website. Never add credentials to this repository.

## Release record — September 16, 2026

- App version 1.0 (24), source commit `f072c860981113bb19f62f311b920f83a3a0697a`.
- Website source revision `8a06f81807af993cb8eb13e378b55a9f1c4e6fbf`.
- Pinch zoom, smooth return after five seconds of inactivity, subtle dotted icing guides, and full-cake comparison documented.
- TestFlight: https://testflight.apple.com/join/4RGF1HvH
- Public App Store submission was verified Waiting for Review, with automatic release after approval. This is a historical record, not a live approval status.

## Public launch — September 17, 2026

Cake Club is live at https://apps.apple.com/us/app/cake-club/id6808979979. The homepage now uses Apple’s official black Download on the App Store badge. Guide and support availability text link to the public listing. Website source revision: `b4d64e4a0ab7c2a528a94e788bc5c5671653ce3e`.
