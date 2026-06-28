# 🎬 Data Management – MovieLens 100K using Apache Spark & Cassandra

# 📖 Project Overview

This project demonstrates the implementation of an end to end **Big Data Management Pipeline** using the **MovieLens 100K Dataset**. The project integrates **Apache Hadoop Distributed File System (HDFS)**, **Apache Spark**, **Spark SQL** and **Apache Cassandra** to perform distributed data storage, processing, analytics, and NoSQL data persistence.

The workflow begins by loading the MovieLens dataset into **HDFS** followed by creating **Spark Resilient Distributed Datasets (RDDs)** and transforming them into **Spark DataFrames**. Spark SQL is then used to execute several analytical queries while Apache Cassandra serves as the persistent NoSQL database for storing and validating the processed analytical results.

---

# 🎯 Project Objectives

* 📂 Load MovieLens 100K dataset into HDFS.
* ⚡ Perform distributed data processing using Apache Spark.
* 🔄 Transform RDDs into Spark DataFrames.
* 🧹 Perform data preprocessing and validation.
* 📊 Execute analytical queries using Spark SQL.
* 🗄️ Store processed data into Apache Cassandra.
* ✅ Validate Cassandra tables by reading them back into Spark.

---

# 🛠️ Technologies Used

| Technology                   | Purpose                     |
| ---------------------------- | --------------------------- |
| 🐍 Python                    | Programming Language        |
| ⚡ Apache Spark               | Distributed Data Processing |
| 🧩 Spark SQL                 | SQL-based Analytics         |
| 📂 HDFS                      | Distributed File Storage    |
| 🗄️ Apache Cassandra         | NoSQL Database              |
| 🔗 Spark-Cassandra Connector | Spark–Cassandra Integration |
| 💻 HDP Sandbox               | Big Data Environment        |
| 🔐 PuTTY                     | Remote Linux Access         |

---

# 🔄 Project Workflow

```text
MovieLens Dataset
        │
        ▼
📂 Upload into HDFS
        │
        ▼
⚡ Apache Spark
        │
        ▼
RDD Creation
        │
        ▼
Spark DataFrame
        │
        ▼
🧹 Data Cleaning & Preprocessing
        │
        ▼
📊 Spark SQL Analytics
        │
        ▼
🗄️ Apache Cassandra
        │
        ▼
✅ Validation using Spark
```

---

# 📊 Analytical Tasks

The following analytical tasks were implemented using **Apache Spark SQL**.

| Task      | Description                                                      |
| --------- | ---------------------------------------------------------------- |
| ⭐ Task 1  | Calculate the average rating for each movie                      |
| 🏆 Task 2 | Identify the Top 10 highest-rated movies                         |
| 🎭 Task 3 | Identify active users and determine their favourite movie genres |
| 👥 Task 4 | Identify users below 20 years old                                |
| 🔬 Task 5 | Identify scientist users aged between 30 and 40 years            |

---

# ▶️ Execution Workflow

The project is executed in three stages.

## 📌 Step 1 – Environment Setup

```bash
spark-submit ndhsetup.py
```

This script:

* Imports required libraries.
* Loads MovieLens files from HDFS.
* Creates Spark RDDs.
* Converts RDDs into Spark DataFrames.
* Performs data preprocessing.

---

## 📌 Step 2 – Spark SQL Analysis

```bash
spark-submit ndhanalysis.py
```

This script:

* Registers temporary Spark SQL views.
* Executes the five analytical tasks.
* Displays analytical outputs.

---

## 📌 Step 3 – Cassandra Integration

```bash
spark-submit \
--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.3 \
ndhcassandra.py
```

This script:

* Creates Cassandra keyspace.
* Creates Cassandra tables.
* Writes Spark DataFrames into Cassandra.
* Reads Cassandra tables back into Spark.
* Validates the stored data.

---

# 📈 Expected Outputs

After successful execution, the following outputs are generated.

| Output                    | Description                                |
| ------------------------- | ------------------------------------------ |
| 📄 ndhsetup_output.md     | Environment setup execution log            |
| 📄 ndhanalysis_output.md  | Spark SQL analytical results               |
| 📄 ndhcassandra_output.md | Cassandra integration results              |
| 📊 Reporting Analysis     | Interpretation, screenshots and discussion |

---

# ✅ Validation Results

Successful execution is indicated by:

* ✔️ MovieLens dataset successfully loaded from HDFS.
* ✔️ Spark DataFrames successfully created.
* ✔️ Spark SQL analytical queries successfully executed.
* ✔️ Processed data successfully written into Apache Cassandra.
* ✔️ Cassandra tables successfully read back into Spark.
* ✔️ Validation confirms the integrity of stored records.

