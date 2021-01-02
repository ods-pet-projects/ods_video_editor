import unittest

from movie_dsl.movie_dsl import MovClass


class TestMovDSL(unittest.TestCase):
    def test_parse_expr(self):
        examples = [
            ('hb[3:21].v', ('hb', '[3:21]', 'v', '')),
            ('hb[3:21].v.resize(640,360)', ('hb', '[3:21]', 'v', 'resize(640,360)')),
            ('hb.v', ('hb', '', 'v', '')),
            ('hb.v.resize(640,360)', ('hb', '', 'v', 'resize(640,360)')),
            ('hb.v.volume(2)', ('hb', '', 'v', 'volume(2)'))
        ]
        for expr, ans in examples:
            pred = MovClass.get_expr_parts(expr)
            self.assertEqual(ans, pred)

    def test_parse_volume_cmd(self):
        examples = (('volume(2)', 2),
                    ('volume(1.5)', 1.5),
                    )

        for cmd, ans in examples:
            pred = MovClass.parse_volume_cmd(cmd)
            self.assertEqual(ans, pred)

    def test_parse_resize_cmd(self):
        cmd_list = [('resize(640,360)', (640, 360)),
                    ('resize(1024, 768)', (1024, 768)),
                    ('resize(123,  12)', (123, 12)),
                    ]
        for cmd, true in cmd_list:
            pred = MovClass.parse_resize_cmd(cmd)
            self.assertEqual(true, pred)
