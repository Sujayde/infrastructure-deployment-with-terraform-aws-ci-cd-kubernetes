resource "aws_cloudwatch_dashboard" "app_dashboard" {
  dashboard_name = "MyAppDashboard"
  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric"
        x = 0
        y = 0
        width = 12
        height = 6
        properties = {
          metrics = [
            [ "MyApp", "RequestCount", { "stat": "Sum" } ],
            [ ".", "ErrorCount", { "stat": "Sum" } ]
          ]
          period = 300
          title = "App Requests and Errors"
          region = "us-east-1"
        }
      }
      # Add more widgets for ALB, RDS, etc.
    ]
  })
}
