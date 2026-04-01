# TuneZ Discord Bot - GitHub Pages 部署指南

## 📚 文檔結構

```
docs/
├── _config.yml              # Jekyll 配置
├── Gemfile                  # Ruby 依賴
├── index.md                 # 預設重定向頁面
├── _layouts/               # HTML 模板
│   └── default.html
├── _includes/               # 可重用組件
├── assets/                  # 靜態資源
│   ├── css/style.css
│   ├── js/main.js
│   ├── icon.png
│   ├── demo.png
│   └── opened_bot.png
├── en/                      # 英文版本
│   ├── index.md
│   ├── installation.md
│   ├── commands.md
│   ├── custom-playlist.md
│   └── faq.md
├── zh-TW/                   # 繁體中文版本
│   ├── index.md
│   ├── installation.md
│   ├── commands.md
│   ├── custom-playlist.md
│   └── faq.md
└── zh-CN/                   # 簡體中文版本
    ├── index.md
    ├── installation.md
    ├── commands.md
    ├── custom-playlist.md
    └── faq.md
```

## 🚀 部署到 GitHub Pages

### 方案一：使用 GitHub Actions（推薦）

1. **將 `docs` 資料夾的內容推送到 GitHub**

   由於 GitHub Pages 需要從 repository 根目錄讀取，您可以：
   
   - 將 `docs/` 資料夾的內容移動到 repository 根目錄
   - 或使用 `main` 分支的 `/docs` 資料夾作為來源

2. **設定 GitHub Pages**

   1. 前往您的 repository 設定 (Settings)
   2. 在左側選單點擊 "Pages"
   3. 在 "Source" 部分：
      - 選擇 `main` 分支
      - 選擇 `/ (root)` 資料夾
   4. 點擊 "Save"

4. **啟用 GitHub Actions**

   推送代碼後，GitHub Actions 會自動構建並部署網站。

### 方案二：手動部署

1. **在本機安裝 Jekyll**

   ```bash
   gem install jekyll bundler
   ```

2. **進入 docs 資料夾**

   ```bash
   cd docs
   ```

3. **安裝依賴**

   ```bash
   bundle install
   ```

4. **本地預覽**

   ```bash
   bundle exec jekyll serve
   ```

5. **構建網站**

   ```bash
   bundle exec jekyll build
   ```

   生成的靜態檔案會在 `_site/` 目錄中。

## 🔧 自訂網址

如果您想要使用自訂網域：

1. 在 `docs/` 資料夾中創建 `CNAME` 檔案
2. 在其中輸入您的自訂網域
3. 在您的 DNS 設定中添加 CNAME 記錄

## 📝 注意事項

- 圖片資源已複製到 `docs/assets/`
- 預設語言為英文
- 使用 `lang` front matter 來指定頁面語言
- 語言切換功能通過 URL 前綴實現（`/en/`、`/zh-TW/`、`/zh-CN/`）

## 🌐 多語言支援

網站支援三種語言：

| 語言 | 路徑 |
|------|------|
| English | `/en/` |
| 繁體中文 | `/zh-TW/` |
| 简体中文 | `/zh-CN/` |

## ❓ 幫助

如有問題，請查看：
- [Jekyll 文檔](https://jekyllrb.com/docs/)
- [GitHub Pages 文檔](https://docs.github.com/en/pages)
