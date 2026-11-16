import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "model" / "ticket_classifier.pkl"
model = joblib.load(model_path)

def predict_ticket(description):
    prediction=model.predict([description])
    probabilities=model.predict_proba([description])
    confidence = max(probabilities[0]) * 100

    print("Predicted Category:", prediction[0])
    print(f"Confidence: {confidence}%")

test_cases = [
    {
        "description": "My password is rejected and I cannot sign in to my account.",
        "expected": "Login Issue"
    },
    {
        "description": "Whenever I click submit, the application crashes and shows an unexpected error.",
        "expected": "Application Error"
    },
    {
        "description": "Please change the email address linked to my account.",
        "expected": "Account Update"
    },
    {
        "description": "The website takes several minutes to load and responds very slowly.",
        "expected": "Performance"
    },
    {
        "description": "I need to download the monthly sales report for last quarter.",
        "expected": "Report"
    }
]

def run_test_cases():
    for i, test in enumerate(test_cases, start=1):
        prediction = model.predict([test["description"]])[0]

        probabilities = model.predict_proba([test["description"]])
        confidence = max(probabilities[0]) * 100

        print(f"\nTest Case {i}")
        print("Ticket:", test["description"])
        print("Expected Category:", test["expected"])
        print("Predicted Category:", prediction)
        print(f"Confidence: {confidence}%")

        if prediction == test["expected"]:
            print("Result: PASS")
        else:
            print("Result: FAIL")

print("Customer Support Ticket Classification System")
print("1. Predict a new ticket")
print("2. Test 5 new tickets")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    description = input("Enter Ticket Description: ")

    if description.strip():
        predict_ticket(description)
    else:
        print("Please enter a valid ticket description.")

elif choice == "2":
    run_test_cases()

else:
    print("Invalid choice. Please select 1 or 2.")
