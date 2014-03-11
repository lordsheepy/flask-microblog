import unittest
from microblog import app
import config


class WritePostTests(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestingConfig')

    def tearDown(self):
        pass

    def test_write_post(self):
        pass

    def test_write_post_empty_title(self):
        pass

    def test_write_post_title_long(self):
        pass

    def test_write_post_empty_text(self):
        pass


class ReadPostsAndReadPostTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_post(self):
        pass

    def test_read_posts(self):
        pass

if __name__ == '__main__':
    unittest.main()
