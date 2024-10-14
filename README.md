# Operationalizing Machine Learning

*TODO:* Write an overview to your project.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 
### 1. Create and run Auto ML Experiment
- Bankmarketing Dataset uploaded to ML Studio
  
    <img width="924" alt="Registered Bankmarketing Dataset available" src="https://github.com/user-attachments/assets/d6810df3-0d12-47d3-a81e-aaf7ceed1399">

- Auto ML Experiment is shown as completed
  
    <img width="1001" alt="Completed Experiment and Best model" src="https://github.com/user-attachments/assets/8ff69742-463d-4a50-a5a8-a54c92cba4de">

- Best model: Voting Ensemble


### 2. Deploy the best model
- Best model deployed.
  
   <img width="486" alt="Deployed Best Model" src="https://github.com/user-attachments/assets/833f8ba9-4f96-4a30-bde9-2d5c4ff66e04">
   
- Logging when run logs.py
  
    <img width="851" alt="Logging" src="https://github.com/user-attachments/assets/fef40384-14ef-4981-9541-4d236948b937"> 
      
-  Enabled application insights.
  
   <img width="486" alt="Enabled Application Insights " src="https://github.com/user-attachments/assets/967b1f37-c2cc-4305-84df-5ac2b59a488a">

### 3. Swagger Documentation and Consuming Endpoints
- Swagger runs on localhost showing the HTTP API methods and responses for the model
  
  <img width="527" alt="image" src="https://github.com/user-attachments/assets/ec0b53fa-0ed9-4a38-af03-d0027c464de0">
  
- endpoint.py  script runs against API producing JSON output from model
  
### 4. Create, Publish and Consume a Pipeline
- Pipeline has been created
  
- Pipeline endpoint
  
- Bankmarketing dataset with AutoML module
  
- 'Published pipeline overview' showing a REST endpoint and a status of ACTIVE
  
- In Jupyter Notebook, showing that 'Use RunDetails Widget' shows the step runs
  
- In ML Studio showing scheduled run
  
## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

