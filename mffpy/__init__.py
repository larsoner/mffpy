
from . import xml_files
from . import bin_files
from .mffdir import MFFDirectory

class Reader(MFFDirectory):

    @property
    def sampling_rates(self):
        return {
            fn: bin_file.sampling_rate
            for fn, bin_file in self.blobs.items()
        }

    @property
    def durations(self):
        return {
            fn: bin_file.duration
            for fn, bin_file in self.blobs.items()
        }

    @property
    def startdatetime(self):
        try:
            return self._startdatetime
        except AttributeError:
            info = xml_files.open(self.filename('info'))
            self._startdatetime = info.recordTime
        return self.startdatetime

    @property
    def blobs(self):
        """return dictionary of `BinFile` data readers by signal type"""
        try:
            return self._blobs
        except AttributeError:
            self._blobs = {}
            for si in self.signals_with_info():
                bf = bin_files.BinFile(si.signal, si.info)
                self._blobs[bf.signal_type] = bf
        return self.blobs

    def get_physical_samples(self, t0, dt, channels=None):
        """return signal data in the range `(t0, t0+dt)` in seconds from
        `channels`"""
        if channels is None:
            channels = list(self.blobs.keys())

        return {
            typ: blob.read_raw_samples(t0, dt)
            for typ, blob in self.blobs.items()
            if typ in channels
        }
