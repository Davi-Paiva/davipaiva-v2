import os
from dotenv import load_dotenv
from aws_cdk import (
    Stack,
    RemovalPolicy,
    CfnOutput,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_certificatemanager as acm,
)
from constructs import Construct

load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        domain_name = os.getenv("DOMAIN", None)
        subdomain = os.getenv("SUBDOMAIN", None)
        certificate_arn = os.getenv("CERTIFICATE_ARN", None)
        
        # Create S3 bucket
        website_bucket = s3.Bucket(
            self, "WebsiteBucket",
            bucket_name=f"davipaiva-v2-website-{self.account}-{self.region}",
            website_index_document="index.html",
            website_error_document="error.html",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
            removal_policy=RemovalPolicy.DESTROY,  # Be careful in production!
            auto_delete_objects=True,  # Allows CDK to delete bucket contents
        )

        # Create Origin Access Identity for CloudFront
        oai = cloudfront.OriginAccessIdentity(
            self, "WebsiteOAI",
            comment="OAI for davipaiva-v2 website"
        )
        
        # Grant CloudFront OAI read access to S3 bucket
        website_bucket.grant_read(oai)

        # Look up the existing hosted zone in Route 53
        hosted_zone = route53.HostedZone.from_lookup(
            self, "HostedZone",
            domain_name=domain_name
        )
        
        # Import existing certificate
        certificate = acm.Certificate.from_certificate_arn(
            self, "Certificate",
            certificate_arn=certificate_arn
        )
        
        # Create CloudFront distribution
        distribution = cloudfront.Distribution(
            self, "WebsiteDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    website_bucket,
                    origin_access_identity=oai
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            domain_names=[subdomain],
            certificate=certificate,
            default_root_object="index.html",
        )
        
        # Create Route 53 A record pointing to CloudFront
        route53.ARecord(
            self, "WebsiteRecord",
            zone=hosted_zone,
            record_name="v2",
            target=route53.RecordTarget.from_alias(
                targets.CloudFrontTarget(distribution)
            )
        )

        # Deploy content from build to S3 bucket
        s3deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[s3deploy.Source.asset("../dist")],
            destination_bucket=website_bucket,
            distribution=distribution,
            distribution_paths=["/*"],  # Invalidate all CloudFront cache on deploy
        )
        
        # Output the custom domain URL
        CfnOutput(
            self, "WebsiteURL",
            value=f"https://{subdomain}",
            description="URL of the website"
        )
        
        # Output the CloudFront URL as backup
        CfnOutput(
            self, "CloudFrontURL",
            value=f"https://{distribution.distribution_domain_name}",
            description="CloudFront URL (backup)"
        )
        
        # Output the distribution ID
        CfnOutput(
            self, "DistributionId",
            value=distribution.distribution_id,
            description="CloudFront distribution ID"
        )