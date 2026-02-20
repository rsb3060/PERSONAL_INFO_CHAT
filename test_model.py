from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel
import vertexai

vertexai.init(project="gen-lang-client-0629514970", location="us-central1")

model = GenerativeModel("gemini-2.5-flash-lite")
response = model.generate_content("Say OK if working")

print(response.text)
