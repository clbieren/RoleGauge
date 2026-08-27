import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'data-engineer')
evidence_dir = os.path.join(base_dir, 'evidence', 'data-engineer')
roles_dir = os.path.join(base_dir, 'roles', 'data-engineer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

skills = {}

# 1. de_programming
skills["de_programming"] = {
  "skill_id": "de_programming",
  "name": "Data Engineering Programming & Systems",
  "category": "programming",
  "description": "Proficiency in core programming languages for data engineering (Python, Scala/Java, SQL), object-oriented and functional data processing, type safety, concurrency, memory management, and serialization protocols.",
  "subskills": [
    {
      "id": "python_core_oop",
      "name": "Python Core & Object-Oriented Design",
      "description": "Data structures, generators, decorators, context managers, classes, abstract base classes, and clean architecture in Python.",
      "keywords": ["generator", "yield", "decorator", "contextmanager", "dunder methods", "dataclass", "pydantic", "abc", "protocol", "OOP", "inheritance", "composition"]
    },
    {
      "id": "typing_data_structures",
      "name": "Type Safety & Specialized Data Structures",
      "description": "Type hinting with typing module, Pydantic data validation, collections (deque, defaultdict, Counter), and efficient in-memory data structures.",
      "keywords": ["type hints", "typing", "Union", "Optional", "Literal", "Pydantic", "BaseModel", "namedtuple", "defaultdict", "deque", "Counter", "dataclasses"]
    },
    {
      "id": "functional_programming",
      "name": "Functional Data Processing & Immutability",
      "description": "Pure functions, immutability, map/filter/reduce, lambda expressions, itertools, functools, and functional pipelines.",
      "keywords": ["pure functions", "immutability", "map", "filter", "reduce", "itertools", "functools", "partial", "lru_cache", "pipe", "higher-order functions"]
    },
    {
      "id": "concurrency_multiprocessing",
      "name": "Concurrency, Multiprocessing & AsyncIO",
      "description": "Thread vs Process vs Coroutine, ThreadPoolExecutor, ProcessPoolExecutor, asyncio for I/O-bound data fetching, and GIL implications.",
      "keywords": ["multiprocessing", "threading", "asyncio", "ThreadPoolExecutor", "ProcessPoolExecutor", "GIL", "locks", "semaphores", "queue", "concurrent.futures"]
    },
    {
      "id": "memory_management_profiling",
      "name": "Memory Management & Performance Profiling",
      "description": "Garbage collection, memory leaks in long-running jobs, memory profiling (memory_profiler, tracemalloc), cProfile, and CPU profiling.",
      "keywords": ["memory_profiler", "tracemalloc", "cProfile", "garbage collection", "gc", "sys.getsizeof", "memory leak", "CPU profiling", "line_profiler"]
    },
    {
      "id": "serialization_protocols",
      "name": "Data Serialization & Binary Protocols",
      "description": "Working with JSON, Pickle, Protocol Buffers (protobuf), FlatBuffers, Avro, MessagePack, and schema evolution rules.",
      "keywords": ["protobuf", "Protocol Buffers", "Avro", "MessagePack", "Pickle", "json serialization", "binary encoding", "schema evolution", "gRPC"]
    },
    {
      "id": "scala_jvm_ecosystem",
      "name": "Scala & JVM Ecosystem for Big Data",
      "description": "Scala syntax, case classes, pattern matching, traits, implicits, JVM memory tuning, and sbt build tool for big data engines.",
      "keywords": ["Scala", "JVM", "sbt", "case class", "pattern matching", "traits", "implicits", "garbage collection tuning", "heap size", "JVM flags"]
    },
    {
      "id": "data_structures_algorithms",
      "name": "Algorithms & Data Structures for Scale",
      "description": "Sorting, searching, hash maps, binary trees, graph traversals for DAG dependencies, and Big-O computational complexity.",
      "keywords": ["Big-O", "hash table", "binary search", "graph traversal", "topological sort", "DAG", "priority queue", "heap", "sliding window"]
    },
    {
      "id": "package_dependency_management",
      "name": "Packaging, Environments & Dependency Isolation",
      "description": "Managing virtual environments (venv, uv, poetry), wheel builds, pyproject.toml, requirements locking, and private PyPI registries.",
      "keywords": ["poetry", "uv", "pip", "pyproject.toml", "virtualenv", "wheel", "conda", "setup.py", "requirements.txt", "lockfile"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Designed high-throughput Python data pipelines and microservices",
        "strength": 0.5,
        "maps_to": ["de_programming.python_core_oop", "de_programming.concurrency_multiprocessing"]
      },
      {
        "signal": "Developed big data processing jobs in Scala using JVM optimization",
        "strength": 0.5,
        "maps_to": ["de_programming.scala_jvm_ecosystem", "de_programming.memory_management_profiling"]
      }
    ],
    "linkedin": [
      {
        "signal": "Skill endorsements for Python, Scala, and Concurrency",
        "strength": 0.3,
        "maps_to": ["de_programming.python_core_oop", "de_programming.typing_data_structures"]
      }
    ],
    "github": [
      {
        "pattern": "*.py|pyproject.toml|poetry.lock|*.scala|build.sbt",
        "strength": 1.0,
        "maps_to": [
          "de_programming.python_core_oop",
          "de_programming.typing_data_structures",
          "de_programming.functional_programming",
          "de_programming.concurrency_multiprocessing",
          "de_programming.memory_management_profiling",
          "de_programming.serialization_protocols",
          "de_programming.scala_jvm_ecosystem",
          "de_programming.data_structures_algorithms",
          "de_programming.package_dependency_management"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Python/Scala algorithms and concurrent data pipeline test",
        "strength": 1.0,
        "maps_to": [
          "de_programming.python_core_oop",
          "de_programming.typing_data_structures",
          "de_programming.functional_programming",
          "de_programming.concurrency_multiprocessing",
          "de_programming.memory_management_profiling",
          "de_programming.serialization_protocols",
          "de_programming.scala_jvm_ecosystem",
          "de_programming.data_structures_algorithms",
          "de_programming.package_dependency_management"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["python_core_oop", "typing_data_structures", "package_dependency_management"],
      "description": "Writes clean, type-annotated Python scripts, manages virtual environments, and builds OOP data extraction utilities."
    },
    "mid": {
      "expected_subskills": ["functional_programming", "concurrency_multiprocessing", "serialization_protocols", "data_structures_algorithms"],
      "description": "Builds high-throughput concurrent data applications, applies functional paradigms, and optimizes data serialization."
    },
    "senior": {
      "expected_subskills": ["memory_management_profiling", "scala_jvm_ecosystem"],
      "description": "Solves complex memory leaks, profiles CPU/memory bottlenecks in long-running jobs, and architects Scala/JVM data pipelines."
    }
  }
}

# 2. de_sql_advanced
skills["de_sql_advanced"] = {
  "skill_id": "de_sql_advanced",
  "name": "Advanced SQL & Database Internals",
  "category": "database",
  "description": "Advanced analytical querying, complex joins, window functions, recursive CTEs, query optimization, indexing strategies, and database execution internals.",
  "subskills": [
    {
      "id": "complex_joins_subqueries",
      "name": "Complex Joins, Sets & Correlated Subqueries",
      "description": "Inner, outer, cross, anti-joins, semi-joins, set operations (UNION, INTERSECT, EXCEPT), and correlated subquery optimization.",
      "keywords": ["LEFT JOIN", "INNER JOIN", "FULL OUTER JOIN", "CROSS JOIN", "ANTI JOIN", "SEMI JOIN", "UNION ALL", "INTERSECT", "EXCEPT", "correlated subquery"]
    },
    {
      "id": "window_functions_analytical",
      "name": "Window Functions & Analytical Aggregations",
      "description": "OVER clause, PARTITION BY, ORDER BY, framing (ROWS/RANGE BETWEEN), ranking (ROW_NUMBER, RANK, DENSE_RANK), navigation (LEAD, LAG), and running aggregates.",
      "keywords": ["ROW_NUMBER", "RANK", "DENSE_RANK", "NTILE", "LEAD", "LAG", "FIRST_VALUE", "LAST_VALUE", "PARTITION BY", "ROWS BETWEEN", "UNBOUNDED PRECEDING"]
    },
    {
      "id": "ctes_recursive_queries",
      "name": "Common Table Expressions & Recursive Queries",
      "description": "Modular CTEs, WITH clauses, recursive queries for hierarchical data traversal, and query modularity.",
      "keywords": ["CTE", "WITH RECURSIVE", "hierarchical queries", "graph traversal SQL", "anchor member", "recursive member", "table expression"]
    },
    {
      "id": "indexing_b_tree_strategies",
      "name": "Indexing Strategies & Internal Structures",
      "description": "B-Tree, Hash, GiST, GIN, Bitmap indexes, composite indexes, covering indexes, partial indexes, and index selectivity.",
      "keywords": ["B-Tree", "GIN", "GiST", "Bitmap index", "composite index", "covering index", "INCLUDE clause", "partial index", "index selectivity"]
    },
    {
      "id": "query_execution_plans",
      "name": "Query Execution Plans & Cost-Based Optimization",
      "description": "Analyzing EXPLAIN / EXPLAIN ANALYZE, cost metrics, Seq Scan vs Index Scan, Hash Join vs Merge Join vs Nested Loop, and cardinality estimation.",
      "keywords": ["EXPLAIN ANALYZE", "Query Plan", "Seq Scan", "Index Scan", "Index Only Scan", "Hash Join", "Merge Join", "Nested Loop", "cost estimation", "cardinality"]
    },
    {
      "id": "partitioning_sharding",
      "name": "Table Partitioning & Database Sharding",
      "description": "Range, List, and Hash partitioning, partition pruning, dynamic partition elimination, and horizontal sharding strategies.",
      "keywords": ["partitioning", "RANGE partitioning", "LIST partitioning", "HASH partitioning", "partition pruning", "sharding", "distributed tables", "subpartitioning"]
    },
    {
      "id": "transactions_acid_isolation",
      "name": "Transactions, ACID Properties & Isolation Levels",
      "description": "ACID compliance, transaction management, isolation levels (Read Committed, Repeatable Read, Serializable), MVCC, and deadlocks.",
      "keywords": ["ACID", "isolation levels", "Read Committed", "Repeatable Read", "Serializable", "dirty read", "phantom read", "MVCC", "deadlock", "WAL"]
    },
    {
      "id": "stored_procedures_udfs",
      "name": "Stored Procedures, Triggers & User-Defined Functions",
      "description": "PL/pgSQL, T-SQL, procedural control flow, triggers, table-valued functions, and custom SQL UDFs.",
      "keywords": ["PL/pgSQL", "stored procedure", "trigger", "UDF", "table-valued function", "control flow", "cursor", "dynamic SQL"]
    },
    {
      "id": "db_performance_tuning",
      "name": "Database Performance Tuning & Statistics",
      "description": "ANALYZE, VACUUM, buffer cache hit ratio, connection pooling, temporary spill to disk, work_mem, and maintenance_work_mem tuning.",
      "keywords": ["VACUUM", "ANALYZE", "work_mem", "buffer cache", "connection pooling", "PgBouncer", "disk spill", "statistics collector", "query tuning"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Optimized slow-running analytical SQL queries and database indexes",
        "strength": 0.5,
        "maps_to": ["de_sql_advanced.query_execution_plans", "de_sql_advanced.indexing_b_tree_strategies", "de_sql_advanced.db_performance_tuning"]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements for Advanced SQL, PostgreSQL, and Query Optimization",
        "strength": 0.3,
        "maps_to": ["de_sql_advanced.window_functions_analytical", "de_sql_advanced.complex_joins_subqueries"]
      }
    ],
    "github": [
      {
        "pattern": "*.sql|queries/*.sql|migrations/*.sql|schema/*.sql",
        "strength": 1.0,
        "maps_to": [
          "de_sql_advanced.complex_joins_subqueries",
          "de_sql_advanced.window_functions_analytical",
          "de_sql_advanced.ctes_recursive_queries",
          "de_sql_advanced.indexing_b_tree_strategies",
          "de_sql_advanced.query_execution_plans",
          "de_sql_advanced.partitioning_sharding",
          "de_sql_advanced.transactions_acid_isolation",
          "de_sql_advanced.stored_procedures_udfs",
          "de_sql_advanced.db_performance_tuning"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive Advanced SQL query and database optimization assessment",
        "strength": 1.0,
        "maps_to": [
          "de_sql_advanced.complex_joins_subqueries",
          "de_sql_advanced.window_functions_analytical",
          "de_sql_advanced.ctes_recursive_queries",
          "de_sql_advanced.indexing_b_tree_strategies",
          "de_sql_advanced.query_execution_plans",
          "de_sql_advanced.partitioning_sharding",
          "de_sql_advanced.transactions_acid_isolation",
          "de_sql_advanced.stored_procedures_udfs",
          "de_sql_advanced.db_performance_tuning"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["complex_joins_subqueries", "window_functions_analytical", "ctes_recursive_queries"],
      "description": "Writes complex multi-table queries, analytical window functions, and recursive/modular CTEs."
    },
    "mid": {
      "expected_subskills": ["indexing_b_tree_strategies", "partitioning_sharding", "transactions_acid_isolation", "stored_procedures_udfs"],
      "description": "Designs indexing strategies, partitions large tables, manages transaction isolation levels, and writes stored procedures."
    },
    "senior": {
      "expected_subskills": ["query_execution_plans", "db_performance_tuning"],
      "description": "Interprets complex EXPLAIN ANALYZE cost trees, tunes database memory/buffers, and resolves execution bottlenecks across distributed databases."
    }
  }
}

# 3. de_data_warehousing
skills["de_data_warehousing"] = {
  "skill_id": "de_data_warehousing",
  "name": "Data Warehousing & Dimensional Modeling",
  "category": "architecture",
  "description": "Dimensional data modeling (Kimball & Inmon), Star and Snowflake schemas, Fact and Dimension design, Slowly Changing Dimensions (SCD), and Cloud Data Warehouses (Snowflake, BigQuery, Redshift).",
  "subskills": [
    {
      "id": "dimensional_star_snowflake",
      "name": "Dimensional Modeling & Star/Snowflake Schemas",
      "description": "Kimball methodology, Star schema vs Snowflake schema, normalized vs denormalized analytical modeling, and grain definition.",
      "keywords": ["Kimball", "star schema", "snowflake schema", "dimensional modeling", "grain", "denormalization", "conformed dimension"]
    },
    {
      "id": "fact_dimension_design",
      "name": "Fact & Dimension Table Architecture",
      "description": "Transaction, Periodic Snapshot, and Accumulating Snapshot fact tables, Degenerate, Junk, Role-Playing, and Conformed dimensions.",
      "keywords": ["fact table", "dimension table", "surrogate key", "degenerate dimension", "junk dimension", "role-playing dimension", "accumulating snapshot", "periodic snapshot"]
    },
    {
      "id": "scd_type_management",
      "name": "Slowly Changing Dimensions (SCD Types 0-6)",
      "description": "Designing and implementing SCD Type 1 (overwrite), Type 2 (historical versioning with valid_from/valid_to/is_current), Type 3 (previous column), and hybrid types.",
      "keywords": ["SCD Type 1", "SCD Type 2", "SCD Type 3", "valid_from", "valid_to", "is_current", "surrogate key", "historical tracking", "dimension evolution"]
    },
    {
      "id": "snowflake_architecture",
      "name": "Snowflake Cloud Warehouse Architecture",
      "description": "Multi-cluster shared data architecture, virtual warehouses, auto-suspend/resume, zero-copy cloning, time travel, fail-safe, and micro-partitions.",
      "keywords": ["Snowflake", "virtual warehouse", "micro-partitions", "zero-copy clone", "time travel", "fail-safe", "clustering keys", "Snowpipe", "Stages"]
    },
    {
      "id": "bigquery_architecture",
      "name": "Google BigQuery Serverless Warehouse",
      "description": "Dremel execution engine, Capacitor storage, slot allocation, partitioning by date/integer, clustering, BI Engine, and reservation management.",
      "keywords": ["BigQuery", "slots", "Dremel", "Capacitor", "partitioning", "clustering", "sharded tables", "BigQuery BI Engine", "dry-run"]
    },
    {
      "id": "redshift_architecture",
      "name": "AWS Redshift & Distributed Storage",
      "description": "Leader vs Compute nodes, distribution styles (KEY, ALL, EVEN, AUTO), sort keys (compound vs interleaved), vacuum, and Redshift Serverless.",
      "keywords": ["Redshift", "distribution key", "sort key", "DISTSTYLE", "SORTKEY", "Redshift Serverless", "RA3 instances", "Redshift Spectrum", "WLM"]
    },
    {
      "id": "columnar_storage_compression",
      "name": "Columnar Storage Formats & Compression Encoding",
      "description": "Columnar projection, dictionary encoding, run-length encoding (RLE), ZSTD, Snappy, and I/O minimization during aggregation.",
      "keywords": ["columnar storage", "compression encoding", "ZSTD", "Snappy", "dictionary encoding", "RLE", "block size", "I/O pruning"]
    },
    {
      "id": "semantic_layer_metrics",
      "name": "Semantic Layers & Metric Store Architecture",
      "description": "Building centralized semantic layers, consistent business metrics definition, Cube.js, dbt Semantic Layer, and BI integration.",
      "keywords": ["semantic layer", "metrics store", "dbt Semantic Layer", "Cube.js", "metric definition", "business glossary", "dimensions and measures"]
    },
    {
      "id": "warehouse_cost_optimization",
      "name": "Warehouse Cost Optimization & Workload Management",
      "description": "Monitoring compute consumption, query tagging, warehouse sizing, auto-scaling policies, query queuing, and FinOps for data warehouses.",
      "keywords": ["cost optimization", "warehouse sizing", "auto-scaling", "credit consumption", "query tagging", "FinOps", "concurrency scaling"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Designed enterprise star-schema data models and managed Snowflake/BigQuery warehouses",
        "strength": 0.5,
        "maps_to": ["de_data_warehousing.dimensional_star_snowflake", "de_data_warehousing.scd_type_management", "de_data_warehousing.snowflake_architecture"]
      }
    ],
    "linkedin": [
      {
        "signal": "Certified Data Warehouse Specialist or Snowflake SnowPro Core",
        "strength": 0.3,
        "maps_to": ["de_data_warehousing.snowflake_architecture", "de_data_warehousing.fact_dimension_design"]
      }
    ],
    "github": [
      {
        "pattern": "*.sql|models/**/*.sql|schemas/**/*.sql|snowflake/*.sql|bigquery/*.sql",
        "strength": 1.0,
        "maps_to": [
          "de_data_warehousing.dimensional_star_snowflake",
          "de_data_warehousing.fact_dimension_design",
          "de_data_warehousing.scd_type_management",
          "de_data_warehousing.snowflake_architecture",
          "de_data_warehousing.bigquery_architecture",
          "de_data_warehousing.redshift_architecture",
          "de_data_warehousing.columnar_storage_compression",
          "de_data_warehousing.semantic_layer_metrics",
          "de_data_warehousing.warehouse_cost_optimization"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Data Warehousing and Dimensional Modeling Architecture Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_data_warehousing.dimensional_star_snowflake",
          "de_data_warehousing.fact_dimension_design",
          "de_data_warehousing.scd_type_management",
          "de_data_warehousing.snowflake_architecture",
          "de_data_warehousing.bigquery_architecture",
          "de_data_warehousing.redshift_architecture",
          "de_data_warehousing.columnar_storage_compression",
          "de_data_warehousing.semantic_layer_metrics",
          "de_data_warehousing.warehouse_cost_optimization"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["dimensional_star_snowflake", "fact_dimension_design", "scd_type_management"],
      "description": "Models star/snowflake schemas, designs fact and dimension tables, and implements SCD Type 1 & 2 logic."
    },
    "mid": {
      "expected_subskills": ["snowflake_architecture", "bigquery_architecture", "columnar_storage_compression"],
      "description": "Configures and manages cloud data warehouses (Snowflake, BigQuery), tunes clustering, and optimizes columnar storage compression."
    },
    "senior": {
      "expected_subskills": ["redshift_architecture", "semantic_layer_metrics", "warehouse_cost_optimization"],
      "description": "Architects multi-warehouse enterprise topologies, establishes unified semantic metric layers, and governs warehouse compute costs."
    }
  }
}

# 4. de_data_lakes_storage
skills["de_data_lakes_storage"] = {
  "skill_id": "de_data_lakes_storage",
  "name": "Data Lakes & Open Table Formats",
  "category": "storage",
  "description": "Modern Data Lake and Lakehouse architecture, object storage (S3, GCS, ADLS), open table formats (Delta Lake, Apache Iceberg, Apache Hudi), ACID on data lakes, time travel, and file compaction.",
  "subskills": [
    {
      "id": "object_storage_s3_gcs_blob",
      "name": "Cloud Object Storage & IAM Access Patterns",
      "description": "AWS S3, Google Cloud Storage, Azure Data Lake Storage Gen2 (ADLS), storage tiers, lifecycle rules, bucket policies, and high-throughput prefixes.",
      "keywords": ["AWS S3", "GCS", "ADLS Gen2", "object storage", "multipart upload", "lifecycle policies", "storage classes", "S3 Select", "prefix partitioning"]
    },
    {
      "id": "parquet_orc_file_formats",
      "name": "Columnar File Formats (Parquet, ORC, Avro)",
      "description": "Parquet file anatomy (Header, Data Pages, Column Chunks, Footer/Metadata), dictionary pages, statistics (min/max), and Avro row-based schema.",
      "keywords": ["Parquet", "ORC", "Avro", "footer metadata", "row group", "column chunk", "dictionary page", "min/max statistics", "predicate pushdown"]
    },
    {
      "id": "delta_lake_acid",
      "name": "Delta Lake & Transaction Logs",
      "description": "Delta Lake ACID transactions, _delta_log JSON transaction log, checkpoint parquet files, optimistic concurrency control, and merge operations.",
      "keywords": ["Delta Lake", "_delta_log", "ACID", "optimistic concurrency", "MERGE INTO", "Delta checkpoint", "vacuum", "optimize", "Databricks Delta"]
    },
    {
      "id": "apache_iceberg_architecture",
      "name": "Apache Iceberg Open Table Format",
      "description": "Iceberg architecture: Iceberg Catalog, Metadata File (JSON), Manifest List (Avro), Manifest Files (Avro), data files, snapshot isolation, and hidden partitioning.",
      "keywords": ["Apache Iceberg", "Iceberg Catalog", "Manifest List", "Manifest File", "snapshot isolation", "hidden partitioning", "schema evolution", "Nessie", "REST Catalog"]
    },
    {
      "id": "apache_hudi_upserts",
      "name": "Apache Hudi & Upsert Architecture",
      "description": "Hudi Copy-on-Write (CoW) vs Merge-on-Read (MoR), timeline metadata, key-based record indexing, file sizing, and incremental data consumption.",
      "keywords": ["Apache Hudi", "Copy-on-Write", "Merge-on-Read", "Hudi timeline", "upsert", "HoodieKey", "file groups", "incremental query"]
    },
    {
      "id": "partitioning_z_ordering",
      "name": "Data Skipping, Partitioning & Z-Ordering",
      "description": "Multi-dimensional clustering with Z-Order Curves, Hilbert curves, partition pruning, min/max file skipping, and avoiding over-partitioning.",
      "keywords": ["Z-Order", "Z-Ordering", "data skipping", "clustering", "partition pruning", "over-partitioning", "Hilbert curve", "bloom filters"]
    },
    {
      "id": "small_files_compaction",
      "name": "Small File Problem & Automated Compaction",
      "description": "Mitigating the small files problem in streaming/batch ingest, bin-packing, OPTIMIZE compaction jobs, and maintenance procedures.",
      "keywords": ["small file problem", "compaction", "bin-packing", "OPTIMIZE", "VACUUM", "file rewrite", "maintenance job", "target file size"]
    },
    {
      "id": "lakehouse_medallion_architecture",
      "name": "Medallion Architecture (Bronze / Silver / Gold)",
      "description": "Designing Bronze (raw, append-only), Silver (cleaned, deduplicated, enriched), and Gold (aggregated, business-level dimensional) lakehouse layers.",
      "keywords": ["Medallion architecture", "Bronze layer", "Silver layer", "Gold layer", "raw data", "conformed layer", "curated data", "Lakehouse"]
    },
    {
      "id": "time_travel_schema_evolution",
      "name": "Time Travel, Rollback & Schema Evolution",
      "description": "Querying historical snapshots (TIMESTAMP AS OF / VERSION AS OF), rollbacks, additive vs breaking schema changes, and column renaming.",
      "keywords": ["time travel", "VERSION AS OF", "TIMESTAMP AS OF", "schema evolution", "schema enforcement", "rollback", "audit history", "add column"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Built enterprise Lakehouse using Delta Lake and Apache Iceberg with Medallion architecture",
        "strength": 0.5,
        "maps_to": ["de_data_lakes_storage.delta_lake_acid", "de_data_lakes_storage.lakehouse_medallion_architecture", "de_data_lakes_storage.apache_iceberg_architecture"]
      }
    ],
    "linkedin": [
      {
        "signal": "Hands-on experience with Delta Lake, Apache Iceberg, and AWS S3 storage",
        "strength": 0.3,
        "maps_to": ["de_data_lakes_storage.parquet_orc_file_formats", "de_data_lakes_storage.object_storage_s3_gcs_blob"]
      }
    ],
    "github": [
      {
        "pattern": "*iceberg*|*delta*|*.parquet|lakehouse/**/*.py|storage/**/*.tf",
        "strength": 1.0,
        "maps_to": [
          "de_data_lakes_storage.object_storage_s3_gcs_blob",
          "de_data_lakes_storage.parquet_orc_file_formats",
          "de_data_lakes_storage.delta_lake_acid",
          "de_data_lakes_storage.apache_iceberg_architecture",
          "de_data_lakes_storage.apache_hudi_upserts",
          "de_data_lakes_storage.partitioning_z_ordering",
          "de_data_lakes_storage.small_files_compaction",
          "de_data_lakes_storage.lakehouse_medallion_architecture",
          "de_data_lakes_storage.time_travel_schema_evolution"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Data Lakes & Open Table Formats Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_data_lakes_storage.object_storage_s3_gcs_blob",
          "de_data_lakes_storage.parquet_orc_file_formats",
          "de_data_lakes_storage.delta_lake_acid",
          "de_data_lakes_storage.apache_iceberg_architecture",
          "de_data_lakes_storage.apache_hudi_upserts",
          "de_data_lakes_storage.partitioning_z_ordering",
          "de_data_lakes_storage.small_files_compaction",
          "de_data_lakes_storage.lakehouse_medallion_architecture",
          "de_data_lakes_storage.time_travel_schema_evolution"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["object_storage_s3_gcs_blob", "parquet_orc_file_formats", "lakehouse_medallion_architecture"],
      "description": "Interacts with cloud object storage, writes optimized Parquet datasets, and organizes data along Medallion (Bronze/Silver/Gold) stages."
    },
    "mid": {
      "expected_subskills": ["delta_lake_acid", "apache_iceberg_architecture", "partitioning_z_ordering", "time_travel_schema_evolution"],
      "description": "Implements ACID table formats (Delta/Iceberg), manages snapshot isolation, time travel queries, and configures Z-ordering."
    },
    "senior": {
      "expected_subskills": ["apache_hudi_upserts", "small_files_compaction"],
      "description": "Architects high-throughput lakehouse upserts with Hudi/Iceberg, designs automated compaction strategies, and governs lakehouse metadata integrity."
    }
  }
}

# 5. de_distributed_computing
skills["de_distributed_computing"] = {
  "skill_id": "de_distributed_computing",
  "name": "Distributed Computing & Apache Spark",
  "category": "processing",
  "description": "Large-scale distributed data processing using Apache Spark (PySpark & Scala), Catalyst optimizer, Tungsten execution engine, partitioning, shuffling, caching, and memory tuning.",
  "subskills": [
    {
      "id": "spark_architecture_cluster_managers",
      "name": "Spark Cluster Architecture & Resource Managers",
      "description": "Driver, Executor, Master/Worker nodes, Task, Stage, Job breakdown, and cluster managers (Kubernetes, YARN, Standalone).",
      "keywords": ["Spark Driver", "Spark Executor", "Spark Stage", "DAGScheduler", "TaskScheduler", "YARN", "Kubernetes Spark", "spark-submit", "cluster mode", "client mode"]
    },
    {
      "id": "rdd_vs_dataframe_dataset",
      "name": "RDDs vs DataFrames vs Datasets APIs",
      "description": "Understanding Low-level RDD transformations/actions vs high-level DataFrame and typed Dataset APIs, immutability, and lazy evaluation.",
      "keywords": ["RDD", "DataFrame", "Dataset", "lazy evaluation", "transformations", "actions", "map", "flatMap", "filter", "collect", "count"]
    },
    {
      "id": "spark_sql_catalyst_optimizer",
      "name": "Spark SQL & Catalyst Optimizer",
      "description": "Analysis, Logical Optimization, Physical Planning, Code Generation (Tungsten), Whole-Stage CodeGen, and cost-based optimization (CBO).",
      "keywords": ["Catalyst Optimizer", "Tungsten", "Logical Plan", "Physical Plan", "Whole-Stage CodeGen", "CBO", "Adaptive Query Execution", "AQE", "predicate pushdown"]
    },
    {
      "id": "partitioning_bucketing_coalesce",
      "name": "Partition Management: Coalesce, Repartition & Bucketing",
      "description": "Controlling parallelism with repartition vs coalesce, partition sizes, bucketing on high-cardinality keys, and avoiding narrow/wide shuffle hazards.",
      "keywords": ["repartition", "coalesce", "bucketing", "spark.sql.shuffle.partitions", "partition size", "hash partitioning", "range partitioning", "bucketBy"]
    },
    {
      "id": "shuffling_skew_repartition",
      "name": "Shuffle Operations & Data Skew Mitigation",
      "description": "Understanding Shuffle Read/Write, Wide transformations, salting skewed keys, Adaptive Query Execution skew join handling, and isolate bad keys.",
      "keywords": ["shuffle", "data skew", "salting", "AQE skew join", "shuffle partitions", "SortMergeJoin", "ShuffleHashJoin", "spill to disk"]
    },
    {
      "id": "broadcast_joins_accumulators",
      "name": "Broadcast Joins, Broadcast Variables & Accumulators",
      "description": "BroadcastHashJoin optimization (spark.sql.autoBroadcastJoinThreshold), distributing read-only lookups, and distributed accumulators.",
      "keywords": ["BroadcastHashJoin", "broadcast()", "autoBroadcastJoinThreshold", "Broadcast Variable", "Accumulator", "BHJ", "lookup table"]
    },
    {
      "id": "spark_caching_persistence",
      "name": "Caching, Checkpointing & Storage Levels",
      "description": "cache() vs persist(), StorageLevel (MEMORY_ONLY, MEMORY_AND_DISK, SER), unpersisting, and breaking lineage with local/reliable checkpointing.",
      "keywords": ["cache", "persist", "StorageLevel", "MEMORY_AND_DISK", "unpersist", "checkpoint", "lineage truncation", "recomputation"]
    },
    {
      "id": "spark_memory_tuning_oom",
      "name": "Spark Memory Tuning & OOM Troubleshooting",
      "description": "Executor memory breakdown (Storage vs Execution memory, Reserved memory, User memory), Off-Heap memory, JVM garbage collection (G1GC), and diagnosing OutOfMemory (OOM) errors.",
      "keywords": ["spark.executor.memory", "spark.memory.fraction", "spark.memory.storageFraction", "spark.executor.memoryOverhead", "OOM", "GC pause", "G1GC", "off-heap"]
    },
    {
      "id": "spark_structured_streaming",
      "name": "Spark Structured Streaming Engine",
      "description": "Micro-batch processing, Continuous processing, streaming DataFrames, trigger policies, watermarking, stateful streaming, and streaming sinks.",
      "keywords": ["Structured Streaming", "micro-batch", "watermark", "Trigger.AvailableNow", "outputMode", "stateStore", "checkpointLocation", "streaming join"]
    },
    {
      "id": "pyspark_udfs_vectorization",
      "name": "PySpark Vectorized UDFs & PyArrow / Pandas API",
      "description": "Python UDF overhead, PySpark Pandas UDFs (@pandas_udf) with Apache Arrow serialization, and pyspark.pandas (formerly Koalas).",
      "keywords": ["pandas_udf", "PyArrow", "vectorized UDF", "Apache Arrow", "Python UDF", "pyspark.pandas", "SeriesToSeries", "Iterator"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Engineered terabyte-scale distributed data pipelines using PySpark on Kubernetes",
        "strength": 0.5,
        "maps_to": ["de_distributed_computing.spark_architecture_cluster_managers", "de_distributed_computing.spark_sql_catalyst_optimizer", "de_distributed_computing.shuffling_skew_repartition"]
      }
    ],
    "linkedin": [
      {
        "signal": "Apache Spark certified developer or Databricks Data Engineer Associate/Professional",
        "strength": 0.3,
        "maps_to": ["de_distributed_computing.rdd_vs_dataframe_dataset", "de_distributed_computing.broadcast_joins_accumulators"]
      }
    ],
    "github": [
      {
        "pattern": "*spark*.py|*pyspark*|spark-submit*.sh|jobs/**/*.scala|jobs/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "de_distributed_computing.spark_architecture_cluster_managers",
          "de_distributed_computing.rdd_vs_dataframe_dataset",
          "de_distributed_computing.spark_sql_catalyst_optimizer",
          "de_distributed_computing.partitioning_bucketing_coalesce",
          "de_distributed_computing.shuffling_skew_repartition",
          "de_distributed_computing.broadcast_joins_accumulators",
          "de_distributed_computing.spark_caching_persistence",
          "de_distributed_computing.spark_memory_tuning_oom",
          "de_distributed_computing.spark_structured_streaming",
          "de_distributed_computing.pyspark_udfs_vectorization"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Apache Spark Distributed Computing & Performance Optimization Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_distributed_computing.spark_architecture_cluster_managers",
          "de_distributed_computing.rdd_vs_dataframe_dataset",
          "de_distributed_computing.spark_sql_catalyst_optimizer",
          "de_distributed_computing.partitioning_bucketing_coalesce",
          "de_distributed_computing.shuffling_skew_repartition",
          "de_distributed_computing.broadcast_joins_accumulators",
          "de_distributed_computing.spark_caching_persistence",
          "de_distributed_computing.spark_memory_tuning_oom",
          "de_distributed_computing.spark_structured_streaming",
          "de_distributed_computing.pyspark_udfs_vectorization"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["rdd_vs_dataframe_dataset", "spark_sql_catalyst_optimizer", "spark_architecture_cluster_managers"],
      "description": "Writes PySpark/Spark SQL queries, operates with DataFrames, and understands cluster master/worker anatomy."
    },
    "mid": {
      "expected_subskills": ["partitioning_bucketing_coalesce", "broadcast_joins_accumulators", "spark_caching_persistence", "pyspark_udfs_vectorization"],
      "description": "Optimizes joins with broadcasting, writes vectorized Arrow/Pandas UDFs, manages persistence storage levels, and tunes partition counts."
    },
    "senior": {
      "expected_subskills": ["shuffling_skew_repartition", "spark_memory_tuning_oom", "spark_structured_streaming"],
      "description": "Eliminates heavy shuffle data skews with salting/AQE, diagnoses executor OOM memory dumps, and designs stateful Structured Streaming pipelines."
    }
  }
}

# 6. de_data_pipelines_orchestration
skills["de_data_pipelines_orchestration"] = {
  "skill_id": "de_data_pipelines_orchestration",
  "name": "Data Pipeline Orchestration & Workflow Engines",
  "category": "orchestration",
  "description": "Workflow scheduling and orchestration with Apache Airflow, Prefect, Dagster, DAG authoring best practices, backfilling, idempotency, failure alerting, and distributed task execution.",
  "subskills": [
    {
      "id": "airflow_dag_design_best_practices",
      "name": "Airflow DAG Architecture & Design Best Practices",
      "description": "DAG authoring, avoid top-level code execution in DAG files, dynamic DAG generation, schedule intervals, cron vs timetable expressions.",
      "keywords": ["Airflow DAG", "DAG parsing", "top-level code", "schedule_interval", "cron", "timetable", "dynamic DAG", "start_date", "catchup"]
    },
    {
      "id": "airflow_operators_hooks_sensors",
      "name": "Airflow Operators, Hooks & Custom Sensors",
      "description": "Standard operators (Bash, Python, SQLExecute), cloud operators (S3, GCS, BigQuery, Snowflake), Hooks, and Poke vs Reschedule Sensors.",
      "keywords": ["PythonOperator", "BashOperator", "BaseHook", "Sensor", "mode=reschedule", "poke", "S3KeySensor", "ExternalTaskSensor", "custom operator"]
    },
    {
      "id": "airflow_taskflow_api_xcoms",
      "name": "Airflow 2.x TaskFlow API & XCom Backend",
      "description": "Decorators (@dag, @task, @task.branch), TaskFlow API data passing, XCom limits, and configuring custom S3/GCS XCom backends.",
      "keywords": ["TaskFlow API", "@task", "@dag", "XCom", "custom XCom backend", "task dependencies", "bitshift operators >>", "branching"]
    },
    {
      "id": "airflow_backfilling_catchup",
      "name": "Airflow Backfilling, Catchup & Reprocessing",
      "description": "Historical backfilling via CLI, execution_date / logical_date vs data_interval_start/end, managing catchup=False safely, and rerun policies.",
      "keywords": ["airflow dags backfill", "logical_date", "execution_date", "data_interval_start", "catchup", "reprocessing", "clear task instances"]
    },
    {
      "id": "prefect_orchestration",
      "name": "Prefect Modern Flow Orchestration",
      "description": "Prefect 2/3 architecture, flows, tasks, deployments, work pools, parameterization, and hybrid execution model.",
      "keywords": ["Prefect", "@flow", "@task", "prefect deployment", "work pool", "prefect worker", "subflow", "Prefect Cloud"]
    },
    {
      "id": "dagster_software_defined_assets",
      "name": "Dagster & Software-Defined Assets (SDA)",
      "description": "Dagster asset-oriented orchestration, @asset decorator, asset partitions, auto-materialize policies, IOManagers, and resource bindings.",
      "keywords": ["Dagster", "Software-Defined Assets", "@asset", "IOManager", "asset lineage", "auto-materialize", "Dagster partitions", "Resources"]
    },
    {
      "id": "idempotency_data_reprocessing",
      "name": "Idempotent Pipeline Design & Atomic Swaps",
      "description": "Ensuring deterministic pipeline re-runs, atomic partition replacement, temporary stage write and rename, and avoiding duplicate records.",
      "keywords": ["idempotency", "atomic write", "atomic partition swap", "stage table", "deduplication", "deterministic", "retry safety"]
    },
    {
      "id": "pipeline_sla_alerting",
      "name": "Pipeline SLA Monitoring, Callbacks & Alerting",
      "description": "SLA missed callbacks, on_failure_callback, on_retry_callback, Slack/PagerDuty webhook alerting, and pipeline runtime tracking.",
      "keywords": ["SLA", "sla_miss_callback", "on_failure_callback", "PagerDuty", "Slack webhook", "alerting", "heartbeat", "pipeline monitoring"]
    },
    {
      "id": "distributed_executors_celery_k8s",
      "name": "Airflow Distributed Executors (Celery, Kubernetes)",
      "description": "Configuring CeleryExecutor with Redis/RabbitMQ, KubernetesExecutor (pod-per-task), CeleryKubernetesExecutor, worker autoscaling, and concurrency limits.",
      "keywords": ["KubernetesExecutor", "CeleryExecutor", "CeleryKubernetesExecutor", "Redis", "Airflow worker", "concurrency limits", "max_active_tasks", "pod resource requests"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Architected mission-critical data pipelines in Apache Airflow with KubernetesExecutor",
        "strength": 0.5,
        "maps_to": ["de_data_pipelines_orchestration.airflow_dag_design_best_practices", "de_data_pipelines_orchestration.distributed_executors_celery_k8s", "de_data_pipelines_orchestration.idempotency_data_reprocessing"]
      }
    ],
    "linkedin": [
      {
        "signal": "Expert in Apache Airflow, Prefect, and Workflow Orchestration",
        "strength": 0.3,
        "maps_to": ["de_data_pipelines_orchestration.airflow_operators_hooks_sensors", "de_data_pipelines_orchestration.airflow_taskflow_api_xcoms"]
      }
    ],
    "github": [
      {
        "pattern": "dags/**/*.py|airflow/*.py|prefect*.py|dagster*.py",
        "strength": 1.0,
        "maps_to": [
          "de_data_pipelines_orchestration.airflow_dag_design_best_practices",
          "de_data_pipelines_orchestration.airflow_operators_hooks_sensors",
          "de_data_pipelines_orchestration.airflow_taskflow_api_xcoms",
          "de_data_pipelines_orchestration.airflow_backfilling_catchup",
          "de_data_pipelines_orchestration.prefect_orchestration",
          "de_data_pipelines_orchestration.dagster_software_defined_assets",
          "de_data_pipelines_orchestration.idempotency_data_reprocessing",
          "de_data_pipelines_orchestration.pipeline_sla_alerting",
          "de_data_pipelines_orchestration.distributed_executors_celery_k8s"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Workflow Orchestration & Data Pipeline Architecture Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_data_pipelines_orchestration.airflow_dag_design_best_practices",
          "de_data_pipelines_orchestration.airflow_operators_hooks_sensors",
          "de_data_pipelines_orchestration.airflow_taskflow_api_xcoms",
          "de_data_pipelines_orchestration.airflow_backfilling_catchup",
          "de_data_pipelines_orchestration.prefect_orchestration",
          "de_data_pipelines_orchestration.dagster_software_defined_assets",
          "de_data_pipelines_orchestration.idempotency_data_reprocessing",
          "de_data_pipelines_orchestration.pipeline_sla_alerting",
          "de_data_pipelines_orchestration.distributed_executors_celery_k8s"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["airflow_dag_design_best_practices", "airflow_operators_hooks_sensors", "airflow_taskflow_api_xcoms"],
      "description": "Authors basic Airflow DAGs using TaskFlow API, configures standard hooks/operators, and passes state cleanly via XCom."
    },
    "mid": {
      "expected_subskills": ["airflow_backfilling_catchup", "idempotency_data_reprocessing", "pipeline_sla_alerting", "prefect_orchestration"],
      "description": "Implements idempotent pipelines, executes safe backfills without data duplication, configures SLA alerting, and develops with Prefect."
    },
    "senior": {
      "expected_subskills": ["dagster_software_defined_assets", "distributed_executors_celery_k8s"],
      "description": "Architects modern asset-based data platforms in Dagster, scales Kubernetes/Celery executors under heavy workload, and establishes enterprise orchestration governance."
    }
  }
}

# 7. de_streaming_realtime
skills["de_streaming_realtime"] = {
  "skill_id": "de_streaming_realtime",
  "name": "Real-Time Streaming & Event Processing",
  "category": "streaming",
  "description": "Real-time event stream processing using Apache Kafka, Apache Flink, Kafka Streams, Schema Registry, event time watermarks, stream windowing, and exactly-once semantics.",
  "subskills": [
    {
      "id": "kafka_architecture_topics_partitions",
      "name": "Kafka Cluster Architecture, Topics & Partitions",
      "description": "Brokers, Controller / KRaft mode (KRaft vs ZooKeeper), topic partition distribution, replication factor, ISR (In-Sync Replicas), and leader election.",
      "keywords": ["Apache Kafka", "broker", "KRaft", "ZooKeeper", "topic", "partition", "replication factor", "ISR", "in-sync replicas", "leader election"]
    },
    {
      "id": "producer_consumer_consumer_groups",
      "name": "Producers, Consumers & Consumer Group Rebalancing",
      "description": "Producer acks (0, 1, all), batch size, linger.ms, consumer groups, partition assignment strategies (Range, RoundRobin, CooperativeSticky), and commit offsets.",
      "keywords": ["KafkaProducer", "KafkaConsumer", "consumer group", "rebalance", "CooperativeSticky", "acks=all", "linger.ms", "enable.auto.commit", "commitSync"]
    },
    {
      "id": "kafka_schema_registry_avro_protobuf",
      "name": "Confluent Schema Registry & Schema Evolution",
      "description": "Schema Registry integration, Avro / Protobuf serialization, schema compatibility modes (BACKWARD, FORWARD, FULL), and preventing schema drift.",
      "keywords": ["Schema Registry", "Confluent", "Avro schema", "Protobuf", "schema compatibility", "BACKWARD compatibility", "FULL compatibility", "schema drift"]
    },
    {
      "id": "kafka_streams_ksqldb",
      "name": "Kafka Streams & ksqlDB Stream Processing",
      "description": "KStream, KTable, GlobalKTable, stateless vs stateful operations, RocksDB state stores, and real-time SQL stream analysis with ksqlDB.",
      "keywords": ["Kafka Streams", "KStream", "KTable", "GlobalKTable", "RocksDB", "ksqlDB", "CREATE STREAM", "CREATE TABLE", "topology"]
    },
    {
      "id": "apache_flink_stream_processing",
      "name": "Apache Flink Architecture & Stateful Stream Processing",
      "description": "JobManager, TaskManager, slots, DataStream API, stateful transformations (ValueState, ListState, MapState), and Flink SQL.",
      "keywords": ["Apache Flink", "JobManager", "TaskManager", "DataStream API", "Flink SQL", "ValueState", "keyed stream", "operator state"]
    },
    {
      "id": "event_time_watermarks_late_data",
      "name": "Event Time, Processing Time & Watermarks",
      "description": "Event Time vs Processing Time vs Ingestion Time, watermark generation strategies (bounded-out-of-orderness, punctuated), and handling late-arriving records with side outputs.",
      "keywords": ["event time", "processing time", "watermark", "bounded out-of-orderness", "late data", "side output", "allowed lateness"]
    },
    {
      "id": "windowing_tumbling_sliding_session",
      "name": "Stream Windowing (Tumbling, Sliding, Session)",
      "description": "Tumbling windows (fixed, non-overlapping), Sliding/Hopping windows (overlapping), Session windows (gap-based), and custom window triggers/evictors.",
      "keywords": ["tumbling window", "sliding window", "session window", "window trigger", "window evictor", "gap duration", "time window"]
    },
    {
      "id": "exactly_once_semantics_transactions",
      "name": "Exactly-Once Semantics (EOS) & Two-Phase Commit",
      "description": "At-least-once vs At-most-once vs Exactly-Once (EOS), transactional producers, Two-Phase Commit (2PC) sinks in Flink/Kafka, and idempotent writes.",
      "keywords": ["Exactly-Once", "EOS", "Two-Phase Commit", "2PC", "transactional producer", "isolation.level=read_committed", "idempotent producer", "at-least-once"]
    },
    {
      "id": "stream_state_backends_checkpointing",
      "name": "State Backends, Checkpointing & Savepoints",
      "description": "Flink state backends (HashMapStateBackend, EmbeddedRocksDBStateBackend), Chandy-Lamport distributed checkpointing, unaligned checkpoints, and manual savepoints.",
      "keywords": ["checkpointing", "savepoint", "RocksDB state backend", "Chandy-Lamport", "unaligned checkpoint", "state recovery", "checkpoint interval"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Engineered real-time streaming pipelines using Kafka, Schema Registry, and Apache Flink",
        "strength": 0.5,
        "maps_to": ["de_streaming_realtime.kafka_architecture_topics_partitions", "de_streaming_realtime.apache_flink_stream_processing", "de_streaming_realtime.exactly_once_semantics_transactions"]
      }
    ],
    "linkedin": [
      {
        "signal": "Confluent Certified Developer for Apache Kafka (CCDAK)",
        "strength": 0.3,
        "maps_to": ["de_streaming_realtime.producer_consumer_consumer_groups", "de_streaming_realtime.kafka_schema_registry_avro_protobuf"]
      }
    ],
    "github": [
      {
        "pattern": "*kafka*.py|*producer*.py|*consumer*.py|*flink*.py|*flink*.scala",
        "strength": 1.0,
        "maps_to": [
          "de_streaming_realtime.kafka_architecture_topics_partitions",
          "de_streaming_realtime.producer_consumer_consumer_groups",
          "de_streaming_realtime.kafka_schema_registry_avro_protobuf",
          "de_streaming_realtime.kafka_streams_ksqldb",
          "de_streaming_realtime.apache_flink_stream_processing",
          "de_streaming_realtime.event_time_watermarks_late_data",
          "de_streaming_realtime.windowing_tumbling_sliding_session",
          "de_streaming_realtime.exactly_once_semantics_transactions",
          "de_streaming_realtime.stream_state_backends_checkpointing"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Real-Time Event Streaming & Stream Processing Architecture Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_streaming_realtime.kafka_architecture_topics_partitions",
          "de_streaming_realtime.producer_consumer_consumer_groups",
          "de_streaming_realtime.kafka_schema_registry_avro_protobuf",
          "de_streaming_realtime.kafka_streams_ksqldb",
          "de_streaming_realtime.apache_flink_stream_processing",
          "de_streaming_realtime.event_time_watermarks_late_data",
          "de_streaming_realtime.windowing_tumbling_sliding_session",
          "de_streaming_realtime.exactly_once_semantics_transactions",
          "de_streaming_realtime.stream_state_backends_checkpointing"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["kafka_architecture_topics_partitions", "producer_consumer_consumer_groups", "kafka_schema_registry_avro_protobuf"],
      "description": "Produces and consumes messages from Kafka topics, avoids basic consumer lag, and enforces schema registry Avro schemas."
    },
    "mid": {
      "expected_subskills": ["kafka_streams_ksqldb", "event_time_watermarks_late_data", "windowing_tumbling_sliding_session"],
      "description": "Develops stream applications with Kafka Streams / ksqlDB, defines watermarks for out-of-order records, and implements tumbling/sliding time windows."
    },
    "senior": {
      "expected_subskills": ["apache_flink_stream_processing", "exactly_once_semantics_transactions", "stream_state_backends_checkpointing"],
      "description": "Architects end-to-end Exactly-Once stateful stream pipelines using Apache Flink, tunes RocksDB state backends, and designs zero-downtime savepoint upgrades."
    }
  }
}

# 8. de_data_modeling_transformation
skills["de_data_modeling_transformation"] = {
  "skill_id": "de_data_modeling_transformation",
  "name": "Data Transformation & dbt (Data Build Tool)",
  "category": "transformation",
  "description": "Modular SQL transformations, dbt (Data Build Tool), Jinja templating, incremental materializations, automated testing, dbt snapshots, data lineage, and semantic layers.",
  "subskills": [
    {
      "id": "dbt_models_ref_source",
      "name": "dbt Project Structure, ref() & source() Functions",
      "description": "dbt project layout (models, staging, marts, intermediate), source freshness tests, and building dynamic DAGs with ref() and source() macros.",
      "keywords": ["dbt", "dbt_project.yml", "ref()", "source()", "staging models", "marts", "intermediate models", "source freshness"]
    },
    {
      "id": "dbt_jinja_macros_packages",
      "name": "Jinja Templating, Custom Macros & dbt Packages",
      "description": "Jinja control structures (for loops, if conditions), creating reusable SQL macros, using dbt-utils, dbt-expectations packages.",
      "keywords": ["Jinja", "dbt macro", "{% macro %}", "dbt-utils", "dbt-expectations", "hub.getdbt.com", "reusable SQL", "dynamic SQL"]
    },
    {
      "id": "dbt_materializations_incremental",
      "name": "dbt Materializations & Incremental Strategies",
      "description": "View, Table, Ephemeral, and Incremental materializations, is_incremental() macro, merge vs delete+insert vs append incremental strategies, and unique_key design.",
      "keywords": ["materialization", "incremental", "is_incremental()", "merge strategy", "delete+insert", "unique_key", "ephemeral", "table materialization"]
    },
    {
      "id": "dbt_testing_generic_singular",
      "name": "dbt Testing (Generic, Singular & Custom Tests)",
      "description": "Built-in generic tests (unique, not_null, accepted_values, relationships), writing singular SQL tests, store_failures, and test severity levels.",
      "keywords": ["dbt test", "unique", "not_null", "accepted_values", "relationships", "singular test", "generic test", "store_failures", "warn vs error"]
    },
    {
      "id": "dbt_snapshots_scd",
      "name": "dbt Snapshots & Automated SCD Type 2",
      "description": "Automating Slowly Changing Dimension Type 2 tables with dbt snapshot, timestamp vs check strategies, target_schema, and dbt_valid_from/to.",
      "keywords": ["dbt snapshot", "SCD Type 2", "strategy='timestamp'", "strategy='check'", "updated_at", "check_cols", "dbt_valid_from", "dbt_valid_to"]
    },
    {
      "id": "dbt_documentation_lineage",
      "name": "dbt Documentation, Column Descriptions & Lineage Graph",
      "description": "Documenting models with schema.yml doc blocks, generating dbt docs, inspecting interactive lineage DAGs, and model selection syntax.",
      "keywords": ["dbt docs generate", "schema.yml", "doc blocks", "lineage graph", "model selection", "+model_name+", "tag:nightly", "catalog.json"]
    },
    {
      "id": "sqlmesh_alternative_engines",
      "name": "SQLMesh & Next-Gen Transformation Engines",
      "description": "Virtual data environments, column-level lineage, SQLMesh plan & apply, automated plan evaluations, and comparison with dbt-core.",
      "keywords": ["SQLMesh", "virtual data environments", "sqlmesh plan", "column-level lineage", "Tobiko", "dbt alternative", "environment promotion"]
    },
    {
      "id": "modular_data_transformation_pipelines",
      "name": "Modular ELT Pipeline Design & Layering",
      "description": "Decoupled transformation design: Ingestion -> Raw Staging -> Base Layer -> Core Business Entities -> Aggregated Data Marts.",
      "keywords": ["ELT", "modular design", "staging layer", "marts layer", "business logic decoupling", "dry code", "clean analytical architecture"]
    },
    {
      "id": "dbt_semantic_layer_metrics",
      "name": "dbt Semantic Layer & MetricFlow Integration",
      "description": "Defining semantic models, dimensions, entities, measures, cumulative metrics, derived metrics in MetricFlow, and downstream querying.",
      "keywords": ["dbt Semantic Layer", "MetricFlow", "semantic_models", "measures", "dimensions", "cumulative metrics", "derived metrics", "dbt sl query"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Led migration of legacy SQL stored procedures to modular dbt Core pipelines with automated testing",
        "strength": 0.5,
        "maps_to": ["de_data_modeling_transformation.dbt_models_ref_source", "de_data_modeling_transformation.dbt_materializations_incremental", "de_data_modeling_transformation.dbt_testing_generic_singular"]
      }
    ],
    "linkedin": [
      {
        "signal": "dbt Certified Developer certification",
        "strength": 0.3,
        "maps_to": ["de_data_modeling_transformation.dbt_jinja_macros_packages", "de_data_modeling_transformation.dbt_snapshots_scd"]
      }
    ],
    "github": [
      {
        "pattern": "dbt_project.yml|models/**/*.sql|macros/**/*.sql|snapshots/**/*.sql|schema.yml",
        "strength": 1.0,
        "maps_to": [
          "de_data_modeling_transformation.dbt_models_ref_source",
          "de_data_modeling_transformation.dbt_jinja_macros_packages",
          "de_data_modeling_transformation.dbt_materializations_incremental",
          "de_data_modeling_transformation.dbt_testing_generic_singular",
          "de_data_modeling_transformation.dbt_snapshots_scd",
          "de_data_modeling_transformation.dbt_documentation_lineage",
          "de_data_modeling_transformation.sqlmesh_alternative_engines",
          "de_data_modeling_transformation.modular_data_transformation_pipelines",
          "de_data_modeling_transformation.dbt_semantic_layer_metrics"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes dbt Transformation & Modular Data Modeling Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_data_modeling_transformation.dbt_models_ref_source",
          "de_data_modeling_transformation.dbt_jinja_macros_packages",
          "de_data_modeling_transformation.dbt_materializations_incremental",
          "de_data_modeling_transformation.dbt_testing_generic_singular",
          "de_data_modeling_transformation.dbt_snapshots_scd",
          "de_data_modeling_transformation.dbt_documentation_lineage",
          "de_data_modeling_transformation.sqlmesh_alternative_engines",
          "de_data_modeling_transformation.modular_data_transformation_pipelines",
          "de_data_modeling_transformation.dbt_semantic_layer_metrics"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["dbt_models_ref_source", "dbt_testing_generic_singular", "dbt_documentation_lineage"],
      "description": "Structures dbt projects, writes clean ref/source models, implements standard tests (unique, not_null), and generates documentation."
    },
    "mid": {
      "expected_subskills": ["dbt_jinja_macros_packages", "dbt_materializations_incremental", "dbt_snapshots_scd", "modular_data_transformation_pipelines"],
      "description": "Develops complex Jinja macros, builds high-performance incremental models, automates SCD Type 2 snapshots, and designs decoupled marts."
    },
    "senior": {
      "expected_subskills": ["sqlmesh_alternative_engines", "dbt_semantic_layer_metrics"],
      "description": "Evaluates and implements next-gen virtual data engines (SQLMesh), architects enterprise semantic metric layers, and establishes company-wide transformation standards."
    }
  }
}

# 9. de_data_quality_governance
skills["de_data_quality_governance"] = {
  "skill_id": "de_data_quality_governance",
  "name": "Data Quality, Governance & Observability",
  "category": "governance",
  "description": "Automated data quality validation (Great Expectations, Soda), anomaly detection, end-to-end data lineage (OpenLineage), metadata catalogs (DataHub, Amundsen), Data Observability, data contracts, and GDPR/PII masking.",
  "subskills": [
    {
      "id": "data_validation_great_expectations_soda",
      "name": "Data Quality Validation (Great Expectations & Soda)",
      "description": "Expectation Suites in Great Expectations (GX), Checkpoints, Data Docs, Soda Core / SodaCL checks, and pipeline assertion gates.",
      "keywords": ["Great Expectations", "GX", "Expectation Suite", "Checkpoint", "Data Docs", "SodaCL", "Soda Core", "automated data validation", "data quality gates"]
    },
    {
      "id": "data_profiling_anomaly_detection",
      "name": "Data Profiling & Volume/Schema Anomaly Detection",
      "description": "Automated statistical profiling (ydata-profiling), missingness rates, distribution drift, volume drop detection, and fresh data checks.",
      "keywords": ["data profiling", "anomaly detection", "volume anomaly", "freshness check", "distribution drift", "ydata-profiling", "z-score anomaly", "IQR"]
    },
    {
      "id": "data_lineage_metadata_openlineage",
      "name": "Data Lineage & OpenLineage Standard",
      "description": "Dataset and job-level lineage collection, OpenLineage specification, Marquez backend, tracking lineage across Airflow, Spark, and dbt.",
      "keywords": ["data lineage", "OpenLineage", "Marquez", "column-level lineage", "dataset lineage", "job run facets", "lineage metadata"]
    },
    {
      "id": "data_catalog_amundsen_datahub",
      "name": "Enterprise Data Catalogs (DataHub, Amundsen)",
      "description": "Metadata ingestion, automated schema harvesting, data ownership tagging, business glossary management, and search in DataHub or Amundsen.",
      "keywords": ["DataHub", "Amundsen", "data catalog", "metadata ingestion", "data discovery", "business glossary", "data stewardship", "glossary terms"]
    },
    {
      "id": "data_observability_montecarl_metaplane",
      "name": "Data Observability Pillars & Incident Management",
      "description": "Five pillars of data observability (Freshness, Distribution, Volume, Schema, Lineage), root-cause analysis, Monte Carlo, and automated incident alerts.",
      "keywords": ["Data Observability", "Monte Carlo", "Metaplane", "five pillars", "data downtime", "root-cause analysis", "data incident response", "SLA monitoring"]
    },
    {
      "id": "data_contract_schemas_enforcement",
      "name": "Data Contracts & Producer-Consumer Schemas",
      "description": "Defining Data Contracts between software engineers and data teams (YAML schema, SLAs, semantics), contract CI validation, and breaking change prevention.",
      "keywords": ["Data Contract", "producer-consumer agreement", "schema contract", "contract enforcement", "breaking change prevention", "data contract CLI"]
    },
    {
      "id": "gdpr_pii_anonymization_masking",
      "name": "Data Privacy, GDPR Compliance & PII Masking",
      "description": "Right to be Forgotten implementations, pseudonymization, hashing (SHA-256 with salt), dynamic data masking, tokenization, and PII detection.",
      "keywords": ["GDPR", "PII", "data masking", "dynamic data masking", "pseudonymization", "tokenization", "Right to be Forgotten", "salt hashing", "anonymization"]
    },
    {
      "id": "data_access_rbac_abac_policies",
      "name": "Data Access Governance (RBAC & ABAC Policies)",
      "description": "Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), row-level security (RLS), column-level masking policies, and Apache Ranger.",
      "keywords": ["RBAC", "ABAC", "row-level security", "RLS", "column masking policy", "Apache Ranger", "Immuta", "Privacera", "least privilege"]
    },
    {
      "id": "data_retention_archival_policies",
      "name": "Data Retention, Archival & Purge Lifecycles",
      "description": "Designing legal data retention periods, automated cold tier archival, scheduled purge routines, and compliance auditing.",
      "keywords": ["data retention", "archival policy", "purge policy", "cold storage", "glacier archival", "audit logging", "compliance lifecycle"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Implemented enterprise data quality framework with Great Expectations and established DataHub catalog",
        "strength": 0.5,
        "maps_to": ["de_data_quality_governance.data_validation_great_expectations_soda", "de_data_quality_governance.data_catalog_amundsen_datahub", "de_data_quality_governance.gdpr_pii_anonymization_masking"]
      }
    ],
    "linkedin": [
      {
        "signal": "Data Governance, Quality & Compliance specialist endorsement",
        "strength": 0.3,
        "maps_to": ["de_data_quality_governance.data_profiling_anomaly_detection", "de_data_quality_governance.data_lineage_metadata_openlineage"]
      }
    ],
    "github": [
      {
        "pattern": "*expectations*|*soda*|contracts/**/*.yml|governance/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "de_data_quality_governance.data_validation_great_expectations_soda",
          "de_data_quality_governance.data_profiling_anomaly_detection",
          "de_data_quality_governance.data_lineage_metadata_openlineage",
          "de_data_quality_governance.data_catalog_amundsen_datahub",
          "de_data_quality_governance.data_observability_montecarl_metaplane",
          "de_data_quality_governance.data_contract_schemas_enforcement",
          "de_data_quality_governance.gdpr_pii_anonymization_masking",
          "de_data_quality_governance.data_access_rbac_abac_policies",
          "de_data_quality_governance.data_retention_archival_policies"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Data Quality, Governance, Observability & Privacy Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_data_quality_governance.data_validation_great_expectations_soda",
          "de_data_quality_governance.data_profiling_anomaly_detection",
          "de_data_quality_governance.data_lineage_metadata_openlineage",
          "de_data_quality_governance.data_catalog_amundsen_datahub",
          "de_data_quality_governance.data_observability_montecarl_metaplane",
          "de_data_quality_governance.data_contract_schemas_enforcement",
          "de_data_quality_governance.gdpr_pii_anonymization_masking",
          "de_data_quality_governance.data_access_rbac_abac_policies",
          "de_data_quality_governance.data_retention_archival_policies"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["data_validation_great_expectations_soda", "data_profiling_anomaly_detection", "data_retention_archival_policies"],
      "description": "Writes automated test assertions with Great Expectations / Soda, profiles statistical data distributions, and enforces retention rules."
    },
    "mid": {
      "expected_subskills": ["data_lineage_metadata_openlineage", "data_catalog_amundsen_datahub", "gdpr_pii_anonymization_masking", "data_access_rbac_abac_policies"],
      "description": "Connects lineage metadata with OpenLineage, registers assets in DataHub, masks PII to ensure GDPR compliance, and implements row/column security policies."
    },
    "senior": {
      "expected_subskills": ["data_observability_montecarl_metaplane", "data_contract_schemas_enforcement"],
      "description": "Architects end-to-end Data Observability frameworks, establishes cross-team Data Contracts, and leads enterprise data governance initiatives."
    }
  }
}

# 10. de_cloud_infrastructure_dataops
skills["de_cloud_infrastructure_dataops"] = {
  "skill_id": "de_cloud_infrastructure_dataops",
  "name": "Cloud Infrastructure & DataOps CI/CD",
  "category": "infrastructure",
  "description": "Infrastructure as Code (Terraform) for data platforms, IAM security, Docker containerization for data pipelines, Kubernetes orchestration, CI/CD with GitHub Actions, synthetic test data generation, and FinOps cloud cost management.",
  "subskills": [
    {
      "id": "cloud_iam_service_accounts_security",
      "name": "Cloud IAM, Service Accounts & Secret Management",
      "description": "IAM roles, least privilege policies, assume-role delegation, AWS Secrets Manager, GCP Secret Manager, and HashiCorp Vault.",
      "keywords": ["IAM role", "service account", "least privilege", "AWS Secrets Manager", "GCP Secret Manager", "Vault", "KMS encryption", "assume role"]
    },
    {
      "id": "terraform_iac_data_infrastructure",
      "name": "Terraform Infrastructure as Code for Data Stacks",
      "description": "Provisioning S3/GCS buckets, Snowflake/BigQuery resources, Kafka clusters, RDS databases, Terraform state management, and reusable data modules.",
      "keywords": ["Terraform", "IaC", "terraform apply", "terraform plan", "remote state", "Terraform modules", "HCL", "provider snowflake", "provider aws"]
    },
    {
      "id": "docker_containers_for_data",
      "name": "Docker Containerization for Data Workloads",
      "description": "Multi-stage Dockerfiles for Python/Spark/dbt applications, container security, non-root users, caching dependencies, and minimizing image sizes.",
      "keywords": ["Dockerfile", "multi-stage build", "Docker Compose", "containerization", "non-root user", "slim image", "container registry", "ECR", "GCR"]
    },
    {
      "id": "kubernetes_data_workloads",
      "name": "Kubernetes for Data Engineering (Spark on K8s, Airflow)",
      "description": "Deploying data workloads on K8s, Spark-on-K8s operator, pod resource requests/limits, persistent volumes, node selectors, and spot instances.",
      "keywords": ["Kubernetes", "Spark on K8s", "SparkOperator", "Helm", "resource limits", "pod affinity", "spot instances", "PVC", "k8s namespace"]
    },
    {
      "id": "ci_cd_pipelines_for_data_github_actions",
      "name": "CI/CD Pipelines for Data Pipelines (GitHub Actions / GitLab)",
      "description": "Automated linting (sqlfluff, ruff, black), unit test suites, staging environment promotion, dbt slim CI, and automated deployment pipelines.",
      "keywords": ["GitHub Actions", "GitLab CI", "CI/CD", "sqlfluff", "ruff", "dbt slim CI", "state:modified+", "automated deployment", "PR validation"]
    },
    {
      "id": "unit_integration_testing_data_pipelines",
      "name": "Unit & Integration Testing for Data Pipelines",
      "description": "Writing pytest suites for data transformations, mocking databases and cloud storage with Moto/Testcontainers, and end-to-end integration tests.",
      "keywords": ["pytest", "Testcontainers", "moto", "mocking", "integration test", "unit test", "fixtures", "data transformation testing"]
    },
    {
      "id": "data_mocking_synthetic_generation",
      "name": "Synthetic Data Generation & Test Fixtures",
      "description": "Generating realistic synthetic test datasets using Faker, synthetic data generators, anonymized production samples, and deterministic test fixtures.",
      "keywords": ["Faker", "synthetic data", "mock data", "test fixture", "deterministic mock", "sample data generator"]
    },
    {
      "id": "cloud_cost_governance_finops",
      "name": "Data Cloud FinOps & Cost Governance",
      "description": "Tagging cloud data assets, tracking compute/storage costs, identifying idle clusters, auto-scaling down off-hours, and FinOps budgeting.",
      "keywords": ["FinOps", "cost allocation", "cost tagging", "idle cluster", "auto-termination", "spot instances", "AWS Cost Explorer", "BigQuery cost optimization"]
    },
    {
      "id": "disaster_recovery_backup_data_systems",
      "name": "Disaster Recovery, High Availability & Backups",
      "description": "Multi-region data replication, point-in-time recovery (PITR), automated database backups, RTO/RPO targets, and failover runbooks.",
      "keywords": ["Disaster Recovery", "PITR", "RTO", "RPO", "multi-region replication", "failover", "backup strategy", "runbook", "high availability"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Provisioned multi-environment cloud data platform via Terraform and GitHub Actions CI/CD",
        "strength": 0.5,
        "maps_to": ["de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure", "de_cloud_infrastructure_dataops.ci_cd_pipelines_for_data_github_actions", "de_cloud_infrastructure_dataops.cloud_iam_service_accounts_security"]
      }
    ],
    "linkedin": [
      {
        "signal": "AWS Certified Data Engineer or HashiCorp Terraform Associate",
        "strength": 0.3,
        "maps_to": ["de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure", "de_cloud_infrastructure_dataops.docker_containers_for_data"]
      }
    ],
    "github": [
      {
        "pattern": "*.tf|terraform/**/*.tf|.github/workflows/*.yml|Dockerfile|docker-compose.yml",
        "strength": 1.0,
        "maps_to": [
          "de_cloud_infrastructure_dataops.cloud_iam_service_accounts_security",
          "de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure",
          "de_cloud_infrastructure_dataops.docker_containers_for_data",
          "de_cloud_infrastructure_dataops.kubernetes_data_workloads",
          "de_cloud_infrastructure_dataops.ci_cd_pipelines_for_data_github_actions",
          "de_cloud_infrastructure_dataops.unit_integration_testing_data_pipelines",
          "de_cloud_infrastructure_dataops.data_mocking_synthetic_generation",
          "de_cloud_infrastructure_dataops.cloud_cost_governance_finops",
          "de_cloud_infrastructure_dataops.disaster_recovery_backup_data_systems"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Cloud Data Infrastructure & DataOps CI/CD Assessment",
        "strength": 1.0,
        "maps_to": [
          "de_cloud_infrastructure_dataops.cloud_iam_service_accounts_security",
          "de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure",
          "de_cloud_infrastructure_dataops.docker_containers_for_data",
          "de_cloud_infrastructure_dataops.kubernetes_data_workloads",
          "de_cloud_infrastructure_dataops.ci_cd_pipelines_for_data_github_actions",
          "de_cloud_infrastructure_dataops.unit_integration_testing_data_pipelines",
          "de_cloud_infrastructure_dataops.data_mocking_synthetic_generation",
          "de_cloud_infrastructure_dataops.cloud_cost_governance_finops",
          "de_cloud_infrastructure_dataops.disaster_recovery_backup_data_systems"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["docker_containers_for_data", "ci_cd_pipelines_for_data_github_actions", "unit_integration_testing_data_pipelines"],
      "description": "Containerizes data applications with Docker, configures GitHub Actions CI workflows, and writes pytest suites with mocks."
    },
    "mid": {
      "expected_subskills": ["cloud_iam_service_accounts_security", "terraform_iac_data_infrastructure", "data_mocking_synthetic_generation"],
      "description": "Provisions data infrastructure with Terraform, manages least privilege cloud IAM security, and generates synthetic test fixtures."
    },
    "senior": {
      "expected_subskills": ["kubernetes_data_workloads", "cloud_cost_governance_finops", "disaster_recovery_backup_data_systems"],
      "description": "Orchestrates distributed workloads (Spark) on Kubernetes, manages FinOps cloud cost optimization, and architects multi-region disaster recovery systems."
    }
  }
}

# Write skill files
for skill_id, data in skills.items():
  filepath = os.path.join(skills_dir, f'{skill_id}.json')
  with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(skills)} skill JSON files in {skills_dir}")

# -------------------------------------------------------------
# ROLES DEFINITION (junior, mid, senior)
# -------------------------------------------------------------
roles = {
  "junior": {
    "role_id": "data_engineer",
    "level": "junior",
    "title": "Junior Data Engineer",
    "description": "Entry-level data engineering position focused on foundational SQL, Python script automation, data extraction, basic Airflow DAGs, dbt models, and automated data quality checks under guidance.",
    "experience_range": "0-2 years",
    "skills": [
      {
        "skill_id": "de_sql_advanced",
        "importance": 0.95,
        "rationale": "Writing clean analytical SQL, joins, CTEs, and window functions is non-negotiable for daily data tasks."
      },
      {
        "skill_id": "de_programming",
        "importance": 0.90,
        "rationale": "Strong Python programming for data extraction, manipulation, and pipeline scripting."
      },
      {
        "skill_id": "de_data_modeling_transformation",
        "importance": 0.85,
        "rationale": "Building dbt models, implementing tests, and documenting schemas is a core daily activity."
      },
      {
        "skill_id": "de_data_pipelines_orchestration",
        "importance": 0.80,
        "rationale": "Creating and scheduling basic Airflow DAGs with TaskFlow API."
      },
      {
        "skill_id": "de_data_warehousing",
        "importance": 0.75,
        "rationale": "Understanding dimensional modeling, star schemas, and fact/dimension concepts."
      },
      {
        "skill_id": "de_data_lakes_storage",
        "importance": 0.70,
        "rationale": "Working with S3/GCS object storage, Parquet files, and Medallion architecture basics."
      },
      {
        "skill_id": "de_data_quality_governance",
        "importance": 0.65,
        "rationale": "Writing data quality assertions with Great Expectations or Soda."
      },
      {
        "skill_id": "de_cloud_infrastructure_dataops",
        "importance": 0.60,
        "rationale": "Dockerizing data jobs, writing unit tests with pytest, and using CI/CD."
      },
      {
        "skill_id": "de_distributed_computing",
        "importance": 0.50,
        "rationale": "Basic PySpark DataFrame operations and understanding distributed architecture."
      },
      {
        "skill_id": "de_streaming_realtime",
        "importance": 0.40,
        "rationale": "Foundational understanding of Kafka topics and producer/consumer mechanics."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.35, "description": "Insufficient foundational knowledge in SQL and Python data manipulation." },
        "partially_ready": { "min": 0.35, "max": 0.60, "description": "Meets basic scripting needs but lacks production orchestration and data modeling depth." },
        "ready": { "min": 0.60, "max": 0.85, "description": "Solid junior engineer capable of writing ELT pipelines and maintaining dbt/Airflow workflows under guidance." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceeds junior requirements with strong grasp of distributed engines and data warehouse performance." }
      }
    }
  },
  "mid": {
    "role_id": "data_engineer",
    "level": "mid",
    "title": "Mid-Level Data Engineer",
    "description": "Mid-level data engineering position focused on building scalable, production-grade ETL/ELT pipelines, distributed data processing with PySpark, dimensional data warehousing, ACID Lakehouse formats, Kafka streaming, and robust DataOps practices.",
    "experience_range": "2-5 years",
    "skills": [
      {
        "skill_id": "de_sql_advanced",
        "importance": 0.95,
        "rationale": "Mastery of database indexing, table partitioning, transactions, and execution plan optimization."
      },
      {
        "skill_id": "de_programming",
        "importance": 0.90,
        "rationale": "Writing high-concurrency, functional, type-safe Python/Scala data processing services."
      },
      {
        "skill_id": "de_distributed_computing",
        "importance": 0.90,
        "rationale": "Developing and tuning Spark jobs, partition management, broadcast joins, and caching."
      },
      {
        "skill_id": "de_data_warehousing",
        "importance": 0.90,
        "rationale": "Architecting Snowflake/BigQuery warehouses, clustering, and managing complex SCD Type 2 logic."
      },
      {
        "skill_id": "de_data_pipelines_orchestration",
        "importance": 0.85,
        "rationale": "Designing robust idempotent Airflow/Prefect pipelines, handling backfills, and managing SLAs."
      },
      {
        "skill_id": "de_data_modeling_transformation",
        "importance": 0.85,
        "rationale": "Authoring enterprise dbt incremental models, reusable Jinja macros, and custom tests."
      },
      {
        "skill_id": "de_data_lakes_storage",
        "importance": 0.85,
        "rationale": "Operating Delta Lake / Iceberg tables, managing time travel, and Z-Order optimization."
      },
      {
        "skill_id": "de_streaming_realtime",
        "importance": 0.75,
        "rationale": "Building Kafka Streams / ksqlDB pipelines and handling event time windowing."
      },
      {
        "skill_id": "de_cloud_infrastructure_dataops",
        "importance": 0.75,
        "rationale": "Provisioning data infrastructure with Terraform, IAM security, and automated CI/CD."
      },
      {
        "skill_id": "de_data_quality_governance",
        "importance": 0.70,
        "rationale": "Implementing OpenLineage metadata, DataHub catalogs, and PII anonymization policies."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.40, "description": "Lacks production experience with distributed processing and Lakehouse table formats." },
        "partially_ready": { "min": 0.40, "max": 0.65, "description": "Competent in batch ETL but requires guidance on Spark tuning and streaming architectures." },
        "ready": { "min": 0.65, "max": 0.88, "description": "Fully autonomous data engineer capable of delivering reliable enterprise data pipelines and optimizing cloud compute." },
        "exceeds": { "min": 0.88, "max": 1.0, "description": "Demonstrates senior-level technical leadership, distributed internals mastery, and architectural vision." }
      }
    }
  },
  "senior": {
    "role_id": "data_engineer",
    "level": "senior",
    "title": "Senior Data Engineer / Data Architect",
    "description": "Senior technical leadership position driving data architecture, distributed systems scaling (Spark, Flink, Kafka), multi-engine Lakehouse strategy, cost governance (FinOps), enterprise DataOps, and company-wide data quality & privacy compliance.",
    "experience_range": "5+ years",
    "skills": [
      {
        "skill_id": "de_distributed_computing",
        "importance": 0.95,
        "rationale": "Deep distributed internals, solving heavy shuffle data skew, memory tuning, and Structured Streaming at scale."
      },
      {
        "skill_id": "de_data_warehousing",
        "importance": 0.95,
        "rationale": "Designing multi-warehouse topologies, semantic layers, and comprehensive cost governance."
      },
      {
        "skill_id": "de_data_lakes_storage",
        "importance": 0.95,
        "rationale": "Lakehouse governance, Apache Iceberg / Hudi upsert architecture, and compaction lifecycles."
      },
      {
        "skill_id": "de_sql_advanced",
        "importance": 0.90,
        "rationale": "Cost-based execution plan optimization, internal storage engines, and enterprise database tuning."
      },
      {
        "skill_id": "de_streaming_realtime",
        "importance": 0.90,
        "rationale": "Stateful stream processing with Apache Flink, Exactly-Once semantics, and RocksDB state tuning."
      },
      {
        "skill_id": "de_data_pipelines_orchestration",
        "importance": 0.90,
        "rationale": "Asset-based orchestration in Dagster, distributed Kubernetes executors, and high-availability design."
      },
      {
        "skill_id": "de_data_quality_governance",
        "importance": 0.85,
        "rationale": "Architecting Data Observability platforms, cross-team Data Contracts, and regulatory compliance."
      },
      {
        "skill_id": "de_cloud_infrastructure_dataops",
        "importance": 0.85,
        "rationale": "Kubernetes data operators, multi-region disaster recovery, and FinOps budgeting."
      },
      {
        "skill_id": "de_programming",
        "importance": 0.85,
        "rationale": "Profiling long-running memory bottlenecks, JVM optimization, and core systems architecture."
      },
      {
        "skill_id": "de_data_modeling_transformation",
        "importance": 0.80,
        "rationale": "Enterprise semantic layer design, virtual data engines (SQLMesh), and transformation governance."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.45, "description": "Does not meet the architectural depth, distributed tuning, or system leadership required for senior roles." },
        "partially_ready": { "min": 0.45, "max": 0.70, "description": "Strong pipeline builder but lacks distributed system internals, streaming EOS, or FinOps architectural experience." },
        "ready": { "min": 0.70, "max": 0.90, "description": "Proven senior engineer with comprehensive data platform design, distributed tuning, and governance mastery." },
        "exceeds": { "min": 0.90, "max": 1.0, "description": "Outstanding data architect capable of setting enterprise-wide standards, cutting cloud costs, and building petabyte-scale platforms." }
      }
    }
  }
}

for role_level, data in roles.items():
  filepath = os.path.join(roles_dir, f'{role_level}.json')
  with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(roles)} role JSON files in {roles_dir}")

# -------------------------------------------------------------
# EVIDENCE DEFINITIONS (cv.json, linkedin.json, github.json, assessment.json)
# -------------------------------------------------------------

# 1. cv.json
cv_data = {
  "source_id": "cv",
  "name": "CV / Resume Parser - Data Engineering",
  "description": "Extraction and scoring rules for Data Engineering CVs/Resumes based on section strengths and keyword associations.",
  "sections": [
    {
      "section_id": "work_experience",
      "name": "Work Experience",
      "base_strength": 0.5,
      "description": "Professional data engineering roles, projects, and impact metrics.",
      "signal_extractors": [
        {
          "pattern": "Apache Spark|PySpark|Scala|Spark SQL",
          "strength": 0.5,
          "maps_to": [
            "de_distributed_computing.spark_architecture_cluster_managers",
            "de_distributed_computing.rdd_vs_dataframe_dataset",
            "de_distributed_computing.spark_sql_catalyst_optimizer",
            "de_distributed_computing.shuffling_skew_repartition"
          ]
        },
        {
          "pattern": "Snowflake|BigQuery|Redshift|Star Schema|Dimensional Modeling",
          "strength": 0.5,
          "maps_to": [
            "de_data_warehousing.dimensional_star_snowflake",
            "de_data_warehousing.fact_dimension_design",
            "de_data_warehousing.scd_type_management",
            "de_data_warehousing.snowflake_architecture",
            "de_data_warehousing.bigquery_architecture"
          ]
        },
        {
          "pattern": "Apache Airflow|Prefect|Dagster|DAG|ETL|ELT",
          "strength": 0.5,
          "maps_to": [
            "de_data_pipelines_orchestration.airflow_dag_design_best_practices",
            "de_data_pipelines_orchestration.airflow_operators_hooks_sensors",
            "de_data_pipelines_orchestration.airflow_taskflow_api_xcoms",
            "de_data_pipelines_orchestration.idempotency_data_reprocessing"
          ]
        },
        {
          "pattern": "Delta Lake|Apache Iceberg|Apache Hudi|Parquet|Lakehouse",
          "strength": 0.5,
          "maps_to": [
            "de_data_lakes_storage.delta_lake_acid",
            "de_data_lakes_storage.apache_iceberg_architecture",
            "de_data_lakes_storage.parquet_orc_file_formats",
            "de_data_lakes_storage.lakehouse_medallion_architecture"
          ]
        },
        {
          "pattern": "Apache Kafka|Kafka Streams|Flink|ksqlDB|Streaming",
          "strength": 0.5,
          "maps_to": [
            "de_streaming_realtime.kafka_architecture_topics_partitions",
            "de_streaming_realtime.producer_consumer_consumer_groups",
            "de_streaming_realtime.apache_flink_stream_processing",
            "de_streaming_realtime.exactly_once_semantics_transactions"
          ]
        },
        {
          "pattern": "dbt|dbt Core|dbt Cloud|Jinja|Data Transformation",
          "strength": 0.5,
          "maps_to": [
            "de_data_modeling_transformation.dbt_models_ref_source",
            "de_data_modeling_transformation.dbt_jinja_macros_packages",
            "de_data_modeling_transformation.dbt_materializations_incremental",
            "de_data_modeling_transformation.dbt_testing_generic_singular"
          ]
        },
        {
          "pattern": "Great Expectations|Soda|DataHub|OpenLineage|Data Quality",
          "strength": 0.5,
          "maps_to": [
            "de_data_quality_governance.data_validation_great_expectations_soda",
            "de_data_quality_governance.data_lineage_metadata_openlineage",
            "de_data_quality_governance.data_catalog_amundsen_datahub",
            "de_data_quality_governance.gdpr_pii_anonymization_masking"
          ]
        },
        {
          "pattern": "Terraform|Docker|Kubernetes|GitHub Actions|CI/CD|FinOps",
          "strength": 0.5,
          "maps_to": [
            "de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure",
            "de_cloud_infrastructure_dataops.docker_containers_for_data",
            "de_cloud_infrastructure_dataops.ci_cd_pipelines_for_data_github_actions",
            "de_cloud_infrastructure_dataops.cloud_cost_governance_finops"
          ]
        },
        {
          "pattern": "Advanced SQL|Window Functions|Query Optimization|PostgreSQL",
          "strength": 0.5,
          "maps_to": [
            "de_sql_advanced.complex_joins_subqueries",
            "de_sql_advanced.window_functions_analytical",
            "de_sql_advanced.query_execution_plans",
            "de_sql_advanced.indexing_b_tree_strategies"
          ]
        },
        {
          "pattern": "Python|AsyncIO|Concurrency|OOP|Memory Profiling|Scala",
          "strength": 0.5,
          "maps_to": [
            "de_programming.python_core_oop",
            "de_programming.concurrency_multiprocessing",
            "de_programming.memory_management_profiling",
            "de_programming.scala_jvm_ecosystem"
          ]
        }
      ]
    },
    {
      "section_id": "projects",
      "name": "Projects",
      "base_strength": 0.5,
      "description": "Data engineering projects and open-source contributions."
    },
    {
      "section_id": "skills_list",
      "name": "Skills List",
      "base_strength": 0.3,
      "description": "Self-reported technical skill keywords."
    },
    {
      "section_id": "education",
      "name": "Education & Certifications",
      "base_strength": 0.3,
      "description": "Degrees and vendor certifications."
    }
  ]
}

with open(os.path.join(evidence_dir, 'cv.json'), 'w', encoding='utf-8') as f:
  json.dump(cv_data, f, indent=2)

# 2. linkedin.json
linkedin_data = {
  "source_id": "linkedin",
  "name": "LinkedIn Profile Signals - Data Engineering",
  "description": "Signals and skill mappings derived from LinkedIn profiles.",
  "sections": [
    {
      "section_id": "experience",
      "base_strength": 0.5,
      "description": "Job titles, responsibilities, and achievements in data engineering roles."
    },
    {
      "section_id": "headline_summary",
      "base_strength": 0.3,
      "description": "Profile headline and professional summary keywords."
    },
    {
      "section_id": "skills_endorsements",
      "base_strength": 0.3,
      "description": "Endorsed skills related to big data, SQL, cloud warehouses, and pipeline orchestration."
    },
    {
      "section_id": "recommendations",
      "base_strength": 0.5,
      "description": "Colleague recommendations highlighting data engineering impact."
    }
  ]
}

with open(os.path.join(evidence_dir, 'linkedin.json'), 'w', encoding='utf-8') as f:
  json.dump(linkedin_data, f, indent=2)

# 3. github.json
github_data = {
  "source_id": "github",
  "name": "GitHub Repository Analysis - Data Engineering",
  "description": "Automated code and manifest scanning rules for detecting data engineering proficiency.",
  "preprocessing_pipeline": {
    "steps": [
      {
        "step": 1,
        "name": "repository_metadata",
        "description": "Scans languages, dependencies, and commit activity."
      },
      {
        "step": 2,
        "name": "file_tree_scan",
        "description": "Scans for pipeline definitions, dbt projects, IaC files, and SQL models.",
        "target_files": [
          { "pattern": "dbt_project.yml|packages.yml", "skill": "de_data_modeling_transformation", "priority": "high" },
          { "pattern": "dags/**/*.py|airflow.cfg", "skill": "de_data_pipelines_orchestration", "priority": "high" },
          { "pattern": "*.tf|terraform.tfvars", "skill": "de_cloud_infrastructure_dataops", "priority": "high" },
          { "pattern": "*spark*.py|build.sbt|*.scala", "skill": "de_distributed_computing", "priority": "high" },
          { "pattern": "*.sql|migrations/*.sql", "skill": "de_sql_advanced", "priority": "high" },
          { "pattern": "*kafka*|*flink*", "skill": "de_streaming_realtime", "priority": "high" },
          { "pattern": "*great_expectations*|*soda*.yml", "skill": "de_data_quality_governance", "priority": "high" }
        ]
      }
    ]
  }
}

with open(os.path.join(evidence_dir, 'github.json'), 'w', encoding='utf-8') as f:
  json.dump(github_data, f, indent=2)

# 4. assessment.json
# Generate high quality questions for ALL 91 composite keys
questions_by_key = {
  # de_programming (9)
  "de_programming.python_core_oop": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do Python generators conserve memory when processing large data files compared to lists?",
      "expected_answer_keywords": ["yield", "lazy evaluation", "iterator", "memory efficient", "stream", "one item at a time"]
    }
  ],
  "de_programming.typing_data_structures": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is Pydantic and typing module preferred over raw dicts for parsing incoming data payload records?",
      "expected_answer_keywords": ["type validation", "BaseModel", "schema enforcement", "data parsing", "type hints", "runtime validation"]
    }
  ],
  "de_programming.functional_programming": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is a pure function in functional programming and why is immutability crucial in distributed data processing?",
      "expected_answer_keywords": ["pure function", "no side effects", "deterministic", "immutability", "concurrency safe", "cacheable"]
    }
  ],
  "de_programming.concurrency_multiprocessing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "When would you choose Python's multiprocessing module over threading for a data transformation pipeline?",
      "expected_answer_keywords": ["GIL", "Global Interpreter Lock", "CPU-bound", "multi-core", "ProcessPoolExecutor", "parallel execution"]
    }
  ],
  "de_programming.memory_management_profiling": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How would you identify and fix a memory leak in a long-running batch ingestion daemon in Python?",
      "expected_answer_keywords": ["tracemalloc", "memory_profiler", "gc", "garbage collection", "circular reference", "heap dump"]
    }
  ],
  "de_programming.serialization_protocols": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What are the structural advantages of Apache Avro or Protocol Buffers over JSON in high-throughput data streams?",
      "expected_answer_keywords": ["binary format", "schema evolution", "compact size", "serialization speed", "strongly typed"]
    }
  ],
  "de_programming.scala_jvm_ecosystem": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do case classes and pattern matching in Scala simplify building complex distributed ETL transformations?",
      "expected_answer_keywords": ["case class", "pattern matching", "immutability", "type safety", "unapply", "ADT"]
    }
  ],
  "de_programming.data_structures_algorithms": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How would you perform a topological sort on a set of interdependent pipeline tasks to determine valid execution order?",
      "expected_answer_keywords": ["topological sort", "DAG", "indegree", "Kahn's algorithm", "cycle detection", "dependency graph"]
    }
  ],
  "de_programming.package_dependency_management": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is lockfile pinning (e.g. poetry.lock or uv.lock) critical in deterministic data pipeline deployments?",
      "expected_answer_keywords": ["reproducibility", "lockfile", "deterministic build", "dependency resolution", "pyproject.toml", "version pinning"]
    }
  ],

  # de_sql_advanced (9)
  "de_sql_advanced.complex_joins_subqueries": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the difference between a LEFT JOIN and a LEFT ANTI JOIN in SQL, and when would you use an anti-join?",
      "expected_answer_keywords": ["LEFT ANTI JOIN", "NOT EXISTS", "IS NULL", "filter non-matching", "exclusion", "subquery"]
    }
  ],
  "de_sql_advanced.window_functions_analytical": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you compute a running 7-day average of transactions using SQL window functions?",
      "expected_answer_keywords": ["AVG()", "OVER", "PARTITION BY", "ORDER BY", "ROWS BETWEEN 6 PRECEDING AND CURRENT ROW", "window frame"]
    }
  ],
  "de_sql_advanced.ctes_recursive_queries": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How does a WITH RECURSIVE query traverse an organizational hierarchy table (manager_id -> employee_id)?",
      "expected_answer_keywords": ["WITH RECURSIVE", "anchor member", "UNION ALL", "recursive member", "termination condition", "parent-child"]
    }
  ],
  "de_sql_advanced.indexing_b_tree_strategies": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is a covering index and how does the INCLUDE clause enable Index-Only Scans?",
      "expected_answer_keywords": ["covering index", "Index-Only Scan", "INCLUDE clause", "leaf node", "avoid table lookup", "B-Tree"]
    }
  ],
  "de_sql_advanced.query_execution_plans": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "When analyzing EXPLAIN ANALYZE output, what indicates that a planner chose a Hash Join over a Merge Join, and when is that optimal?",
      "expected_answer_keywords": ["Hash Join", "Merge Join", "hash table in memory", "unsorted input", "work_mem", "cardinality estimation"]
    }
  ],
  "de_sql_advanced.partitioning_sharding": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does partition pruning improve analytical query performance on billion-row date-partitioned tables?",
      "expected_answer_keywords": ["partition pruning", "skip partitions", "filter condition", "WHERE clause", "I/O reduction", "range partition"]
    }
  ],
  "de_sql_advanced.transactions_acid_isolation": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is the difference between Read Committed and Repeatable Read isolation levels, and what anomaly does Repeatable Read prevent?",
      "expected_answer_keywords": ["isolation level", "Read Committed", "Repeatable Read", "non-repeatable read", "phantom read", "MVCC snapshot"]
    }
  ],
  "de_sql_advanced.stored_procedures_udfs": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "What are the performance trade-offs of using scalar SQL User-Defined Functions (UDFs) vs inline set-based operations?",
      "expected_answer_keywords": ["row-by-row execution", "RBAR", "black box optimizer", "set-based", "inlining", "performance penalty"]
    }
  ],
  "de_sql_advanced.db_performance_tuning": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you detect and resolve disk-spill sorting bottlenecks in analytical database queries?",
      "expected_answer_keywords": ["work_mem", "temporary file spill", "disk sort", "buffer cache", "EXPLAIN ANALYZE Sort Method", "memory allocation"]
    }
  ],

  # de_data_warehousing (9)
  "de_data_warehousing.dimensional_star_snowflake": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Compare Star Schema and Snowflake Schema in terms of normalization, query complexity, and analytical performance.",
      "expected_answer_keywords": ["star schema", "snowflake schema", "normalization", "denormalization", "join complexity", "query performance", "grain"]
    }
  ],
  "de_data_warehousing.fact_dimension_design": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the difference between a Transaction Fact table, Periodic Snapshot Fact table, and Accumulating Snapshot Fact table?",
      "expected_answer_keywords": ["transaction fact", "periodic snapshot", "accumulating snapshot", "milestones", "grain", "time interval"]
    }
  ],
  "de_data_warehousing.scd_type_management": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "Explain how an SCD Type 2 dimension tracks history with surrogate keys, valid_from, valid_to, and is_current columns.",
      "expected_answer_keywords": ["SCD Type 2", "surrogate key", "valid_from", "valid_to", "is_current", "versioning", "historical tracking"]
    }
  ],
  "de_data_warehousing.snowflake_architecture": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does Snowflake's separation of storage and compute enable independent scaling and zero-copy cloning?",
      "expected_answer_keywords": ["separation of storage and compute", "virtual warehouse", "micro-partitions", "zero-copy cloning", "metadata pointers", "centralized storage"]
    }
  ],
  "de_data_warehousing.bigquery_architecture": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does BigQuery slot allocation and table clustering optimize query performance and reduce scanned bytes?",
      "expected_answer_keywords": ["slots", "clustering", "partitioning", "pruning", "scanned bytes", "Dremel engine", "cost reduction"]
    }
  ],
  "de_data_warehousing.redshift_architecture": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "When designing an Amazon Redshift table, how do you select between KEY, ALL, and EVEN distribution styles to prevent network broadcast?",
      "expected_answer_keywords": ["DISTSTYLE", "DISTKEY", "distribution style", "KEY distribution", "colocated join", "EVEN", "ALL", "network shuffle"]
    }
  ],
  "de_data_warehousing.columnar_storage_compression": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Why is Run-Length Encoding (RLE) and Dictionary Encoding highly effective on sorted columnar data?",
      "expected_answer_keywords": ["dictionary encoding", "RLE", "run-length encoding", "sorted data", "compression ratio", "I/O pruning", "columnar"]
    }
  ],
  "de_data_warehousing.semantic_layer_metrics": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "What business problems does a centralized Semantic Layer solve compared to defining metrics directly in BI dashboards?",
      "expected_answer_keywords": ["semantic layer", "single source of truth", "metric consistency", "governed metrics", "dbt semantic layer", "Cube.js", "DRY"]
    }
  ],
  "de_data_warehousing.warehouse_cost_optimization": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you implement query tagging, auto-suspend policies, and warehouse right-sizing to reduce Snowflake credit consumption by 40%?",
      "expected_answer_keywords": ["auto-suspend", "warehouse sizing", "query tagging", "credit monitoring", "concurrency scaling", "resource monitor", "FinOps"]
    }
  ],

  # de_data_lakes_storage (9)
  "de_data_lakes_storage.object_storage_s3_gcs_blob": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is prefix partitioning and avoiding hot partition keys important when reading/writing petabytes of data to AWS S3?",
      "expected_answer_keywords": ["prefix partitioning", "S3 TPS limits", "request rate", "hash prefix", "multipart upload", "object storage"]
    }
  ],
  "de_data_lakes_storage.parquet_orc_file_formats": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the internal structure of a Parquet file: Row Groups, Column Chunks, and File Footer metadata.",
      "expected_answer_keywords": ["row group", "column chunk", "footer metadata", "min/max statistics", "predicate pushdown", "Parquet anatomy"]
    }
  ],
  "de_data_lakes_storage.delta_lake_acid": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Delta Lake use the _delta_log transaction log and optimistic concurrency control to guarantee ACID transactions on S3?",
      "expected_answer_keywords": ["_delta_log", "JSON commits", "checkpoint Parquet", "optimistic concurrency control", "ACID", "atomic commits"]
    }
  ],
  "de_data_lakes_storage.apache_iceberg_architecture": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Describe the hierarchical tree structure of Apache Iceberg: Iceberg Catalog, Metadata file, Manifest List, and Manifest files.",
      "expected_answer_keywords": ["Iceberg Catalog", "Metadata JSON", "Manifest List", "Manifest file", "snapshot isolation", "hidden partitioning", "Avro metadata"]
    }
  ],
  "de_data_lakes_storage.apache_hudi_upserts": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "What is the architectural difference between Apache Hudi Copy-on-Write (CoW) and Merge-on-Read (MoR) storage types?",
      "expected_answer_keywords": ["Copy-on-Write", "Merge-on-Read", "CoW", "MoR", "log files", "compaction", "write amplification", "read latency"]
    }
  ],
  "de_data_lakes_storage.partitioning_z_ordering": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Z-Ordering (multi-dimensional clustering) overcome the limitations of hierarchical directory partitioning?",
      "expected_answer_keywords": ["Z-Order curve", "multi-dimensional clustering", "data skipping", "high cardinality", "over-partitioning", "file pruning"]
    }
  ],
  "de_data_lakes_storage.small_files_compaction": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Why does streaming ingestion cause the 'small file problem' on data lakes, and how do you design an automated compaction job?",
      "expected_answer_keywords": ["small file problem", "bin-packing", "OPTIMIZE", "compaction", "metadata overhead", "target file size", "VACUUM"]
    }
  ],
  "de_data_lakes_storage.lakehouse_medallion_architecture": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Describe the responsibility of Bronze, Silver, and Gold layers in a Medallion Lakehouse architecture.",
      "expected_answer_keywords": ["Bronze raw", "Silver cleansed enriched", "Gold business aggregated", "Medallion", "deduplication", "single source of truth"]
    }
  ],
  "de_data_lakes_storage.time_travel_schema_evolution": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you query historical snapshot versions using time travel in Delta Lake or Apache Iceberg?",
      "expected_answer_keywords": ["VERSION AS OF", "TIMESTAMP AS OF", "time travel", "snapshot id", "audit", "rollback", "historical query"]
    }
  ],

  # de_distributed_computing (10)
  "de_distributed_computing.spark_architecture_cluster_managers": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the roles of Spark Driver, Cluster Manager, and Executors during spark application execution.",
      "expected_answer_keywords": ["Spark Driver", "Cluster Manager", "Executor", "DAGScheduler", "TaskScheduler", "tasks", "stages"]
    }
  ],
  "de_distributed_computing.rdd_vs_dataframe_dataset": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why are DataFrames significantly faster than raw RDDs in PySpark?",
      "expected_answer_keywords": ["Catalyst optimizer", "Tungsten execution engine", "serialization overhead", "off-heap memory", "schema awareness"]
    }
  ],
  "de_distributed_computing.spark_sql_catalyst_optimizer": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What stages does a Spark SQL query undergo in the Catalyst Optimizer before generating physical bytecode?",
      "expected_answer_keywords": ["Unresolved Logical Plan", "Analyzed Logical Plan", "Optimized Logical Plan", "Physical Plan", "Whole-Stage CodeGen", "Catalyst"]
    }
  ],
  "de_distributed_computing.partitioning_bucketing_coalesce": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "When should you use coalesce() instead of repartition() in PySpark, and what is the key difference?",
      "expected_answer_keywords": ["coalesce", "repartition", "avoid full shuffle", "decrease partitions", "repartition full shuffle", "narrow dependency"]
    }
  ],
  "de_distributed_computing.shuffling_skew_repartition": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you detect and remediate severe data skew on a join key in Apache Spark using salting and AQE?",
      "expected_answer_keywords": ["data skew", "salting", "random salt key", "AQE skew join", "straggler tasks", "Adaptive Query Execution"]
    }
  ],
  "de_distributed_computing.broadcast_joins_accumulators": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does BroadcastHashJoin (BHJ) eliminate shuffle overhead when joining a small dimension table with a massive fact table?",
      "expected_answer_keywords": ["BroadcastHashJoin", "broadcast()", "autoBroadcastJoinThreshold", "avoid shuffle", "executor memory", "hash table"]
    }
  ],
  "de_distributed_computing.spark_caching_persistence": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is the difference between cache() and persist(StorageLevel.MEMORY_AND_DISK_SER) in Spark?",
      "expected_answer_keywords": ["cache", "persist", "MEMORY_ONLY", "MEMORY_AND_DISK_SER", "serialization", "spill to disk", "StorageLevel"]
    }
  ],
  "de_distributed_computing.spark_memory_tuning_oom": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you diagnose and fix Executor OOM (Container killed by YARN/K8s for exceeding memory limits) errors in Spark?",
      "expected_answer_keywords": ["spark.executor.memoryOverhead", "spark.memory.fraction", "off-heap memory", "GC pause", "G1GC", "high partition size", "OOM"]
    }
  ],
  "de_distributed_computing.spark_structured_streaming": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does Spark Structured Streaming use watermarks and checkpointLocation to handle out-of-order data and ensure fault tolerance?",
      "expected_answer_keywords": ["watermark", "checkpointLocation", "write-ahead log", "stateStore", "late data", "Trigger.AvailableNow"]
    }
  ],
  "de_distributed_computing.pyspark_udfs_vectorization": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why are PySpark Pandas UDFs (@pandas_udf) orders of magnitude faster than standard Python UDFs?",
      "expected_answer_keywords": ["@pandas_udf", "Apache Arrow", "vectorized execution", "PyArrow serialization", "batch processing", "zero-copy"]
    }
  ],

  # de_data_pipelines_orchestration (9)
  "de_data_pipelines_orchestration.airflow_dag_design_best_practices": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why should you never write top-level API requests or database queries inside an Airflow DAG file?",
      "expected_answer_keywords": ["DAG parsing loop", "scheduler overhead", "top-level code", "delay parsing", "database load", "best practices"]
    }
  ],
  "de_data_pipelines_orchestration.airflow_operators_hooks_sensors": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the advantage of using mode='reschedule' over mode='poke' in Airflow sensors?",
      "expected_answer_keywords": ["mode='reschedule'", "mode='poke'", "free worker slot", "resource exhaustion", "sensor deadlock", "reschedule slot"]
    }
  ],
  "de_data_pipelines_orchestration.airflow_taskflow_api_xcoms": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How does Airflow 2.x TaskFlow API (@task) handle data passing between tasks, and why should you avoid passing gigabyte DataFrames via XCom?",
      "expected_answer_keywords": ["TaskFlow API", "@task", "XCom", "metadata database size", "custom XCom backend", "S3/GCS pointer"]
    }
  ],
  "de_data_pipelines_orchestration.airflow_backfilling_catchup": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain the role of logical_date (execution_date) and data_interval_start/end in Airflow historical backfills.",
      "expected_answer_keywords": ["logical_date", "execution_date", "data_interval_start", "data_interval_end", "airflow dags backfill", "deterministic"]
    }
  ],
  "de_data_pipelines_orchestration.prefect_orchestration": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How do Prefect Flows, Tasks, and Work Pools provide dynamic orchestration compared to static DAG definitions?",
      "expected_answer_keywords": ["Prefect", "@flow", "@task", "work pool", "dynamic DAG", "hybrid model", "Prefect worker"]
    }
  ],
  "de_data_pipelines_orchestration.dagster_software_defined_assets": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "How does Dagster's Software-Defined Assets (SDA) paradigm shift orchestration from task-centric to asset-centric data modeling?",
      "expected_answer_keywords": ["Software-Defined Assets", "@asset", "asset lineage", "data asset", "declarative orchestration", "IOManager", "reconciliation"]
    }
  ],
  "de_data_pipelines_orchestration.idempotency_data_reprocessing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you design an idempotent ETL pipeline that safely reruns without producing duplicate records or corrupted partial states?",
      "expected_answer_keywords": ["idempotency", "atomic write", "staging table swap", "partition overwrite", "deterministic", "delete and insert"]
    }
  ],
  "de_data_pipelines_orchestration.pipeline_sla_alerting": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure SLA miss callbacks and on_failure_callback notifications in Airflow for critical data deliverables?",
      "expected_answer_keywords": ["sla_miss_callback", "on_failure_callback", "Slack webhook", "PagerDuty", "SLA monitoring", "callback context"]
    }
  ],
  "de_data_pipelines_orchestration.distributed_executors_celery_k8s": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Compare CeleryExecutor and KubernetesExecutor in terms of resource isolation, task startup latency, and cluster scaling.",
      "expected_answer_keywords": ["KubernetesExecutor", "CeleryExecutor", "pod isolation", "startup latency", "Celery workers", "resource cleanup", "autoscaling"]
    }
  ],

  # de_streaming_realtime (9)
  "de_streaming_realtime.kafka_architecture_topics_partitions": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain how Kafka topic partitions enable consumer parallelization and ordering guarantees.",
      "expected_answer_keywords": ["partition", "ordering within partition", "consumer parallelization", "message key", "hash partitioning", "offset"]
    }
  ],
  "de_streaming_realtime.producer_consumer_consumer_groups": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "What happens when a new consumer joins an active Kafka consumer group, and how does CooperativeSticky rebalance reduce stop-the-world pauses?",
      "expected_answer_keywords": ["consumer group rebalance", "CooperativeSticky", "incremental rebalance", "partition assignment", "stop-the-world"]
    }
  ],
  "de_streaming_realtime.kafka_schema_registry_avro_protobuf": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does Confluent Schema Registry enforce BACKWARD and FULL compatibility rules on evolving Avro event payloads?",
      "expected_answer_keywords": ["Schema Registry", "BACKWARD compatibility", "FULL compatibility", "default values", "schema evolution", "Avro schema"]
    }
  ],
  "de_streaming_realtime.kafka_streams_ksqldb": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is the duality between KStream and KTable in Kafka Streams, and how are changelogs maintained?",
      "expected_answer_keywords": ["KStream", "KTable", "stream table duality", "changelog topic", "state store", "RocksDB", "upsert semantics"]
    }
  ],
  "de_streaming_realtime.apache_flink_stream_processing": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does Apache Flink maintain managed operator state (ValueState, ListState) across millions of keyed stream keys?",
      "expected_answer_keywords": ["Flink", "ValueState", "keyed stream", "StateTtlConfig", "RocksDB state backend", "checkpointing", "heap vs off-heap"]
    }
  ],
  "de_streaming_realtime.event_time_watermarks_late_data": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do watermarks handle out-of-order event streams, and how do you capture late-arriving events using Flink Side Outputs?",
      "expected_answer_keywords": ["watermark", "event time", "bounded out-of-orderness", "side output", "allowed lateness", "late event handling"]
    }
  ],
  "de_streaming_realtime.windowing_tumbling_sliding_session": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Compare Tumbling Windows, Sliding Windows, and Session Windows with concrete streaming use cases for each.",
      "expected_answer_keywords": ["tumbling window", "sliding window", "session window", "inactivity gap", "overlapping window", "aggregation"]
    }
  ],
  "de_streaming_realtime.exactly_once_semantics_transactions": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do Flink and Kafka achieve end-to-end Exactly-Once Semantics (EOS) using the Two-Phase Commit (2PC) protocol?",
      "expected_answer_keywords": ["Two-Phase Commit", "2PC", "Kafka transaction", "Exactly-Once", "pre-commit", "commit", "checkpoint barrier", "EOS"]
    }
  ],
  "de_streaming_realtime.stream_state_backends_checkpointing": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain how the Chandy-Lamport algorithm enables non-blocking distributed checkpointing in Apache Flink.",
      "expected_answer_keywords": ["Chandy-Lamport", "checkpoint barrier", "non-blocking", "RocksDB", "snapshot", "unaligned checkpoints", "state recovery"]
    }
  ],

  # de_data_modeling_transformation (9)
  "de_data_modeling_transformation.dbt_models_ref_source": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does dbt use the ref() function to build automatic DAG dependency graphs between models?",
      "expected_answer_keywords": ["ref()", "source()", "DAG lineage", "topological order", "dependency resolution", "dbt run"]
    }
  ],
  "de_data_modeling_transformation.dbt_jinja_macros_packages": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Write a Jinja macro in dbt to dynamically pivot payment methods from a column into separate aggregated sum columns.",
      "expected_answer_keywords": ["macro", "Jinja", "for loop", "{% macro %}", "dbt_utils.pivot", "dynamic SQL", "SUM(CASE)"]
    }
  ],
  "de_data_modeling_transformation.dbt_materializations_incremental": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does dbt incremental materialization work using the is_incremental() macro and unique_key merge strategy?",
      "expected_answer_keywords": ["is_incremental()", "incremental", "unique_key", "merge", "lookback window", "WHERE _loaded_at > max(_loaded_at)"]
    }
  ],
  "de_data_modeling_transformation.dbt_testing_generic_singular": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What are the four built-in generic schema tests in dbt, and when should you write a singular SQL test?",
      "expected_answer_keywords": ["unique", "not_null", "accepted_values", "relationships", "singular test", "custom business rule"]
    }
  ],
  "de_data_modeling_transformation.dbt_snapshots_scd": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do dbt snapshots automatically implement SCD Type 2 tables using the timestamp and check strategies?",
      "expected_answer_keywords": ["dbt snapshot", "SCD Type 2", "strategy='timestamp'", "strategy='check'", "dbt_valid_from", "dbt_valid_to", "check_cols"]
    }
  ],
  "de_data_modeling_transformation.dbt_documentation_lineage": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does dbt generate documentation and interactive lineage graphs from doc blocks in schema.yml files?",
      "expected_answer_keywords": ["dbt docs generate", "schema.yml", "doc blocks", "lineage graph", "catalog.json", "manifest.json"]
    }
  ],
  "de_data_modeling_transformation.sqlmesh_alternative_engines": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "How does SQLMesh's Virtual Data Environments and automated plan evaluation improve upon traditional dbt CI/CD workflows?",
      "expected_answer_keywords": ["SQLMesh", "Virtual Data Environments", "sqlmesh plan", "column-level lineage", "zero-copy promotion", "cost evaluation"]
    }
  ],
  "de_data_modeling_transformation.modular_data_transformation_pipelines": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Explain the architectural separation of Staging, Intermediate, and Marts layers in modern dbt modeling.",
      "expected_answer_keywords": ["staging layer", "intermediate layer", "marts layer", "clean separation", "business logic encapsulation", "DRY"]
    }
  ],
  "de_data_modeling_transformation.dbt_semantic_layer_metrics": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you define semantic models, measures, and dimensions in MetricFlow / dbt Semantic Layer for cross-tool BI consistency?",
      "expected_answer_keywords": ["semantic_models", "MetricFlow", "measures", "dimensions", "entities", "dbt Semantic Layer", "consistent metrics"]
    }
  ],

  # de_data_quality_governance (9)
  "de_data_quality_governance.data_validation_great_expectations_soda": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you define Expectation Suites in Great Expectations and block downstream pipeline execution upon validation failure?",
      "expected_answer_keywords": ["Expectation Suite", "Checkpoint", "Great Expectations", "action_list", "Data Docs", "assertion gate", "validation"]
    }
  ],
  "de_data_quality_governance.data_profiling_anomaly_detection": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do statistical data profiling and volume anomaly detection flag silent data pipeline failures (e.g. 90% row drop)?",
      "expected_answer_keywords": ["volume anomaly", "statistical profiling", "missingness", "distribution drift", "row count check", "silent failure"]
    }
  ],
  "de_data_quality_governance.data_lineage_metadata_openlineage": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does the OpenLineage standard collect runtime dataset and job run facets across Airflow, Spark, and dbt?",
      "expected_answer_keywords": ["OpenLineage", "Marquez", "lineage facets", "dataset lineage", "job run event", "metadata standard"]
    }
  ],
  "de_data_quality_governance.data_catalog_amundsen_datahub": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What are the core capabilities of enterprise metadata catalogs like DataHub and Amundsen for data discovery and governance?",
      "expected_answer_keywords": ["DataHub", "Amundsen", "data catalog", "metadata harvesting", "business glossary", "data ownership", "search discovery"]
    }
  ],
  "de_data_quality_governance.data_observability_montecarl_metaplane": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "Explain the five pillars of Data Observability (Freshness, Volume, Distribution, Schema, Lineage) and how they reduce data downtime.",
      "expected_answer_keywords": ["Freshness", "Volume", "Distribution", "Schema", "Lineage", "five pillars", "data observability", "data downtime", "Monte Carlo"]
    }
  ],
  "de_data_quality_governance.data_contract_schemas_enforcement": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do Data Contracts prevent upstream backend application migrations from breaking downstream analytical data pipelines?",
      "expected_answer_keywords": ["Data Contract", "producer-consumer agreement", "schema enforcement", "breaking change prevention", "CI validation", "SLA"]
    }
  ],
  "de_data_quality_governance.gdpr_pii_anonymization_masking": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you implement dynamic data masking and salted cryptographic hashing to anonymize PII for GDPR compliance?",
      "expected_answer_keywords": ["GDPR", "PII masking", "dynamic data masking", "salt hashing", "SHA-256", "pseudonymization", "tokenization"]
    }
  ],
  "de_data_quality_governance.data_access_rbac_abac_policies": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How do Row-Level Security (RLS) and Attribute-Based Access Control (ABAC) restrict analytical data access by user department or region?",
      "expected_answer_keywords": ["Row-Level Security", "RLS", "ABAC", "RBAC", "column masking policy", "least privilege", "access governance"]
    }
  ],
  "de_data_quality_governance.data_retention_archival_policies": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is establishing automated data retention and cold storage archival lifecycles critical for compliance and cost control?",
      "expected_answer_keywords": ["data retention", "archival lifecycle", "cold storage", "purge policy", "compliance", "cost reduction", "S3 Glacier"]
    }
  ],

  # de_cloud_infrastructure_dataops (9)
  "de_cloud_infrastructure_dataops.cloud_iam_service_accounts_security": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure least-privilege IAM roles and assume-role policies for Airflow / Spark jobs reading from S3 or GCS?",
      "expected_answer_keywords": ["least privilege", "IAM role", "assume role", "service account", "Secrets Manager", "bucket policy", "temporary credentials"]
    }
  ],
  "de_cloud_infrastructure_dataops.terraform_iac_data_infrastructure": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you structure reusable Terraform modules to provision Snowflake warehouses, S3 lakehouse buckets, and Kafka clusters?",
      "expected_answer_keywords": ["Terraform", "IaC", "Terraform modules", "remote state", "HCL", "variables", "outputs", "state management"]
    }
  ],
  "de_cloud_infrastructure_dataops.docker_containers_for_data": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you write a multi-stage Dockerfile for a Python/dbt application running as a secure non-root user?",
      "expected_answer_keywords": ["Dockerfile", "multi-stage build", "non-root user", "USER appuser", "slim image", "build stage", "layer caching"]
    }
  ],
  "de_cloud_infrastructure_dataops.kubernetes_data_workloads": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you deploy Apache Spark on Kubernetes using the Spark Operator with dynamic pod allocation and Spot instances?",
      "expected_answer_keywords": ["Spark on K8s", "SparkOperator", "CRD", "spot instances", "node affinity", "tolerations", "driver pod", "executor pod"]
    }
  ],
  "de_cloud_infrastructure_dataops.ci_cd_pipelines_for_data_github_actions": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you design a GitHub Actions CI pipeline that lints SQL with sqlfluff, runs pytest, and triggers dbt slim CI on modified models?",
      "expected_answer_keywords": ["GitHub Actions", "sqlfluff", "pytest", "dbt slim CI", "state:modified+", "manifest.json comparison", "CI/CD"]
    }
  ],
  "de_cloud_infrastructure_dataops.unit_integration_testing_data_pipelines": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you use pytest, fixtures, and Moto/Testcontainers to unit and integration test data pipeline transformations without hitting live databases?",
      "expected_answer_keywords": ["pytest", "Testcontainers", "moto", "fixtures", "mocking", "integration testing", "in-memory database"]
    }
  ],
  "de_cloud_infrastructure_dataops.data_mocking_synthetic_generation": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How do you generate realistic, referentially intact synthetic test datasets using Python Faker and seed values?",
      "expected_answer_keywords": ["Faker", "synthetic data", "seed value", "deterministic", "referential integrity", "mock datasets"]
    }
  ],
  "de_cloud_infrastructure_dataops.cloud_cost_governance_finops": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you establish FinOps tagging policies, identify zombie compute clusters, and implement auto-scaling to optimize cloud data spend?",
      "expected_answer_keywords": ["FinOps", "cost allocation tags", "zombie clusters", "auto-termination", "spot instances", "cost governance", "AWS Cost Explorer"]
    }
  ],
  "de_cloud_infrastructure_dataops.disaster_recovery_backup_data_systems": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you design a multi-region disaster recovery and Point-In-Time Recovery (PITR) strategy for an enterprise data platform to satisfy RTO and RPO targets?",
      "expected_answer_keywords": ["Disaster Recovery", "PITR", "RTO", "RPO", "cross-region replication", "failover runbook", "backup strategy"]
    }
  ]
}

