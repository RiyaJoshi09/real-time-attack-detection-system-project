import unittest
from detection_engine import detect_attack

class AttackDetectionTestCase(unittest.TestCase):

    def test_script_tag(self):
        payload = {"input": "<script>alert('XSS')</script>"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)<script.*?>.*?</script>", result)

    def test_union_select(self):
        payload = {"query": "UNION SELECT * FROM users"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)union\s+select", result)

    def test_or_1_equals_1(self):
        payload = {"login": "admin' OR 1=1 --"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)or\s+1=1", result)

    def test_drop_table(self):
        payload = {"input": "DROP TABLE users"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)drop\s+table", result)

    def test_etc_passwd(self):
        payload = {"url": "/etc/passwd"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)etc/passwd", result)

    def test_single_quote_or(self):
        payload = {"input": "' or '1'='1"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)' or '1'='1", result)

    def test_alert_function(self):
        payload = {"script": "alert('hi')"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)alert\(.*?\)", result)

    def test_select_star(self):
        payload = {"query": "SELECT * FROM users"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)select\s+\*\s+from", result)

    def test_insert_into(self):
        payload = {"data": "INSERT INTO accounts VALUES(...)"} 
        result = detect_attack(payload)
        self.assertIn(r"(?i)insert\s+into", result)

    def test_exec_xp_cmdshell(self):
        payload = {"command": "exec xp_cmdshell 'dir'"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)exec\s+xp_cmdshell", result)

    def test_benchmark_function(self):
        payload = {"query": "benchmark(1000000,sha1('test'))"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)benchmark\s*\(", result)

    def test_load_file_function(self):
        payload = {"query": "load_file('/etc/passwd')"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)load_file\s*\(", result)

    def test_outfile_usage(self):
        payload = {"sql": "SELECT * INTO OUTFILE '/tmp/file.txt'"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)outfile\s+'", result)

    def test_sql_comment_double_dash(self):
        payload = {"query": "SELECT * FROM users --"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)--", result)

    def test_sql_comment_hash(self):
        payload = {"query": "SELECT * FROM users #"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)#", result)

    def test_iframe_injection(self):
        payload = {"html": "<iframe src='malicious.html'></iframe>"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)<iframe.*?>", result)

    def test_img_onerror_xss(self):
        payload = {"html": "<img src=x onerror=alert('xss')>"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)<img\s+src=.*?onerror=", result)

    def test_document_cookie(self):
        payload = {"script": "document.cookie"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)document\.cookie", result)

    def test_meta_http_equiv(self):
        payload = {"html": "<meta http-equiv='refresh' content='0;url=evil.com'>"}
        result = detect_attack(payload)
        self.assertIn(r"(?i)<meta\s+http-equiv", result)

    def test_clean_payload(self):
        payload = {"username": "safeuser", "password": "safepassword"}
        result = detect_attack(payload)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
