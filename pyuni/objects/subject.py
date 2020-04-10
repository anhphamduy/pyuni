class Subject:

    def __init__(self, name, code, period, sessions):
        self.name = name
        self.code = code
        self.period = period
        self.sessions = sessions

    def add_session(self, session):
        self.sessions.append(session)

    def __eq__(self, other):
        return self.name == other.name and self.code == other.code and self.period == other.period


class SubjectSession:

    def __init__(self, code, form, date):
        self.code = code
        self.form = form
        self.date = date
