resource "aws_instance" "web-1" {
    count = 3 #0,1,2
    #ami = var.imagename
     ami = "ami-09d56f8956ab235b3"
    #ami = "${data.aws_ami.my_ami.id}"
    availability_zone = "us-east-1a"
    instance_type = "t2.nano"
    key_name = "devkey"
    subnet_id = "${aws_subnet.subnet1-public.id}"
    vpc_security_group_ids = ["${aws_security_group.allow_all.id}"]
    associate_public_ip_address = true	
    tags = {
        Name = "Server-${count.index+1}"
        Env = "Prod"
        Owner = "Ravi"
	    CostCenter = "ABCD"
    }
}