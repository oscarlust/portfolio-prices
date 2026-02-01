# Portfolio Tracker - Automatic Price Updates

This repository automatically fetches stock and crypto prices every 5 minutes and serves them via GitHub Pages.

## Setup Instructions (5 minutes)

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Name it: `portfolio-prices` (or any name you like)
3. Make it **Public** (required for GitHub Pages)
4. Click "Create repository"

### 2. Upload Files

Upload these 4 files to your repository:

- `.github/workflows/fetch-prices.yml` - The workflow file
- `fetch_prices.py` - Python script that fetches prices
- `prices.json` - Initial empty prices file
- `index.html` - Your portfolio tracker app

**How to upload:**
1. Click "Add file" → "Upload files"
2. Drag and drop all 4 files
3. Click "Commit changes"

### 3. Add API Key Secret

1. Go to your repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `FMP_API_KEY`
4. Value: `PYg3qNmBoOYHuRnnUGEBd32s0JtBdIIj`
5. Click "Add secret"

### 4. Enable GitHub Pages

1. Go to repository Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` (or `master`), folder: `/ (root)`
4. Click "Save"

### 5. Run First Update

1. Go to "Actions" tab in your repository
2. Click "Update Stock Prices" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait 1-2 minutes for it to complete

### 6. Access Your App

Your portfolio tracker will be available at:
```
https://YOUR-USERNAME.github.io/portfolio-prices/
```

Replace `YOUR-USERNAME` with your GitHub username.

## How It Works

- GitHub Actions runs every 5 minutes during market hours (9:30 AM - 4:00 PM ET)
- Fetches all your stock and crypto prices
- Saves them to `prices.json`
- Your app reads from this file (unlimited, free, no CORS issues!)

## Customization

To add/remove stocks, edit the `HOLDINGS` list in `fetch_prices.py`

## Completely Free!

- ✅ Unlimited requests (your app just reads a JSON file)
- ✅ No rate limits
- ✅ Updates automatically every 5 minutes
- ✅ Works on mobile (add to home screen)
- ✅ No backend server needed
