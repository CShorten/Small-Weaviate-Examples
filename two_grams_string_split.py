test = "Message from the Chair - CSWEA Section Chair for the next year,"
removed_test = re.sub(r'[^\w\s]', '', test).replace("  ", " ")

all_words = removed_test.split(" ")
two_grams = set()
for i in range(len(all_words)):
  try:
    two_grams.add(all_words[i] + " " + all_words[i+1])
  except:
    print("end of list.")

print(two_grams)
