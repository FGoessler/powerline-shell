from ..utils import BasicSegment
import os
import datetime

class Segment(BasicSegment):
    def add_to_powerline(self):
        expDate = os.environ.get("AWS_EXPIRATION_DATE")
        if expDate:
            now = datetime.datetime.now();
            exp = datetime.datetime.strptime(expDate, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=2)
            diff = exp - now
            if diff.total_seconds() > 0:
                scloud_state = ':'.join(str(diff).split(':')[:2])
                self.powerline.append(" AWS %s " % scloud_state, 15, 2)
            else:
                self.powerline.append(" AWS *EXP* ", 15, 1)
        else:
            self.powerline.append(" AWS - ", 15, 1)
