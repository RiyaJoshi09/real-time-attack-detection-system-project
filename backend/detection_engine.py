import re
import json
from typing import Union

SUSPICIOUS_PATTERNS = [
    r"(?i)<script.*?>.*?</script>",
    r"(?i)union\s+select",
    r"(?i)or\s+1=1",
    r"(?i)drop\s+table",
    r"(?i)etc/passwd",
    r"(?i)' or '1'='1",
    r"(?i)alert\(.*?\)",
    r"(?i)select\s+\*\s+from",
    r"(?i)insert\s+into",
    r"(?i)exec\s+xp_cmdshell",
    r"(?i)benchmark\s*\(",
    r"(?i)load_file\s*\(",
    r"(?i)outfile\s+'",
    r"(?i)--",                         # SQL comment
    r"(?i)#",                          # Another comment
    r"(?i)<iframe.*?>",               # iframe injection
    r"(?i)<img\s+src=.*?onerror=",    # XSS via img onerror
    r"(?i)document\.cookie",
    r"(?i)<meta\s+http-equiv",        # Meta tag injection
]

def detect_attack(payload: Union[str, dict]) -> list:
    """
    Detects suspicious patterns in a given payload.
    Accepts either a JSON string or a dictionary.
    """
    if isinstance(payload, dict):
        payload = json.dumps(payload)

    matches = []
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, payload):
            matches.append(pattern)
    return matches
