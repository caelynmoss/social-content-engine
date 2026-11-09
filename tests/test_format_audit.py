import csv
import tempfile
import unittest
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]/'.claude/skills/social-content-engine'
spec=importlib.util.spec_from_file_location('format_audit', ROOT/'scripts/format_audit.py')
fmt=importlib.util.module_from_spec(spec);spec.loader.exec_module(fmt)

class FormatAuditTests(unittest.TestCase):
    def test_article_winner_is_account_specific_and_excludes_reposts(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'private.csv'
            with open(p,'w',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=['account_id','format','category','is_original','views']);writer.writeheader()
                for _ in range(6):writer.writerow(dict(account_id='official',format='ARTICLE',category='analysis',is_original='true',views=11000))
                for _ in range(7):writer.writerow(dict(account_id='official',format='SHORT_POST',category='analysis',is_original='true',views=500))
                for _ in range(15):writer.writerow(dict(account_id='official',format='SHORT_POST',category='analysis',is_original='false',views=900000))
                for _ in range(8):writer.writerow(dict(account_id='personal',format='SHORT_POST',category='analysis',is_original='true',views=30000))
            result=fmt.summarize(p,'official',category='analysis',min_n=5)
            self.assertEqual(result['winning_format'],'ARTICLE')
            self.assertEqual(result['summary']['SHORT_POST']['n'],7)
            self.assertEqual(fmt.summarize(p,'personal',category='analysis',min_n=5)['winning_format'],'UNKNOWN / TEST NEEDED')
    def test_no_unverified_single_format_win(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'private.csv';p.write_text('account_id,format,category,is_original,views\na,ARTICLE,analysis,true,100000\n')
            self.assertEqual(fmt.summarize(p,'a')['winning_format'],'UNKNOWN / TEST NEEDED')
    def test_profile_starts_with_account_winning_format(self):
        t=(ROOT/'assets/account-profile-template.md').read_text()
        self.assertTrue(t.startswith('**WINNING FORMAT'))
        source=(ROOT/'assets/approved-source-register-template.md').read_text()
        self.assertIn('APPROVED_PUBLIC',source)
        body=(ROOT/'SKILL.md').read_text()
        for phrase in ['ARTICLE','ACCOUNT_ALIGN','ROUTE_CONTENT','Approved facts have a home','WINNING FORMAT']:
            self.assertIn(phrase,body)
        self.assertIn('first', (ROOT/'references/format-performance.md').read_text().lower())
if __name__=='__main__':unittest.main()
