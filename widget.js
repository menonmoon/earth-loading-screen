// Earth Loading Screen — Scriptable widget
// Shows a random Wikipedia image + its real caption, in the style of the
// "earth loading screen" trend. Data feed lives in the same GitHub repo.
//
// Setup (2 minutes):
// 1. Install the free "Scriptable" app from the App Store.
// 2. In Scriptable tap + and paste this whole file. Name it "Earth Loading".
// 3. Long-press your home screen, add a Scriptable widget, then long-press
//    it > Edit Widget > Script > choose "Earth Loading".
// iOS decides when widgets refresh (usually every 15-60 minutes), so the
// widget rotates more slowly than the web version. Tap opens the article.

const FEED = "https://menonmoon.github.io/earth-loading-screen/figures.json";
const INK = new Color("#202122");
const LINK = new Color("#3366cc");
const GRAY = new Color("#72777d");

async function loadItem() {
  const req = new Request(FEED);
  const items = await req.loadJSON();
  return items[Math.floor(Math.random() * items.length)];
}

function addCaption(stack, item, size, lines) {
  const t = stack.addText(item.caption);
  t.font = Font.systemFont(size);
  t.textColor = INK;
  t.lineLimit = lines;
  return t;
}

function addLoadingLine(stack, size) {
  const t = stack.addText("🌍 Loading…");
  t.font = Font.italicSystemFont(size);
  t.textColor = LINK;
  return t;
}

async function createWidget() {
  const item = await loadItem();
  const imgReq = new Request(item.img);
  const img = await imgReq.loadImage();

  const w = new ListWidget();
  w.backgroundColor = new Color("#ffffff");
  w.setPadding(10, 10, 10, 10);
  w.url = "https://en.wikipedia.org/wiki/" + encodeURIComponent(item.article.replace(/ /g, "_"));

  const family = config.widgetFamily || "medium";

  if (family === "small") {
    const im = w.addImage(img);
    im.imageSize = new Size(146, 96);
    im.cornerRadius = 2;
    w.addSpacer(4);
    addCaption(w, item, 10, 3);
    w.addSpacer(2);
    addLoadingLine(w, 9);
  } else if (family === "large") {
    const im = w.addImage(img);
    im.imageSize = new Size(330, 228);
    im.cornerRadius = 2;
    w.addSpacer(6);
    addCaption(w, item, 12, 6);
    w.addSpacer();
    addLoadingLine(w, 11);
  } else {
    // medium: photo left, caption right
    const row = w.addStack();
    row.layoutHorizontally();
    const im = row.addImage(img);
    im.imageSize = new Size(150, 140);
    im.cornerRadius = 2;
    row.addSpacer(10);
    const col = row.addStack();
    col.layoutVertically();
    addCaption(col, item, 12, 7);
    col.addSpacer();
    addLoadingLine(col, 10);
  }

  // Ask iOS for the next refresh in ~15 minutes (it decides in the end).
  w.refreshAfterDate = new Date(Date.now() + 15 * 60 * 1000);
  return w;
}

const widget = await createWidget();
if (config.runsInWidget) {
  Script.setWidget(widget);
} else {
  await widget.presentMedium();
}
Script.complete();
