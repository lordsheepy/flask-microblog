import unittest
import os
os.environ['FLASK_MODE'] = os.getenv('FLASK_MODE') or 'testing'
import microblog
import config
from flask.ext.sqlalchemy import SQLAlchemy


class WritePostTests(unittest.TestCase):

    def setUp(self):
        microblog.db.create_all()

    def tearDown(self):
        microblog.db.session.close()
        microblog.db.drop_all()

    def test_write_post(self):
        post = microblog.Post('this is a title', 'wordswouldgohere')
        microblog.db.session.add(post)
        microblog.db.session.commit()
        self.assertEqual(str(microblog.Post.query.one()),
                         "<post u'this is a title'>")

    def test_write_post_title_long(self):
        post = microblog.Post('this title is far to long and cannot really\
            be represented within the length provided and will therefor raise\
            an error when put into my database', 'nuthin')
        self.assertRaises(microblog.db.session.add(post))

    def test_write_post_empty_text(self):
        post = microblog.Post('title', None)
        self.assertRaises(microblog.db.session.add(post))


class ReadPostsAndReadPostTests(unittest.TestCase):

    def setUp(self):
        microblog.db.create_all()
        oldest = microblog.Post('oldest', 'text of oldest')
        middle = microblog.Post('middle', 'text of middle')
        newest = microblog.Post('newest', 'text of newest')
        microblog.db.session.add(oldest)
        microblog.db.session.add(middle)
        microblog.db.session.add(newest)
        microblog.db.session.commit()

    def tearDown(self):
        microblog.db.session.close()
        microblog.db.drop_all()

    def test_read_post(self):
        self.assertTrue(microblog.read_post(1))

    def test_read_posts(self):
        self.assertEqual(len(microblog.read_posts()), 3)

class TestListView(unittest.TestCase):

    def setUp(self):


if __name__ == '__main__':
    unittest.main()
