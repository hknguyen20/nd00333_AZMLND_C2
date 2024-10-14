# Operationalizing Machine Learning

In this project, I started by running an Auto ML experiment with the classification task on the Bankmarketing dataset. Then, I deploy the best model from the run, with logging and application insights enabled for monitoring and explanability. Next, I hosted swagger locally to view the available HTTP API methods and responses. The `endpoint.py` script was used to interact with the API, returning the model’s predictions in JSON format. Finally, I created and published a pipeline using the Bankmarketing dataset and the AutoML module, and consumed the pipeline endpoint.
 
## Architectural Diagram

  ![Architectural Diagram](https://github.com/user-attachments/assets/c56a2f7a-440e-4772-98c6-78e6a5bfcf1f)


## Key Steps
### 1. Create and run Auto ML Experiment
- Bankmarketing Dataset uploaded to ML Studio

  <img width="941" alt="dataset" src="https://github.com/user-attachments/assets/239ad4e9-b99c-4ee6-bbdd-b96b6e45728a">

- Auto ML Experiment is shown as completed
  
  <img width="529" alt="exp completed" src="https://github.com/user-attachments/assets/a39fc5c5-b73c-475e-a8e8-b41ffcfdee20">
  
- Best model: Voting Ensemble

  <img width="459" alt="best model" src="https://github.com/user-attachments/assets/2823eade-9bb8-4dd7-bdc4-2d13e8352e6d">


### 2. Deploy the best model
- Best model deployed.

  <img width="481" alt="deployment completed" src="https://github.com/user-attachments/assets/943ea607-479f-4210-ae73-491299cac96d">

- Logging when run logs.py

  <img width="940" alt="logging" src="https://github.com/user-attachments/assets/a50df1cc-a7c0-47b6-b965-edef923c8409">
     
-  Enabled application insights.

    <img width="461" alt="application insights enabled" src="https://github.com/user-attachments/assets/5ee6b17d-81a3-476a-ad71-55be927c7825">


### 3. Swagger Documentation and Consuming Endpoints
- Swagger runs on localhost showing the HTTP API methods and responses for the model

  <img width="1202" alt="swagger" src="https://github.com/user-attachments/assets/08fa1438-54d1-4676-b9ae-db72b5cd972e">

- endpoint.py  script runs against API producing JSON output from model

  <img width="568" alt="consume" src="https://github.com/user-attachments/assets/47bb7cc8-f8fd-42cd-8342-6bf7e13b7174">

### 4. Create, Publish and Consume a Pipeline
- Pipeline has been created

  <img width="1238" alt="pipeline created" src="https://github.com/user-attachments/assets/91af668e-851d-4090-9bbf-0bc63d2d2635">

- Pipeline endpoint

  <img width="1241" alt="pipeline endpoint" src="https://github.com/user-attachments/assets/48e01b76-b99b-4f5a-9db3-419ddea9f498">

- Bankmarketing dataset with AutoML module

  <img width="681" alt="pipeline visualized" src="https://github.com/user-attachments/assets/8606d088-d502-49cf-8506-6887ef846279">

  
- 'Published pipeline overview' showing a REST endpoint and a status of ACTIVE

  <img width="1238" alt="published pipeline overview" src="https://github.com/user-attachments/assets/ad8a75ce-2c97-440e-ac6b-3e472b3b872e">

- In Jupyter Notebook, showing that 'Use RunDetails Widget' shows the step runs

  <img width="987" alt="steps run" src="https://github.com/user-attachments/assets/8fdf5aee-bfc3-4972-ab3d-ed2a5207b75e">
  
- In ML Studio showing run jobs

  <img width="1252" alt="run jobs" src="https://github.com/user-attachments/assets/7d42b60e-7909-403c-9fac-05223868eb90">

  
## Screen Recording

[Screencast on Youtube](https://youtu.be/H679kVAIDHQ)
