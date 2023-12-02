
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo 'Hello, Terraform!' > output.txt"
  }
}

# Output the result
output "example_output" {
  value = null_resource.example.id
}
