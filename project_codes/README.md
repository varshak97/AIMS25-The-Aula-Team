# Project Codes:

**Proposed solution part II: Focussing AIMS’ fine-tuned AIMSDistill BERT Model on Survivor Stories** as outline in our [Comprehensive Project Package (CPP)](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/Survivors%20Dashboard%20Complete%20Project%20Package%20AIMS%20Hackathon%202025%20Aula.pdf)

For a given Region x Industry combination, we begin by segmenting sentences from each narrative using Python’s Regex library [1] (refer to the Schematic below, Step 1). We ensure that the segmented sentences are cleaned for common edge cases such as abbreviations, decimal numbers, and punctuation marks that could otherwise break sentence structure. Each resulting sentence is then written into a CSV file, with one sentence per row, ensuring a structured and consistent format for subsequent analysis.

<img src="schematic_diagrams/aims_schematic_1.png" alt="Sentence Segmentation Process"/>

The code used for the pre-processing step is available in [utils.py](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/project_codes/utils.py)

Following the sentence segmentation step for that Region x Industry, we leverage the AIMSDistill [2] BERT model fine-tuned for sentence classification on the annotated AIMS.au [4] dataset to perform sentence classification. The AIMSDistill model performs multi-label binary classification at the sentence level. The labels and the schematic diagram for this task are shown in Fig. 3.2.b.We then filter out the sentences classified as “C3: risk description” with a logit score ≥ 0.9, retaining only sentences for which the model is most confident. This filtered set of sentences is then used to generate a concise factual summary by prompting the Google Gemini [3] API. The summarisation is performed in a two-step chunk-wise process (as detailed in the schematic below, Step 2) and explained next. 

<img src="schematic_diagrams/aims_schematic_2.png" alt="Sentence Classification"/>

The filtered set of sentences is divided into multiple non-overlapping subsets, each containing 80 sentences. To perform two-step chunk-wise summarisation, each subset is first used to prompt Google’s Gemini [3] API for summarisation. The intermediate summaries generated for each chunk are then combined and used as input to Gemini in a second step to produce the final summary. The prompts used for both steps are available in our [CPP](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/Survivors%20Dashboard%20Complete%20Project%20Package%20AIMS%20Hackathon%202025%20Aula.pdf)

<img src="schematic_diagrams/aims_schematic_3.png" alt="Two-step Summarisation"/>

The codes used for Step 2 and 3 are available in the [jupyter notebook](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/project_codes/01_(FINAL)_AIMSDistill_prediction%2BGemini_summarising.ipynb)

# Output Summaries:

[Annex 5.5 in the CPP](https://github.com/varshak97/AIMS25-The-Aula-Team/blob/main/documentation/Survivors%20Dashboard%20Complete%20Project%20Package%20AIMS%20Hackathon%202025%20Aula.pdf) contains sample output for all 6 demo combinations (Australia x Cleaning, Canada x Narcotics, Colombia x Mining, India x IT, Kenya x Sex, Nigeria x Cocoa)

# Additional codes (Optional):
