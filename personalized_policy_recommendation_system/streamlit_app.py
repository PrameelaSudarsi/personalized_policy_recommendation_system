import streamlit as st
from fpdf import FPDF
from data_models import UserData
from llm_controller import get_recommendations
from utils.input_validation import validate_age, validate_health_status
from controller import calculate_risk_score
import os

# Set up page configuration
st.set_page_config(page_title="Personalized Insurance Recommendations", layout="wide", page_icon="🛡️")

# Header with title and subtitle
st.title("Personalized Insurance Policy Recommendations")
st.write("A professional solution to find tailored insurance policies based on your unique profile.")

# Sidebar for information and instructions
with st.sidebar:
    st.header("Useful Information")
    st.markdown("""
    **Why Personalized Insurance?**
    - Personalized insurance policies offer better coverage based on your needs.
    - Avoid paying for unnecessary features.
    - Increase peace of mind with targeted protection.
    """)
    st.header("Save Your Recommendations")
    st.markdown("""
    - After generating recommendations, click "Save" to download them.
    - You can save as a text file or PDF and consult with your insurance provider for more options.
    """)

# Initialize session state for recommendations and risk score if not present
if 'recommendations' not in st.session_state:
    st.session_state['recommendations'] = ""
if 'risk_score' not in st.session_state:
    st.session_state['risk_score'] = 0

# Main layout columns for user input and recommendations display
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Enter Your Details")
    
    # Collect user inputs
    age = st.number_input("Enter your age:", min_value=18, max_value=120, help="Your age must be between 18 and 120.")
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"], key="gender", help="Choose the option that best describes your gender.")
    marital_status = st.selectbox("Select your marital status:", ["Single", "Married", "Divorced", "Widowed"], key="marital_status", help="Choose your marital status.")
    smoking_status = st.selectbox("Do you smoke?", ["Yes", "No"], key="smoking_status", help="Indicate if you are a current smoker.")
    drinking_status = st.selectbox("Do you drink alcohol?", ["Yes", "No"], key="drinking_status", help="Indicate if you consume alcohol.")
    chronic_conditions = st.text_area("List any chronic conditions:", placeholder="e.g., diabetes, hypertension", key="chronic_conditions", help="Mention any long-term health conditions.")
    income = st.number_input("Enter your annual income:", min_value=1.0, step=1000.0, help="Please enter your annual income in your local currency.")
    occupation = st.text_input("Occupation:", placeholder="e.g., Engineer, Teacher", key="occupation", help="Your profession, which can impact risk assessment.")
    dependents = st.number_input("Number of dependents:", min_value=0, key="dependents", help="Enter the number of people financially dependent on you.")
    health_status = st.selectbox("Select your health status:", ["good", "fair", "poor"], key="health_status", help="Choose the option that best describes your current health status.")
    family_history = st.text_area("Enter any relevant family health history:", placeholder="e.g., family history of diabetes, heart disease.", key="family_history", help="Mention any significant health issues that run in your family.")
    
    # Generate Recommendations
    if st.button("Get Recommendations"):
        if validate_age(age) and validate_health_status(health_status):
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
            
            # Fetch recommendations and risk score
            recommendations = get_recommendations(user_data)
            risk_score = calculate_risk_score(user_data)
            
            # Store in session state for later use
            st.session_state['recommendations'] = recommendations
            st.session_state['risk_score'] = risk_score
        else:
            st.error("Please enter valid data.")

