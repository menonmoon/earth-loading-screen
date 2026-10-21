# Earth Loading Screen — real iPhone widget

The web version (Add to Home Screen) is the full experience: new image every
few seconds, music, tap to advance. This Scriptable widget puts the same
Wikipedia images + captions into a **real home-screen widget**.

## Install (about 2 minutes)

1. Install **Scriptable** (free) from the App Store.
2. Open `widget.js` in this repo, copy the whole file.
   Raw link: https://raw.githubusercontent.com/menonmoon/earth-loading-screen/main/widget.js
3. In Scriptable, tap **+**, paste the code, then tap the script's title at
   the top and name it **Earth Loading**. Tap Done.
4. Long-press your home screen → **+** → **Scriptable** → pick a size
   (medium recommended) → **Add Widget**.
5. Long-press the new widget → **Edit Widget** → **Script** → choose
   **Earth Loading**.

## Good to know

- iOS refreshes widgets on its own schedule (roughly every 15–60 minutes),
  so the widget rotates slower than the web version. That's an Apple rule
  for every widget, not a setting.
- Tapping the widget opens the Wikipedia article the image came from.
- The widget pulls from the same `figures.json` feed as the web version,
  so improving the feed improves both.

## Credits

- Images and captions: Wikipedia / Wikimedia Commons (each image links to
  its article).
- Music in the web version: Erik Satie, *Gymnopédie No. 1* — public domain
  recording via Wikimedia Commons.
