from config.llm_config import clients
from logger import log_info, log_error, log_exception

def get_recommendations(user_data):
    """Fetches insurance recommendations based on user data using the Groq API."""
    client = clients['llama3-70b-8192']
    
    # Construct prompt for the recommendation engine
    prompt = (
        f"User details:\n"
        f"- Age: {user_data.age}\n"
        f"- Gender: {user_data.gender}\n"
        f"- Marital Status: {user_data.marital_status}\n"
        f"- Smoking Status: {user_data.smoking_status}\n"
        f"- Drinking Status: {user_data.drinking_status}\n"
        f"- Chronic Conditions: {user_data.chronic_conditions}\n"
        f"- Annual Income: {user_data.annual_income}\n"
        f"- Occupation: {user_data.occupation}\n"
        f"- Number of Dependents: {user_data.dependents}\n"
        f"- Health Status: {user_data.health_status}\n"
        f"- Family Health History: {user_data.family_health_history}\n\n"
        f"Provide personalized insurance policy recommendations based on this data."
    )
    
    try:
        log_info("Sending request to Groq API for recommendations.")
        
        # Fetch response from the Groq API
        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "Generate personalized insurance policy recommendations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
        )

        # Log raw response data for debugging if needed
        log_info(f"Received response from Groq API: {chat_completion}")

        # Extract recommendations
        recommendations = chat_completion.choices[0].message.content
        log_info("Recommendations successfully extracted from API response.")
        
        return recommendations

    except AttributeError as e:
        log_error("AttributeError when accessing API response.")
        log_exception(f"Error accessing Groq API: {e}")
        return f"API response error: {e}"

    except TypeError as e:
        log_error("TypeError due to unexpected response structure.")
        log_exception(f"Unexpected response structure from Groq API: {e}")
        return f"API response structure error: {e}"

    except Exception as e:
        log_exception("An unexpected error occurred while communicating with Groq API.")
        return f"An unexpected error occurred: {e}"
