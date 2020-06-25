class Aktie(object):
    def __init__(self, name, start_kurs, amount):
        self._name = name
        self._start_kurs = start_kurs
        self._n = amount
        self._current_k urs = None
        self._end_kurs = None
        self._sold = None

    def compute_total_volume(self):
        return self._current_kurs * self._n

    @property
    def current_kurs(self):
        return self._current_kurs

    @current_kurs.setter
    def current_kurs(self,  current_kurs):
        self._current_kurs = current_kurs


