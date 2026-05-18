Frontend Client 
│
├──► (Static Hosting) ──► AWS S3 Bucket (Public Website Configuration)
│
└──► (Dynamic Content) ──► AWS API Gateway ──► AWS Lambda (Python) ──► Amazon DynamoDB (NoSQL Counter)




### 🔹 Frontend Layer
* **Storage & Hosting:** AWS S3 configured for static website hosting.
* **Tech Stack:** Semantic HTML5, CSS3 responsive layout, and Vanilla asynchronous JavaScript (`Fetch API`).
* **Dynamic Content:** A custom client-side script that calls the backend production endpoint asynchronously on page load to retrieve and increment the global view count seamlessly without blocking layout rendering.

### 🔹 Backend Layer (Serverless API)
* **API Routing:** AWS API Gateway REST API handling traffic routing, CORS policies, and abstraction of the underlying function endpoints.
* **Compute Integration:** AWS Lambda executing an optimized Python execution environment. The function securely performs an atomic conditional update operation on the state database.
* **State Database:** Amazon DynamoDB handling tracking data natively in a single NoSQL item structure designed for sub-millisecond data persistence.

### 🔹 DevOps & Infrastructure as Code (IaC)
* **Provisioning:** Entire stack built declaratively using HashiCorp Terraform configuration blocks (`main.tf`).
* **State Operations:** Automated resource dependency mapping ensuring proper deployment execution chains (e.g., ensuring API permissions exist prior to public interface exposure).
* **Asset Lifecycle:** Programmatic management of website application binaries (`index.html`, `main.js`) using native `aws_s3_object` synchronization resources to eliminate manual interface coupling.

---

## Repository Directory Tree

```text
.
├── frontend/                  # Static website application code
│   ├── index.html             # Resume content and structure
│   ├── style.css              # Custom styling and layout design
│   └── main.js                # Asynchronous JavaScript API counter logic
└── terraform/                 # Infrastructure as Code (IaC) configurations
    ├── main.tf                # Core AWS resource blueprints (S3, API Gateway, Lambda, DynamoDB)
    ├── provider.tf            # AWS configuration constraints
    └── terraform.tfstate      # Locally recorded infrastructure state configuration
⚙️ Cloud Resources Provisioned Natively
aws_s3_bucket & aws_s3_bucket_website_configuration: Configures access controls, bucket policies, and sets up index documents for static file servers.

aws_dynamodb_table: Schema configured with an atomic partition key (HashKey) to store global tracking metrics safely across concurrent access instances.

aws_lambda_function: Packages code runtimes, defines execution execution limits, environment variables, and assigns explicit IAM Execution Roles.

aws_api_gateway_rest_api: Exposes /visitor endpoint structures, orchestrates integrations, and structures access points.

aws_iam_role & aws_iam_policy: Strict Principle of Least Privilege (PoLP) configuration granting precise read/write access explicitly restricted to target DynamoDB tables.

aws_s3_object: Direct declarative pipeline deployment maps that bind, content-type tag, and deploy local development workspace code to AWS live storage targets automatically.

  Local Implementation & Replication Guide
To replicate or modify this infrastructure stack locally, ensure you have configured your development system with the Terraform CLI and authentic AWS Identity credentials.

1. Backend Endpoint Adjustments
Navigate to frontend/main.js and modify the targeted backend endpoint mapping:

JavaScript
const apiEndpoint = "https://YOUR_API_GATEWAY_[ID.execute-api.us-east-1.amazonaws.com/visitor](https://ID.execute-api.us-east-1.amazonaws.com/visitor)";
2. Initialize and Deploy Infrastructure
Navigate to your IaC workspace folder in your command-line workspace and execute resource alignment:

```bash
cd terraform

# Initialize provider modules and cloud registry backends
./terraform init

# Run deterministic environment checks to view structural updates
./terraform plan

# Deploy infrastructure configurations natively to your live AWS account
./terraform apply -auto-approve
💡 Key Architectural Takeaways
Atomic State Updates: The database access function relies on an optimized conditional database update script rather than reading and rewriting states sequentially, protecting transaction counters against runtime race conditions.

Infrastructure Decoupling: Modifying client interface layouts requires no functional code changes to API endpoints or resource permissions, highlighting true microservices engineering patterns.

Optimized Cost Modeling: By opting for a serverless execution design, standard baseline operating costs remain precisely $0.00 within the AWS Free Tier, scaling lineally with operational use.

 Professional Contact
Name: Julia Ithemani

Role: Cloud & DevOps Engineer

Email: Jwbh2022@gmail.com

Project Hosting Endpoint: Live Portfolio Link
"""
