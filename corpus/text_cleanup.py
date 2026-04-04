from HanziNLP import load_stopwords,word_tokenize
import pprint
import json
from pathlib import Path

FILEPATH = Path(__file__).parent / "speeches.json"
OUTPATH = Path(__file__).parent / "tokenized_speeches.json"
OUTPATH_TWO = Path(__file__).parent / "all_tokens.json"

tokenized_speeches = []
all_tokens = []

# Tokenizing and removing stop words

with open(FILEPATH,"r") as f:

    speeches = json.load(f) 

    for speech in speeches:

        # Tokenization and removal of stopwords. Punctuation is removed by 
        # default
        speech["tokenized"] = word_tokenize(speech["text"],
                                            mode = "precise",
                                            stopwords = "baidu_stopwords.txt",
                                            custom_stopwords = ["\u3000"])
        
        tokenized_speeches.append(speech) 

        for token in speech["tokenized"]:
            all_tokens.append(token)

# Saving
with open(OUTPATH, "w", encoding = "utf-8") as json_file:
    json.dump(tokenized_speeches, json_file, indent=1, ensure_ascii=False)

with open(OUTPATH_TWO,"w",encoding = "utf-8") as json_file_2:
    json.dump(all_tokens,json_file_2,indent=1,ensure_ascii=False)


        

        
