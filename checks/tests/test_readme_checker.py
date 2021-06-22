import unittest
import os
from checks.check_readmes import ReadmeChecker, MissingReadmeError

class TestReadmeChecker(unittest.TestCase):
    def test_setup_topic_readmes_presence(self):
        modules_path = os.path.join(
            os.path.dirname(__file__),
            'fixtures',
            'Green-Syllabus')
        paths = ReadmeChecker(modules_path).run()
        path = f'{modules_path}/00-Setup/01-First-Challenge'
        self.assertIn(path, paths)

    def test_any_topic_readmes_presence(self):
        modules_path = os.path.join(os.path.dirname(__file__), 'fixtures',
                                    'Green-Syllabus')
        paths = ReadmeChecker(modules_path).run()
        path = f'{modules_path}/01-First-Module/01-First-Topic/01-First-Challenge'
        self.assertIn(path, paths)

    def test_readmes_count(self):
        modules_path = os.path.join(os.path.dirname(__file__), 'fixtures',
                                    'Green-Syllabus')
        paths = ReadmeChecker(modules_path).run()
        self.assertEqual(len(paths), 4)

    def test_readmes_absence(self):
        modules_path = os.path.join(os.path.dirname(__file__), 'fixtures',
                                    'Red-Syllabus')
        try:
            paths = ReadmeChecker(modules_path).run()
        except MissingReadmeError as error:
            self.assertIsInstance(error, MissingReadmeError)
