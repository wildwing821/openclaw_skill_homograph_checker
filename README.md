README.md
🛡️ Homograph Domain Checker (OpenClaw Skill)
📖 Introduction / 簡介
English:
A security-focused Python skill designed for the OpenClaw ecosystem. It detects Homograph (IDN) Spoofing Attacks by analyzing domain scripts (e.g., distinguishing between a Latin 'a' and a Cyrillic 'а'). This tool serves as a critical defense layer before any web navigation or data fetching.

中文：
這是一個為 OpenClaw 生態系統設計的安全性 Python 技能。它透過分析網域字元集（例如區分拉丁字母 'a' 與西里爾字母 'а'）來偵測 同形異義字（IDN）欺騙攻擊。在進行任何網頁導航或資料抓取前，此工具可作為關鍵的防禦層。

✨ Features / 功能亮點
Punycode Conversion: Automatically decodes and exposes the true address of masked domains.

Mixed Script Detection: Identifies if a domain uses multiple character sets (a primary indicator of phishing).

Risk Assessment: Categorizes domains into HIGH or LOW risk based on script entropy.

OpenClaw Ready: Pre-configured as a system skill for seamless LLM integration.

🛠️ Installation / 安裝指南
Prerequisites / 前置需求
Python 3.9+

pip package manager

Setup / 安裝步驟
Clone or Copy this folder into your OpenClaw workspace:

Bash
# Path inside OpenClaw environment
mkdir -p /app/.openclaw/workspace/skills/homograph_checker/
Install Dependencies / 安裝依賴項:

Bash
pip install idna pydantic
🚀 Usage / 使用說明
Manual Execution / 手動執行
You can test the detector manually via CLI:
您可以透過命令列手動測試偵測器：

Bash
python3 /app/.openclaw/workspace/skills/homograph_checker/checker.py
OpenClaw Integration / OpenClaw 整合
When integrated as a skill, OpenClaw agents should follow these rules:
當整合為系統技能時，OpenClaw 代理應遵守以下規範：

Trigger: Use this skill before any browser navigation or web_fetch.

Logic: If risk_assessment is HIGH, stop the process and warn the user.

觸發時機：在執行 browser 導航或 web_fetch 抓取前調用。

邏輯處理：若 risk_assessment 回傳為 HIGH，必須立即停止並告知使用者。

🏗️ Architecture / 技術架構
Following the First Principles of clean code / 遵循潔淨程式碼之第一性原理：

Domain-Driven Design: Separates Configuration, Interfaces, and Business Logic.

Strict Typing: Uses pydantic and typing for robust data validation.

Defensive Programming: Path dependency checks and error handling are built-in.

📜 License / 授權
MIT License. Feel free to use and improve this shield.
