# Earth Loading Screen

The TikTok trend as a real web app: an endless "loading screen" that cycles
genuine Wikipedia article photos with their real captions, in Wikipedia
thumbnail style, with a little globe and a "Loading…" that keeps changing
languages. 969 image + caption pairs harvested from Wikipedia articles.

**Live:** https://menonmoon.github.io/earth-loading-screen/

## Features

- Double-buffered crossfades (the next photo fully decodes before it fades
  in) with a slow Ken Burns zoom
- Category filters: All · Animals · Earth & Space · Ocean & Water ·
  Plants & Nature
- ♥ Save cards to a favorites collection; share a card's article; dark mode
  (Wikipedia's night palette); swipe, tap, or arrow keys to move
- Progress ring around the globe tracks the 6.5 s cycle; the loading word
  rotates through 12 languages
- Music: "Monkeys Spinning Monkeys" by Kevin MacLeod (CC BY 3.0), plus a
  ♪+ button to use your own audio file instead — it's stored only on your
  device, never uploaded. Long-press ♪+ to go back to the built-in track

## Add it to your iPhone home screen

1. Open the live site in **Safari**.
2. Tap **Share** → **Add to Home Screen**.
3. It gets the Earth icon and opens fullscreen — works offline too.

For a *real* home-screen widget (Scriptable), see `WIDGET.md`.

## Files

- `index.html` — the whole app
- `figures.json` — the card feed (img, caption_html, caption, article, category)
- `music.mp3` — Kevin MacLeod, "Monkeys Spinning Monkeys" (CC BY 3.0)
- `globe.jpg` — Blue Marble thumbnail (NASA / Wikimedia Commons)
- `widget.js` / `WIDGET.md` — Scriptable widget + setup
- `sw.js`, `manifest.webmanifest`, `icon-*.png` — PWA plumbing

## Credits

- Images and captions: Wikipedia / Wikimedia Commons; each card names and
  links its source article.
- Music: Kevin MacLeod (incompetech.com), licensed CC BY 3.0.
- The vibe: "Coloured Candles" by Tony Hymas (Bruton, 1979) — the sound
  from the original TikTok by banankaka. It's commercial library music, so
  it can't be bundled here; use the ♪+ button with your own copy.
