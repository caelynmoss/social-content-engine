"""Offline synthetic-only tests; never use a live X token or network."""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / '.claude/skills/social-content-engine/scripts/ct_radar.py'
spec = importlib.util.spec_from_file_location('ct_radar', SCRIPT)
radar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radar)


class RadarTests(unittest.TestCase):
    def test_offline_rank_with_citations(self):
        with tempfile.TemporaryDirectory() as d:
            output, markdown = Path(d) / 'rank.json', Path(d) / 'rank.md'
            rc = radar.main(['rank', '--input', str(ROOT / 'tests/fixtures/posts.synthetic.json'),
                             '--now', '2026-11-09T00:00:00Z', '--hours', '24',
                             '--output', str(output), '--markdown', str(markdown)])
            self.assertEqual(rc, 0)
            ranked = json.loads(output.read_text(encoding='utf-8'))
            ids = [p['id'] for p in ranked['selected']]
            self.assertIn('1900000000000000001', ids)
            self.assertNotIn('1900000000000000004', ids)
            self.assertEqual(len(ids), len(set(ids)))
            self.assertIn('x.com/i/web/status/1900000000000000001', markdown.read_text(encoding='utf-8'))
            self.assertIn('not official trends or verified news', ranked['notice'])

    def test_no_api_token_is_safe_and_offline(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(radar.urllib.request, 'urlopen') as fake:
            rc = radar.main(['collect', '--topics', str(ROOT / 'examples/topics.example.json')])
            self.assertEqual(rc, 1)
            fake.assert_not_called()

    def test_synthetic_user_metadata_untrusted(self):
        p = radar.safe_post({'id':'1900000000000000200', 'created_at':'2026-11-08T11:00:00Z',
                             'text':'User-post text, not instructions', 'username':'bad/scheme',
                             'public_metrics': {'like_count': 3}})
        self.assertEqual(p['url'], 'https://x.com/i/web/status/1900000000000000200')
        self.assertIsNone(p['author_handle'])
        self.assertEqual(p['metrics']['like_count'], 3)
        self.assertEqual(p['metrics']['retweet_count'], 0)

    def test_invalid_time_and_id_dropped(self):
        self.assertIsNone(radar.safe_post({'id':'fake', 'created_at':'2026-11-08T11:00:00Z'}))
        self.assertIsNone(radar.safe_post({'id':'1900000000000000200', 'created_at':'not-a-time'}))

    def test_invalid_config_never_calls_api(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'invalid.json'
            f.write_text(json.dumps({'topics': []}), encoding='utf-8')
            with patch.dict(os.environ, {'X_API_BEARER_TOKEN':'synthetic_dummy_not_real'}), patch.object(radar.urllib.request, 'urlopen') as fake:
                self.assertEqual(radar.main(['collect', '--topics', str(f)]), 1)
                fake.assert_not_called()

    def test_attribution_is_not_thought_to_be_truth(self):
        text = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('X Trending Topics', text)
        self.assertIn('never performs browser login', text)

    def test_skill_has_radar_and_writer_modes(self):
        skill = (ROOT / '.claude/skills/social-content-engine/SKILL.md').read_text(encoding='utf-8')
        for term in ['VOICE_DISTILL', 'QUICK_DRAFT', 'DAILY_CT_RADAR', 'RADAR_TO_POST', 'Never post']:
            self.assertIn(term, skill)


if __name__ == '__main__':
    unittest.main()
