### Serverless Cloud Resume Infrastructure
This repository contains the full-stack codebase and Infrastructure as Code (IaC) configurations for a serverless, highly available web application hosting a professional engineering portfolio.

## Directory Structure
.
├── frontend/                  # Static website application code
│   ├── index.html             # Resume content and structure
│   ├── style.css              # Custom styling and layout design
│   └── main.js                # Asynchronous JavaScript API counter logic
└── terraform/                 # Infrastructure as Code (IaC) configurations
    ├── main.tf                # Core AWS resource blueprints (S3, API Gateway, Lambda, DynamoDB)
    ├── provider.tf            # AWS configuration constraints
    └── terraform.tfstate      # Locally recorded infrastructure state configuration

### Cloud Resources Provisioned Natively
## aws_s3_bucket & aws_s3_bucket_website_configuration
Configures access controls, bucket policies, and sets up index documents for static file hosting.

## aws_dynamodb_table
Schema configured with an atomic partition key (HashKey) to store global tracking metrics safely across concurrent access instances.

## aws_lambda_function
Packages code runtimes, defines execution limits, environment variables, and assigns explicit IAM Execution Roles.

## aws_api_gateway_rest_api
Exposes /visitor endpoint structures, orchestrates backend integrations, and structures public access points.

## aws_iam_role & aws_iam_policy
Enforces the Principle of Least Privilege (PoLP), granting precise read/write access explicitly restricted to target DynamoDB tables.

## aws_s3_object
Direct declarative pipeline deployment maps that bind, content-type tag, and deploy local development workspace code to AWS live storage targets automatically.

### Local Implementation & Replication Guide
To replicate or modify this infrastructure stack locally, ensure you have configured your development system with the Terraform CLI and authenticated AWS credentials.

### 1. Backend Endpoint Adjustments
Navigate to frontend/main.js and modify the targeted backend endpoint mapping to match your deployed API Gateway stage:

```javascript
const apiEndpoint = "https://h0mgq2wpq5.execute-api.us-east-1.amazonaws.com/visitor";

2. Initialize and Deploy Infrastructure
## Navigate to your IaC workspace folder in your terminal and execute the deployment lifecycle:

cd terraform

# Initialize provider modules and cloud registry backends
terraform init

# Run deterministic environment checks to view structural updates
terraform plan

# Deploy infrastructure configurations natively to your live AWS account
terraform apply -auto-approve

# Deploy infrastructure configurations natively to your live AWS account
terraform apply -auto-approve
💡 Key Architectural Takeaways
⚡ Atomic State Updates: The database access function relies on an optimized conditional database update script rather than reading and rewriting states sequentially, protecting transaction counters against runtime race conditions.

Infrastructure Decoupling: Modifying client interface layouts requires no functional code changes to API endpoints or resource permissions, highlighting true microservices engineering patterns.

Optimized Cost Modeling: By opting for a serverless execution design, standard baseline operating costs remain precisely $0.00 within the AWS Free Tier, scaling lineally with operational use.

----

👥 Professional Contact
Name: Julia Ithemani

Role: Cloud & DevOps Engineer

Email: Jwbh2022@gmail.com

Project Hosting Endpoint: Live Portfolio Link