assessment_data = {
  "source_id": "assessment",
  "name": "Data Engineering Adaptive Technical Assessment",
  "description": "Comprehensive technical question bank and adaptive testing engine for evaluating Data Engineer candidate proficiency across all 91 composite subskills.",
  "trigger_conditions": {
    "rules": [
      "When a subskill has status 'not_yet_evidenced' (confidence = 0.0) for a target role level",
      "When a subskill has status 'insufficient_evidence' and confidence < 0.4",
      "When CV/LinkedIn claims a skill but GitHub code has no supporting implementation",
      "When a skill is critical for the target role (importance >= 0.80) and evidence is ambiguous"
    ]
  },
  "question_types": [
    { "type": "conceptual", "strength": 0.6, "description": "Tests deep theoretical and architectural understanding." },
    { "type": "scenario", "strength": 0.8, "description": "Tests practical problem-solving and production troubleshooting." },
    { "type": "practical_task", "strength": 1.0, "description": "Hands-on implementation task validating production code." }
  ],
  "sample_questions_by_composite_key": questions_by_key
}

with open(os.path.join(evidence_dir, 'assessment.json'), 'w', encoding='utf-8') as f:
  json.dump(assessment_data, f, indent=2)

print(f"Generated complete evidence files in {evidence_dir}")
print(f"Total questions mapped in assessment.json: {len(questions_by_key)}")
