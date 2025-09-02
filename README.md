
# #Terraform AWS Infrastructure Setup

This Terraform project provisions a VPC with public/private subnets across 2 AZs, Internet and NAT gateways, Application Load Balancer, Auto Scaling Group, RDS PostgreSQL, Bastion host, and related security groups.

---

## Prerequisites

- Terraform Version
- AWS CLI configured with appropriate credentials
- SSH key pair created in the target AWS region

---

## Setup and Deployment

1. Clone this repo

```bash
git clone <repo-url>
cd terraform-infra
