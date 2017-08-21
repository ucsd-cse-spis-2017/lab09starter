import urllib.request

def parseData(fname):
    for l in urllib.request.urlopen(fname):
        yield eval(l)

if __name__ == "__main__":
  print("Reading Data...")
  data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/non-alcoholic-beer.json"))
  print("done")


  #comment
