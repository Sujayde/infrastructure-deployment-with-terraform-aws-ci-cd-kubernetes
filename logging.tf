resource "aws_eks_cluster" "cluster" {
  # ...
  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
}
