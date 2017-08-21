from non_alcoholic_data import parseData

def reviewSummary(review):
    return "beer name: " + review['beer/name'] + \
           " overall: " + str(review['review/overall']) + \
           " reviewer: " + review['user/profileName']


def niceReviewSummary(review):
    return str(review['review/overall']).rjust(5) + \
           review['beer/name'].rjust(50) + \
           review['user/profileName'].rjust(20)


if __name__ == "__main__":

  print "Reading Data..."
  data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/non-alcoholic-beer.json"))

  print  "review".rjust(5), "beer name".rjust(50), "reviewer".rjust(20)
  for i in range(10):
    print niceReviewSummary(data[i])

  print "done"
