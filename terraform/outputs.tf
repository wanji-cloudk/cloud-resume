output "api_invoke_url" {
  value       = aws_apigatewayv2_api.http_api.api_endpoint
  description = "The root URL for your API Gateway instance"
}

output "s3_website_endpoint" {
  value       = aws_s3_bucket_website_configuration.s3_hosting.website_endpoint
  description = "The public URL to view your static resume site"
}