from src.data_loader import load_eeg_data, basic_sanity_check


def main():

    eeg_df = load_eeg_data()

    basic_sanity_check(eeg_df)


if __name__ == "__main__":
    main()
