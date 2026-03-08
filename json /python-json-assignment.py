import json

# Step 1: Store JSON-formatted string (simulating API response)
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Step 2: Parse JSON string into Python dictionary
data = json.loads(api_response)

# Step 3: Extract required values
request_id = data.get("id")
status = data.get("status")
text_result = data.get("result", {}).get("text")
confidence_score = data.get("result", {}).get("confidence")

# Step 4: Print extracted values
print(f"Request ID: {request_id}")
print(f"Status: {status}")
print(f"Text: {text_result}")
print(f"Confidence: {confidence_score}")

# Step 5: Check confidence threshold
if confidence_score is not None and confidence_score < 0.9:
    print("⚠ Warning: Confidence score is below acceptable threshold!")

# Step 6: Create a follow-up Python dictionary
follow_up_result = {
    "request_id": request_id,
    "status": "processed",
    "message": "Result stored successfully",
    "original_confidence": confidence_score
}

# Step 7: Convert dictionary to JSON
json_output = json.dumps(follow_up_result, indent=4)

# Step 8: Write JSON to file
with open("response.json", "w") as file:
    file.write(json_output)

print("\nFollow-up response written to response.json")