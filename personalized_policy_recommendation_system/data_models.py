from pydantic import BaseModel, Field

class UserData(BaseModel):
    age: int = Field(..., gt=17, lt=121, description="User age, must be between 18 and 120.")
    gender: str = Field(..., description="User gender, options: Male, Female, Other.")
    marital_status: str = Field(..., description="Marital status, options: Single, Married, Divorced, or Widowed.")
    smoking_status: str = Field(..., description="Smoking status, options: Yes or No.")
    drinking_status: str = Field(..., description="Drinking status, options: Yes or No.")
    chronic_conditions: str = Field("", description="List of chronic conditions, comma-separated.")
    annual_income: float = Field(..., gt=0, description="Annual income, must be positive.")
    occupation: str = Field(..., description="User's occupation.")
    dependents: int = Field(0, ge=0, description="Number of dependents.")
    health_status: str = Field(..., description="Health status, options: good, fair, or poor.")
    family_health_history: str = Field("", description="Family health history, comma-separated conditions.")

    class Config:
        schema_extra = {
            "example": {
                "age": 30,
                "gender": "Male",
                "marital_status": "Married",
                "smoking_status": "No",
                "drinking_status": "Yes",
                "chronic_conditions": "hypertension, diabetes",
                "annual_income": 60000.0,
                "occupation": "Engineer",
                "dependents": 2,
                "health_status": "good",
                "family_health_history": "heart disease, diabetes"
            }
        }
