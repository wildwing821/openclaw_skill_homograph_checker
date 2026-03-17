# Homograph Domain Checker Plugin

In the digital realm, "visual similarity" is often a veil for impurity. This high-fidelity security utility is designed to detect Internationalized Domain Name (IDN) Homograph attacks, identifying malicious attempts where attackers mix different scripts (e.g., Cyrillic 'а' vs. Latin 'a') to deceive users.

## Why Homograph Domain Checker?

Visual deception is a primary vector for phishing. By analyzing the underlying Unicode script consistency, this tool acts as a "Purity Firewall," ensuring that your AI Agent can identify hidden threats before any browser interaction or data fetching occurs.

## Skill Marketplace (homograph_checker)

This plugin provides a mandatory security checkpoint for any web-based workflow:

| Skill Mode | Core Capability | Integration Workflow |
| :--- | :--- | :--- |
| **Analyze** | Detects mixed scripts, resolves Punycode, and performs high-precision risk assessment. | **Mandatory**: Must be invoked before `browser` navigation or `web_fetch` on suspicious URLs. |

## Getting Started

### Prerequisites
Maintain a purified environment with the following dependencies:
* **Libraries**: `idna`, `pydantic`.
* **Architecture**: Python 3.x with support for `unicodedata`.

### Installation & Usage
```bash
# 1. Install necessary components
pip install idna pydantic

# 2. Execute the built-in test suite to verify integrity
python3 /app/.openclaw/workspace/skills/homograph_checker/checker.py
```

### Critical Integration Rule
If the `risk_assessment` returns **'HIGH'**, the Agent is strictly prohibited from proceeding with the URL. The user must be notified immediately.

## Project Structure

The project strictly adheres to a layered architecture, ensuring the separation of concerns and logic purity:

```text
homograph_checker/
├── checker.py               # Core implementation (Config, Interface, Logic)
├── SKILL.md                 # Metadata and Agent integration rules
└── README.md                # Technical overview and design philosophy
```

## Core Engineering Philosophy

### 1. Layered Defense & Dependency Inversion
* **Configuration Layer**: Uses `AppConfig (Pydantic)` for type-safe environment management.
* **Interface Layer**: Defines `IDomainAnalyzer (ABC)`, allowing the core logic to depend on abstractions rather than low-level implementations.

### 2. Type Safety & Contractual Purity
* **Strict Typing**: Full implementation of Python Type Hints and Pydantic for data validation.
* **Zero Magic Numbers**: Risk levels and script permissions are managed through structured domain models.

### 3. Professional Observability
* **Forbidden `print()`**: The business logic utilizes `logging` with configurable levels (e.g., `INFO`) instead of standard print statements for professional system auditing.

### 4. Defensive Initialization (Path Dependency)
* While the current logic focuses on computation, the deployment follows the **Path Dependency Trap** protocol: always verify the skill's location at `/app/.openclaw/workspace/skills/homograph_checker/` before execution.

------------------------------------------------------------------------------------------------------------

# 同形異義字網域檢查器插件 (Homograph Domain Checker Plugin)

在數位世界中，「視覺相似」往往是汙穢（惡意攻擊）的偽裝。本工具是一款高精度的安全防禦組件，專為偵測 IDN 同形異義字欺騙攻擊而設計。它能精準識別攻擊者利用不同語系字元（如西里爾字母 'а' 與拉丁字母 'a'）所構建的釣魚網域。

## 為什麼需要同形異義字檢查

視覺欺騙是網路釣魚的核心手段之一。透過分析底層的 Unicode 腳本一致性，本工具能建立一道「純淨防火牆」，確保您的 AI Agent 在執行瀏覽或抓取動作前，能先行穿透偽裝並識別潛在威脅。

## 技能矩陣 (Skill Marketplace: homograph_checker)

本插件為所有涉及網路存取的工作流提供強制性的安全審查節點：

| 技能模式 | 核心能力 | 建議工作流 |
| :--- | :--- | :--- |
| **Analyze** | 執行多語系腳本偵測、Punycode 自動還原，並產出高精度的風險評估報告。 | **強制要求**：在透過 `browser` 導覽或對可疑 URL 執行 `web_fetch` 前必須調用。 |

## 快速上手 (Getting Started)

### 環境要求
請確保您的執行環境已配置以下必要依賴，維持系統的純確性：
* **核心套件**：`idna`, `pydantic`。
* **架構環境**：支援 `unicodedata` 模組的 Python 3.x 環境。

### 安裝與執行
```bash
# 1. 淨化環境並安裝必要組件
pip install idna pydantic

# 2. 執行內建測試案例以驗證系統穩定性
python3 /app/.openclaw/workspace/skills/homograph_checker/checker.py
```

### 關鍵整合規則
若風險評估結果回傳為 **'HIGH'**，系統嚴禁繼續存取該網址，且必須立即通知使用者。

## 專案結構 (Project Structure)

本插件嚴格遵守分層架構設計，確保各層邏輯完全解耦：

```text
homograph_checker/
├── checker.py               # 核心實作（包含配置層、介面層與業務邏輯）
├── SKILL.md                 # AI Agent 整合規範與元數據
└── README.md                # 技術概覽與設計哲學
```

## 核心設計哲學

### 1. 分層防禦與依賴反轉 (DIP)
* **配置層**：使用 `AppConfig (Pydantic)` 進行強型別的環境參數管理。
* **介面層**：定義 `IDomainAnalyzer (ABC)` 抽象類別，使核心邏輯依賴於抽象介面而非具體實作，提升系統擴充性。

### 2. 類型安全與契約精神 (Type Safety)
* **嚴格型別**：全面導入 Python Type Hints 與 Pydantic 模型進行資料驗證。
* **拒絕魔法數字**：風險等級與許可腳本皆透過結構化的領域模型進行定義。

### 3. 專業級可觀測性 (Observability)
* **禁用 print()**：業務邏輯層採用標準 `logging` 模組，支援可配置的日誌等級（如 `INFO`），滿足專業系統審計需求。

### 4. 防禦性啟動原則 (Path Dependency)
* 部署與調用必須嚴格遵守 **「路徑依賴陷阱」** 審查，確保在執行前已確認 `/app/.openclaw/workspace/skills/homograph_checker/` 目錄的絕對存在。

