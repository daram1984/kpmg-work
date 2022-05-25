resource "aws_vpc" "my_vpc" {
  cidr_block       = "${var.vpc_cidr}"
  enable_dns_hostnames = true

  tags = {
    Name = "${var.vpc_name}"
    envronment = "PROD"
  }
}

resource "aws_internet_gateway" "myvpcigw" {
  vpc_id = "${aws_vpc.my_vpc.id}"

  tags = {
    Name = "${var.igw_name}"
    environment = "PROD"
  }
}
