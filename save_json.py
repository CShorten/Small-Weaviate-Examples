import json
Corpus_json_object = json.dumps(corpus, indent=4)
with open(corpus_save_path, "w") as outfile:
  outfile.write(Corpus_json_object)