# Display recommendations and save options
with col2:
    st.subheader("Recommended Policies")
    if st.session_state['recommendations']:
        st.write(st.session_state['recommendations'])
        st.write(f"**Risk Score:** {st.session_state['risk_score']}")
        
        # Save as Text File
        if st.button("Save as Text"):
            try:
                with open("recommendations.txt", "w", encoding="utf-8") as file:
                    file.write(st.session_state['recommendations'])
                    file.write(f"\nRisk Score: {st.session_state['risk_score']}")
                st.success("Recommendations saved as 'recommendations.txt'.")
                # Provide download link
                with open("recommendations.txt", "rb") as file:
                    st.download_button(
                        label="Download Text File",
                        data=file,
                        file_name="personalized_recommendations.txt",
                        mime="text/plain"
                    )
            except UnicodeEncodeError as e:
                st.error(f"Error saving recommendations: {e}")
        
        # Save as PDF with font handling and adjusted layout
        if st.button("Save as PDF"):
            try:
                font_path = os.path.join(os.getcwd(), "DejaVuSans.ttf")
                
                pdf = FPDF()
                pdf.add_page()
                
                # Check for custom font and apply, or default to Arial
                if os.path.exists(font_path):
                    pdf.add_font("DejaVu", "", font_path, uni=True)
                    pdf.set_font("DejaVu", "", 12)
                else:
                    pdf.set_font("Arial", "", 12)
                    st.warning("DejaVuSans.ttf font not found. Using default font.")
                
                # Adjust margins and ensure maximum width is used
                pdf.set_left_margin(5)
                pdf.set_right_margin(5)
                pdf.set_auto_page_break(auto=True, margin=10)
                
                # Add recommendations text with adjusted width
                recommendations = st.session_state['recommendations']
                for line in recommendations.splitlines():
                    if len(line) > 0:
                        pdf.cell(190, 10, line, ln=True)

                # Add risk score separately
                pdf.cell(190, 10, f"Risk Score: {st.session_state['risk_score']}", ln=True)
                
                pdf_output = "recommendations.pdf"
                pdf.output(pdf_output)
                st.success("Recommendations saved as 'recommendations.pdf'.")
                
                # Provide download link
                with open(pdf_output, "rb") as file:
                    st.download_button(
                        label="Download PDF File",
                        data=file,
                        file_name="personalized_recommendations.pdf",
                        mime="application/pdf"
                    )
                    
            except Exception as e:
                st.error(f"Error generating PDF: {e}")

    else:
        st.info("Enter your details and click 'Get Recommendations' to see the results.")

# Hypothetical Scenario Testing for Dynamic Risk Analysis
st.sidebar.header("Test Hypothetical Scenarios")
age_hypothetical = st.sidebar.slider("Age", 18, 120, age, key="age_hypothetical", help="Adjust your age to see how it affects your risk score.")
marital_status_hypothetical = st.sidebar.selectbox("Select marital status:", ["Single", "Married", "Divorced", "Widowed"], key="marital_status_hypothetical")
smoking_status_hypothetical = st.sidebar.selectbox("Do you smoke?", ["Yes", "No"], index=["Yes", "No"].index(smoking_status), key="smoking_status_hypothetical", help="Indicate if you are a current smoker.")
drinking_status_hypothetical = st.sidebar.selectbox("Do you drink alcohol?", ["Yes", "No"], key="drinking_status_hypothetical")
chronic_conditions_hypothetical = st.sidebar.text_area("List chronic conditions (comma-separated):", chronic_conditions, key="chronic_conditions_hypothetical", help="Mention any long-term health conditions.")
health_status_hypothetical = st.sidebar.selectbox("Select your health status:", ["good", "fair", "poor"], key="health_status_hypothetical", help="Choose the option that best describes your current health status.")

# Display updated risk profile based on hypothetical scenario
if st.sidebar.button("Calculate Hypothetical Risk", key="calculate_hypothetical_risk"):
    hypothetical_data = UserData(
        age=age_hypothetical,
        gender=gender,
        marital_status=marital_status_hypothetical,
        smoking_status=smoking_status_hypothetical,
        drinking_status=drinking_status_hypothetical,
        chronic_conditions=chronic_conditions_hypothetical,
        annual_income=income,
        occupation=occupation,
        dependents=dependents,
        health_status=health_status_hypothetical,
        family_health_history=family_history
    )
    hypothetical_risk_score = calculate_risk_score(hypothetical_data)
    st.sidebar.subheader("Hypothetical Risk Score")
    st.sidebar.write(f"Risk Score: {hypothetical_risk_score}")
