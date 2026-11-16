import joblib
from pathlib import Path
from responses import generate_response

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "model" / "ticket_classifier.pkl"
model = joblib.load(model_path)

def main():

    print("=" * 45)
    print("       CUSTOMER SUPPORT CLASSIFIER")
    print("=" * 45)

    description = input("Enter Ticket Description: ").strip()

    if not description:
        print("Please enter a valid ticket description.")
        return

    prediction = model.predict([description])[0]

    probabilities = model.predict_proba([description])
    confidence = max(probabilities[0]) * 100

    suggested_response = generate_response(prediction)

    print("\n" + "-" * 45)
    print("Predicted Category:",prediction)
    print(f"Confidence: {confidence}%")

    print("\nSuggested Response:")
    print(suggested_response)
    print("-" * 45)


if __name__ == "__main__":
    main()

