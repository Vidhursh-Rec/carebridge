// Layout probe for check_site.py: loads each page at phone and desktop width and reports scrollWidth.
// Usage: node tests/layout.cjs <site-root> page1.html page2.html ...   (prints JSON)
// Optional: SHOTS=1 also saves screenshots to <site-root>/shots/.
const fs = require("fs");
const path = require("path");

function puppeteer() {
  try { return require("puppeteer-core"); } catch {}
  const npx = path.join(process.env.LOCALAPPDATA || "", "npm-cache", "_npx");
  for (const d of fs.existsSync(npx) ? fs.readdirSync(npx) : []) {
    const p = path.join(npx, d, "node_modules", "puppeteer-core");
    if (fs.existsSync(p)) return require(p);
  }
  throw new Error("puppeteer-core not found");
}
const CHROME = ["C:/Program Files/Google/Chrome/Application/chrome.exe", "/usr/bin/google-chrome"].find((p) => fs.existsSync(p));

(async () => {
  const [root, ...pages] = process.argv.slice(2);
  const browser = await puppeteer().launch({ executablePath: CHROME, headless: "new", args: ["--allow-file-access-from-files"] });
  const out = [];
  if (process.env.SHOTS) fs.mkdirSync(path.join(root, "shots"), { recursive: true });
  for (const p of pages) {
    for (const [w, h] of [[390, 844], [1280, 800]]) {
      const page = await browser.newPage();
      await page.setViewport({ width: w, height: h });
      await page.goto("file:///" + path.join(root, p).replace(/\\/g, "/"), { waitUntil: "networkidle0" });
      const [sw, sh] = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight]);
      out.push({ page: p, width: w, height: h, scrollWidth: sw, scrollHeight: sh });
      if (process.env.SHOTS) await page.screenshot({ path: path.join(root, "shots", `${p.replace(".html", "")}-${w}.png`) });
      await page.close();
    }
  }
  console.log(JSON.stringify(out));
  await browser.close();
})().catch((e) => { console.error(e.message); process.exit(1); });
