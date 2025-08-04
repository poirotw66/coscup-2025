# COSCUP 2025 Data Analysis Project

## 專案簡介 / Project Overview

這是一個分析 COSCUP 2025 年會議資料的專案，包含資料爬取、處理和趨勢分析功能。

This project focuses on analyzing COSCUP 2025 conference data, including data scraping, processing, and trend analysis.

## 專案結構 / Project Structure

```
coscup-2025/
├── README.md                      # 專案說明文件
├── 總覽.md                        # 技術趨勢總覽報告
├── 總覽.pdf                       # 趨勢總覽 PDF 版本
├── GenAI Workflow.pdf             # GenAI 工作流程文件
├── coscup_scraper.py              # COSCUP 資料爬蟲程式
├── extract_coscup_data.py         # 資料提取與處理程式
├── coscup_detail.json             # 原始 JSON 資料
└── coscup_sessions_extracted.csv  # 處理後的會議資料 CSV
```

## 主要檔案說明 / Main Files Description

### 📊 資料分析 / Data Analysis
- **`總覽.md`**: COSCUP 2025 技術趨勢分析報告，包含 Mermaid 圖表
- **`總覽.pdf`**: 趨勢分析的 PDF 版本

### 🛠️ 資料處理工具 / Data Processing Tools
- **`extract_coscup_data.py`**: 從 JSON 檔案提取中文標題和描述，並輸出為 CSV 格式
- **`coscup_scraper.py`**: COSCUP 網站資料爬蟲（開發中）

### 📁 資料檔案 / Data Files
- **`coscup_detail.json`**: 從 COSCUP API 取得的原始會議資料
- **`coscup_sessions_extracted.csv`**: 處理後的會議資料，包含以下欄位：
  - session_id: 會議 ID
  - uri: 會議連結
  - title: 會議標題
  - description: 會議描述
  - language: 使用語言
  - speakers: 講者
  - start_time/end_time: 開始/結束時間
  - room: 會議室
  - type: 會議類型
  - tags: 標籤

## 技術趨勢重點 / Key Technology Trends

根據分析，COSCUP 2025 的主要技術趨勢包括：

1. **人工智慧與 AI Agents** - LLM 應用、AI 自動化工作流
2. **Web3 與去中心化技術** - 智能合約安全、DeFi 基礎設施
3. **開源硬體與嵌入式系統** - RISC-V 生態系、IoT 安全
4. **開源治理與永續發展** - 開源政策、社群經營
5. **雲端原生與 DevOps** - 資料庫技術、系統監控

## 使用方法 / Usage

### 資料提取 / Data Extraction

```bash
# 執行資料提取程式
python3 extract_coscup_data.py

# 自訂輸出檔案名稱
python3 extract_coscup_data.py --output custom_output.csv
```

### 環境需求 / Requirements

```bash
# 安裝必要的 Python 套件
pip install json csv re datetime
```

## 資料來源 / Data Source

- **COSCUP 2025 官方網站**: https://coscup.org/2025/
- **會議資料 API**: COSCUP 官方 API

## 授權 / License

本專案採用開源授權，請參考 COSCUP 資料使用規範。

This project is open source. Please refer to COSCUP data usage guidelines.

## 貢獻 / Contributing

歡迎提交 Issue 和 Pull Request 來改進這個專案！

Issues and Pull Requests are welcome to improve this project!

## 聯絡資訊 / Contact

如有任何問題或建議，請透過 GitHub Issues 聯繫。

For any questions or suggestions, please contact via GitHub Issues.

---

*Last updated: 2025年8月4日*
