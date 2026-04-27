# Deploy aldrich.fyi

Five clicks in Cloudflare to take this repo live.

## Part 1 — aldrich.fyi (this site)

**1. Create the Pages project**

- https://dash.cloudflare.com → **Compute** (Workers & Pages, left sidebar)
- **Create** button → **Pages** tab → **Connect to Git**
- (First time only) authorize the GitHub app on `Chen17-sq`
- Pick repository: `Chen17-sq/aldrich-fyi`

**2. Build configuration** (leave empty)

- Project name: `aldrich-fyi` (or whatever)
- Production branch: `main`
- Framework preset: **None**
- Build command: *blank*
- Build output directory: `/`
- Environment variables: *none*

Click **Save and Deploy**. ~30-60 seconds → first deploy. You'll get a `aldrich-fyi.pages.dev` URL.

**3. Bind aldrich.fyi**

- Inside the new project → **Custom domains** tab → **Set up a custom domain**
- Enter `aldrich.fyi` → continue
- Cloudflare auto-detects you own the domain (it's already on your CF account) → **Activate**
- DNS records added automatically. Live in ~1 min.

Go to https://aldrich.fyi → done.

---

## Part 2 — ks.aldrich.fyi (Kickstarter Tracker)

The tracker is currently at `https://chen17-sq.github.io/kickstarter-china-tracker/`. Adding a custom domain to GitHub Pages:

**1. Add CNAME in Cloudflare DNS**

- Cloudflare → `aldrich.fyi` → DNS → Records → **Add record**
- Type: `CNAME`
- Name: `ks`
- Target: `chen17-sq.github.io`
- Proxy status: **DNS only** (gray cloud — GitHub Pages SSL doesn't work with proxy)
- Save

**2. Add CNAME file to KS Tracker repo**

```bash
cd /Users/chensiqi/CC/kickstarter-china-tracker
echo "ks.aldrich.fyi" > site/CNAME
git add site/CNAME
git commit -m "feat: custom domain ks.aldrich.fyi"
git push
```

**3. Configure in GitHub repo settings**

- https://github.com/Chen17-sq/kickstarter-china-tracker/settings/pages
- Custom domain: `ks.aldrich.fyi` → Save
- Wait ~5 min for SSL cert provisioning, then check **Enforce HTTPS**

Live at https://ks.aldrich.fyi.

---

## Part 3 (optional) — hi@aldrich.fyi forwarding

Make `*@aldrich.fyi` forward into your gmail. Free.

- Cloudflare → `aldrich.fyi` → **Email** → **Email Routing** → **Get started**
- Cloudflare adds 3 DNS records automatically (MX + 2 TXT for SPF)
- Add a route: `hi@aldrich.fyi` → `schen.aldrich@gmail.com`
- Verify the gmail by clicking the link in the verification email
- Optional catch-all: forward `*@aldrich.fyi` to gmail

Now `hi@aldrich.fyi` works. Good for resume / business cards / handing out.

---

## Future updates

The Cloudflare Pages project auto-deploys on every `git push origin main`. So:

```bash
cd /Users/chensiqi/CC/aldrich-fyi
# edit index.html...
git commit -am "tweak"
git push
# 30s later, aldrich.fyi shows the new version
```
