from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from pdfminer.high_level import extract_text
from keybert import KeyBERT
spacy.cli.download("en_core_web_lg")
import re
def get_text(filepath):
    text = extract_text(filepath)
    countlines = lambda txt: txt.count('\n')
    print(f"linecount: {countlines(text)}, charcount: {len(text)}")
    return text

def get_summary(text: str):
    model_name = "google/pegasus-xsum"
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    tokens = pegasus_tokenizer(text, truncation=True, padding="longest",
    return_tensors="pt", max_length=450, min_length=300)

    encoded_summary = pegasus_model.generate(**tokens)

    decoded_summary = pegasus_tokenizer.decode(
        encoded_summary[0],
        skip_special_tokens=True)

    return decoded_summary

def get_keywords(text: str):
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("textrank")
    doc = nlp(test)
    
    extract_text = ""
    for i in doc._.textrank.summary(limit_sentences=5):
        extract_text += str(i)

    kw_model = KeyBERT()
    return keywords = kw_model.extract_keywords(extract_text)
    
def cleanup(text: str):
    return new_text = re.sub(r"[^a-zA-Z0-9 ]", "", decoded_summary)
