class DownloadAktiekurs(object):
    def __init__(self, id, navn):
        # En aktiekurs skal bestå af aktie_id, aktienavnet, dict med tidstempel og kurs
        self._aktie_kurs = None
        self._navn = None
        self._id = None


    def get_aktie_kurs(self, frekvens=10):
        s = lambda aktie, key: "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={aktie}&interval={f}min&outputsize=full&apikey={key}".format(aktie=aktie, key=key, f=frekvens)
