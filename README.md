# Protein Physicochemical Analysis Dashboard
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Biopython](https://img.shields.io/badge/Biopython-Latest-green)
![Linux](https://img.shields.io/badge/Linux-Compatible-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/7207ab5c-8b55-4ac7-82c7-937f7a78d9a7" />


A Python-based bioinformatics toolkit for automated physicochemical profiling and comparative analysis of protein sequences using Biopython.

This project enables rapid analysis of multiple protein sequences provided in FASTA format and computes important physicochemical descriptors commonly used in structural bioinformatics, protein engineering, recombinant protein expression, biomarker discovery, and computational biology workflows.

---

# Overview

Physicochemical characterization of proteins is a fundamental step in computational biology and structural bioinformatics. Properties such as molecular weight, isoelectric point, hydrophobicity, and instability index provide valuable insight into protein behavior, solubility, structural stability, and biochemical functionality.

This toolkit automates batch analysis of protein sequences using the Biopython ProtParam module and exports the results in a structured CSV format for downstream analysis and visualization.

The project was designed to support scalable protein analysis workflows in computational biology and bioinformatics environments.

---

# Features

* Supports batch analysis of multiple protein sequences
* FASTA-based input workflow
* Automated physicochemical property calculation
* CSV export for downstream analysis
* Linux-compatible workflow
* Lightweight and reproducible Python implementation
* Uses Biopython ProtParam (industry-standard bioinformatics library)

---

# Physicochemical Properties Calculated

The toolkit computes:

* Molecular Weight (MW)
* Isoelectric Point (pI)
* GRAVY (Grand Average of Hydropathicity)
* Instability Index

Additional metrics can be integrated in future versions:

* Aliphatic Index
* Amino Acid Composition
* Aromaticity
* Extinction Coefficient
* Secondary Structure Fraction

---

# Workflow

FASTA Input
↓
Sequence Validation
↓
Physicochemical Property Calculation (Biopython ProtParam)
↓
Comparative Protein Analysis
↓
CSV Export & Reporting

---

# Biological Significance

Physicochemical profiling is widely used in:

* Recombinant protein expression optimization
* Protein engineering and mutation analysis
* Biomarker discovery
* Structural bioinformatics workflows
* Therapeutic protein characterization
* Comparative sequence analysis
* Rational protein design
* Drug discovery and target characterization

---

# Repository Structure

## Repository Structure

```bash
Protein-Physicochemical-Analysis-Toolkit/
│
├── app.py
│
├── data/
│   └── input_proteins.fasta
│
├── results/
│   └── physicochemical_results.csv
│
├── scripts/
│   └── protein_physchem_analysis.py
│
├── docs/
│   └── dashboard.png
│
├── requirements.txt
├── LICENSE
└── README.md
```



# Input Format

The input file must be a standard FASTA file containing one or more protein sequences.

Example:

```fasta
>Protein_1
MKWVTFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGE

>Protein_2
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTK
```

---

# Important Notes

* Input file must be saved as plain text
* Only valid amino acid characters (A–Z) should be used
* Remove special symbols such as:

  * *
  * $
  * whitespace formatting artifacts
* Sequences should be biologically valid protein sequences

---

# Installation

## Clone Repository


git clone https://github.com/AbhignaNagaraj/Protein-Physicochemical-Analysis-Dashboard.git
cd Protein-Physicochemical-Analysis-Dashboard
```

---

# Requirements

* Python 3
* Biopython
* Pandas
* Streamlit
* Plotly
* Linux/Unix

Install dependencies:

python3 -m pip install -r requirements.txt

---

# How to Run


## Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# Example Output

Analysis Results
Protein ID	Molecular Weight	Isoelectric Point	GRAVY	Instability Index
NP_000577.2	17627.53	7.67	-0.007	47.71
mutated	17629.46	6.82	-0.055	47.71


---

# Interpretation of Results

## GRAVY

* Negative values indicate hydrophilic proteins
* Positive values indicate hydrophobic proteins

Hydrophilic proteins are generally more soluble in aqueous environments.

---

## Isoelectric Point (pI)

* Lower pI values often correlate with acidic proteins
* Higher pI values indicate basic proteins

pI is important for:

* protein purification
* buffer optimization
* solubility assessment

---

## Instability Index

* Values < 40 indicate stable proteins
* Values > 40 suggest intrinsic instability

## Interactive Streamlit Dashboard

This project also includes a Streamlit-based interactive dashboard for automated physicochemical analysis of protein sequences.

### Features

* FASTA file upload
* Automated protein property analysis
* Interactive results table
* CSV export support
* Comparative protein analysis

### Run Streamlit App


streamlit run app.py



Useful for:

* recombinant protein design
* mutation impact studies
* therapeutic protein engineering

---

# Applications

This toolkit can be used for:

* Protein engineering
* Mutation impact analysis
* Biomarker research
* Structural bioinformatics
* Comparative protein characterization
* Recombinant protein expression planning
* Bioinformatics teaching and training
* Computational biology technical assessments

---

# Technologies Used

* Python 3
* Streamlit
* Biopython
* Pandas
* Plotly
* Linux/Unix


---

# Future Improvements

Planned future developments include:

* AlphaFold structure integration
* Automated visualization dashboards
* REST API deployment
* Docker containerization
* Nextflow workflow integration
* Parallel batch processing support
* Interactive comparative protein analysis plots

---

# Example Use Cases

## Case 1: Mutation Analysis

Compare wild-type vs mutant proteins to assess:

* stability changes
* hydrophobicity changes
* biochemical behavior shifts

---

## Case 2: Recombinant Expression Planning

Identify proteins likely to exhibit:

* aggregation
* instability
* poor solubility

before experimental expression.

---

## Case 3: Structural Bioinformatics

Generate physicochemical descriptors for:

* structural modeling
* docking studies
* therapeutic target analysis

---

# Author

Dr. Abhigna N U

PhD Bioinformatics | Computational Biology | Structural Bioinformatics | AI-Assisted Drug Discovery | Genomics & Workflow Automation

GitHub:
https://github.com/AbhignaNagaraj

LinkedIn:
https://www.linkedin.com/in/dr-abhigna-bioinformatics/

---

# License

This project is licensed under the MIT License.

---

# Citation

If you use this project in academic or research work, please cite appropriately or provide repository attribution.

---

# Acknowledgements

* Biopython Development Team
* Open-source bioinformatics community
* Python scientific computing ecosystem
 academic, educational, and evaluation purposes.

