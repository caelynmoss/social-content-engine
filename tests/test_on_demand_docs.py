"""Ensure Crypto Twitter Radar is user-triggered and sourced only from X posts."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'.claude/skills/social-content-engine'
class OnDemandDocsTests(unittest.TestCase):
    def test_no_schedule_entrypoint(self):
        self.assertFalse((ROOT/'routines/daily-radar.prompt.md').exists())
        self.assertFalse((SKILL/'references/automation-and-x-policy.md').exists())
        for path in ['README.md','README.zh-CN.md','docs/SETUP_ZH.md','docs/SETUP_EN.md','.claude/skills/social-content-engine/SKILL.md']:
            s=(ROOT/path).read_text(encoding='utf8')
            self.assertNotIn('/schedule',s)
            self.assertNotIn('routines/daily-radar.prompt.md',s)
    def test_sources_and_fallback(self):
        t=(SKILL/'SKILL.md').read_text(encoding='utf8')
        self.assertIn('Live discovery order',t)
        self.assertIn('Never replace X-post evidence with generic news articles',t)
        self.assertIn('radar runs only when requested',t)
