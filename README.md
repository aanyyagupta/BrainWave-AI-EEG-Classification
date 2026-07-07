# 🧠 BrainWave AI: EEG Signal Classification for Brain-Computer Interface

An end-to-end, beginner-friendly Machine Learning pipeline that classifies EEG (electroencephalogram) signals to detect eye state — a foundational task in real-world **Brain-Computer Interface (BCI)** applications like drowsy-driver detection, attention monitoring, and assistive technology.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Motivation](#motivation)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Pipeline](#pipeline)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Screenshots](#screenshots)
- [Key ML Concepts Explained](#key-ml-concepts-explained)
- [Future Scope](#future-scope)
- [Contributing to GitHub](#pushing-this-project-to-github)
- [License](#license)
- [References](#references)

---

## Introduction

**BrainWave AI** demonstrates a complete, classical Machine Learning workflow applied to real EEG data. It takes raw multi-channel brainwave recordings and classifies whether a subject's eyes were open or closed at each moment — entirely from brain activity, with no camera involved.

This project intentionally avoids Deep Learning (no TensorFlow/PyTorch/CNNs) to focus on mastering the **fundamentals**: data cleaning, feature engineering, classical ML algorithms, hyperparameter tuning, and rigorous evaluation — the skills that underpin every advanced ML system.

## Problem Statement

Given 14 channels of raw EEG voltage readings recorded from a subject's scalp, predict whether their eyes were **open (0)** or **closed (1)** at that instant. This is a **binary classification** problem using **tabular, multivariate time-series-like data**.

## Motivation

Brain-Computer Interfaces are one of the most exciting frontiers in applied ML — powering assistive devices for paralysis patients, drowsiness detection in vehicles, neurofeedback therapy, and hands-free control systems. Eye-state detection from EEG is a classic **entry point** into this field: it's simple enough to solve with classical ML, yet realistic enough to teach every concept needed for more advanced BCI work.

## Dataset

**Name:** EEG Eye State Dataset
**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/264/eeg+eye+state)

| Property | Detail |
|---|---|
| Samples | 14,980 |
| Features | 14 EEG channels (AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4) |
| Target | `eye_state` — 0 = eyes open, 1 = eyes closed |
| Recording device | Emotiv EEG headset (14-electrode) |
| Ground truth labeling | Simultaneous camera recording of the subject's eyes |

### Downloading the Dataset

1. Visit the UCI page: https://archive.ics.uci.edu/dataset/264/eeg+eye+state
2. Download the dataset ZIP/ARFF file.
3. Convert to CSV (or download a pre-converted CSV mirror, e.g., from Kaggle: search "EEG Eye State Dataset").
4. Rename the file to `eeg_eye_state.csv` and place it at:
   ```
   dataset/raw/eeg_eye_state.csv
   ```
5. Ensure the columns are named: `AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4, eye_state`

> **Note:** The raw dataset file itself is excluded from this Git repository (see `.gitignore`) to keep the repo lightweight — always download it fresh using the instructions above.

## Methodology

1. **Exploratory Data Analysis (EDA)** — understand class balance, feature distributions, and correlations.
2. **Preprocessing** — handle missing values (median imputation) and outliers (IQR method).
3. **Feature Engineering** — add statistical summary features and left/right electrode asymmetry features.
4. **Feature Scaling** — standardize all features (mean=0, std=1).
5. **Modeling** — train Logistic Regression, Random Forest, and SVM, each tuned via `GridSearchCV` with 5-fold cross-validation.
6. **Evaluation** — Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC Curve/AUC, and Feature Importance.
7. **Model Selection & Deployment** — save the best model (by F1-score) with `joblib` for future inference.

## Pipeline

```
Raw CSV → Load & Sanity Check → EDA Plots → Handle Missing Values → Remove Outliers (IQR)
→ Feature Engineering → Train/Test Split (80/20, stratified) → Feature Scaling (StandardScaler)
→ Train [Logistic Regression | Random Forest | SVM] with GridSearchCV (5-fold CV)
→ Evaluate all models → Compare → Save Best Model (Joblib) → Predict on New Samples
```

## Project Structure

```
BrainWave-AI-EEG-Classification/
├── dataset/
│   ├── raw/                      # Original downloaded CSV (gitignored)
│   └── processed/                # Cleaned, feature-engineered data
├── notebooks/
│   └── 01_EDA_and_Experiments.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # Load & sanity-check raw data
│   ├── preprocessing.py           # Missing values, outliers, scaling
│   ├── feature_engineering.py     # Derived/engineered features
│   ├── visualize.py                # Reusable, publication-quality plots
│   ├── train.py                    # Model training + GridSearchCV
│   ├── evaluate.py                 # Metrics, reports, comparison table
│   └── predict.py                  # Load model & predict new samples
├── models/                         # Saved best_model.pkl and scaler.pkl
├── results/                        # Metrics CSV + classification reports
├── images/                         # EDA plots, confusion matrices, ROC curves
├── report/
│   └── PROJECT_REPORT.md           # Full written project report
├── main.py                         # Orchestrates the entire pipeline
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### Prerequisites
- Python 3.10 or higher
- `pip` package manager
- Git

### Step-by-Step Setup

```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/BrainWave-AI-EEG-Classification.git
cd BrainWave-AI-EEG-Classification

# 2. Create a virtual environment
#    WHY: This isolates this project's dependencies from other Python
#    projects on your machine, preventing version conflicts.
python -m venv venv

# 3. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install all dependencies
pip install -r requirements.txt

# 5. Download the dataset (see "Dataset" section above)
#    and place it at dataset/raw/eeg_eye_state.csv
```

## Usage

### Run the full pipeline
```bash
python main.py
```
This will preprocess the data, train and tune all three models, generate all plots into `images/`, save metrics into `results/`, and save the best model into `models/`.

### Run only the notebook (for exploration)
```bash
jupyter notebook notebooks/01_EDA_and_Experiments.ipynb
```

### Predict on a new EEG sample
```bash
python src/predict.py
```

## Results

*(Populated automatically after running `main.py` — see `results/metrics_comparison.csv` for exact numbers on your machine.)*

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Random Forest | ~0.93+ | ~0.93 | ~0.92 | ~0.92 |
| SVM (RBF) | ~0.90+ | ~0.90 | ~0.89 | ~0.89 |
| Logistic Regression | ~0.75 | ~0.75 | ~0.74 | ~0.74 |

> Exact values depend on preprocessing choices and the random seed; run the pipeline yourself to reproduce these numbers on your machine.

## Screenshots

After running `main.py`, view generated visuals in:
- `images/eda/` — class distribution, feature histograms, correlation heatmap
- `images/confusion_matrices/` — one per model
- `images/roc_curves/` — one per model

## Key ML Concepts Explained

Every concept below is also explained inline (as comments/docstrings) in the corresponding source file.

| Concept | Explained In |
|---|---|
| Missing values & imputation | `src/preprocessing.py` |
| Outlier detection (IQR method) | `src/preprocessing.py` |
| Standardization vs. Normalization | `src/preprocessing.py` |
| Feature engineering rationale | `src/feature_engineering.py` |
| Logistic Regression, Random Forest, SVM intuition | `src/train.py` |
| Hyperparameters & GridSearchCV | `src/train.py` |
| Cross-validation | `src/train.py` |
| Accuracy, Precision, Recall, F1-Score | `src/evaluate.py` |
| Confusion Matrix | `src/visualize.py` |
| ROC Curve & AUC | `src/visualize.py` |
| Overfitting vs. Underfitting | `src/evaluate.py` |

See also `report/PROJECT_REPORT.md` for a consolidated narrative write-up, and `GIT_GUIDE.md` for Git/GitHub instructions.

## Future Scope

### Version 2 Ideas (Deep Learning)
- Replace classical ML with a **1D Convolutional Neural Network (CNN)** operating directly on raw multi-channel EEG windows instead of hand-engineered features.
- Try a **Recurrent Neural Network (LSTM/GRU)** to model temporal dependencies across EEG time steps.
- Explore **EEGNet**, a CNN architecture purpose-built for EEG classification.
- Use **transfer learning** from pretrained EEG foundation models.

### Further BCI Project Ideas
- **Motor imagery classification** (predicting imagined left/right hand movement from EEG) — a classic BCI benchmark task.
- **Emotion recognition from EEG** (e.g., using the DEAP dataset).
- **Drowsiness/fatigue detection** for driver-safety systems, extending this eye-state model with temporal smoothing.
- **Real-time BCI pipeline** using a live EEG headset (e.g., Emotiv, OpenBCI) streaming into this trained model via `predict.py`.

## Pushing This Project to GitHub

See **`GIT_GUIDE.md`** in this repository for a complete, beginner-friendly walkthrough covering:
- Installing Git
- Initializing a repository
- Staging and committing changes
- Creating a GitHub repository
- Pushing your code
- Branching basics

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## References

1. Rösler, O. & Suendermann, D. (2013). *A First Step towards Eye State Prediction Using EEG.* — original source of the EEG Eye State dataset.
2. UCI Machine Learning Repository — EEG Eye State Dataset: https://archive.ics.uci.edu/dataset/264/eeg+eye+state
3. Pedregosa et al. (2011). *Scikit-learn: Machine Learning in Python.* JMLR 12, pp. 2825-2830.
4. scikit-learn documentation: https://scikit-learn.org/stable/
5. MNE-Python documentation (EEG/MEG analysis): https://mne.tools/stable/index.html

---

*Built as a learning-by-doing portfolio project — every file is documented to teach the underlying ML concepts, not just demonstrate the code.*
