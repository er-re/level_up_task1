import unittest

from sanitize import Sanitize
from post import Post


class TestSanitizeClass(unittest.TestCase):
    def test_escape_html_angle_brackets(self):
        sanitize = Sanitize('<span>', False, '')
        self.assertEqual(sanitize.string, '&lt;span&gt;')

    def test_escape_html_ampersand(self):
        sanitize = Sanitize('&lorem', False, '')
        self.assertEqual(sanitize.string, '&amp;lorem')

    def test_escape_html_double_quote(self):
        sanitize = Sanitize('&"', False, '')
        self.assertEqual(sanitize.string, '&amp;&quot;')

    def test_sanitize_markdown_using_scape(self):
        sanitize = Sanitize('#topic', False, '')
        self.assertEqual(sanitize.string, 'topic')

    def test_remove_html_span(self):
        sanitize = Sanitize('<span>hi</span>', True, '')
        self.assertEqual(sanitize.string, 'hi')

    def test_remove_html_has_ampersand(self):
        sanitize = Sanitize('<p1>&hi&<p1>', True, '')
        self.assertEqual(sanitize.string, '&hi&')

    def test_escape_html_has_bad_chars(self):
        sanitize = Sanitize('<img src="myphoto.jpg" alt="My Photo"> <p>1000$</p>', False, '@#$%^')
        self.assertEqual(sanitize.string, '&lt;img src=&quot;myphoto.jpg&quot; alt=&quot;My Photo&quot;&gt; &lt;p&gt;1000&lt;/p&gt;')

    def test_remove_html_has_bad_chars(self):
        sanitize = Sanitize('<img src="myphoto.jpg" alt="My Photo"><p>1000$</p>', True, '@#$%^')
        self.assertEqual(sanitize.string, '1000')


class TestPostClass(unittest.TestCase):
    def test_post_request(self):
        post = Post('http://jsonplaceholder.typicode.com/posts', 'test')
        self.assertTrue(post.success)


if __name__ == '__main__':
    unittest.main()
