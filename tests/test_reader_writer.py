import os
import sys
import tempfile
import unittest

import excelcsv

if sys.version_info[0] > 2:
    import io

    text_type = str
    StringIO = io.StringIO

else:
    import StringIO

    text_type = unicode
    StringIO = StringIO.StringIO


class TestReader(unittest.TestCase):

    def test_read(self):
        csv = [
            u'a,b,c',
            u'd,e,f'
        ]
        rows = list(excelcsv.reader(csv))
        for row in rows:
            for x in row:
                self.assertIsInstance(x, text_type)
        expect = [
            [u'a', u'b', u'c'],
            [u'd', u'e', u'f'],
        ]
        self.assertListEqual(rows, expect)


class TestWriter(unittest.TestCase):

    def test_write(self):
        io = StringIO()
        writer = excelcsv.writer(io)
        writer.writerow([u'a', u'b', u'c'])
        writer.writerow([u'd', u'e', u'f'])

        value = io.getvalue()
        self.assertIsInstance(value, text_type)
        self.assertEqual(value, u'a,b,c\r\nd,e,f\r\n')

        io.close()


class TestReadExcel(unittest.TestCase):

    def setUp(self):
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, 'wb') as f:
            f.write(u'a\tb\tc\rd\te\tf\r'.encode('utf-16'))
        self.path = path

    def tearDown(self):
        os.remove(self.path)

    def test_read_excel(self):
        with excelcsv.read_excel_tsv(self.path) as reader:
            rows = list(reader)

        for row in rows:
            for x in row:
                self.assertIsInstance(x, text_type)
        expect = [
            [u'a', u'b', u'c'],
            [u'd', u'e', u'f'],
        ]
        self.assertListEqual(rows, expect)


class TestWriteExcel(unittest.TestCase):

    def setUp(self):
        _, path = tempfile.mkstemp()
        self.path = path

    def tearDown(self):
        os.remove(self.path)

    def test_read_excel(self):
        with excelcsv.write_excel_tsv(self.path) as writer:
            writer.writerow([u'a', u'b', u'c'])
            writer.writerow([u'd', u'e', u'f'])

        expect = u'a\tb\tc\r\nd\te\tf\r\n'.encode('utf-16')
        with open(self.path, 'rb') as f:
            actual = f.read()
        self.assertEqual(actual, expect)
