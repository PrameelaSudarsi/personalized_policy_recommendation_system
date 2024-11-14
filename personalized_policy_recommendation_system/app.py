from fastapi import FastAPI, HTTPException
from data_models import PolicyRecommendationRequest
from controller import controller
from logger import logger
import uvicorn
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(title="Personalized Policy Recommendation System", root_path="/policy-recommendation")

@app.get("/")
def test_route():
    logger.debug("API test route called")
    return {"status": "API is running"}

@app.post("/inference/policy-recommendation")
async def generate_policy_recommendation(request: PolicyRecommendationRequest):
    """
    Endpoint to handle policy recommendation generation based on user input data.
    """
    try:
        logger.info(f"Processing user data: {request.user_data}")

        # Call the controller to handle the logic and generate the policy recommendation
        recommendation = controller(request)

        logger.info(f"Successfully generated policy recommendation.")
        return {"recommendation": recommendation}

    except Exception as e:
        logger.error(f"Error processing user data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to process recommendation for user data: {str(e)}")

if __name__ == "__main__":
    logger.info("Starting API...")
    uvicorn.run(app, host="0.0.0.0", port=6101)
