# AutoJudge – Automated Programming Problem Difficulty Prediction System

## Project Overview
AutoJudge is a machine learning–based system that automatically predicts the difficulty of programming problems. It analyzes problem statements using natural language processing and supervised learning techniques to estimate:

- Difficulty category: Easy / Medium / Hard (classification)
- Numerical difficulty score: Continuous score representing relative complexity (regression)

The system provides an interactive web interface that allows users to input a programming problem and receive real-time predictions.

---

## Repository Structure
autojudge/
│
├── data/ # Raw and processed datasets
├── notebooks/ # Data preprocessing, feature extraction, model training
├── models/ # Saved trained models (.pkl files)
├── web/ # Web interface (Streamlit)
│ └── app.py
├── requirements.txt # Python dependencies
├── report.pdf # Detailed project report (4–8 pages)
└── README.md

---

## Dataset Used
The dataset consists of programming problems collected from competitive programming platforms and curated repositories. Each problem includes:

- Problem statement text
- Constraints
- Difficulty labels
- Derived numerical features

### Target Variables
- Classification: Easy / Medium / Hard  
- Regression: Continuous difficulty score

---

## Methodology

### Data Preprocessing
- Text cleaning (lowercasing, punctuation removal)
- Stopword removal
- Tokenization
- Handling missing values using mean imputation

### Feature Engineering
- TF-IDF vectorization of problem statements
- Numerical features:
  - Problem statement length
  - Constraint count
  - Algorithmic keyword frequency (DP, graph, modulo, etc.)

### Machine Learning Models

#### Classification Model
- Model: Random Forest Classifier
- Task: Predict difficulty class (Easy / Medium / Hard)

#### Regression Model
- Model: Random Forest Regressor
- Task: Predict numerical difficulty score

---

## Evaluation Metrics

### Classification Performance
- Accuracy: 43.26%

> Note: Moderate accuracy is expected due to overlap between Medium and Hard difficulty levels.

### Regression Performance
- Mean Absolute Error (MAE): 1.69
- Root Mean Squared Error (RMSE): 2.02

---

## Web Interface
- Framework: Streamlit
- Allows users to:
  - Enter a programming problem statement
  - View predicted difficulty class
  - View predicted numerical difficulty score

### Web Application Workflow
1. User inputs problem statement
2. Text is preprocessed and vectorized
3. Models generate predictions
4. Results are displayed instantly

Screenshots and detailed explanation are included in report.pdf.

---

## Steps to Run the Project Locally

### (Optional) Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
Install Dependencies
pip install -r requirements.txt

Run the Web Application
streamlit run web/app.py


Open the displayed localhost URL in your browser.
### Saved Trained Models

The following trained models are included:

models/difficulty_classifier.pkl

models/difficulty_regressor.pkl
demo video link :-https://drive.google.com/file/d/18hAlePYeqqViYmU0Jcf3aVsXbZcy7MoV/view?usp=sharing
