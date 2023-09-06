# NLG_metrics

This repository provides a script for an integrated evaluation of Natural Language Generation (NLG) metrics.

It utilizes components of the CommonGen evaluation function, and you can modify the concept settings as needed.

## 0. Repository Structure

```plaintext
NLG_metrics/
├── BARTScore  
├── BERTScore  
├── BLEU  
├── CiDEr  
├── METEOR  
├── ROUGE  
├── SPICE  
├── result  
├── test  
├── Dockerfile        # Docker execution file
├── install.sh        # Script to install required packages
├── similarity.py     # Integrated evaluation function
├── similarity.sh     # Script to execute integrated evaluation
└── requirements.txt  # List of required packages
```

## 1. Installation

To install the required packages, you can run the following commands:

```bash
conda create -n $YOUR_ENV$ python==3.8
conda activate $YOUR_ENV$
sh install.sh
```
You should also download the following file and move on your **SPICE/lib** folder

> https://drive.google.com/file/d/1Hwu0qXV5s3hM1sq43fDUGdi_mlyXZHpK/view?usp=sharing


## 2. Usage

**Please make sure to specify the paths and dataset file settings within the shell files before running the script.**

To execute the integrated evaluation, run:

```bash
sh similarity.sh
```

## 3. Citation

```
@Code{
year={2023},
title={NLG_metric},
author={Jaehyung Seo},
affiliation={Korea University, NLP & AI LAB},
email={seojae777@korea.ac.kr}}
```

## 4. Thanks

This script is based on [CommonGen](https://github.com/INK-USC/CommonGen),  [BERTScore](https://github.com/Tiiiger/bert_score),  [BARTScore](https://github.com/neulab/BARTScore/tree/main). We thank the authors for their academic contribution.
