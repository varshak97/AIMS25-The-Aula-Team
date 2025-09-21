# convert stories to csv files of sentences
import re
import csv

def sentence_segment(text):
    abbrev = r'(Mr|Mrs|Ms|Dr|Prof|Sr|Jr|vs|etc|U\.S\.A|i\.e|e\.g|St|a\.m|p\.m|Fig|No)\.'
    text = re.sub(abbrev, lambda x: x.group().replace('.', '<prd>'), text)
    text = re.sub(r'(\d)\.(\d)', r'\1<prd>\2', text)
    text = re.sub(r'([.!?])\s+', r'\1<stop>', text)
    sentences = text.split('<stop>')
    sentences = [s.replace('<prd>', '.').strip() for s in sentences if s.strip()]
    return sentences

with open("SC3-CAN.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = sentence_segment(text)

# Write sentences to a CSV file
with open("segmented_SC3-CAN.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sentence"])  # header
    for s in sentences:
        writer.writerow([s])