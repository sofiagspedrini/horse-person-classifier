## Architecture Overview

<pre>

+------------------+       +------------------+       +-------------------+
| Data Sources     |-----> | Data Ingestion   |-----> | Data Lake /       |
| (i.e. APIs)      |       | (i.e. S3)        |       | (i.e. S3)         |
+------------------+       +------------------+       +-------------------+
                                                           |
                                                           v
                                                  +------------------+
                                                  | Data Preprocessing|
                                                  | (i.e. ETL Jobs)   |
                                                  +------------------+
                                                           |
                                                           v
                                              +--------------------------+
                                              | Model Training & Tuning  |
                                              | (i.e. MLFlow)            |
                                              +--------------------------+
                                                           |
                                                           v
                                              +--------------------------+
                                              | Model Registry           |
                                              | (i.e. MLFlow)            |
                                              +--------------------------+
                                                           |
                                                           v
                                              +--------------------------+
                                              | Model Serving            |
                                              | (i.e. Lambda)            |
                                              +--------------------------+
                                                           |
                                                           v
                                              +--------------------------+
                                              | Monitoring & Retraining  |
                                              | (i.e. Custom Metrics)    |
                                              +--------------------------+
</pre>

## Components & Connections
1. Data Sources

Images and videos from multiple sources, as cameras, APIs, etc.

2. Data Ingestion

Receives and batches data from the sources into a centralized storage in real time.


3. Data Storage

Stores raw and preprocessed images/videos as history, that can be later used for debug, performance tests and auditabilition process.


4. Data Preprocessing

Performs the necessary preprocessing. In this project, it included data resizing, and grayscaling and reshaping.


5. Model Training & Hyperparameter Tuning

Ideally included a distributed GPU training for the multi-class classification model. Automatically tunes the model in the pipeline.


6. Model Registry

Keeps and tracks the code version control and metrics.


7. Model Serving

Scalable REST API for real-time inference.


8. Monitoring & Retraining

Monitors the model quality, in case the data pattern changes and the model needs to be retrained for example. 
Also monitors infra health (i.e. overloads and peaks)