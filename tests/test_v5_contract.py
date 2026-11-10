"""Static V5 contract checks: not an LLM-quality benchmark."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.claude/skills/social-content-engine'


class V5ContractTests(unittest.TestCase):
    def test_v5_entrypoint_modes_and_research(self):
        body = (SKILL / 'SKILL.md').read_text(encoding='utf8')
        for value in ('Insight & Voice Engine (V5)', 'IDEA_EXPAND', 'WRITING_MODE',
                      'RESEARCH_SUPPORT', 'HUMAN_EDIT', 'EDITORIAL_MEMORY',
                      'PROFESSIONAL', 'CONVERSATIONAL', 'RESEARCH_DRIVEN',
                      'OPINIONATED', 'BUILDERS_NOTES', 'R0', 'R1', 'R2',
                      'Information Gain', 'ARTICLE', 'DAILY_CT_RADAR'):
            with self.subTest(value=value):
                self.assertIn(value, body)
        self.assertIn('Never replace X-post evidence with generic news articles', body)
        self.assertIn('Only run when the user asks', body)

    def test_all_progressive_references_exist(self):
        p = SKILL / 'SKILL.md'
        body = p.read_text(encoding='utf8')
        for name in ('idea-expansion', 'writing-modes', 'information-gain',
                     'research-depth', 'human-voice-editor', 'editorial-memory'):
            path = SKILL / 'references' / (name + '.md')
            self.assertTrue(path.is_file(), name)
            self.assertIn('references/' + name + '.md', body)
        for name in ('editorial-memory-template', 'information-gain-card-template',
                     'writing-options-template'):
            self.assertTrue((SKILL / 'assets' / (name + '.md')).is_file())

    def test_research_integrity_and_user_consent(self):
        r = (SKILL / 'references/research-depth.md').read_text(encoding='utf8')
        v = (SKILL / 'references/human-voice-editor.md').read_text(encoding='utf8')
        m = (SKILL / 'references/editorial-memory.md').read_text(encoding='utf8')
        self.assertIn('UNVERIFIED', r)
        self.assertIn('actual retrievable evidence', r.lower())
        self.assertIn('Never invent', v)
        self.assertIn('explicit', m)
        self.assertIn('private', m)

    def test_docs_are_bilingual_and_article_retained(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf8')
        self.assertLess(readme.index('## 中文'), readme.index('## English'))
        for term in ('Writing Mode', 'Information Gap', 'Humanity Fingerprint',
                     'R0', 'R1', 'R2', 'Article', 'never performs browser login', 'X Trending Topics'):
            # legacy README expectations, plus V5 descriptions
            self.assertIn(term, readme)
        self.assertFalse((ROOT / 'routines/daily-radar.prompt.md').exists())

if __name__ == '__main__':
    unittest.main()
