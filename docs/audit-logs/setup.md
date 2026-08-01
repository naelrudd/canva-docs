Source: https://www.canva.dev/docs/audit-logs/setup/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Canva audit logs

How to set up an AWS S3 bucket for Canva audit logs.

Canva stores audit log data in an [Amazon S3 bucket](https://aws.amazon.com/s3/) that your organization owns and manages. We add events to your S3 bucket every minute as a gzipped archive containing [JSONL](https://jsonlines.org/) content. We store the files in hourly folders, in the format `orgId/yyyy/MM/dd/HH`. To let Canva send audit logs to your S3 bucket, Canva requires [`PutObject` permission](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) on the S3 bucket.

To start receiving audit logs, you need to:

1. Open the Canva Audit logs configuration page.
2. Create an Amazon S3 bucket.
3. Grant Canva access to the S3 bucket.
4. Save the S3 bucket details to your Canva account.

This article walks you through creating the required AWS resources and adding their details to your Canva account.

## Open the Canva Audit logs configuration page

Access the [Canva Audit logs page](https://www.canva.com/settings/audit-logs). From the Canva homepage, go to **Settings**, under **Organization settings**, select **Audit logs**.

## Create an S3 bucket

1. Sign into the [AWS Management Console](https://aws.amazon.com/console/).
2. Open the [S3 console](https://console.aws.amazon.com/s3/).
3. Select **Create bucket**.
4. Choose your AWS Region, enter a bucket name (e.g., `canva-audit-logs`), and select **General purpose**.
5. Under **Object Ownership**, select **ACLs disabled (recommended)**.
6. Under **Block Public Access**, select **Block *all* public access**.
7. Configure **Default encryption** (SSE-S3, SSE-KMS, or DSSE-KMS).
8. Click **Create bucket**.

## Grant Canva access to the S3 bucket

### Create a policy

For SSE-S3 encryption:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject"],
      "Resource": "arn:aws:s3:::<audit-logs-s3-bucket-name>/*"
    }
  ]
}
```

For SSE-KMS or DSSE-KMS encryption, add `kms:GenerateDataKey` permission with the KMS key ARN.

### Create a role

1. In the IAM console, select **Roles** > **Create role**.
2. Under **Trusted entity type**, select **Custom trust policy**.
3. From the Canva Audit logs settings page, copy the **Trust policy** (specific to your organization) and paste it into the editor.
4. Attach the policy you created.
5. Enter a role name (e.g., `canva-audit-logs-s3-upload-role`) and click **Create Role**.
6. Copy the AWS role ARN.

## Save the S3 bucket details to your Canva account

On the Canva **Audit logs** page, configure:

* **Region**: The AWS region of the S3 bucket.
* **AWS role ARN**: The ARN of the IAM role.
* **S3 bucket name**: The name of your S3 bucket.
* **S3 key prefix** (optional): An S3 key prefix.

Click **Save**. Audit logs will begin arriving within a few minutes.
