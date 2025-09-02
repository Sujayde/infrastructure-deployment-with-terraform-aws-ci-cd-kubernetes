resource "aws_cloudwatch_metric_alarm" "high_error_rate" {
  alarm_name          = "HighErrorRate"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "ErrorCount"
  namespace           = "MyApp"
  period              = 300
  statistic           = "Sum"
  threshold           = 10

  alarm_actions = [var.sns_topic_arn] # Notify via SNS
}
