# Project 06: Real-time Processing

## Description
*Company XYZ* is new uprising online retail startups. Recently, their Software Enginner team applying user activity tracker on their web and apps. Data Analyst and Data Scientist team are interest on exploring these data. CDO of *Company XYZ* approach you, a Data Engineer, to help him building Real-Time Data Processing framework, so the data could be further analyzed.

You will be given data stream specification, along with dummy data producer. They want the data to be stored in **PostgreSQL** database. Create view to show simple summary about their real-time data.

## Documentation

### Producer

Producer instances will generate dummy event data into Kafka topics. All of events are click link event, which triggered when user click any element or page in application. Tracker will send data in encoded JSON.

<br>

**Data Structure**

```js
{
    "core": {
        "page_type": str. Page label/type (home, product, checkout or payment),
        "page_url": str. URL of element/page clicked
    },
    "user": {
        "user_id": int. User unique ID,
        "session_id": int. Session unique ID
    }
}
```

## Requirements
- Create data processing framework to process real-time data into PostgreSQL

## Tasks
- Create Kafka instances for producer topics
- Create PostgreSQL instances
- Create Consumer instances to load data into PostgreSQL

To view this project solution, access this [link](./solution).