from src import preprocess_data
from src import train_model
from src import generate_predictions
from src import generate_explainability

def main():
    print("Starting Machine Learning Risk Scoring System...")

    preprocess_data()
    train_model()
    generate_predictions()
    generate_explainability()

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
