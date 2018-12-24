import os
from . import records
from .recordreader import RecordReader


class StringTable(object):
    def __init__(self, fp):
        self._reader = RecordReader(fp)
        self._parse()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __getitem__(self, key):
        return self._strings[key]

    def _parse(self):
        strings = list()
        self._reader.seek(0, os.SEEK_SET)
        for rectype, rec in self._reader:
            if rectype == records.SST_ITEM:
                strings.append(rec.t)
            elif rectype == records.END_SST:
                break
        self._strings = strings

    def get_string(self, idx):
        return self._strings[idx]

    def close(self):
        self._reader.close()
