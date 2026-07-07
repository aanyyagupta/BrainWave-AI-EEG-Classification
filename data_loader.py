import pandas as pd
import os
def load_eeg_data(file_path="dataset/raw/eeg_eye_state.csv") -> pd.DataFrame:

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found at '{file_path}'.\n"
            "Please download it first - see the 'Dataset' section in README.md "
            "for step-by-step download instructions."
        )
    df = pd.read_csv(file_path)
    return df


def basic_sanity_check(df: pd.DataFrame) -> None:
    print("=" * 60)
    print("BASIC SANITY CHECK")
    print("=" * 60)

    
    n_rows, n_cols = df.shape
    print(f"Number of rows (samples): {n_rows}")
    print(f"Number of columns (features + label): {n_cols}")
    print(f"Column names: {list(df.columns)}")
    if n_rows == 0:
        print("WARNING: The dataset is empty!")
    if n_cols != 15:
        print(
            f"WARNING: Expected 15 columns (14 EEG channels + 1 label), "
            f"but found {n_cols}. Double-check the downloaded file."
        )

    print("=" * 60)


if __name__ == "__main__":
    DATA_PATH = os.path.join("dataset", "raw", "eeg_eye_state.csv")
    eeg_df = load_eeg_data(DATA_PATH)
    basic_sanity_check(eeg_df)
    print(eeg_df.head())  
