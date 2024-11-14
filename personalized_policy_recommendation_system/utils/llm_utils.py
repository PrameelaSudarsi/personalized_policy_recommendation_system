from .prompt_template import user_prompt, system_prompt

def groq_request(user_data: dict, system_prompt=system_prompt):
    """Prepares the message for Groq's API based on the user inputs."""
    message = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_data,
        },
    ]
    return message

def prompt_engineer(user_data, broker, max_tokens=1000, prompt=user_prompt, system_prompt=system_prompt):
    """Prepares the prompt for the AI model based on user data and broker."""
    if broker == "groq":
        return groq_request(user_data, system_prompt=system_prompt)
    else:
        raise ValueError(f"Unsupported broker: {broker}")
