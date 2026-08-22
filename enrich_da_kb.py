import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "data-analyst")
evidence_dir = os.path.join(base_dir, "evidence", "data-analyst")

# 1. Enrich da_sql.json
da_sql = {
  "skill_id": "da_sql",
  "name": "SQL & Querying",
  "category": "database",
  "description": "Focuses strictly on query writing: SELECT, JOINs, aggregations, window functions, and optimization.",
  "subskills": [
    {
      "id": "select_filtering",
      "name": "Basic SELECT & Filtering",
      "description": "Extracting columns and filtering rows using WHERE, IN, BETWEEN, and LIKE operators.",
      "keywords": ["SELECT", "WHERE", "IN", "BETWEEN", "LIKE", "AND", "OR", "NOT"]
    },
    {
      "id": "basic_joins",
      "name": "Basic JOINs (INNER/LEFT)",
      "description": "Combining tables using INNER JOIN and LEFT JOIN based on relational keys.",
      "keywords": ["INNER JOIN", "LEFT JOIN", "ON", "USING", "FOREIGN KEY"]
    },
    {
      "id": "group_by_aggs",
      "name": "GROUP BY & Aggregations",
      "description": "Aggregating data using GROUP BY and functions like SUM, COUNT, AVG, MIN, MAX.",
      "keywords": ["GROUP BY", "HAVING", "SUM", "COUNT", "AVG", "MIN", "MAX"]
    },
    {
      "id": "subqueries",
      "name": "Subqueries",
      "description": "Writing nested queries in SELECT, FROM, or WHERE clauses.",
      "keywords": ["subquery", "nested query", "EXISTS", "ANY", "ALL"]
    },
    {
      "id": "window_functions",
      "name": "Window Functions",
      "description": "Performing calculations across a set of table rows related to the current row using OVER, PARTITION BY, RANK, etc.",
      "keywords": ["OVER", "PARTITION BY", "ROW_NUMBER", "RANK", "DENSE_RANK", "LEAD", "LAG"]
    },
    {
      "id": "ctes",
      "name": "Common Table Expressions (CTEs)",
      "description": "Creating temporary named result sets using the WITH clause for better readability and recursion.",
      "keywords": ["WITH", "CTE", "recursive CTE"]
    },
    {
      "id": "query_optimization",
      "name": "Query Optimization",
      "description": "Analyzing execution plans and rewriting queries to reduce runtime and resource consumption.",
      "keywords": ["EXPLAIN", "EXPLAIN ANALYZE", "index scan", "table scan", "cost", "optimization"]
    },
    {
      "id": "complex_joins",
      "name": "Complex/Advanced JOINs",
      "description": "Using RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN, and self-joins for complex relational mapping.",
      "keywords": ["FULL OUTER JOIN", "RIGHT JOIN", "CROSS JOIN", "self join"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "SQL files with complex window functions",
        "detection": "content_analysis",
        "pattern": "(?i)OVER\\s*\\(\\s*PARTITION\\s+BY",
        "strength": 0.8,
        "maps_to": ["da_sql.window_functions"]
      },
      {
        "signal": "SQL files utilizing CTEs",
        "detection": "content_analysis",
        "pattern": "(?i)WITH\\s+\\w+\\s+AS\\s*\\(",
        "strength": 0.7,
        "maps_to": ["da_sql.ctes"]
      },
      {
        "signal": "SQL files analyzing query plans",
        "detection": "content_analysis",
        "pattern": "(?i)EXPLAIN\\s+ANALYZE",
        "strength": 0.9,
        "maps_to": ["da_sql.query_optimization"]
      }
    ],
    "cv": [
      {
        "signal": "Advanced SQL queries or optimization mentioned in projects",
        "strength": 0.6,
        "maps_to": ["da_sql.query_optimization", "da_sql.window_functions", "da_sql.ctes"]
      }
    ],
    "linkedin": [
      {
        "signal": "SQL optimization skill endorsed",
        "strength": 0.5,
        "maps_to": ["da_sql.query_optimization"]
      }
    ],
    "assessment": [
      {
        "signal": "Can write a query calculating running totals using window functions",
        "strength": 1.0,
        "maps_to": ["da_sql.window_functions"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["select_filtering", "basic_joins", "group_by_aggs"],
      "description": "Can write basic operational queries to extract and aggregate data from a few joined tables."
    },
    "mid": {
      "expected_subskills": ["subqueries", "window_functions", "ctes"],
      "description": "Can write analytical queries using CTEs and window functions for ranking and running totals."
    },
    "senior": {
      "expected_subskills": ["query_optimization", "complex_joins"],
      "description": "Can optimize slow-running queries, analyze execution plans, and handle complex self-joins or cross-joins."
    }
  }
}

# 2. Enrich da_data_collection.json
da_data_collection = {
  "skill_id": "da_data_collection",
  "name": "Data Collection & Access",
  "category": "data_engineering",
  "description": "Focuses on connecting to APIs, databases, reading files (CSV/Excel), and web scraping.",
  "subskills": [
    {
      "id": "csv_excel_reading",
      "name": "Reading CSV/Excel files",
      "description": "Loading flat files into memory using pandas, csv module, or openpyxl.",
      "keywords": ["read_csv", "read_excel", "openpyxl", "csv.reader"]
    },
    {
      "id": "basic_db_connections",
      "name": "Database Connection Strings",
      "description": "Connecting to SQL/NoSQL databases programmatically using drivers like psycopg2, pyodbc, or sqlalchemy.",
      "keywords": ["sqlalchemy", "psycopg2", "pyodbc", "create_engine", "pymongo"]
    },
    {
      "id": "api_requests",
      "name": "REST API Requests",
      "description": "Fetching JSON/XML data from REST APIs using requests or urllib.",
      "keywords": ["requests.get", "requests.post", "urllib", "json.loads", "REST API"]
    },
    {
      "id": "web_scraping",
      "name": "Web Scraping",
      "description": "Extracting unstructured data from HTML pages using BeautifulSoup, Scrapy, or Selenium.",
      "keywords": ["BeautifulSoup", "Scrapy", "Selenium", "find_all", "xpath"]
    },
    {
      "id": "pagination_handling",
      "name": "API Pagination Handling",
      "description": "Looping through API pages (cursor or offset based) to collect full datasets.",
      "keywords": ["offset", "limit", "next_page", "cursor", "pagination"]
    },
    {
      "id": "cloud_storage_access",
      "name": "S3/GCS Access",
      "description": "Programmatically reading/writing files from cloud object storage (AWS S3, Google Cloud Storage).",
      "keywords": ["boto3", "google-cloud-storage", "s3fs", "blob storage"]
    },
    {
      "id": "streaming_data",
      "name": "Streaming Data APIs",
      "description": "Connecting to WebSockets or streaming endpoints (e.g., Kafka, Twitter API).",
      "keywords": ["websocket", "kafka", "streaming", "confluent_kafka"]
    },
    {
      "id": "automated_etl_scripts",
      "name": "Automated Data Pulls",
      "description": "Scheduling scripts (cron, Airflow basics) to periodically fetch and dump data.",
      "keywords": ["cron", "airflow", "schedule", "job", "ETL script"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Python script using BeautifulSoup or Selenium",
        "detection": "dependency_extraction",
        "pattern": "bs4|beautifulsoup4|selenium",
        "strength": 0.8,
        "maps_to": ["da_data_collection.web_scraping"]
      },
      {
        "signal": "Python script connecting to databases via SQLAlchemy",
        "detection": "content_analysis",
        "pattern": "create_engine|sessionmaker",
        "strength": 0.7,
        "maps_to": ["da_data_collection.basic_db_connections"]
      },
      {
        "signal": "Python script interacting with S3 via boto3",
        "detection": "content_analysis",
        "pattern": "boto3\\.client\\('s3'\\)",
        "strength": 0.9,
        "maps_to": ["da_data_collection.cloud_storage_access"]
      }
    ],
    "cv": [
      {
        "signal": "Experience building web scrapers",
        "strength": 0.6,
        "maps_to": ["da_data_collection.web_scraping"]
      }
    ],
    "linkedin": [
      {
        "signal": "Web Scraping endorsed",
        "strength": 0.4,
        "maps_to": ["da_data_collection.web_scraping"]
      }
    ],
    "assessment": [
      {
        "signal": "Can write a script to paginate through a REST API to fetch all records",
        "strength": 1.0,
        "maps_to": ["da_data_collection.pagination_handling", "da_data_collection.api_requests"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["csv_excel_reading", "basic_db_connections"],
      "description": "Can connect to local/network databases and read standard flat files into analysis tools."
    },
    "mid": {
      "expected_subskills": ["api_requests", "web_scraping", "pagination_handling"],
      "description": "Can extract data from the web using REST APIs and scraping, handling pagination and rate limits."
    },
    "senior": {
      "expected_subskills": ["cloud_storage_access", "streaming_data", "automated_etl_scripts"],
      "description": "Can architect automated, scheduled scripts to pull from cloud storage or streaming APIs."
    }
  }
}

with open(os.path.join(skills_dir, "da_sql.json"), "w", encoding="utf-8") as f:
    json.dump(da_sql, f, indent=2)

with open(os.path.join(skills_dir, "da_data_collection.json"), "w", encoding="utf-8") as f:
    json.dump(da_data_collection, f, indent=2)


# 3. Update Assessment with real Big Data questions
assessment_path = os.path.join(evidence_dir, "assessment.json")
with open(assessment_path, "r", encoding="utf-8") as f:
    assessment_data = json.load(f)

# Replace the generic big data questions with real ones
if "da_machine_learning.big_data_hadoop" in assessment_data["sample_questions_by_composite_key"]:
    assessment_data["sample_questions_by_composite_key"]["da_machine_learning.big_data_hadoop"] = [
        {
            "level": "senior",
            "type": "scenario",
            "question": "You have a 500GB log dataset stored in HDFS. Explain how the MapReduce paradigm would process this data, and how you would query it using Hive.",
            "expected_answer_keywords": [
                "MapReduce",
                "HDFS",
                "NameNode",
                "DataNode",
                "HiveQL",
                "schema on read",
                "distributed processing"
            ]
        }
    ]

if "da_machine_learning.big_data_spark" in assessment_data["sample_questions_by_composite_key"]:
    assessment_data["sample_questions_by_composite_key"]["da_machine_learning.big_data_spark"] = [
        {
            "level": "senior",
            "type": "scenario",
            "question": "Your pandas script is throwing OutOfMemory errors on a 50GB dataset. How would you migrate this logic to PySpark, and what is the difference between a DataFrame transformation and an action?",
            "expected_answer_keywords": [
                "PySpark",
                "RDD",
                "lazy evaluation",
                "transformations",
                "actions",
                "cluster computing",
                "distributed dataframe"
            ]
        }
    ]

with open(assessment_path, "w", encoding="utf-8") as f:
    json.dump(assessment_data, f, indent=2)

print("Files enriched successfully.")
