from llm_controller import get_recommendations
from data_models import UserData
from sklearn.linear_model import LogisticRegression
from logger import log_info, log_error, log_exception

# Placeholder logistic model setup for health risk prediction
model = LogisticRegression()

def calculate_risk_score(user_data):
    """Calculate a risk score based on user data."""
    try:
        score = 0
        if user_data.age > 50:
            score += 2
        elif user_data.age > 30:
            score += 1
        
        if user_data.smoking_status == "Yes":
            score += 3
        if user_data.drinking_status == "Yes":
            score += 2
        if user_data.marital_status == "Single":
            score += 1  # Example adjustment: single users may have different coverage needs
        if user_data.chronic_conditions:
            score += len(user_data.chronic_conditions.split(", ")) * 2
        
        log_info(f"Calculated risk score: {score}")
        return score
    except Exception as e:
        log_exception("Error calculating risk score.")
        raise e

def generate_explanations(user_data):
    """Generate simple explanations based on risk factors in user data."""
    explanations = []
    try:
        if user_data.age > 50:
            explanations.append("Age over 50 increases risk for certain health conditions.")
        if user_data.smoking_status == "Yes":
            explanations.append("Smoking status adds significant health risks, increasing premium.")
        if user_data.drinking_status == "Yes":
            explanations.append("Alcohol consumption may increase health risks.")
        if user_data.marital_status == "Single":
            explanations.append("Being single may affect insurance needs and coverage options.")
        if user_data.chronic_conditions:
            explanations.append("Chronic conditions add to health risk and can affect insurance eligibility.")

        log_info("Generated explanations for user data.")
        return explanations

    except Exception as e:
        log_exception("Error generating explanations.")
        raise e

def predict_health_risk(user_data):
    """Predict health risk using a placeholder logistic regression model."""
    try:
        # Placeholder feature array for logistic regression model
        features = [
            user_data.age,
            int(user_data.smoking_status == "Yes"),
            int(user_data.drinking_status == "Yes"),
            len(user_data.chronic_conditions.split(", "))
        ]
        # Mock prediction (normally, you would train and use a real model)
        prediction = 0.65  # Example: 65% risk as a placeholder

        log_info(f"Predicted health risk: {prediction}")
        return prediction

    except Exception as e:
        log_exception("Error predicting health risk.")
        raise e

def handle_user_input(age, gender, marital_status, smoking_status, drinking_status, chronic_conditions, income, occupation, dependents, health_status, family_history):
    """Process user input and generate insurance recommendations, risk score, explanations, and health risk prediction."""
    try:
        # Create UserData instance
        user_data = UserData(
            age=age,
            gender=gender,
            marital_status=marital_status,
            smoking_status=smoking_status,
            drinking_status=drinking_status,
            chronic_conditions=chronic_conditions,
            annual_income=income,
            occupation=occupation,
            dependents=dependents,
            health_status=health_status,
            family_health_history=family_history
        )

        log_info("Created UserData instance with validated user input.")

        # Calculate risk score and generate explanations
        risk_score = calculate_risk_score(user_data)
        explanations = generate_explanations(user_data)
        health_risk_prediction = predict_health_risk(user_data)

        # Get recommendations from the AI model
        recommendations = get_recommendations(user_data)
        log_info("Received recommendations from the AI model.")

        return {
            "recommendations": recommendations,
            "risk_score": risk_score,
            "explanations": explanations,
            "health_risk_prediction": health_risk_prediction
        }

    except Exception as e:
        log_exception("An error occurred while handling user input.")
        return {"error": f"An unexpected error occurred: {e}"}
