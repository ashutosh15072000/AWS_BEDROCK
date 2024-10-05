import boto3
import json
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

prompt_data="""
Acts as a shakespeare and write a poem on Generative AI

"""
# Set the model ID, e.g., Titan Text Premier.
model_id = "anthropic.claude-v2"
bedrock=boto3.client(service_name="bedrock-runtime",region_name="us-east-1")

payload={
  "messages": [
   {
    "role": "user",
    "content": prompt_data
   }
  ],
  "max_tokens":512,
  "temperature":0.5,
   "top_p":0.9
}

body=json.dumps(payload)
model_id="ai21.jamba-1-5-mini-v1:0"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
response_text=response_body['choices'][0]['message']['content']
print(response_text)