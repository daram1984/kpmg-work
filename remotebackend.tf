terraform {
    backend "s3" {
        bucket = "raviterraformstatefile"
        key = "myterraform.tfstate"
        region = "us-east-1"
        dynamodb_table = "terraform-state-lock"        
        }
}
