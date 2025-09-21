
Our team has manually curated a demonstration database consisting of survivor stories, scam patterns, media reports, and scientific studies for 6 Region x Industry combination (Australia x Cleaning, Canada x Narcotics, Colombia x Mining, India x IT, Kenya x Sex, Nigeria x Cocoa). 

### Demonstration Database  

The demonstration database contains **103 sources**:  

- **Kenya + Sex:** 22 sources  
- **Colombia + Mining:** 17 sources  
- **India + IT:** 16 sources  
- **Australia + Cleaning:** 16 sources  
- **Nigeria + Cocoa:** 16 sources  
- **Canada + Narcotics:** 16 sources 

### Data Access  

**Curated Demonstration Database (103 sources):** [Excel File Link](https://docs.google.com/spreadsheets/d/1IoD1XaAM2eRxFw19PfnobQhcrqrmzwN3bcfdVhCfxeU/edit?usp=drive_link)  

The segmented sentences used in our proposed **Solution II**, where we perform sentence-level classification on our curated data using the AIMSDistill BERT model provided during the hackathon, are prepared through the pre-processing steps outlined below, and are available in Google Drive:  
**Processed sentences (CSV files for each Region × Industry combination):** [Google Drive Link](https://drive.google.com/drive/folders/1kcbeI4mR__aP_zqNxyWhVYxUNhzGttl-?usp=drive_link)  

Pre-processing outline:
- For each **Region × Industry** combination:
  - Segment sentences from narratives using Python’s Regex library.  
  - Clean sentences for edge cases (abbreviations, decimal numbers, punctuation marks).  
  - Store each sentence in a CSV file, with one sentence per row.  

<img src="schematic_diagrams/step1.png" alt="Sentence Segmentation Process" width="400"/>

### Details of the Database  

#### Data Categories: 

**1. Survivor Stories**  
- **Data type:** Links to public repositories of survivor stories.  
- **Notes:** Preferably sourced from NGOs; other sources are acceptable if the focus remains on survivor accounts. These stories aim to raise awareness and compassion, encouraging people to take action. NGOs also share them to attract potential donors. The Survivor’s Dashboard does not host the stories directly but provides a reference database linking stories to specific countries and products.  

**2. Scam Patterns**  
- **Data type:** Links to public scam pattern descriptions.  
- **Notes:** Ideally from law enforcement, though other reliable sources are acceptable. The focus should be on explaining how the scam is carried out, ideally from start to finish.  

**3. Scientific Research**  
- **Data type:** Citations and links to peer-reviewed studies relevant to specific countries and products.  
- **Notes:** Must be peer-reviewed (any field). Preferably with a PDF or open data link; otherwise, a link to the journal is sufficient. For the short description, use the full abstract.  

**4. Media Reporting**  
- **Data type:** Links to original news sources, preferably local.  
- **Notes:** Emphasis on reputable, in-country news outlets that provide broad coverage. If unavailable, international reporting is acceptable.  
 

 
