# Google Cloud + Vertex AI + Gemini Setup (From Scratch)

## 0) Install gcloud CLI (Ubuntu/WSL)

``` bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates gnupg curl

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg |   gpg --dearmor | sudo tee /usr/share/keyrings/cloud.google.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get update
sudo apt-get install -y google-cloud-cli
```

Verify:

``` bash
gcloud --version
```

------------------------------------------------------------------------

## 1) Create / Select Project

``` bash
gcloud projects create MY_PROJECT_ID
gcloud config set project MY_PROJECT_ID
gcloud config list project
```

------------------------------------------------------------------------

## 2) Enable Billing

Enable billing from Cloud Console → Billing → Link to project.

------------------------------------------------------------------------

## 3) Authenticate

### CLI Login

``` bash
gcloud auth login --update-adc
```

### ADC Login

``` bash
gcloud auth application-default login
gcloud auth application-default set-quota-project MY_PROJECT_ID
```

------------------------------------------------------------------------

## 4) Enable Required APIs

``` bash
gcloud services enable aiplatform.googleapis.com

gcloud services enable   iam.googleapis.com   cloudresourcemanager.googleapis.com   compute.googleapis.com   storage.googleapis.com   artifactregistry.googleapis.com
```

Verify:

``` bash
gcloud services list --enabled | grep aiplatform
```

------------------------------------------------------------------------

## 5) Set Region

``` bash
gcloud config set ai/region us-central1
```

------------------------------------------------------------------------

## 6) Grant IAM Permission

``` bash
gcloud projects add-iam-policy-binding MY_PROJECT_ID   --member="user:YOUR_EMAIL"   --role="roles/aiplatform.user"
```

------------------------------------------------------------------------

## 7) Verify Gemini Access

``` bash
gcloud ai models list --region=us-central1 | grep gemini
```

------------------------------------------------------------------------

## 8) Environment Variables (.env)

``` env
GOOGLE_CLOUD_PROJECT=MY_PROJECT_ID
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=True
```

------------------------------------------------------------------------

## 9) Quick Python Test

``` bash
pip install google-genai
```

``` python
from google import genai

client = genai.Client(
    vertexai=True,
    project="MY_PROJECT_ID",
    location="us-central1"
)

print(client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Say OK").text)
```

------------------------------------------------------------------------

## 10) Troubleshooting

Invalid grant:

``` bash
gcloud auth login --update-adc
```

Permission denied: Add Vertex AI User role.

Model not found: Use region `us-central1`.

------------------------------------------------------------------------

## Final Checklist

-   Project set correctly
-   Vertex API enabled
-   ADC token works
-   Gemini models listed

You are now ready for ADK + Gemini development.
