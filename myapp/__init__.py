

def __init__(self):
    self._logger = logging.getLogger("SPOT.INGEST.HDFS_client")
    session = Session()
    print("Init loaded  ", self._logger + " " + session)

