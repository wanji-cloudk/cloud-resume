pip install boto3

2, Install Terraform
wget https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip

##Unzip the file:
bashunzip terraform_1.7.0_linux_amd64.zip

## Move it to your PATH:
```bash
sudo mv terraform /usr/local/bin/

##NB use below command if you have already install terraform
Download from terraform.io/downloads

3, Download the aws installer:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

## Unzip it:
unzip awscliv2.zip

##Install it:
sudo ./aws/install

##Verify
aws --version

## Make sure you sign up at aws.amazon.com

4,aws configure credetials:

```bash
aws configure

  AWS Access Key ID:      - your key
  AWS Secret Access Key:  - your secret
  Default region name:    us-east-1
  Default output format:  - press Enter

## Setup & Deployment

## Clone the repository:
bashgit clone https://github.com/your-username/EC2-Instance-State-Change-Monitoring.git
cd EC2-Instance-State-Change-Monitoring/ec2-monitoring

## Files and what they do:

Terraform (`main.tf`) This file sets up our EC2 instance, the SNS topic for alerts, and the CloudWatch Event Rule that "listens" for EC2 state changes

Boto3 (`upload.py`) Instead of using the AWS Console, i used this Python script to stop the instance. This will trigger the CloudWatch Event Rule i just built

## Verify your AMI ID

Get a valid Amazon Linux 2 AMI for us-east-1:

```bash
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" \
  --query "sort_by(Images, &CreationDate)[-1].ImageId" \
  --output text \
  --region us-east-1
Type yes when prompted. Copy the instance_id from the output.

## Deploy with Terraform
```bash
terraform init
terraform plan
terraform apply

Project Hosting Endpoint: Live Portfolio Link
"""
