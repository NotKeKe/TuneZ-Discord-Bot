# GitHub Pages URL 修復計劃

## 問題分析

### 根本原因
當前 GitHub Pages 設置為從 `main` 分支的 `/docs` 資料夾部署。這種模式下：
- **不會運行 Jekyll 構建**
- 直接提供原始 markdown 文件
- `_config.yml` 中的 `baseurl` 設定不會被應用
- 導致所有頁面返回 404

### 解決方案
將部署方式改為 **GitHub Actions**，讓 Jekyll 正確構建並部署。

---

## 修復步驟

### 步驟 1：在 GitHub 上修改 Pages 設置
1. 進入倉庫 **Settings** > **Pages**
2. **Build and deployment** > **Source** 改為 **GitHub Actions**
3. 這樣 GitHub Actions workflow 才能部署到 GitHub Pages

### 步驟 2：修改 workflow 文件
修改 `docs/.github/workflows/jekyll.yml`：

```yaml
name: Deploy Jekyll site to GitHub Pages

on:
  push:
    branches:
      - main  # 只在推送 main 分支時觸發
  workflow_dispatch:  # 允許手動觸發

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Setup Pages
        uses: actions/configure-pages@v4
        
      - name: Setup Ruby
        uses: ruby/setup-ruby@ec73b3a2de993d9d0e16c22c5d3b9f0ff2e4a0c2
        with:
          ruby-version: '3.1'
          bundler-cache: true
          cache: 'bundler'
        
      - name: Build Jekyll site
        run: bundle exec jekyll build --baseurl "${{ github.event.repository.name }}"
        env:
          JEKYLL_ENV: production
          
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '_site'

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**關鍵變更**：
- 使用 `--baseurl "${{ github.event.repository.name }}"` 動態獲取倉庫名稱
- 保持 workflow 在推送 main 分支時自動構建

### 步驟 3：驗證所有配置

檢查以下文件確保 URL 生成正確：

| 文件 | 檢查項目 |
|------|---------|
| `docs/_config.yml` | `baseurl` 設定（將被 workflow 動態覆蓋） |
| `docs/_layouts/default.html` | 所有連結使用 `relative_url` filter |
| `docs/en/*.md` | `permalink` 設定正確（如 `/en/faq/`） |
| `docs/zh-TW/*.md` | `permalink` 設定正確（如 `/zh-TW/faq/`） |
| `docs/zh-CN/*.md` | `permalink` 設定正確（如 `/zh-CN/faq/`） |

### 步驟 4：提交並推送

```bash
git add .
git commit -m "Fix GitHub Pages deployment with proper Jekyll build"
git push origin main
```

### 步驟 5：等待並測試

1. GitHub Actions 將自動構建（約 1-2 分鐘）
2. 訪問 `https://notkeke.github.io/TuneZ-Discord-Bot/`
3. 測試各頁面：
   - `/TuneZ-Discord-Bot/en/faq/` ✅
   - `/TuneZ-Discord-Bot/zh-TW/installation/` ✅
   - `/TuneZ-Discord-Bot/zh-CN/commands/` ✅

---

## 分支操作說明

### 如何在本地操作多個分支

```bash
# 1. 查看所有分支
git branch -a

# 2. 切換到 main 分支
git checkout main

# 3. 如果需要創建新分支
git checkout -b gh-pages

# 4. 在新分支上工作後推送
git push origin gh-pages

# 5. 切換回 main
git checkout main
```

### 推薦工作流程

1. **在 main 分支上開發** - 主要的文檔工作在這裡
2. **觸發 workflow** - 每次推送到 main 都會自動構建和部署
3. **測試** - 在 `https://notkeke.github.io/TuneZ-Discord-Bot/` 驗證

---

## 驗證清單

在部署後，確認以下 URL 都能正確訪問：

| URL | 預期結果 |
|-----|---------|
| `https://notkeke.github.io/TuneZ-Discord-Bot/` | 首頁（英文） |
| `https://notkeke.github.io/TuneZ-Discord-Bot/en/` | 英文首頁 |
| `https://notkeke.github.io/TuneZ-Discord-Bot/en/faq/` | 英文 FAQ |
| `https://notkeke.github.io/TuneZ-Discord-Bot/en/installation/` | 英文安裝指南 |
| `https://notkeke.github.io/TuneZ-Discord-Bot/zh-TW/` | 繁體中文首頁 |
| `https://notkeke.github.io/TuneZ-Discord-Bot/zh-CN/` | 簡體中文首頁 |
| `https://notkeke.github.io/TuneZ-Discord-Bot/assets/css/style.css` | CSS 檔案（無 404） |

---

## 風險與應對

| 風險 | 應對方式 |
|-----|---------|
| 構建失敗 | 檢查 GitHub Actions 日誌 |
| CSS 404 | 確認 `relative_url` filter 使用正確 |
| 頁面路徑錯誤 | 確認 permalink 設定與實際路徑一致 |