import idna
import unicodedata
import logging
from typing import List, Dict
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

# --- 1. 配置層 (Configuration) ---
class AppConfig(BaseModel):
    ALLOWED_SCRIPTS: List[str] = Field(default_factory=lambda: ["Latin"])
    LOG_LEVEL: str = "INFO"

config = AppConfig()

# --- 2. 介面層 (Interfaces) ---
class IDomainAnalyzer(ABC):
    @abstractmethod
    def analyze(self, domain: str) -> Dict[str, any]:
        pass

# --- 3. 業務邏輯層 (Business Logic) ---
class HomographDetector(IDomainAnalyzer):
    def __init__(self, allowed_scripts: List[str]):
        self._allowed_scripts = set(allowed_scripts)
        self._logger = logging.getLogger(self.__class__.__name__)

    def analyze(self, domain: str) -> Dict[str, any]:
        self._logger.info(f"Analyzing domain: {domain}")
        try:
            punycode = idna.encode(domain).decode('ascii')
        except idna.IDNAError:
            return {"status": "invalid", "reason": "Invalid domain encoding"}

        is_idn = domain != punycode
        scripts_found = self._identify_scripts(domain)
        is_mixed_script = len(scripts_found) > 1
        risk_level = "HIGH" if (is_idn and is_mixed_script) else "LOW"

        return {
            "original_display": domain,
            "punycode_actual": punycode,
            "is_idn": is_idn,
            "scripts_detected": list(scripts_found),
            "is_mixed_script": is_mixed_script,
            "risk_assessment": risk_level,
            "explanation": self._generate_reason(is_idn, is_mixed_script, punycode)
        }

    def _identify_scripts(self, text: str) -> set:
        scripts = set()
        for char in text:
            if char == '.':
                continue
            try:
                name = unicodedata.name(char)
                script = name.split()[0]
                scripts.add(script)
            except ValueError:
                continue
        return scripts

    def _generate_reason(self, is_idn: bool, is_mixed: bool, punycode: str) -> str:
        if is_idn and is_mixed:
            return f"Critical: Domain mixes multiple scripts (e.g. Latin & Cyrillic). True domain is {punycode}"
        if is_idn:
            return f"Notice: This is an International Domain (IDN). True domain is {punycode}"
        return "Safe: Standard ASCII domain."

# --- 4. 進入點 (Entry Point) ---
def main():
    logging.basicConfig(level=config.LOG_LEVEL)
    detector: IDomainAnalyzer = HomographDetector(allowed_scripts=config.ALLOWED_SCRIPTS)
    test_cases = [
        "apple.com",
        "аpple.com",  # 釣魚 (Cyrillic 'a')
        "google.com",
        "googIe.com", # 視覺混淆
        "xn--pple-43d.com" # 轉碼釣魚網址
    ]

    print(f"{'Domain':<15} | {'Risk':<5} | {'True Address (Punycode)':<20} | {'Scripts'}")
    print("-" * 80)
    for domain in test_cases:
        try:
            domain_for_analysis = idna.decode(domain) if domain.startswith("xn--") else domain
            result = detector.analyze(domain_for_analysis)
            print(f"{domain:<15} | {result['risk_assessment']:<5} | {result['punycode_actual']:<20} | {result['scripts_detected']}")
        except Exception as e:
            logging.error(f"Failed to analyze {domain}: {e}")

if __name__ == "__main__":
    main()