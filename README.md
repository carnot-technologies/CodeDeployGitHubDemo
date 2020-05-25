# Motivation
In the early stage, most of our servers were deployed on Heroku. Heroku is a platform as a service (PAAS) which supports continuous integration from github.  

As the project scale started to grow, we started shifting our servers from Heroku to AWS for cheaper rates & better performance. Unlike Heroku, AWS is IAAS (Infrastructure as a service) and continuous integration of source code is not enabled by default. Instead, AWS provides us with its powerful CICD tools to manage this.  

Needless to say that without these tools, the code integration task itself would consume a lot of bandwidth, which can be otherwise used for fruitful development.

# What is AWS Code Deploy
To understand, what AWS Code Deploy is, we will first look at the broad picture of AWS code pipeline.

Below picture demonstrates a typical development cycle.

![AWS Code Pipeline](https://d1.awsstatic.com/Products/product-name/diagrams/product-page-diagram_CodePipeLine.7b8dd19eb6478b7f6f747d936c2f0b0b66757bbf.png)

1. For new features / bug fixes / maintenance, we change the source code and upload it to a version control software.
2. Prior to releasing these changes on the production, we typically want to ensure that the code build is stable after new changes
3. Optionally, we can create additional functional tests to ensure critical features are not mistakenly affected by a bad code
4. Many a times, it is a good practice to test out the new changes on a staging server where external components can interact with each other with test traffic.
5. Finally, once all stability is proven & testing is done, we want these changes to be deployed to production server.

This entire process can be automated to save the headache of manual work after each change.   
**AWS CodePipeline** is the automation-manager.  

For 1, AWS provides **CodeCommit** as the version control software which is built on top of github. However, we are continuing to use github directly which is also supported by AWS CICD.  
For 2 & 3, AWS provides **CodeBuild** where we can add our own test criteria.  
For 4 & 5, AWS provides **CodeDeploy** where we can choose the environment (dev/staging/prod) and deployment groups (EC2 / Lambda / ASG instances). CodeDeploy also supports rollback feature which can be used to go back to a stable deployment if something was wrong with the latest one.

All the automation configuration can be customized through AWS CodePipeline

For more details on setup, checkout the wiki page.
