# Language models' definitions vs dictionaries' ones
## Project Overview
![](https://github.com/2006coder/LMs-words-defs-vs-dictionaries-defs/blob/main/visualization1.gif)
<p align="justify">
This project compares the originality of the definitions generated in large language models, including ChatGPT, Gemini, and Bard, against established dictionary definitions, including WordNet, Merriam-Webster, and dictionary.com. This will help detect possible plagiarism by comparing the similarities in AI-generated definitions with those from reputable dictionaries.
</p>
## Objective
<p align="justify">
To investigate whether AI-generated definitions mimic dictionary definitions or offer original content. This is achieved by transforming definitions into vectors and comparing them using the sentence_transformers library to detect similarities.
</p>
## Method
<p align="justify">
- Collect definitions for 10,000 common English words from some large language models (chatGPT, Gemini, etc).
- Gather definitions from trusted dictionaries (WordNet, Merriam-Webster dictionary, and dictionary.com).
- Convert the definitions into vectors or embeddings for comparison using 2 models from the sentence_transformers library: all-mpnet-base-v2 and bert-base-nli-mean-tokens.
- Evaluate potential plagiarism by measuring vector similarities between AI and dictionary definitions using the k-nearest neighbors (knn) algorithm.
- Provide statistics and plots to illustrate model performance in maintaining originality.
</p>

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/2006coder/LMs-words-defs-vs-dictionaries-defs
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up API keys (if required) for language models like ChatGPT, Gemini, etc.

## Create an evaluation for your own: 
<p align="justify">
1. Prepare the list of words you wish to analyze.
2. Run the script to collect definitions from LLMs and dictionaries. You can split the 10000.csv into smaller .csv files and run the script simultaneously.
3. Convert the definitions into vectors using the provided script.
4. Perform the similarity analysis and view the results in the output report.
</p>
