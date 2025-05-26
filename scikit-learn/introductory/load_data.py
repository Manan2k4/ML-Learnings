import time
from sklearn.datasets import fetch_20newsgroups

print("Loading 20 newsgroup training data")
start = time.time()
newsgroups = fetch_20newsgroups(
    categories = [
        "alt.atheism",
        "comp.graphics",
        "comp.sys.ibm.pc.hardware",
        "misc.forsale",
        "rec.autos",
        "sci.space",
        "talk.religion.misc",
    ]
)

newsgroups = fetch_20newsgroups(subset="train", categories=categories) 
raw_data = newsgroups.data
data_sixe_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6

print("Data fetched in {:.2f} seconds".format(time.time() - start))
