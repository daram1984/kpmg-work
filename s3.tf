resource "aws_s3_bucket" "prodbucket" {
  bucket = "myprod84bucket"

  tags = {
    Name        = "devbucket84"
    Environment = "PRODENV"
  }
   depends_on = [
    aws_vpc.my_vpc
  ]
}
