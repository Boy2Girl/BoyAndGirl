import datetime


class DateEncoderUtil:

    def changeDate(self, params):
        param = params.__dict__
        for i in param:
            if isinstance(param[i], datetime.date):
                param[i] = param[i].__str__()
        return param


