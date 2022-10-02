from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
from pdfminer.high_level import extract_text

def get_text(filepath):
    text = extract_text('textrank.pdf')
    countlines = lambda txt: txt.count('\n')
    print(f"linecount: {countlines(text)}, charcount: {len(text)}")
    return text

def get_summary(text: str):
    model_name = "google/pegasus-xsum"
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

    pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    tokens = pegasus_tokenizer(text, truncation=True, padding="longest",
    return_tensors="pt", max_length=400)

    encoded_summary = pegasus_model.generate(**tokens)

    decoded_summary = pegasus_tokenizer.decode(
        encoded_summary[0],
        skip_special_tokens=True,
        max_length=450)

    return decoded_summary