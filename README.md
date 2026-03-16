Homograph Domain Checker
Introduction
In the digital realm, "visual similarity" is often a veil for impurity. This tool is a high-fidelity security utility designed to detect Internationalized Domain Name (IDN) Homograph attacks. It identifies malicious attempts where attackers mix different scripts (e.g., Cyrillic 'а' vs. Latin 'a') to deceive users.

Core Principles
This project adheres to strict software engineering standards:

Layered Architecture: Clear separation between Configuration, Interfaces, and Business Logic.

Type Safety: Full implementation of Python Type Hints and Pydantic for robust data validation.

Dependency Inversion: High-level logic depends on abstractions (IDomainAnalyzer), not low-level implementations.

Features
Multi-Script Detection: Analyzes Unicode characters to identify script mixing (e.g., Latin, Cyrillic, Greek).

Punycode Decoding: Automatically resolves xn-- prefixes to their true ASCII representation.

Risk Assessment: Categorizes domains as "HIGH" or "LOW" risk based on IDN status and script consistency.

Logging System: Structured logging instead of standard print statements for professional observability.

Installation
Ensure your environment is purified with the following dependencies:

Bash
pip install idna pydantic
Usage
You can execute the checker directly to run the built-in test suite:

Bash
python3 checker.py
For integration as a skill:

Location: /app/.openclaw/workspace/skills/homograph_checker/

Workflow: Use this skill before any browser navigation or web_fetch operations on suspicious URLs.


同形異義字網域檢查器 (Homograph Checker)
簡介
在數位世界中，「視覺相似」往往是汙穢（惡意攻擊）的偽裝。本工具是一款高精度的安全組件，專門用於偵測 IDN 同形異義字欺騙攻擊。它能精準識別攻擊者利用不同語系字元（如西里爾字母 'а' 與拉丁字母 'a'）所構建的釣魚網域。

設計核心原則
本專案嚴格遵守最高規格的工程規範，確保程式碼的純淨與可維護性：

分層架構：嚴格區分配置層 (Config)、介面層 (Interface) 與業務邏輯層 (Business Logic)。

類型安全：全面導入 Python Type Hints，並使用 Pydantic 進行嚴格的資料模型驗證。

依賴反轉 (DI)：核心邏輯依賴於抽象介面 IDomainAnalyzer，實踐低耦合設計。

核心功能
多語系腳本偵測：分析 Unicode 字元，識別是否存在跨語系混合（如 Latin 與 Cyrillic 混用）。

Punycode 自動解析：自動將 xn-- 開頭的轉碼網域還原為真實地址。

風險評估機制：根據 IDN 狀態與語系一致性，自動判定風險等級（HIGH/LOW）。

專業日誌系統：捨棄 print()，採用標準 logging 模組，提升系統的可觀測性。

安裝需求
請確保您的執行環境已配置以下必要依賴：

Bash
pip install idna pydantic
執行與整合
直接執行腳本即可啟動內建的測試案例：

Bash
python3 checker.py
作為 OpenClaw Skill 整合時：

組件位置：/app/.openclaw/workspace/skills/homograph_checker/

建議工作流：在進行任何 browser 瀏覽或 web_fetch 抓取可疑 URL 之前，必須先調用此工具進行審查。
