variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "bucket_name" {
  type        = string
  description = "julia_aws_s3_bucket"
  default     = "julia-ithemani-cloud-resume-2026" 
}