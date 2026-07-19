#Genome Firewall

AI-based antimicrobial resistance prediction system for Escherichia coli

#Problem

Antimicrobial resistance is increasing worldwide. Rapid prediction of resistance can help optimize antibiotic selection.

#Solution

Genome Firewall predicts antibiotic resistance phenotype using machine learning.

#Pipeline:

BV-BRC AMR Dataset
        |
        v
Feature Engineering
        |
        v
XGBoost Model
        |
        v
Resistance Probability
        |
        v
Clinical Decision Support

#Dataset

Organism:
Escherichia coli

Samples:
~243,000 antibiotic resistance records

Target:
Resistant vs Susceptible

Antibiotic:
Ciprofloxacin


#Model
Algorithm:
XGBoost Classifier

Metric:
ROC-AUC = 0.81

Output:
- Likely Resistant
- Likely Susceptible
- Confidence score

#Demo


<img width="1277" height="617" alt="Снимок экрана 2026-07-19 144337" src="https://github.com/user-attachments/assets/c3aedc97-1863-4fb0-9066-8d66e888216c" />


