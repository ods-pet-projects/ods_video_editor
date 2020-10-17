import unittest

from movie_dsl import MovClass


class TestMovDSL(unittest.TestCase):
    def test_parse_expr(self):
        examples = [
            ('hb[3:21].v', ('hb', '[3:21]', 'v', '')),
            ('hb[3:21].v.resize(640,360)', ('hb', '[3:21]', 'v', 'resize(640,360)')),
            ('hb.v', ('hb', '', 'v', '')),
            ('hb.v.resize(640,360)', ('hb', '', 'v', 'resize(640,360)'))
        ]
        for expr, ans in examples:
            pred = MovClass.get_expr_parts(expr)
            self.assertEqual(ans, pred)
