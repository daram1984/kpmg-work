terraform {
    backend "s3" {
        bucket = "raviterraformstatefile"
        key = "myterraform.tfstate"
        region = "us-east-1"
    }
}