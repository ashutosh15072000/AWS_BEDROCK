import boto3
import json

prompt_data="""
Act as a Shakespare and write a poem on machine 
learning
"""
# Create a Bedrock Runtime client in the AWS Region you want to use.
bedrock=boto3.client(service_name="bedrock-runtime",region_name="us-east-1")

payload={
    "prompt":"[INT]"+prompt_data+"[/INT]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

body=json.dumps(payload)
model_id="meta.llama3-8b-instruct-v1:0"

reponse=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(reponse.get("body").read())
response_text=response_body['generation']
print(response_text)