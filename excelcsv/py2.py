import cStringIO as StringIO
import csv


def _utf8_encoder(unicode_line):
    for line in unicode_line:
        yield line.encode('utf-8')


class reader(object):

    def __init__(self, f, dialect=csv.excel, **kwds):
        f = _utf8_encoder(f)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
        self.line_num = 0

    def next(self):
        row = self.reader.next()
        self.line_num += 1
        return [s.decode('utf-8') for s in row]

    def __iter__(self):
        return self


class writer(object):

    def __init__(self, f, dialect=csv.excel, **kwds):
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f

    def writerow(self, row):
        encoded = [x.encode('utf-8') for x in row]
        self.writer.writerow(encoded)
        data = self.queue.getvalue()
        data = data.decode('utf-8')
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class DictReader(csv.DictReader):

    def __init__(self, f, fieldnames=None, *args, **kwds):
        csv.DictReader.__init__(self, f, fieldnames=fieldnames, *args, **kwds)
        self.reader = reader(f, *args, **kwds)


class DictWriter(csv.DictWriter):

    def __init__(self, f, fieldnames, dialect='excel', *args, **kwds):
        csv.DictWriter.__init__(self, f, fieldnames, *args, **kwds)
        self.writer = writer(f, dialect, *args, **kwds)
