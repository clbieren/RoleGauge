import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'mlops')
evidence_dir = os.path.join(base_dir, 'evidence', 'mlops')
roles_dir = os.path.join(base_dir, 'roles', 'mlops')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

skills = {}

# 1. mlops_lifecycle_governance
skills["mlops_lifecycle_governance"] = {
  "skill_id": "mlops_lifecycle_governance",
  "name": "MLOps Lifecycle, Maturity & Governance",
  "category": "governance",
  "description": "MLOps maturity levels (Level 0 Manual to Level 2 Automated CI/CD/CT), Model Governance, Model Cards, training reproducibility, audit trails, ethical gates, and regulatory compliance.",
  "subskills": [
    {
      "id": "mlops_maturity_levels_0_to_2",
      "name": "MLOps Maturity Framework (Levels 0, 1, 2)",
      "description": "Google MLOps maturity model: Level 0 (manual workflow), Level 1 (automated ML pipeline / CT), Level 2 (CI/CD pipeline automated deployment).",
      "keywords": ["MLOps maturity", "Level 0", "Level 1", "Level 2", "manual workflow", "automated pipeline", "CI/CD/CT automation", "Google MLOps"]
    },
    {
      "id": "model_cards_standardized_documentation",
      "name": "Model Cards & Standardized Documentation",
      "description": "Authoring standardized Model Cards: model details, intended use, factors, evaluation datasets, quantitative metrics, and ethical considerations.",
      "keywords": ["Model Card", "documentation", "intended use", "limitations", "evaluation metrics", "training data provenance", "ethical considerations"]
    },
    {
      "id": "model_lineage_data_code_provenance",
      "name": "End-to-End Model Lineage & Provenance Tracking",
      "description": "Tracing deployed model binary back to exact Git commit hash, DVC dataset hash, training environment parameters, and container image digest.",
      "keywords": ["model lineage", "data provenance", "Git commit hash", "DVC hash", "container digest", "reproducibility", "audit trail"]
    },
    {
      "id": "model_governance_approval_workflows",
      "name": "Model Governance, Review & Approval Gates",
      "description": "Role-based model approval gates before production promotion (Data Scientist -> ML Engineer -> Risk/Compliance Officer sign-off).",
      "keywords": ["model governance", "approval gate", "promotion workflow", "compliance sign-off", "risk review", "RBAC model access", "stage transition"]
    },
    {
      "id": "ethical_ai_fairness_compliance_gates",
      "name": "Ethical AI, Bias Auditing & Compliance Gates",
      "description": "Enforcing automated bias and fairness gates in CI/CD (disparate impact, equalized odds) using Fairlearn / AIF360 before model release.",
      "keywords": ["bias gate", "fairness check", "disparate impact", "Equalized Odds", "Fairlearn", "AIF360", "compliance gate", "automated audit"]
    },
    {
      "id": "model_catalog_metadata_management",
      "name": "Enterprise Model Catalog & Metadata Management",
      "description": "Centralizing model catalog assets in DataHub / MLflow, tracking model status, owners, input/output schemas, and SLAs across business units.",
      "keywords": ["model catalog", "metadata management", "DataHub", "MLflow catalog", "schema definition", "asset tracking", "business ownership"]
    },
    {
      "id": "training_reproducibility_seed_environments",
      "name": "Deterministic Training & Environment Isolation",
      "description": "Ensuring bitwise training reproducibility: setting global random seeds (PyTorch/CUDA/NumPy), pinning dependencies, and deterministic CUDA ops.",
      "keywords": ["reproducibility", "random seed", "torch.use_deterministic_algorithms", "CUDA determinism", "pinned environment", "seedWorker"]
    },
    {
      "id": "regulatory_compliance_ai_act_gdpr",
      "name": "Regulatory Compliance (EU AI Act, GDPR, HIPAA)",
      "description": "High-risk AI system compliance, Right to Explanation under GDPR, model auditing, data residency, and algorithmic impact assessments.",
      "keywords": ["EU AI Act", "GDPR", "HIPAA", "Right to Explanation", "high-risk AI", "impact assessment", "regulatory audit", "data residency"]
    },
    {
      "id": "incident_postmortem_model_failure_runbooks",
      "name": "Model Incident Response & Post-Mortem Runbooks",
      "description": "Authoring post-mortem runbooks for silent model failure, feedback loops, data corruption, and establishing emergency rollback procedures.",
      "keywords": ["post-mortem", "runbook", "incident response", "silent failure", "feedback loop", "emergency rollback", "circuit breaker", "SRE for ML"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Established enterprise MLOps governance, standardized Model Cards, and automated compliance gates",
        "strength": 0.5,
        "maps_to": ["mlops_lifecycle_governance.model_cards_standardized_documentation", "mlops_lifecycle_governance.model_governance_approval_workflows", "mlops_lifecycle_governance.model_lineage_data_code_provenance"]
      }
    ],
    "linkedin": [
      {
        "signal": "MLOps Governance, Model Management, and AI Compliance endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_lifecycle_governance.mlops_maturity_levels_0_to_2", "mlops_lifecycle_governance.ethical_ai_fairness_compliance_gates"]
      }
    ],
    "github": [
      {
        "pattern": "*model_card*.md|governance/**/*.py|compliance/**/*.yml",
        "strength": 1.0,
        "maps_to": [
          "mlops_lifecycle_governance.mlops_maturity_levels_0_to_2",
          "mlops_lifecycle_governance.model_cards_standardized_documentation",
          "mlops_lifecycle_governance.model_lineage_data_code_provenance",
          "mlops_lifecycle_governance.model_governance_approval_workflows",
          "mlops_lifecycle_governance.ethical_ai_fairness_compliance_gates",
          "mlops_lifecycle_governance.model_catalog_metadata_management",
          "mlops_lifecycle_governance.training_reproducibility_seed_environments",
          "mlops_lifecycle_governance.regulatory_compliance_ai_act_gdpr",
          "mlops_lifecycle_governance.incident_postmortem_model_failure_runbooks"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes MLOps Lifecycle, Maturity & Governance Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_lifecycle_governance.mlops_maturity_levels_0_to_2",
          "mlops_lifecycle_governance.model_cards_standardized_documentation",
          "mlops_lifecycle_governance.model_lineage_data_code_provenance",
          "mlops_lifecycle_governance.model_governance_approval_workflows",
          "mlops_lifecycle_governance.ethical_ai_fairness_compliance_gates",
          "mlops_lifecycle_governance.model_catalog_metadata_management",
          "mlops_lifecycle_governance.training_reproducibility_seed_environments",
          "mlops_lifecycle_governance.regulatory_compliance_ai_act_gdpr",
          "mlops_lifecycle_governance.incident_postmortem_model_failure_runbooks"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["mlops_maturity_levels_0_to_2", "model_cards_standardized_documentation", "training_reproducibility_seed_environments"],
      "description": "Understands MLOps maturity stages, authors standardized Model Cards, and sets up deterministic seed environments."
    },
    "mid": {
      "expected_subskills": ["model_lineage_data_code_provenance", "model_governance_approval_workflows", "ethical_ai_fairness_compliance_gates", "model_catalog_metadata_management"],
      "description": "Tracks full model lineage from data to binary, enforces CI/CD fairness gates, and integrates assets into enterprise model catalogs."
    },
    "senior": {
      "expected_subskills": ["regulatory_compliance_ai_act_gdpr", "incident_postmortem_model_failure_runbooks"],
      "description": "Architects EU AI Act/GDPR regulatory compliance frameworks, establishes model risk runbooks, and drives enterprise MLOps transformation."
    }
  }
}

# 2. mlops_experiment_tracking_registry
skills["mlops_experiment_tracking_registry"] = {
  "skill_id": "mlops_experiment_tracking_registry",
  "name": "Experiment Tracking & Model Registry Platforms",
  "category": "experimentation",
  "description": "Logging parameters, metrics, and artifacts across distributed runs (MLflow, Weights & Biases, Comet), model signatures, Model Registry versioning, and stage transition workflows.",
  "subskills": [
    {
      "id": "mlflow_tracking_server_backend_setup",
      "name": "MLflow Tracking Server & Remote Backend Architecture",
      "description": "Configuring central MLflow Tracking Server with PostgreSQL backend store and S3/GCS artifact root, authentication, and team tenancy.",
      "keywords": ["MLflow server", "backend-store-uri", "default-artifact-root", "PostgreSQL backend", "S3 artifact store", "MLflow tracking", "multi-tenancy"]
    },
    {
      "id": "experiment_run_logging_artifacts",
      "name": "Experiment Logging (Parameters, Metrics, Artifacts)",
      "description": "mlflow.start_run(), mlflow.log_params(), mlflow.log_metrics() with step history, autologging (PyTorch, Scikit-Learn, XGBoost), and artifact upload.",
      "keywords": ["mlflow.log_params", "mlflow.log_metrics", "mlflow.autolog", "mlflow.log_artifact", "nested runs", "step metrics", "run tags"]
    },
    {
      "id": "model_signatures_input_schemas",
      "name": "Model Signatures, Input Examples & Schemas",
      "description": "Enforcing MLflow model signatures (ColSpec, TensorSpec), input examples, schema validation, and preventing training-serving signature mismatches.",
      "keywords": ["infer_signature", "ModelSignature", "ColSpec", "TensorSpec", "input_example", "schema validation", "type checking"]
    },
    {
      "id": "mlflow_model_registry_lifecycle",
      "name": "MLflow Model Registry & Stage Transitions",
      "description": "Registering models, semantic versioning, stage transitions (None -> Staging -> Production -> Archived), aliases, and model tags.",
      "keywords": ["Model Registry", "mlflow.register_model", "stage transition", "Production stage", "Staging stage", "model version", "model alias"]
    },
    {
      "id": "weights_biases_experiment_sweeps",
      "name": "Weights & Biases (W&B) Dashboarding & Sweeps",
      "description": "Setting up W&B projects, wandb.init(), wandb.log(), running Bayesian hyperparameter sweeps via sweep.yaml, and team workspaces.",
      "keywords": ["Weights & Biases", "wandb.init", "wandb.log", "wandb sweep", "sweep.yaml", "W&B dashboard", "run comparison"]
    },
    {
      "id": "custom_mlflow_pyfunc_wrappers",
      "name": "Custom MLflow PyFunc Wrapper Modeling",
      "description": "Subclassing mlflow.pyfunc.PythonModel, implementing load_context() and predict(), packaging pre/post-processing logic into self-contained models.",
      "keywords": ["PythonModel", "mlflow.pyfunc", "load_context", "predict", "custom pyfunc", "pre-processing wrapper", "self-contained model"]
    },
    {
      "id": "artifact_storage_retention_lifecycle",
      "name": "Artifact Storage Optimization & Retention Policies",
      "description": "Managing terabytes of checkpoint artifacts, S3 lifecycle rules for old runs, deduplication, and automated artifact pruning.",
      "keywords": ["artifact retention", "S3 lifecycle", "checkpoint pruning", "storage optimization", "artifact cleanup", "disk quota"]
    },
    {
      "id": "model_registry_webhook_automation",
      "name": "Model Registry Webhooks & CI/CD Integration",
      "description": "Configuring MLflow webhooks on model transition events to trigger automated GitHub Actions / Jenkins deployment pipelines.",
      "keywords": ["MLflow webhook", "registry webhook", "event trigger", "model promotion event", "CI/CD trigger", "automated deployment"]
    },
    {
      "id": "run_comparison_metric_diffing",
      "name": "Automated Run Comparison & Metric Diffing",
      "description": "Programmatic run querying using MLflow search_runs(), filtering top-performing models by metric thresholds, and automated leaderboards.",
      "keywords": ["mlflow.search_runs", "filter_string", "metric diffing", "run comparison", "automated leaderboard", "top model selection"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Designed enterprise MLflow Tracking & Model Registry infrastructure managing 500+ production models",
        "strength": 0.5,
        "maps_to": ["mlops_experiment_tracking_registry.mlflow_tracking_server_backend_setup", "mlops_experiment_tracking_registry.mlflow_model_registry_lifecycle", "mlops_experiment_tracking_registry.custom_mlflow_pyfunc_wrappers"]
      }
    ],
    "linkedin": [
      {
        "signal": "MLflow, Weights & Biases, and Experiment Tracking specialist endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_experiment_tracking_registry.experiment_run_logging_artifacts", "mlops_experiment_tracking_registry.weights_biases_experiment_sweeps"]
      }
    ],
    "github": [
      {
        "pattern": "*mlflow*|*wandb*|mlflow.yaml|sweep.yaml|tracking/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "mlops_experiment_tracking_registry.mlflow_tracking_server_backend_setup",
          "mlops_experiment_tracking_registry.experiment_run_logging_artifacts",
          "mlops_experiment_tracking_registry.model_signatures_input_schemas",
          "mlops_experiment_tracking_registry.mlflow_model_registry_lifecycle",
          "mlops_experiment_tracking_registry.weights_biases_experiment_sweeps",
          "mlops_experiment_tracking_registry.custom_mlflow_pyfunc_wrappers",
          "mlops_experiment_tracking_registry.artifact_storage_retention_lifecycle",
          "mlops_experiment_tracking_registry.model_registry_webhook_automation",
          "mlops_experiment_tracking_registry.run_comparison_metric_diffing"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Experiment Tracking & Model Registry Platforms Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_experiment_tracking_registry.mlflow_tracking_server_backend_setup",
          "mlops_experiment_tracking_registry.experiment_run_logging_artifacts",
          "mlops_experiment_tracking_registry.model_signatures_input_schemas",
          "mlops_experiment_tracking_registry.mlflow_model_registry_lifecycle",
          "mlops_experiment_tracking_registry.weights_biases_experiment_sweeps",
          "mlops_experiment_tracking_registry.custom_mlflow_pyfunc_wrappers",
          "mlops_experiment_tracking_registry.artifact_storage_retention_lifecycle",
          "mlops_experiment_tracking_registry.model_registry_webhook_automation",
          "mlops_experiment_tracking_registry.run_comparison_metric_diffing"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["experiment_run_logging_artifacts", "model_signatures_input_schemas", "weights_biases_experiment_sweeps"],
      "description": "Logs runs and parameters to MLflow/W&B, enforces input schemas/signatures, and configures experiment sweeps."
    },
    "mid": {
      "expected_subskills": ["mlflow_tracking_server_backend_setup", "mlflow_model_registry_lifecycle", "custom_mlflow_pyfunc_wrappers", "run_comparison_metric_diffing"],
      "description": "Provisions MLflow tracking servers, manages Model Registry stage lifecycles, and authors custom PyFunc model wrappers."
    },
    "senior": {
      "expected_subskills": ["artifact_storage_retention_lifecycle", "model_registry_webhook_automation"],
      "description": "Architects enterprise model registry automation with webhooks, CI/CD promotion pipelines, and global artifact retention governance."
    }
  }
}

# 3. mlops_data_feature_management
skills["mlops_data_feature_management"] = {
  "skill_id": "mlops_data_feature_management",
  "name": "Feature Stores & Data Versioning (Feast / DVC)",
  "category": "data_management",
  "description": "Feature store architecture (Feast, Hopsworks), online/offline stores, point-in-time correctness, feature views, Data Version Control (DVC), dataset lineage, and preventing training-serving skew.",
  "subskills": [
    {
      "id": "feast_feature_store_architecture",
      "name": "Feast Feature Store Core Architecture",
      "description": "Configuring feature_store.yaml, Entity definitions, Feature Views, batch sources (Parquet/Snowflake/BigQuery), and Feast repository setup.",
      "keywords": ["Feast", "feature_store.yaml", "Entity", "FeatureView", "BatchSource", "feast apply", "feature repository"]
    },
    {
      "id": "point_in_time_correct_historical_joins",
      "name": "Point-in-Time Correct Historical Feature Joins",
      "description": "Time-travel joins in Feast (get_historical_features), preventing future data leakage, entity timestamps, and observation frames.",
      "keywords": ["point-in-time join", "time travel join", "get_historical_features", "data leakage prevention", "entity_df", "timestamp join"]
    },
    {
      "id": "online_feature_store_redis_dynamo",
      "name": "Online Feature Stores (Redis, DynamoDB) & Materialization",
      "description": "feast materialize, materialization intervals, ultra-low latency online feature retrieval with get_online_features(), and cache TTLs.",
      "keywords": ["feast materialize", "online store", "Redis", "DynamoDB", "get_online_features", "sub-millisecond retrieval", "feature cache"]
    },
    {
      "id": "on_demand_streaming_feature_views",
      "name": "On-Demand & Streaming Feature Transformations",
      "description": "OnDemandFeatureView with Python/Pandas logic, RequestSource transformations, and streaming ingestion from Kafka into Feast.",
      "keywords": ["OnDemandFeatureView", "RequestSource", "streaming feature view", "real-time transformation", "Kafka ingestion", "push source"]
    },
    {
      "id": "dvc_data_versioning_s3_gcs",
      "name": "Data Version Control (DVC) with S3/GCS Remotes",
      "description": "Initializing DVC, dvc add, dvc remote add s3, tracking large training datasets, .dvc files in Git, and dvc push/pull.",
      "keywords": ["DVC", "dvc add", "dvc remote", "dvc push", "dvc pull", "S3 remote", ".dvc pointer", "dataset versioning"]
    },
    {
      "id": "dvc_pipeline_stages_dvc_yaml",
      "name": "DVC Pipelines & Reproducible Stages (dvc.yaml)",
      "description": "Authoring dvc.yaml with deps, outs, params, and metrics, building reproducible dependency graphs with dvc repro.",
      "keywords": ["dvc.yaml", "dvc repro", "pipeline stages", "deps", "outs", "params.yaml", "dvc metrics", "reproducible pipeline"]
    },
    {
      "id": "training_serving_feature_skew_mitigation",
      "name": "Training-Serving Feature Skew Mitigation",
      "description": "Ensuring identical transformation code between training and inference paths, shared feature definitions, and drift monitoring.",
      "keywords": ["training-serving skew", "shared transformation", "consistency", "feature parity", "skew detection", "feature store contract"]
    },
    {
      "id": "hopsworks_feature_store_enterprise",
      "name": "Enterprise Feature Stores (Hopsworks, Tecton)",
      "description": "Enterprise feature store features: feature sharing across teams, access control, automated feature monitoring, and pipeline orchestration.",
      "keywords": ["Hopsworks", "Tecton", "enterprise feature store", "feature catalog", "feature sharing", "access control", "feature monitoring"]
    },
    {
      "id": "dataset_checksums_immutability_archival",
      "name": "Dataset Checksums, Immutability & Archival",
      "description": "Cryptographic dataset hashing (SHA-256), immutable S3 object locks, dataset lifecycle archival, and compliance auditing.",
      "keywords": ["dataset checksum", "SHA-256 hash", "immutable dataset", "S3 Object Lock", "dataset archival", "compliance audit"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Architected enterprise Feast Feature Store and DVC data pipelines eliminating training-serving skew",
        "strength": 0.5,
        "maps_to": ["mlops_data_feature_management.feast_feature_store_architecture", "mlops_data_feature_management.point_in_time_correct_historical_joins", "mlops_data_feature_management.training_serving_feature_skew_mitigation"]
      }
    ],
    "linkedin": [
      {
        "signal": "Feature Stores, Feast, DVC, and Data Management endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_data_feature_management.online_feature_store_redis_dynamo", "mlops_data_feature_management.dvc_data_versioning_s3_gcs"]
      }
    ],
    "github": [
      {
        "pattern": "feature_store.yaml|dvc.yaml|.dvc|features/**/*.py|dvc.lock",
        "strength": 1.0,
        "maps_to": [
          "mlops_data_feature_management.feast_feature_store_architecture",
          "mlops_data_feature_management.point_in_time_correct_historical_joins",
          "mlops_data_feature_management.online_feature_store_redis_dynamo",
          "mlops_data_feature_management.on_demand_streaming_feature_views",
          "mlops_data_feature_management.dvc_data_versioning_s3_gcs",
          "mlops_data_feature_management.dvc_pipeline_stages_dvc_yaml",
          "mlops_data_feature_management.training_serving_feature_skew_mitigation",
          "mlops_data_feature_management.hopsworks_feature_store_enterprise",
          "mlops_data_feature_management.dataset_checksums_immutability_archival"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Feature Stores & Data Versioning Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_data_feature_management.feast_feature_store_architecture",
          "mlops_data_feature_management.point_in_time_correct_historical_joins",
          "mlops_data_feature_management.online_feature_store_redis_dynamo",
          "mlops_data_feature_management.on_demand_streaming_feature_views",
          "mlops_data_feature_management.dvc_data_versioning_s3_gcs",
          "mlops_data_feature_management.dvc_pipeline_stages_dvc_yaml",
          "mlops_data_feature_management.training_serving_feature_skew_mitigation",
          "mlops_data_feature_management.hopsworks_feature_store_enterprise",
          "mlops_data_feature_management.dataset_checksums_immutability_archival"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["feast_feature_store_architecture", "dvc_data_versioning_s3_gcs", "dvc_pipeline_stages_dvc_yaml"],
      "description": "Defines basic Feast feature views, tracks dataset versions with DVC, and authors reproducible dvc.yaml pipelines."
    },
    "mid": {
      "expected_subskills": ["point_in_time_correct_historical_joins", "online_feature_store_redis_dynamo", "on_demand_streaming_feature_views", "training_serving_feature_skew_mitigation"],
      "description": "Executes point-in-time correct historical joins, materializes online Redis feature caches, and eliminates training-serving skew."
    },
    "senior": {
      "expected_subskills": ["hopsworks_feature_store_enterprise", "dataset_checksums_immutability_archival"],
      "description": "Architects enterprise multi-tenant feature store platforms, implements streaming Kafka feature views, and governs dataset immutability."
    }
  }
}

# 4. mlops_pipeline_orchestration
skills["mlops_pipeline_orchestration"] = {
  "skill_id": "mlops_pipeline_orchestration",
  "name": "ML Pipeline Orchestration (Kubeflow, Flyte, Argo)",
  "category": "orchestration",
  "description": "Workflow scheduling and orchestration for ML pipelines: Kubeflow Pipelines (KFP v2), Flyte, Argo Workflows, Metaflow, containerized components, caching, GPU node selectors, and fault tolerance.",
  "subskills": [
    {
      "id": "kubeflow_pipelines_kfp_v2_dsl",
      "name": "Kubeflow Pipelines (KFP v2) & @dsl Component Authoring",
      "description": "Authoring KFP v2 pipelines with @dsl.component, @dsl.pipeline, container_component, passing Input/Output artifacts, and pipeline compilation.",
      "keywords": ["Kubeflow", "KFP v2", "@dsl.component", "@dsl.pipeline", "kfp.compiler", "pipeline.yaml", "Input[Artifact]", "Output[Model]"]
    },
    {
      "id": "flyte_orchestration_type_safety",
      "name": "Flyte Type-Safe Workflow Orchestration",
      "description": "Flyte tasks (@task) and workflows (@workflow), strong type checking, FlyteFile/FlyteDirectory, dynamic workflows, and Flytekit SDK.",
      "keywords": ["Flyte", "@task", "@workflow", "Flytekit", "FlyteDirectory", "FlyteFile", "dynamic workflow", "type safety"]
    },
    {
      "id": "argo_workflows_declarative_k8s",
      "name": "Argo Workflows Declarative YAML Pipelines",
      "description": "Kubernetes CRD-based workflow orchestration, Argo WorkflowTemplate, steps, DAG templates, volume mounts, and artifact repositories.",
      "keywords": ["Argo Workflows", "WorkflowTemplate", "DAG template", "CRD", "Argo CLI", "argo submit", "artifact repository", "K8s native"]
    },
    {
      "id": "pipeline_step_caching_memoization",
      "name": "Pipeline Step Caching & Memoization",
      "description": "Configuring step memoization keys in KFP / Flyte, reusing cached outputs for unchanged steps, and speeding up pipeline iterations.",
      "keywords": ["caching", "memoization", "enable_caching", "cache_key", "reusable step output", "skip redundant compute"]
    },
    {
      "id": "gpu_resource_allocation_node_affinity",
      "name": "GPU Resource Allocation & Node Affinity in Pipelines",
      "description": "Setting container resource requests/limits (nvidia.com/gpu: 1), tolerations for tainted GPU nodes, and nodeAffinity selectors in pipeline tasks.",
      "keywords": ["nvidia.com/gpu", "nodeAffinity", "tolerations", "taints", "resource limits", "GPU scheduling", "k8s node selector"]
    },
    {
      "id": "airflow_for_ml_operators_sensors",
      "name": "Apache Airflow for ML Orchestration & Providers",
      "description": "Airflow providers (Astronomer Cosmos for dbt/ML, Amazon SageMaker operators, Google Vertex AI operators), and triggering external ML training jobs.",
      "keywords": ["Airflow for ML", "SageMakerOperator", "VertexAIOperator", "Astronomer Cosmos", "trigger ML job", "Airflow DAG for ML"]
    },
    {
      "id": "pipeline_error_handling_retry_policies",
      "name": "Pipeline Error Handling, Retries & Fallbacks",
      "description": "Configuring task retry policies, exponential backoff, on_exit handler steps for cleanup, and alerting notifications upon pipeline failures.",
      "keywords": ["retry policy", "exponential backoff", "on_exit handler", "cleanup task", "pipeline error handling", "failure alerting"]
    },
    {
      "id": "distributed_training_operators_k8s_kubeflow",
      "name": "Kubeflow Training Operator (PyTorchJob, TFJob)",
      "description": "Deploying PyTorchJob and TFJob Custom Resources for multi-node distributed training, master/worker pods, and gang scheduling with Volcano.",
      "keywords": ["Training Operator", "PyTorchJob", "TFJob", "Kubeflow Training", "multi-node distributed training", "gang scheduling", "Volcano"]
    },
    {
      "id": "metaflow_production_deployments_argo",
      "name": "Metaflow Deployment to Argo Workflows / AWS Step Functions",
      "description": "Compiling Metaflow workflows to Argo Workflows (metaflow argo-workflows create) or AWS Step Functions for scheduled production execution.",
      "keywords": ["Metaflow", "argo-workflows create", "AWS Step Functions", "production scheduler", "FlowSpec export", "seamless deployment"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Engineered distributed ML pipelines on Kubeflow Pipelines and Flyte with GPU dynamic scheduling and step caching",
        "strength": 0.5,
        "maps_to": ["mlops_pipeline_orchestration.kubeflow_pipelines_kfp_v2_dsl", "mlops_pipeline_orchestration.flyte_orchestration_type_safety", "mlops_pipeline_orchestration.gpu_resource_allocation_node_affinity"]
      }
    ],
    "linkedin": [
      {
        "signal": "Kubeflow, Flyte, and ML Pipeline Orchestration endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_pipeline_orchestration.argo_workflows_declarative_k8s", "mlops_pipeline_orchestration.airflow_for_ml_operators_sensors"]
      }
    ],
    "github": [
      {
        "pattern": "pipeline.yaml|*kfp*.py|*flyte*.py|argo/**/*.yml|workflows/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "mlops_pipeline_orchestration.kubeflow_pipelines_kfp_v2_dsl",
          "mlops_pipeline_orchestration.flyte_orchestration_type_safety",
          "mlops_pipeline_orchestration.argo_workflows_declarative_k8s",
          "mlops_pipeline_orchestration.pipeline_step_caching_memoization",
          "mlops_pipeline_orchestration.gpu_resource_allocation_node_affinity",
          "mlops_pipeline_orchestration.airflow_for_ml_operators_sensors",
          "mlops_pipeline_orchestration.pipeline_error_handling_retry_policies",
          "mlops_pipeline_orchestration.distributed_training_operators_k8s_kubeflow",
          "mlops_pipeline_orchestration.metaflow_production_deployments_argo"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes ML Pipeline Orchestration (Kubeflow, Flyte, Argo) Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_pipeline_orchestration.kubeflow_pipelines_kfp_v2_dsl",
          "mlops_pipeline_orchestration.flyte_orchestration_type_safety",
          "mlops_pipeline_orchestration.argo_workflows_declarative_k8s",
          "mlops_pipeline_orchestration.pipeline_step_caching_memoization",
          "mlops_pipeline_orchestration.gpu_resource_allocation_node_affinity",
          "mlops_pipeline_orchestration.airflow_for_ml_operators_sensors",
          "mlops_pipeline_orchestration.pipeline_error_handling_retry_policies",
          "mlops_pipeline_orchestration.distributed_training_operators_k8s_kubeflow",
          "mlops_pipeline_orchestration.metaflow_production_deployments_argo"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["kubeflow_pipelines_kfp_v2_dsl", "pipeline_step_caching_memoization", "airflow_for_ml_operators_sensors"],
      "description": "Authors basic KFP v2 pipelines with @dsl.component, configures step caching, and schedules runs via Airflow."
    },
    "mid": {
      "expected_subskills": ["flyte_orchestration_type_safety", "argo_workflows_declarative_k8s", "gpu_resource_allocation_node_affinity", "pipeline_error_handling_retry_policies"],
      "description": "Develops type-safe workflows in Flyte, writes Argo WorkflowTemplates, manages GPU node affinities, and implements retry policies."
    },
    "senior": {
      "expected_subskills": ["distributed_training_operators_k8s_kubeflow", "metaflow_production_deployments_argo"],
      "description": "Architects multi-node PyTorchJob training clusters with gang scheduling and compiles enterprise workflows to Argo / Step Functions."
    }
  }
}

# 5. mlops_model_packaging_containerization
skills["mlops_model_packaging_containerization"] = {
  "skill_id": "mlops_model_packaging_containerization",
  "name": "Model Packaging & GPU Containerization",
  "category": "packaging",
  "description": "Standardized model packaging formats, BentoML bento bundles, Triton model repository structure, Docker multi-stage GPU builds, CUDA driver compatibility, and ONNX/TorchScript artifacts.",
  "subskills": [
    {
      "id": "docker_multistage_gpu_builds",
      "name": "Multi-Stage Dockerfiles for CUDA/GPU Workloads",
      "description": "Building lean multi-stage GPU Docker containers with NVIDIA CUDA base images, non-root security, layer caching, and minimizing image footprint.",
      "keywords": ["Dockerfile", "multi-stage build", "nvidia/cuda", "devel vs runtime base", "non-root user", "layer caching", "slim image"]
    },
    {
      "id": "bentoml_model_packaging_framework",
      "name": "BentoML Model Packaging & Service Definitions",
      "description": "bentoml.Service, bentoml.models.save_model(), defining runners, BentoCloud deployment, bentofile.yaml specifications, and containerizing bentos.",
      "keywords": ["BentoML", "bentoml.Service", "bentofile.yaml", "bento build", "BentoCloud", "model runners", "bentoml.containerize"]
    },
    {
      "id": "triton_model_repository_configuration",
      "name": "Triton Model Repository Layout & config.pbtxt",
      "description": "Structuring Triton directory trees (model_name/1/model.onnx), writing config.pbtxt with input/output tensors, backend types, and versioning.",
      "keywords": ["Triton repository", "config.pbtxt", "model.onnx", "platform: onnxruntime_onnx", "max_batch_size", "input tensor shape", "output tensor shape"]
    },
    {
      "id": "onnx_torchscript_artifact_packaging",
      "name": "ONNX & TorchScript Serialization Standards",
      "description": "Exporting models to standardized ONNX/TorchScript formats with embedded metadata, dynamic shapes, and verifying parity against PyTorch baseline.",
      "keywords": ["ONNX export", "TorchScript", "torch.onnx.export", "dynamic shapes", "numerical parity test", "serialized artifact"]
    },
    {
      "id": "container_registry_vulnerability_scanning",
      "name": "Container Registry Security & Trivy Scanning",
      "description": "Pushing images to ECR/GCR/Harbor, scanning ML containers for CVE vulnerabilities with Trivy / Clair, and signing images with Cosign.",
      "keywords": ["Trivy", "CVE scan", "container security", "Cosign", "image signature", "Harbor", "ECR", "vulnerability patching"]
    },
    {
      "id": "conda_poetry_lockfile_pinning",
      "name": "Conda, Poetry & uv Hermetic Dependency Pinning",
      "description": "Hermetic dependency isolation: creating reproducible conda environment.yaml or poetry.lock / uv.lock files for exact build parity.",
      "keywords": ["poetry.lock", "uv.lock", "conda environment.yaml", "hermetic build", "dependency pinning", "deterministic environment"]
    },
    {
      "id": "nvidia_container_toolkit_cuda_compatibility",
      "name": "NVIDIA Container Toolkit & CUDA Driver Forward Compatibility",
      "description": "Configuring nvidia-container-runtime, CUDA driver vs toolkit compatibility matrices, and passing GPU capabilities (--gpus all).",
      "keywords": ["NVIDIA Container Toolkit", "nvidia-docker", "CUDA driver compatibility", "libnvidia-container", "--gpus all", "CUDA forward compatibility"]
    },
    {
      "id": "model_artifact_packaging_formats_safetensors",
      "name": "SafeTensors & Modern Weight Serialization",
      "description": "Using SafeTensors for zero-copy deserialization, preventing arbitrary code execution exploits inherent in Python pickle files.",
      "keywords": ["SafeTensors", "pickle vulnerability", "zero-copy deserialization", "safe weight serialization", "Hugging Face safetensors", "fast loading"]
    },
    {
      "id": "caching_wheel_compilation_speedups",
      "name": "BuildKit Cache Mounts & Wheel Pre-Compilation",
      "description": "Accelerating ML Docker builds using BuildKit --mount=type=cache for pip/apt and pre-building complex C++ wheels (flash-attn, vllm).",
      "keywords": ["BuildKit", "--mount=type=cache", "pip cache", "pre-compiled wheel", "flash-attn build", "Docker build optimization"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Built production GPU container images and BentoML services with zero-copy SafeTensors and Trivy security scanning",
        "strength": 0.5,
        "maps_to": ["mlops_model_packaging_containerization.docker_multistage_gpu_builds", "mlops_model_packaging_containerization.bentoml_model_packaging_framework", "mlops_model_packaging_containerization.model_artifact_packaging_formats_safetensors"]
      }
    ],
    "linkedin": [
      {
        "signal": "Docker GPU, BentoML, and Model Packaging endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_model_packaging_containerization.triton_model_repository_configuration", "mlops_model_packaging_containerization.nvidia_container_toolkit_cuda_compatibility"]
      }
    ],
    "github": [
      {
        "pattern": "Dockerfile*|bentofile.yaml|config.pbtxt|environment.yaml|*.safetensors",
        "strength": 1.0,
        "maps_to": [
          "mlops_model_packaging_containerization.docker_multistage_gpu_builds",
          "mlops_model_packaging_containerization.bentoml_model_packaging_framework",
          "mlops_model_packaging_containerization.triton_model_repository_configuration",
          "mlops_model_packaging_containerization.onnx_torchscript_artifact_packaging",
          "mlops_model_packaging_containerization.container_registry_vulnerability_scanning",
          "mlops_model_packaging_containerization.conda_poetry_lockfile_pinning",
          "mlops_model_packaging_containerization.nvidia_container_toolkit_cuda_compatibility",
          "mlops_model_packaging_containerization.model_artifact_packaging_formats_safetensors",
          "mlops_model_packaging_containerization.caching_wheel_compilation_speedups"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Packaging & GPU Containerization Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_model_packaging_containerization.docker_multistage_gpu_builds",
          "mlops_model_packaging_containerization.bentoml_model_packaging_framework",
          "mlops_model_packaging_containerization.triton_model_repository_configuration",
          "mlops_model_packaging_containerization.onnx_torchscript_artifact_packaging",
          "mlops_model_packaging_containerization.container_registry_vulnerability_scanning",
          "mlops_model_packaging_containerization.conda_poetry_lockfile_pinning",
          "mlops_model_packaging_containerization.nvidia_container_toolkit_cuda_compatibility",
          "mlops_model_packaging_containerization.model_artifact_packaging_formats_safetensors",
          "mlops_model_packaging_containerization.caching_wheel_compilation_speedups"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["docker_multistage_gpu_builds", "conda_poetry_lockfile_pinning", "onnx_torchscript_artifact_packaging"],
      "description": "Writes multi-stage GPU Dockerfiles, pins lockfiles, and packages models into ONNX/TorchScript artifacts."
    },
    "mid": {
      "expected_subskills": ["bentoml_model_packaging_framework", "triton_model_repository_configuration", "container_registry_vulnerability_scanning", "model_artifact_packaging_formats_safetensors"],
      "description": "Packages BentoML services, structures Triton repositories with config.pbtxt, scans with Trivy, and utilizes SafeTensors."
    },
    "senior": {
      "expected_subskills": ["nvidia_container_toolkit_cuda_compatibility", "caching_wheel_compilation_speedups"],
      "description": "Architects high-speed BuildKit caching pipelines, builds custom C++ wheels, and ensures forward CUDA driver compatibility across GPU fleets."
    }
  }
}

# 6. mlops_model_serving_infrastructure
skills["mlops_model_serving_infrastructure"] = {
  "skill_id": "mlops_model_serving_infrastructure",
  "name": "Model Serving Platforms & GPU Inference",
  "category": "serving",
  "description": "Cloud-native model serving on Kubernetes: KServe, Seldon Core, Ray Serve, vLLM / TGI high-throughput LLM engines, dynamic GPU autoscaling, ingress routing, and service mesh.",
  "subskills": [
    {
      "id": "kserve_inferenceservice_crd",
      "name": "KServe & InferenceService Custom Resource (CRD)",
      "description": "Deploying models using KServe InferenceService CRDs, predictor, transformer, explainer components, serverless scale-to-zero with Knative, and storageInitializer.",
      "keywords": ["KServe", "InferenceService", "Knative", "scale-to-zero", "storageInitializer", "predictor pod", "transformer component"]
    },
    {
      "id": "seldon_core_advanced_graphs",
      "name": "Seldon Core & Complex Inference Graphs",
      "description": "SeldonDeployment CRD, building multi-model inference pipelines (Combiners, Routers, Ensembles), shadow deployments, and AB testing.",
      "keywords": ["Seldon Core", "SeldonDeployment", "inference graph", "Combiner", "Router", "multi-model pipeline", "shadow routing"]
    },
    {
      "id": "ray_serve_distributed_inference",
      "name": "Ray Serve Distributed Serving & Deployments",
      "description": "Ray Serve @serve.deployment, managing replica actors, dynamic batching, actor concurrency, and scaling across heterogeneous Ray clusters.",
      "keywords": ["Ray Serve", "@serve.deployment", "serve.run", "Ray actor", "replica scaling", "fractional GPU allocation", "distributed inference"]
    },
    {
      "id": "vllm_tgi_high_throughput_llm_serving",
      "name": "High-Throughput Serving Engines (vLLM & TGI)",
      "description": "Operating vLLM (PagedAttention) and Text Generation Inference (TGI), continuous batching, tensor parallelism, and OpenAI-compatible endpoints.",
      "keywords": ["vLLM", "PagedAttention", "TGI", "continuous batching", "tensor parallelism", "OpenAI-compatible server", "KV cache management"]
    },
    {
      "id": "gpu_autoscaling_keda_prometheus",
      "name": "GPU Autoscaling with KEDA & Prometheus Metrics",
      "description": "Configuring Kubernetes Event-driven Autoscaling (KEDA) on GPU metrics (DCGM GPU duty cycle, queue latency, request backlog) rather than basic CPU/memory.",
      "keywords": ["KEDA", "GPU autoscaling", "DCGM metrics", "queue length scaler", "PrometheusScaledObject", "rapid scale up", "HPA for GPU"]
    },
    {
      "id": "dynamic_batching_triton_inference",
      "name": "Dynamic Batching & Concurrent Model Execution",
      "description": "Triton dynamic batch scheduler, max_queue_delay_microseconds, multi-model GPU memory sharing, and maximizing inference throughput.",
      "keywords": ["dynamic batching", "Triton", "max_queue_delay", "GPU memory sharing", "throughput maximization", "queue scheduler"]
    },
    {
      "id": "istio_service_mesh_traffic_splitting",
      "name": "Istio Service Mesh & Canary Traffic Splitting",
      "description": "Using Istio VirtualService and DestinationRule to split live prediction traffic (90% v1 / 10% v2) and mirror traffic for shadow evaluation.",
      "keywords": ["Istio", "VirtualService", "DestinationRule", "traffic splitting", "Canary routing", "mirror traffic", "Service Mesh for ML"]
    },
    {
      "id": "inference_caching_semantic_redis",
      "name": "Inference Caching (Redis & Semantic Cache)",
      "description": "Caching frequent prediction requests in Redis, vector semantic caching (GPTCache), and sub-millisecond response for repeat queries.",
      "keywords": ["inference cache", "Redis cache", "GPTCache", "semantic caching", "sub-millisecond latency", "cost reduction", "cache hit ratio"]
    },
    {
      "id": "cold_start_latency_reduction_gpu",
      "name": "GPU Cold Start Latency Reduction & Pre-Warming",
      "description": "Techniques to eliminate GPU cold start: pre-pulled daemonset container images, warm pools, memory-mapped weights, and rapid model hydration.",
      "keywords": ["cold start", "GPU pre-warming", "daemonset image pre-pull", "mmap weights", "rapid hydration", "serverless GPU optimization"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Deployed and scaled KServe and vLLM inference platforms on Kubernetes with KEDA GPU autoscaling and Istio traffic splitting",
        "strength": 0.5,
        "maps_to": ["mlops_model_serving_infrastructure.kserve_inferenceservice_crd", "mlops_model_serving_infrastructure.vllm_tgi_high_throughput_llm_serving", "mlops_model_serving_infrastructure.gpu_autoscaling_keda_prometheus"]
      }
    ],
    "linkedin": [
      {
        "signal": "KServe, Ray Serve, vLLM, and Model Serving endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_model_serving_infrastructure.ray_serve_distributed_inference", "mlops_model_serving_infrastructure.seldon_core_advanced_graphs"]
      }
    ],
    "github": [
      {
        "pattern": "*inferenceservice*.yml|*seldon*.yml|*ray_serve*.py|*keda*.yml|istio/**/*.yml",
        "strength": 1.0,
        "maps_to": [
          "mlops_model_serving_infrastructure.kserve_inferenceservice_crd",
          "mlops_model_serving_infrastructure.seldon_core_advanced_graphs",
          "mlops_model_serving_infrastructure.ray_serve_distributed_inference",
          "mlops_model_serving_infrastructure.vllm_tgi_high_throughput_llm_serving",
          "mlops_model_serving_infrastructure.gpu_autoscaling_keda_prometheus",
          "mlops_model_serving_infrastructure.dynamic_batching_triton_inference",
          "mlops_model_serving_infrastructure.istio_service_mesh_traffic_splitting",
          "mlops_model_serving_infrastructure.inference_caching_semantic_redis",
          "mlops_model_serving_infrastructure.cold_start_latency_reduction_gpu"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Serving Platforms & GPU Inference Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_model_serving_infrastructure.kserve_inferenceservice_crd",
          "mlops_model_serving_infrastructure.seldon_core_advanced_graphs",
          "mlops_model_serving_infrastructure.ray_serve_distributed_inference",
          "mlops_model_serving_infrastructure.vllm_tgi_high_throughput_llm_serving",
          "mlops_model_serving_infrastructure.gpu_autoscaling_keda_prometheus",
          "mlops_model_serving_infrastructure.dynamic_batching_triton_inference",
          "mlops_model_serving_infrastructure.istio_service_mesh_traffic_splitting",
          "mlops_model_serving_infrastructure.inference_caching_semantic_redis",
          "mlops_model_serving_infrastructure.cold_start_latency_reduction_gpu"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["kserve_inferenceservice_crd", "dynamic_batching_triton_inference", "inference_caching_semantic_redis"],
      "description": "Deploys standard KServe InferenceServices, configures dynamic batching, and implements Redis prediction caching."
    },
    "mid": {
      "expected_subskills": ["seldon_core_advanced_graphs", "ray_serve_distributed_inference", "vllm_tgi_high_throughput_llm_serving", "istio_service_mesh_traffic_splitting"],
      "description": "Builds complex Seldon inference graphs, operates Ray Serve and vLLM clusters, and routes traffic via Istio Canary rules."
    },
    "senior": {
      "expected_subskills": ["gpu_autoscaling_keda_prometheus", "cold_start_latency_reduction_gpu"],
      "description": "Architects event-driven KEDA GPU autoscaling on DCGM metrics and eliminates cold start bottlenecks across multi-region serverless GPU fleets."
    }
  }
}

# 7. mlops_ci_cd_continuous_training
skills["mlops_ci_cd_continuous_training"] = {
  "skill_id": "mlops_ci_cd_continuous_training",
  "name": "CI/CD for Machine Learning & Continuous Training",
  "category": "ci_cd",
  "description": "Continuous Integration, Continuous Delivery, and Continuous Training (CT) for ML: automated PR testing with CML, model validation gates, Champion-Challenger evaluation, Canary rollouts, and rollback automation.",
  "subskills": [
    {
      "id": "cml_github_actions_pull_request_reports",
      "name": "CML (Continuous Machine Learning) PR Reports",
      "description": "Using CML in GitHub Actions/GitLab CI to train benchmark models on pull requests, generate markdown reports with loss curves, and post PR comments.",
      "keywords": ["CML", "Continuous Machine Learning", "GitHub Actions", "cml send-comment", "PR model evaluation", "automated training in CI", "markdown metrics"]
    },
    {
      "id": "model_validation_gates_threshold_checks",
      "name": "Automated Model Validation Gates & Thresholds",
      "description": "Blocking automated deployment if model metrics (F1, AUC, latency, memory footprint) fail minimum acceptance thresholds in CI.",
      "keywords": ["validation gate", "threshold check", "minimum AUC threshold", "latency gate", "block deployment", "automated quality gate"]
    },
    {
      "id": "champion_challenger_evaluation_framework",
      "name": "Champion-Challenger Shadow & Live Comparison",
      "description": "Comparing newly trained Challenger model against live Champion model on fresh production data slices before approving promotion.",
      "keywords": ["Champion-Challenger", "Champion model", "Challenger model", "shadow comparison", "statistical superiority", "model promotion"]
    },
    {
      "id": "automated_continuous_training_triggers",
      "name": "Continuous Training (CT) Trigger Architecture",
      "description": "Event-driven retraining triggers (data drift alert, new data arrival in lakehouse) vs scheduled cron triggers, and idempotency.",
      "keywords": ["Continuous Training", "CT trigger", "event-driven retraining", "drift trigger", "cron schedule", "automated retraining pipeline"]
    },
    {
      "id": "canary_blue_green_model_rollouts",
      "name": "Canary & Blue/Green Model Rollout Pipelines",
      "description": "Automating progressive traffic shifting (1% -> 10% -> 50% -> 100%) with Argo Rollouts or Flagger based on error rates and latency percentiles.",
      "keywords": ["Argo Rollouts", "Flagger", "Canary rollout", "Blue-Green deployment", "progressive traffic shift", "automated promotion"]
    },
    {
      "id": "automated_rollback_health_probes",
      "name": "Automated Rollback & Model Health Probes",
      "description": "Instant automated rollback to previous model version if live error rate exceeds threshold (5xx spikes, high latency, prediction drift).",
      "keywords": ["automated rollback", "health probes", "error rate spike", "instant rollback", "previous model version", "fail-safe"]
    },
    {
      "id": "data_pipeline_unit_integration_testing",
      "name": "Data Pipeline Unit & Integration Testing in CI",
      "description": "Running pytest test suites with Great Expectations and synthetic mock data on feature extraction code before training pipeline execution.",
      "keywords": ["pytest", "pipeline testing", "synthetic mock", "Great Expectations in CI", "unit testing ML", "integration testing"]
    },
    {
      "id": "gitops_for_ml_argo_flux",
      "name": "GitOps for Machine Learning (Argo CD / Flux)",
      "description": "Managing declarative Model Serving manifests in Git repositories and synchronizing state to Kubernetes clusters via Argo CD.",
      "keywords": ["GitOps", "Argo CD", "Flux", "declarative manifest", "Git as single source of truth", "K8s sync", "GitOps for ML"]
    },
    {
      "id": "infrastructure_ci_cd_terraform_github_actions",
      "name": "Infrastructure CI/CD with Terraform & GitHub Actions",
      "description": "Automating Terraform plan and apply in pull request pipelines to provision cloud compute, S3 buckets, and EKS/GKE clusters.",
      "keywords": ["Terraform in CI", "terraform plan PR", "terraform apply", "GitHub Actions IaC", "infrastructure automation", "automated provisioning"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Built enterprise CI/CD/CT pipelines with GitHub Actions, CML, Argo Rollouts, and automated Champion-Challenger validation",
        "strength": 0.5,
        "maps_to": ["mlops_ci_cd_continuous_training.cml_github_actions_pull_request_reports", "mlops_ci_cd_continuous_training.champion_challenger_evaluation_framework", "mlops_ci_cd_continuous_training.canary_blue_green_model_rollouts"]
      }
    ],
    "linkedin": [
      {
        "signal": "Continuous Training, CI/CD for Machine Learning, and GitOps endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_ci_cd_continuous_training.automated_continuous_training_triggers", "mlops_ci_cd_continuous_training.gitops_for_ml_argo_flux"]
      }
    ],
    "github": [
      {
        "pattern": ".github/workflows/*.yml|.gitlab-ci.yml|cml*.sh|rollout*.yml",
        "strength": 1.0,
        "maps_to": [
          "mlops_ci_cd_continuous_training.cml_github_actions_pull_request_reports",
          "mlops_ci_cd_continuous_training.model_validation_gates_threshold_checks",
          "mlops_ci_cd_continuous_training.champion_challenger_evaluation_framework",
          "mlops_ci_cd_continuous_training.automated_continuous_training_triggers",
          "mlops_ci_cd_continuous_training.canary_blue_green_model_rollouts",
          "mlops_ci_cd_continuous_training.automated_rollback_health_probes",
          "mlops_ci_cd_continuous_training.data_pipeline_unit_integration_testing",
          "mlops_ci_cd_continuous_training.gitops_for_ml_argo_flux",
          "mlops_ci_cd_continuous_training.infrastructure_ci_cd_terraform_github_actions"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes CI/CD for Machine Learning & Continuous Training Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_ci_cd_continuous_training.cml_github_actions_pull_request_reports",
          "mlops_ci_cd_continuous_training.model_validation_gates_threshold_checks",
          "mlops_ci_cd_continuous_training.champion_challenger_evaluation_framework",
          "mlops_ci_cd_continuous_training.automated_continuous_training_triggers",
          "mlops_ci_cd_continuous_training.canary_blue_green_model_rollouts",
          "mlops_ci_cd_continuous_training.automated_rollback_health_probes",
          "mlops_ci_cd_continuous_training.data_pipeline_unit_integration_testing",
          "mlops_ci_cd_continuous_training.gitops_for_ml_argo_flux",
          "mlops_ci_cd_continuous_training.infrastructure_ci_cd_terraform_github_actions"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["cml_github_actions_pull_request_reports", "model_validation_gates_threshold_checks", "data_pipeline_unit_integration_testing"],
      "description": "Configures CML PR reports, writes unit tests for data transforms, and establishes model validation threshold checks."
    },
    "mid": {
      "expected_subskills": ["champion_challenger_evaluation_framework", "automated_continuous_training_triggers", "canary_blue_green_model_rollouts", "automated_rollback_health_probes"],
      "description": "Builds Champion-Challenger validation gates, triggers automated retraining, and manages Canary rollouts with health probes."
    },
    "senior": {
      "expected_subskills": ["gitops_for_ml_argo_flux", "infrastructure_ci_cd_terraform_github_actions"],
      "description": "Establishes enterprise GitOps (Argo CD) for machine learning fleets and automates full-stack cloud infrastructure pipelines."
    }
  }
}

# 8. mlops_monitoring_drift_observability
skills["mlops_monitoring_drift_observability"] = {
  "skill_id": "mlops_monitoring_drift_observability",
  "name": "ML Observability, Drift & Prometheus Monitoring",
  "category": "observability",
  "description": "End-to-end production model observability: Prometheus scraping of model latency/throughput, Grafana dashboards, statistical drift detection (Evidently AI, whylogs), prediction drift, and automated incident alerting.",
  "subskills": [
    {
      "id": "prometheus_grafana_ml_metrics_scraping",
      "name": "Prometheus Metrics Scraping & Grafana Dashboards",
      "description": "Instrumenting prediction APIs with prometheus_client (inference latency histograms, request count, error rates, model memory usage) and building Grafana dashboards.",
      "keywords": ["Prometheus", "prometheus_client", "Grafana", "latency histogram", "error rate counter", "requests per second", "ServiceMonitor"]
    },
    {
      "id": "evidently_ai_automated_drift_dashboards",
      "name": "Evidently AI Automated Drift Reports & Test Suites",
      "description": "Generating scheduled Evidently AI HTML reports and JSON test suites to detect data drift, target drift, and data quality degradation.",
      "keywords": ["Evidently AI", "Report", "TestSuite", "DataDriftPreset", "TargetDriftPreset", "HTML report", "automated test suite", "drift metrics"]
    },
    {
      "id": "statistical_drift_tests_ks_psi_wasserstein",
      "name": "Statistical Divergence Tests (PSI, KS-Test, Wasserstein)",
      "description": "Applying Population Stability Index (PSI), Kolmogorov-Smirnov test, Cramer-von Mises, and Jensen-Shannon divergence to identify shifted features.",
      "keywords": ["PSI", "KS-test", "Kolmogorov-Smirnov", "Wasserstein distance", "Jensen-Shannon", "statistical drift", "distribution shift"]
    },
    {
      "id": "prediction_output_distribution_monitoring",
      "name": "Prediction Output & Confidence Drift Monitoring",
      "description": "Tracking shifts in predicted class distribution probabilities, mean score drift, entropy of predictions, and detecting model confidence collapse.",
      "keywords": ["prediction drift", "confidence collapse", "class distribution shift", "predicted probability drift", "entropy tracking"]
    },
    {
      "id": "delayed_ground_truth_performance_estimation",
      "name": "Delayed Ground Truth & Performance Estimation (NannyML)",
      "description": "Estimating production accuracy/F1 drops without ground truth labels using Confidence-based Performance Estimation (CBPE) in NannyML.",
      "keywords": ["NannyML", "CBPE", "delayed ground truth", "performance estimation", "unlabeled data monitoring", "accuracy drop estimation"]
    },
    {
      "id": "alertmanager_webhook_incident_triggers",
      "name": "Alertmanager Rules & Automated Slack/PagerDuty Alerts",
      "description": "Writing PrometheusRule alert expressions (e.g. P99 latency > 100ms for 5m, drift_score > 0.2) and dispatching via Alertmanager to PagerDuty/Slack.",
      "keywords": ["Alertmanager", "PrometheusRule", "PagerDuty", "Slack alert", "incident trigger", "alert threshold", "notification routing"]
    },
    {
      "id": "model_logging_payload_capture_fluentd",
      "name": "Model Request/Response Payload Logging (FluentBit / Kafka)",
      "description": "Asynchronously capturing production input/output payloads to S3/Kafka via FluentBit/Fluentd for post-hoc analysis without blocking prediction latency.",
      "keywords": ["payload logging", "FluentBit", "Fluentd", "Kafka payload capture", "asynchronous logging", "inference audit log"]
    },
    {
      "id": "outlier_out_of_distribution_alerting",
      "name": "Out-of-Distribution (OOD) & Anomaly Alerting",
      "description": "Detecting corrupted or out-of-distribution input payloads using Mahalanobis distance / Isolation Forests and generating real-time security alerts.",
      "keywords": ["OOD alert", "anomaly alert", "Mahalanobis distance", "corrupted input detection", "Isolation Forest monitoring", "input guardrail"]
    },
    {
      "id": "automated_model_retraining_trigger_integration",
      "name": "Automated Retraining Integration via Drift Webhooks",
      "description": "Connecting drift detection pipeline outputs directly to Kubeflow / Airflow webhooks to automatically trigger retraining on fresh data.",
      "keywords": ["retraining webhook", "drift-triggered training", "automated pipeline invocation", "closed-loop MLOps", "self-healing ML"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Architected full-stack ML observability platform with Prometheus, Grafana, and Evidently AI drift-triggered retraining",
        "strength": 0.5,
        "maps_to": ["mlops_monitoring_drift_observability.prometheus_grafana_ml_metrics_scraping", "mlops_monitoring_drift_observability.evidently_ai_automated_drift_dashboards", "mlops_monitoring_drift_observability.automated_model_retraining_trigger_integration"]
      }
    ],
    "linkedin": [
      {
        "signal": "Prometheus, Grafana, ML Observability, and Drift Detection endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_monitoring_drift_observability.statistical_drift_tests_ks_psi_wasserstein", "mlops_monitoring_drift_observability.alertmanager_webhook_incident_triggers"]
      }
    ],
    "github": [
      {
        "pattern": "*prometheus*|*grafana*|*drift*.py|*evidently*.py|alerts/**/*.yml",
        "strength": 1.0,
        "maps_to": [
          "mlops_monitoring_drift_observability.prometheus_grafana_ml_metrics_scraping",
          "mlops_monitoring_drift_observability.evidently_ai_automated_drift_dashboards",
          "mlops_monitoring_drift_observability.statistical_drift_tests_ks_psi_wasserstein",
          "mlops_monitoring_drift_observability.prediction_output_distribution_monitoring",
          "mlops_monitoring_drift_observability.delayed_ground_truth_performance_estimation",
          "mlops_monitoring_drift_observability.alertmanager_webhook_incident_triggers",
          "mlops_monitoring_drift_observability.model_logging_payload_capture_fluentd",
          "mlops_monitoring_drift_observability.outlier_out_of_distribution_alerting",
          "mlops_monitoring_drift_observability.automated_model_retraining_trigger_integration"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes ML Observability, Drift & Prometheus Monitoring Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_monitoring_drift_observability.prometheus_grafana_ml_metrics_scraping",
          "mlops_monitoring_drift_observability.evidently_ai_automated_drift_dashboards",
          "mlops_monitoring_drift_observability.statistical_drift_tests_ks_psi_wasserstein",
          "mlops_monitoring_drift_observability.prediction_output_distribution_monitoring",
          "mlops_monitoring_drift_observability.delayed_ground_truth_performance_estimation",
          "mlops_monitoring_drift_observability.alertmanager_webhook_incident_triggers",
          "mlops_monitoring_drift_observability.model_logging_payload_capture_fluentd",
          "mlops_monitoring_drift_observability.outlier_out_of_distribution_alerting",
          "mlops_monitoring_drift_observability.automated_model_retraining_trigger_integration"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["prometheus_grafana_ml_metrics_scraping", "evidently_ai_automated_drift_dashboards", "statistical_drift_tests_ks_psi_wasserstein"],
      "description": "Instruments APIs with Prometheus metrics, generates Evidently AI reports, and calculates PSI/KS-test drift scores."
    },
    "mid": {
      "expected_subskills": ["prediction_output_distribution_monitoring", "delayed_ground_truth_performance_estimation", "alertmanager_webhook_incident_triggers", "model_logging_payload_capture_fluentd"],
      "description": "Tracks prediction distribution shifts, estimates performance with NannyML, and sets up Alertmanager alerts and payload logging."
    },
    "senior": {
      "expected_subskills": ["outlier_out_of_distribution_alerting", "automated_model_retraining_trigger_integration"],
      "description": "Architects OOD detection guardrails and designs closed-loop self-healing retraining pipelines triggered by drift webhooks."
    }
  }
}

# 9. mlops_infrastructure_iac_cloud
skills["mlops_infrastructure_iac_cloud"] = {
  "skill_id": "mlops_infrastructure_iac_cloud",
  "name": "Cloud Infrastructure & Kubernetes for ML (Terraform / K8s)",
  "category": "infrastructure",
  "description": "Infrastructure as Code (Terraform), Kubernetes cluster architecture for ML (EKS/GKE), Karpenter node provisioning, GPU device plugins, IAM roles & service accounts, and cluster networking.",
  "subskills": [
    {
      "id": "terraform_ml_infrastructure_modules",
      "name": "Terraform Modules for ML Platforms",
      "description": "Authoring modular Terraform for ML: EKS/GKE clusters, S3/GCS model artifact buckets, IAM roles for service accounts (IRSA), and MLflow DBs.",
      "keywords": ["Terraform for ML", "IRSA", "Terraform module", "EKS module", "GKE module", "S3 bucket IaC", "remote state", "HCL"]
    },
    {
      "id": "kubernetes_gpu_device_plugin_setup",
      "name": "NVIDIA GPU Device Plugin & Operator for K8s",
      "description": "Installing NVIDIA GPU Operator on Kubernetes, nvidia-device-plugin DaemonSet, automatic driver injection, and GPU node tagging.",
      "keywords": ["NVIDIA GPU Operator", "k8s-device-plugin", "nvidia.com/gpu", "GPU DaemonSet", "driver container", "GPU node discovery"]
    },
    {
      "id": "karpenter_just_in_time_gpu_node_provisioning",
      "name": "Karpenter Just-in-Time GPU Node Provisioning",
      "description": "Configuring Karpenter NodePools and EC2NodeClasses for fast, dynamic GPU instance provisioning (g5, p4d) directly from pending pod specs.",
      "keywords": ["Karpenter", "NodePool", "EC2NodeClass", "just-in-time provisioning", "GPU instance provisioning", "spot node provisioning", "consolidation"]
    },
    {
      "id": "iam_roles_service_accounts_irsa_security",
      "name": "IAM Roles for Service Accounts (IRSA / Workload Identity)",
      "description": "Binding Kubernetes ServiceAccounts to AWS IAM roles / GCP Workload Identity to grant least privilege S3/GCS bucket access without hardcoded keys.",
      "keywords": ["IRSA", "Workload Identity", "IAM role", "ServiceAccount", "least privilege", "oidc provider", "cloud security"]
    },
    {
      "id": "helm_charts_mlops_platform_deployment",
      "name": "Helm Charts for MLOps Tooling Deployments",
      "description": "Deploying and managing MLOps platform components (MLflow, Feast, KServe, Prometheus) using custom and community Helm charts.",
      "keywords": ["Helm", "values.yaml", "helm upgrade", "MLflow helm", "KServe helm", "chart repository", "K8s package management"]
    },
    {
      "id": "cluster_networking_ingress_cert_manager",
      "name": "Cluster Ingress, TLS Termination & cert-manager",
      "description": "Configuring Ingress-NGINX / Envoy Gateway, Let's Encrypt TLS certificates with cert-manager, and secure external domain routing.",
      "keywords": ["Ingress-NGINX", "cert-manager", "TLS termination", "Let's Encrypt", "Envoy Gateway", "secure routing", "external-dns"]
    },
    {
      "id": "persistent_volumes_nfs_fast_model_loading",
      "name": "High-Throughput Storage (EFS, FSx for Lustre, NVMe)",
      "description": "Mounting high-throughput shared storage (Amazon FSx for Lustre, EFS, local NVMe CSI) to pods for multi-gigabyte model checkpoint loading.",
      "keywords": ["FSx for Lustre", "EFS", "NVMe CSI", "PersistentVolume", "StorageClass", "high throughput storage", "fast checkpoint loading"]
    },
    {
      "id": "multi_tenant_cluster_isolation_namespaces",
      "name": "Multi-Tenant Resource Quotas & NetworkPolicies",
      "description": "Hard multi-tenancy in ML clusters: ResourceQuotas, LimitRanges per team namespace, NetworkPolicies for traffic isolation, and priority classes.",
      "keywords": ["ResourceQuota", "LimitRange", "NetworkPolicy", "multi-tenancy", "PriorityClass", "namespace isolation", "preemption"]
    },
    {
      "id": "multi_region_cloud_disaster_recovery",
      "name": "Multi-Region Cloud Failover & Disaster Recovery",
      "description": "Cross-region S3 replication of model registries, multi-region Route 53 DNS failover, and automated cluster disaster recovery runbooks.",
      "keywords": ["Disaster Recovery", "cross-region replication", "Route 53 failover", "multi-region EKS", "RTO", "RPO", "backup runbook"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Provisioned multi-cluster Kubernetes ML platform using Terraform, Karpenter GPU autoscaling, and FSx for Lustre",
        "strength": 0.5,
        "maps_to": ["mlops_infrastructure_iac_cloud.terraform_ml_infrastructure_modules", "mlops_infrastructure_iac_cloud.karpenter_just_in_time_gpu_node_provisioning", "mlops_infrastructure_iac_cloud.persistent_volumes_nfs_fast_model_loading"]
      }
    ],
    "linkedin": [
      {
        "signal": "Kubernetes for ML, Terraform, and Cloud Infrastructure endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_infrastructure_iac_cloud.kubernetes_gpu_device_plugin_setup", "mlops_infrastructure_iac_cloud.iam_roles_service_accounts_irsa_security"]
      }
    ],
    "github": [
      {
        "pattern": "terraform/**/*.tf|helm/**/*.yaml|karpenter*.yml|*.tfvars",
        "strength": 1.0,
        "maps_to": [
          "mlops_infrastructure_iac_cloud.terraform_ml_infrastructure_modules",
          "mlops_infrastructure_iac_cloud.kubernetes_gpu_device_plugin_setup",
          "mlops_infrastructure_iac_cloud.karpenter_just_in_time_gpu_node_provisioning",
          "mlops_infrastructure_iac_cloud.iam_roles_service_accounts_irsa_security",
          "mlops_infrastructure_iac_cloud.helm_charts_mlops_platform_deployment",
          "mlops_infrastructure_iac_cloud.cluster_networking_ingress_cert_manager",
          "mlops_infrastructure_iac_cloud.persistent_volumes_nfs_fast_model_loading",
          "mlops_infrastructure_iac_cloud.multi_tenant_cluster_isolation_namespaces",
          "mlops_infrastructure_iac_cloud.multi_region_cloud_disaster_recovery"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Cloud Infrastructure & Kubernetes for ML Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_infrastructure_iac_cloud.terraform_ml_infrastructure_modules",
          "mlops_infrastructure_iac_cloud.kubernetes_gpu_device_plugin_setup",
          "mlops_infrastructure_iac_cloud.karpenter_just_in_time_gpu_node_provisioning",
          "mlops_infrastructure_iac_cloud.iam_roles_service_accounts_irsa_security",
          "mlops_infrastructure_iac_cloud.helm_charts_mlops_platform_deployment",
          "mlops_infrastructure_iac_cloud.cluster_networking_ingress_cert_manager",
          "mlops_infrastructure_iac_cloud.persistent_volumes_nfs_fast_model_loading",
          "mlops_infrastructure_iac_cloud.multi_tenant_cluster_isolation_namespaces",
          "mlops_infrastructure_iac_cloud.multi_region_cloud_disaster_recovery"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["kubernetes_gpu_device_plugin_setup", "iam_roles_service_accounts_irsa_security", "helm_charts_mlops_platform_deployment"],
      "description": "Deploys NVIDIA GPU device plugins, configures least-privilege IRSA security, and manages Helm chart releases."
    },
    "mid": {
      "expected_subskills": ["terraform_ml_infrastructure_modules", "cluster_networking_ingress_cert_manager", "persistent_volumes_nfs_fast_model_loading", "multi_tenant_cluster_isolation_namespaces"],
      "description": "Provisions ML clusters with Terraform, mounts high-speed FSx/NVMe volumes, configures TLS cert-manager, and enforces namespace quotas."
    },
    "senior": {
      "expected_subskills": ["karpenter_just_in_time_gpu_node_provisioning", "multi_region_cloud_disaster_recovery"],
      "description": "Architects just-in-time GPU node provisioning with Karpenter and implements enterprise multi-region cloud disaster recovery."
    }
  }
}

# 10. mlops_cost_finops_resource_optimization
skills["mlops_cost_finops_resource_optimization"] = {
  "skill_id": "mlops_cost_finops_resource_optimization",
  "name": "GPU FinOps, Resource Sharing & Cost Optimization",
  "category": "finops",
  "description": "Maximizing GPU hardware efficiency and minimizing cloud spend: NVIDIA Multi-Instance GPU (MIG), GPU time-slicing, Spot instance orchestration, interruption handling, FinOps cost allocation, and model right-sizing.",
  "subskills": [
    {
      "id": "multi_instance_gpu_mig_partitioning",
      "name": "NVIDIA Multi-Instance GPU (MIG) Partitioning",
      "description": "Partitioning A100/H100 GPUs into isolated hardware instances (e.g. 1g.10gb, 3g.40gb) with dedicated compute, memory, and hardware QoS.",
      "keywords": ["MIG", "Multi-Instance GPU", "A100 partitioning", "H100 MIG", "GPU hardware slice", "nvidia.com/mig-*", "hardware QoS"]
    },
    {
      "id": "gpu_time_slicing_sharing",
      "name": "GPU Time-Slicing & Fractional GPU Sharing",
      "description": "Configuring Kubernetes GPU time-slicing configurations to share non-MIG GPUs across multiple inference microservice pods.",
      "keywords": ["GPU time-slicing", "fractional GPU", "GPU sharing", "timeSlicing.resources", "over-subscription", "cost reduction"]
    },
    {
      "id": "spot_instance_orchestration_checkpoints",
      "name": "Spot Instance Orchestration & Fault Tolerance",
      "description": "Running training jobs on cheap Spot/Preemptible instances with automated checkpointing, spot interruption notice listeners, and auto-resumption.",
      "keywords": ["Spot instances", "Preemptible VMs", "spot interruption", "2-minute warning handler", "automated checkpointing", "spot cost savings"]
    },
    {
      "id": "gpu_utilization_profiling_dcgm",
      "name": "GPU Utilization Profiling (NVIDIA DCGM / Nsight)",
      "description": "Monitoring GPU duty cycle, memory bandwidth utilization, tensor core activity, and identifying underutilized 'zombie' GPU allocations with DCGM.",
      "keywords": ["DCGM", "NVIDIA Nsight", "GPU duty cycle", "tensor core utilization", "memory bandwidth", "underutilized GPU", "profiling"]
    },
    {
      "id": "finops_cost_allocation_kubecost",
      "name": "FinOps Cost Allocation & Kubecost for ML",
      "description": "Allocating GPU/CPU compute costs per team, project, and model using Kubecost, AWS Cost Explorer tags, and tracking cost-per-inference.",
      "keywords": ["FinOps", "Kubecost", "cost allocation", "cost-per-inference", "cost tagging", "team chargeback", "cloud spend dashboard"]
    },
    {
      "id": "inference_right_sizing_cpu_vs_gpu",
      "name": "Inference Right-Sizing (CPU vs GPU vs Specialized ASICs)",
      "description": "Benchmarking workloads to determine the most cost-effective hardware: modern CPUs (Intel Xeon AVX-512), cost-efficient GPUs (T4, L4), or AWS Inferentia / Trainium.",
      "keywords": ["right-sizing", "CPU vs GPU inference", "AWS Inferentia", "AWS Trainium", "NVIDIA T4", "NVIDIA L4", "cost-performance ratio"]
    },
    {
      "id": "auto_termination_idle_compute_clusters",
      "name": "Auto-Termination of Idle Clusters & Development Pods",
      "description": "Implementing automated shutdown of idle Jupyter/training pods and scaling development inference endpoints to zero after business hours.",
      "keywords": ["auto-termination", "idle cluster shutdown", "scale-to-zero off-hours", "idle reaper", "cost governance", "scheduled shutdown"]
    },
    {
      "id": "model_compaction_for_lower_gpu_tier",
      "name": "Model Compaction for Lower GPU Tiers (A100 -> L4/T4)",
      "description": "Applying INT8/FP16 quantization to compress models so they fit on cost-effective 24GB L4/T4 GPUs instead of expensive 80GB A100s.",
      "keywords": ["model compaction", "L4 migration", "T4 GPU", "fit on smaller VRAM", "quantize for cost", "80GB to 24GB reduction"]
    },
    {
      "id": "cloud_savings_plans_reserved_instances",
      "name": "Savings Plans, Reserved Instances & Capacity Blocks",
      "description": "Strategic commitment modeling: Compute Savings Plans, 1-year/3-year Reserved Instances, and AWS EC2 Capacity Blocks for ML training reservations.",
      "keywords": ["Savings Plans", "Reserved Instances", "EC2 Capacity Blocks", "GPU reservation", "commitment discount", "FinOps strategy"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Reduced cloud ML spend by 60% by implementing Multi-Instance GPU (MIG), Spot orchestration, and Kubecost FinOps",
        "strength": 0.5,
        "maps_to": ["mlops_cost_finops_resource_optimization.multi_instance_gpu_mig_partitioning", "mlops_cost_finops_resource_optimization.spot_instance_orchestration_checkpoints", "mlops_cost_finops_resource_optimization.finops_cost_allocation_kubecost"]
      }
    ],
    "linkedin": [
      {
        "signal": "GPU FinOps, Cloud Cost Optimization, and MIG endorsements",
        "strength": 0.3,
        "maps_to": ["mlops_cost_finops_resource_optimization.gpu_time_slicing_sharing", "mlops_cost_finops_resource_optimization.inference_right_sizing_cpu_vs_gpu"]
      }
    ],
    "github": [
      {
        "pattern": "*finops*|*kubecost*|*mig*.yml|spot/**/*.py|cost/**/*.yml",
        "strength": 1.0,
        "maps_to": [
          "mlops_cost_finops_resource_optimization.multi_instance_gpu_mig_partitioning",
          "mlops_cost_finops_resource_optimization.gpu_time_slicing_sharing",
          "mlops_cost_finops_resource_optimization.spot_instance_orchestration_checkpoints",
          "mlops_cost_finops_resource_optimization.gpu_utilization_profiling_dcgm",
          "mlops_cost_finops_resource_optimization.finops_cost_allocation_kubecost",
          "mlops_cost_finops_resource_optimization.inference_right_sizing_cpu_vs_gpu",
          "mlops_cost_finops_resource_optimization.auto_termination_idle_compute_clusters",
          "mlops_cost_finops_resource_optimization.model_compaction_for_lower_gpu_tier",
          "mlops_cost_finops_resource_optimization.cloud_savings_plans_reserved_instances"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes GPU FinOps, Resource Sharing & Cost Optimization Assessment",
        "strength": 1.0,
        "maps_to": [
          "mlops_cost_finops_resource_optimization.multi_instance_gpu_mig_partitioning",
          "mlops_cost_finops_resource_optimization.gpu_time_slicing_sharing",
          "mlops_cost_finops_resource_optimization.spot_instance_orchestration_checkpoints",
          "mlops_cost_finops_resource_optimization.gpu_utilization_profiling_dcgm",
          "mlops_cost_finops_resource_optimization.finops_cost_allocation_kubecost",
          "mlops_cost_finops_resource_optimization.inference_right_sizing_cpu_vs_gpu",
          "mlops_cost_finops_resource_optimization.auto_termination_idle_compute_clusters",
          "mlops_cost_finops_resource_optimization.model_compaction_for_lower_gpu_tier",
          "mlops_cost_finops_resource_optimization.cloud_savings_plans_reserved_instances"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["gpu_utilization_profiling_dcgm", "auto_termination_idle_compute_clusters", "model_compaction_for_lower_gpu_tier"],
      "description": "Monitors GPU utilization with DCGM, configures auto-termination of idle dev pods, and quantizes models to fit smaller VRAM."
    },
    "mid": {
      "expected_subskills": ["gpu_time_slicing_sharing", "spot_instance_orchestration_checkpoints", "finops_cost_allocation_kubecost", "inference_right_sizing_cpu_vs_gpu"],
      "description": "Configures GPU time-slicing sharing, runs resilient training on Spot instances with automated checkpoints, and tracks Kubecost cost-per-inference."
    },
    "senior": {
      "expected_subskills": ["multi_instance_gpu_mig_partitioning", "cloud_savings_plans_reserved_instances"],
      "description": "Architects NVIDIA MIG hardware partitioning for high-density serving and formulates enterprise GPU reservation & Savings Plan strategies."
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
    "role_id": "mlops",
    "level": "junior",
    "title": "Junior MLOps Engineer",
    "description": "Entry-level MLOps engineering position focused on experiment tracking (MLflow), dataset versioning (DVC), GPU Docker containerization, basic Kubeflow/Airflow DAGs, and model validation checks under guidance.",
    "experience_range": "0-2 years",
    "skills": [
      {
        "skill_id": "mlops_experiment_tracking_registry",
        "importance": 0.95,
        "rationale": "Tracking runs, model signatures, and metric histories in MLflow or W&B is a core daily activity."
      },
      {
        "skill_id": "mlops_model_packaging_containerization",
        "importance": 0.90,
        "rationale": "Building multi-stage GPU Docker containers and managing dependency lockfiles."
      },
      {
        "skill_id": "mlops_data_feature_management",
        "importance": 0.85,
        "rationale": "Version controlling datasets with DVC and defining basic Feast feature views."
      },
      {
        "skill_id": "mlops_pipeline_orchestration",
        "importance": 0.85,
        "rationale": "Writing containerized KFP v2 components and configuring pipeline step caching."
      },
      {
        "skill_id": "mlops_ci_cd_continuous_training",
        "importance": 0.80,
        "rationale": "Configuring CML PR reports and automated model quality validation gates in GitHub Actions."
      },
      {
        "skill_id": "mlops_monitoring_drift_observability",
        "importance": 0.70,
        "rationale": "Instrumenting prediction endpoints with Prometheus metrics and generating Evidently AI drift reports."
      },
      {
        "skill_id": "mlops_model_serving_infrastructure",
        "importance": 0.65,
        "rationale": "Deploying standard KServe InferenceServices and implementing Redis prediction caches."
      },
      {
        "skill_id": "mlops_infrastructure_iac_cloud",
        "importance": 0.60,
        "rationale": "Managing Helm charts, GPU device plugins, and cloud IAM service accounts."
      },
      {
        "skill_id": "mlops_lifecycle_governance",
        "importance": 0.55,
        "rationale": "Authoring standardized Model Cards and configuring reproducible seed environments."
      },
      {
        "skill_id": "mlops_cost_finops_resource_optimization",
        "importance": 0.45,
        "rationale": "Profiling GPU utilization with DCGM and shutting down idle development compute."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.35, "description": "Insufficient foundational understanding of containerization and experiment tracking." },
        "partially_ready": { "min": 0.35, "max": 0.60, "description": "Can build Docker images and log runs but lacks automated pipeline and serving experience." },
        "ready": { "min": 0.60, "max": 0.85, "description": "Solid junior MLOps engineer capable of automating ML pipelines and managing model registries under guidance." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceeds junior expectations with strong Kubernetes serving and feature store skills." }
      }
    }
  },
  "mid": {
    "role_id": "mlops",
    "level": "mid",
    "title": "Mid-Level MLOps Engineer",
    "description": "Mid-level MLOps engineering position focused on building production ML pipelines (Kubeflow/Flyte), Feast feature store materialization, model serving platforms (KServe/Ray Serve/vLLM), Canary deployments, drift observability, and Spot training orchestration.",
    "experience_range": "2-5 years",
    "skills": [
      {
        "skill_id": "mlops_pipeline_orchestration",
        "importance": 0.95,
        "rationale": "Developing type-safe Flyte workflows, Argo templates, and managing GPU node affinities."
      },
      {
        "skill_id": "mlops_model_serving_infrastructure",
        "importance": 0.90,
        "rationale": "Operating high-throughput inference engines (vLLM, Ray Serve), KServe, and Istio Canary traffic splitting."
      },
      {
        "skill_id": "mlops_ci_cd_continuous_training",
        "importance": 0.90,
        "rationale": "Designing Champion-Challenger validation gates, automated Continuous Training, and health probe rollbacks."
      },
      {
        "skill_id": "mlops_data_feature_management",
        "importance": 0.85,
        "rationale": "Executing point-in-time correct historical joins in Feast and materializing low-latency online Redis stores."
      },
      {
        "skill_id": "mlops_experiment_tracking_registry",
        "importance": 0.85,
        "rationale": "Provisioning remote MLflow tracking architectures and packaging custom PyFunc models."
      },
      {
        "skill_id": "mlops_monitoring_drift_observability",
        "importance": 0.80,
        "rationale": "Tracking prediction distribution drift, NannyML performance estimation, and Alertmanager incident routing."
      },
      {
        "skill_id": "mlops_model_packaging_containerization",
        "importance": 0.80,
        "rationale": "Deploying BentoML services, Triton repository structures, and Trivy security scanning."
      },
      {
        "skill_id": "mlops_infrastructure_iac_cloud",
        "importance": 0.75,
        "rationale": "Provisioning Kubernetes ML infrastructure with Terraform, mounting FSx storage, and namespace isolation."
      },
      {
        "skill_id": "mlops_cost_finops_resource_optimization",
        "importance": 0.75,
        "rationale": "Configuring GPU time-slicing sharing, Spot instance automated checkpointing, and Kubecost allocation."
      },
      {
        "skill_id": "mlops_lifecycle_governance",
        "importance": 0.70,
        "rationale": "Enforcing full data-to-binary lineage, approval workflows, and automated bias compliance gates."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.40, "description": "Lacks production Kubernetes inference or pipeline orchestration experience." },
        "partially_ready": { "min": 0.40, "max": 0.65, "description": "Competent with standalone pipelines but needs guidance on Canary rollouts and GPU scaling." },
        "ready": { "min": 0.65, "max": 0.88, "description": "Fully autonomous MLOps engineer delivering scalable ML pipelines, robust inference platforms, and drift monitoring." },
        "exceeds": { "min": 0.88, "max": 1.0, "description": "Demonstrates advanced technical leadership in GPU FinOps, Karpenter autoscaling, and enterprise platform design." }
      }
    }
  },
  "senior": {
    "role_id": "mlops",
    "level": "senior",
    "title": "Senior MLOps Engineer / ML Platform Architect",
    "description": "Senior technical leadership position driving enterprise MLOps strategy: Karpenter just-in-time GPU scaling, NVIDIA Multi-Instance GPU (MIG) hardware partitioning, closed-loop Continuous Training (CT) self-healing pipelines, GitOps platform synchronization, and EU AI Act regulatory compliance.",
    "experience_range": "5+ years",
    "skills": [
      {
        "skill_id": "mlops_model_serving_infrastructure",
        "importance": 0.95,
        "rationale": "Architecting event-driven KEDA GPU autoscaling on DCGM metrics and sub-millisecond cold start optimization."
      },
      {
        "skill_id": "mlops_cost_finops_resource_optimization",
        "importance": 0.95,
        "rationale": "Architecting NVIDIA MIG hardware partitioning, GPU reservation planning, and cutting cloud ML spend."
      },
      {
        "skill_id": "mlops_ci_cd_continuous_training",
        "importance": 0.95,
        "rationale": "Establishing enterprise GitOps (Argo CD) for machine learning fleets and multi-region Canary automation."
      },
      {
        "skill_id": "mlops_infrastructure_iac_cloud",
        "importance": 0.90,
        "rationale": "Architecting Karpenter just-in-time GPU node provisioning and multi-region disaster recovery systems."
      },
      {
        "skill_id": "mlops_pipeline_orchestration",
        "importance": 0.90,
        "rationale": "Scaling multi-node PyTorchJob distributed training clusters with Volcano gang scheduling."
      },
      {
        "skill_id": "mlops_monitoring_drift_observability",
        "importance": 0.90,
        "rationale": "Architecting Out-of-Distribution (OOD) protection gates and drift-triggered automated self-healing loops."
      },
      {
        "skill_id": "mlops_lifecycle_governance",
        "importance": 0.85,
        "rationale": "Leading EU AI Act/GDPR compliance architectures and enterprise model failure post-mortem runbooks."
      },
      {
        "skill_id": "mlops_data_feature_management",
        "importance": 0.85,
        "rationale": "Governing enterprise multi-tenant feature store topologies and dataset cryptographic immutability."
      },
      {
        "skill_id": "mlops_experiment_tracking_registry",
        "importance": 0.85,
        "rationale": "Automating global Model Registry webhooks and enterprise artifact retention lifecycles."
      },
      {
        "skill_id": "mlops_model_packaging_containerization",
        "importance": 0.80,
        "rationale": "Optimizing BuildKit wheel compilation and forward CUDA driver compatibility across GPU clusters."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.45, "description": "Does not meet the architectural depth, GPU FinOps, or platform leadership required for senior roles." },
        "partially_ready": { "min": 0.45, "max": 0.70, "description": "Strong pipeline builder but lacks hardware partitioning (MIG), Karpenter autoscaling, or enterprise MLOps architecture." },
        "ready": { "min": 0.70, "max": 0.90, "description": "Proven senior MLOps engineer with comprehensive platform design, GPU FinOps, and production serving mastery." },
        "exceeds": { "min": 0.90, "max": 1.0, "description": "Visionary ML platform architect capable of building enterprise-scale, cost-optimized AI infrastructure." }
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
  "name": "CV / Resume Parser - MLOps Engineering",
  "description": "Extraction and scoring rules for MLOps Engineer CVs/Resumes based on section base strengths and keyword associations.",
  "sections": [
    {
      "section_id": "work_experience",
      "name": "Work Experience",
      "base_strength": 0.5,
      "description": "Professional MLOps roles, production pipeline orchestration, and model platform deployments.",
      "signal_extractors": [
        {
          "pattern": "Kubeflow|Flyte|Argo Workflows|Airflow",
          "strength": 0.5,
          "maps_to": [
            "mlops_pipeline_orchestration.kubeflow_pipelines_kfp_v2_dsl",
            "mlops_pipeline_orchestration.flyte_orchestration_type_safety",
            "mlops_pipeline_orchestration.gpu_resource_allocation_node_affinity"
          ]
        },
        {
          "pattern": "KServe|vLLM|Ray Serve|Triton|Seldon",
          "strength": 0.5,
          "maps_to": [
            "mlops_model_serving_infrastructure.kserve_inferenceservice_crd",
            "mlops_model_serving_infrastructure.vllm_tgi_high_throughput_llm_serving",
            "mlops_model_serving_infrastructure.gpu_autoscaling_keda_prometheus"
          ]
        },
        {
          "pattern": "Feast|Hopsworks|DVC|Feature Store|Data Versioning",
          "strength": 0.5,
          "maps_to": [
            "mlops_data_feature_management.feast_feature_store_architecture",
            "mlops_data_feature_management.point_in_time_correct_historical_joins",
            "mlops_data_feature_management.dvc_data_versioning_s3_gcs"
          ]
        },
        {
          "pattern": "MLflow|Weights & Biases|Model Registry|Experiment Tracking",
          "strength": 0.5,
          "maps_to": [
            "mlops_experiment_tracking_registry.mlflow_tracking_server_backend_setup",
            "mlops_experiment_tracking_registry.mlflow_model_registry_lifecycle",
            "mlops_experiment_tracking_registry.custom_mlflow_pyfunc_wrappers"
          ]
        },
        {
          "pattern": "CML|Continuous Training|Argo Rollouts|Champion Challenger|Canary",
          "strength": 0.5,
          "maps_to": [
            "mlops_ci_cd_continuous_training.cml_github_actions_pull_request_reports",
            "mlops_ci_cd_continuous_training.champion_challenger_evaluation_framework",
            "mlops_ci_cd_continuous_training.canary_blue_green_model_rollouts"
          ]
        },
        {
          "pattern": "Evidently AI|Prometheus|Grafana|Data Drift|Concept Drift",
          "strength": 0.5,
          "maps_to": [
            "mlops_monitoring_drift_observability.prometheus_grafana_ml_metrics_scraping",
            "mlops_monitoring_drift_observability.evidently_ai_automated_drift_dashboards",
            "mlops_monitoring_drift_observability.statistical_drift_tests_ks_psi_wasserstein"
          ]
        },
        {
          "pattern": "Terraform|Karpenter|EKS|GKE|Kubernetes|IRSA",
          "strength": 0.5,
          "maps_to": [
            "mlops_infrastructure_iac_cloud.terraform_ml_infrastructure_modules",
            "mlops_infrastructure_iac_cloud.karpenter_just_in_time_gpu_node_provisioning",
            "mlops_infrastructure_iac_cloud.kubernetes_gpu_device_plugin_setup"
          ]
        },
        {
          "pattern": "Multi-Instance GPU|MIG|Spot Instances|FinOps|Kubecost",
          "strength": 0.5,
          "maps_to": [
            "mlops_cost_finops_resource_optimization.multi_instance_gpu_mig_partitioning",
            "mlops_cost_finops_resource_optimization.spot_instance_orchestration_checkpoints",
            "mlops_cost_finops_resource_optimization.finops_cost_allocation_kubecost"
          ]
        },
        {
          "pattern": "BentoML|Docker GPU|Trivy|SafeTensors|CUDA",
          "strength": 0.5,
          "maps_to": [
            "mlops_model_packaging_containerization.docker_multistage_gpu_builds",
            "mlops_model_packaging_containerization.bentoml_model_packaging_framework",
            "mlops_model_packaging_containerization.model_artifact_packaging_formats_safetensors"
          ]
        },
        {
          "pattern": "MLOps Governance|Model Cards|EU AI Act|Lineage|Audit",
          "strength": 0.5,
          "maps_to": [
            "mlops_lifecycle_governance.model_cards_standardized_documentation",
            "mlops_lifecycle_governance.model_lineage_data_code_provenance",
            "mlops_lifecycle_governance.model_governance_approval_workflows"
          ]
        }
      ]
    },
    {
      "section_id": "projects",
      "name": "Projects",
      "base_strength": 0.5,
      "description": "MLOps platform repositories and production pipeline architectures."
    },
    {
      "section_id": "skills_list",
      "name": "Skills List",
      "base_strength": 0.3,
      "description": "Self-reported MLOps tools and platforms."
    },
    {
      "section_id": "education",
      "name": "Education & Certifications",
      "base_strength": 0.3,
      "description": "Degrees and cloud/Kubernetes/MLOps certifications."
    }
  ]
}

with open(os.path.join(evidence_dir, 'cv.json'), 'w', encoding='utf-8') as f:
  json.dump(cv_data, f, indent=2)

# 2. linkedin.json
linkedin_data = {
  "source_id": "linkedin",
  "name": "LinkedIn Profile Signals - MLOps Engineering",
  "description": "Signals and skill endorsements extracted from candidate LinkedIn profiles for MLOps roles.",
  "sections": [
    {
      "section_id": "experience",
      "base_strength": 0.5,
      "description": "Professional experience in MLOps Engineer, ML Platform Engineer, or AI Infrastructure roles."
    },
    {
      "section_id": "headline_summary",
      "base_strength": 0.3,
      "description": "Profile headline and summary keywords."
    },
    {
      "section_id": "skills_endorsements",
      "base_strength": 0.3,
      "description": "Endorsed skills related to Kubeflow, MLflow, Kubernetes, KServe, Feast, and GPU Infrastructure."
    },
    {
      "section_id": "recommendations",
      "base_strength": 0.5,
      "description": "Colleague recommendations validating MLOps delivery."
    }
  ]
}

with open(os.path.join(evidence_dir, 'linkedin.json'), 'w', encoding='utf-8') as f:
  json.dump(linkedin_data, f, indent=2)

# 3. github.json
github_data = {
  "source_id": "github",
  "name": "GitHub Repository Analysis - MLOps Engineering",
  "description": "Automated code and pipeline scanning rules for validating MLOps Engineer implementations.",
  "preprocessing_pipeline": {
    "steps": [
      {
        "step": 1,
        "name": "repository_metadata",
        "description": "Inspects repositories for MLOps manifests, orchestration DAGs, and infrastructure definitions."
      },
      {
        "step": 2,
        "name": "file_tree_scan",
        "description": "Scans for Kubeflow, Flyte, BentoML, KServe, Terraform, and MLflow pipeline configs.",
        "target_files": [
          { "pattern": "pipeline.yaml|*kfp*.py|*flyte*.py", "skill": "mlops_pipeline_orchestration", "priority": "high" },
          { "pattern": "*inferenceservice*.yml|*seldon*.yml|*ray_serve*.py", "skill": "mlops_model_serving_infrastructure", "priority": "high" },
          { "pattern": "feature_store.yaml|dvc.yaml|.dvc", "skill": "mlops_data_feature_management", "priority": "high" },
          { "pattern": "bentofile.yaml|config.pbtxt|Dockerfile*", "skill": "mlops_model_packaging_containerization", "priority": "high" },
          { "pattern": "terraform/**/*.tf|karpenter*.yml|*.tfvars", "skill": "mlops_infrastructure_iac_cloud", "priority": "high" },
          { "pattern": "*mlflow*|*wandb*|sweep.yaml", "skill": "mlops_experiment_tracking_registry", "priority": "high" },
          { "pattern": "*drift*.py|*prometheus*|*evidently*.py", "skill": "mlops_monitoring_drift_observability", "priority": "high" },
          { "pattern": ".github/workflows/*.yml|cml*.sh|rollout*.yml", "skill": "mlops_ci_cd_continuous_training", "priority": "high" },
          { "pattern": "*finops*|*mig*.yml|spot/**/*.py", "skill": "mlops_cost_finops_resource_optimization", "priority": "high" },
          { "pattern": "*model_card*.md|governance/**/*.py", "skill": "mlops_lifecycle_governance", "priority": "high" }
        ]
      }
    ]
  }
}

with open(os.path.join(evidence_dir, 'github.json'), 'w', encoding='utf-8') as f:
  json.dump(github_data, f, indent=2)

# 4. assessment.json
# Generate high quality questions for ALL 90 composite keys
questions_by_key = {
  # mlops_lifecycle_governance (9)
  "mlops_lifecycle_governance.mlops_maturity_levels_0_to_2": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Compare Google MLOps Level 0 (Manual), Level 1 (Continuous Training), and Level 2 (Automated CI/CD/CT pipelines).",
      "expected_answer_keywords": ["MLOps maturity", "Level 0 manual", "Level 1 continuous training", "Level 2 CI/CD automation", "reproducibility", "pipeline triggers"]
    }
  ],
  "mlops_lifecycle_governance.model_cards_standardized_documentation": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What standard sections must be documented in an enterprise Model Card (intended use, limitations, datasets, evaluation metrics)?",
      "expected_answer_keywords": ["Model Card", "intended use", "limitations", "evaluation metrics", "training data provenance", "ethical considerations"]
    }
  ],
  "mlops_lifecycle_governance.model_lineage_data_code_provenance": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you establish cryptographically verifiable end-to-end model lineage linking a production model binary back to its exact Git commit, DVC data hash, and container digest?",
      "expected_answer_keywords": ["model lineage", "data provenance", "Git commit hash", "DVC hash", "container image digest", "MLflow run ID", "audit trail"]
    }
  ],
  "mlops_lifecycle_governance.model_governance_approval_workflows": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you enforce role-based model governance gates in an enterprise Model Registry before a model can transition to Production?",
      "expected_answer_keywords": ["model governance", "approval gate", "RBAC", "stage transition", "compliance sign-off", "ML Engineer review", "risk audit"]
    }
  ],
  "mlops_lifecycle_governance.ethical_ai_fairness_compliance_gates": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you integrate automated bias auditing (Disparate Impact, Equalized Odds) into CI/CD pipelines to block unfair models?",
      "expected_answer_keywords": ["bias gate", "fairness check", "Disparate Impact", "Equalized Odds", "Fairlearn", "AIF360", "CI/CD blocker"]
    }
  ],
  "mlops_lifecycle_governance.model_catalog_metadata_management": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What are the advantages of integrating model metadata into enterprise data catalogs like DataHub alongside upstream data pipelines?",
      "expected_answer_keywords": ["DataHub", "model catalog", "metadata management", "upstream data lineage", "schema tracking", "business ownership"]
    }
  ],
  "mlops_lifecycle_governance.training_reproducibility_seed_environments": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you ensure bitwise training reproducibility in PyTorch across different GPU runs?",
      "expected_answer_keywords": ["torch.use_deterministic_algorithms", "random seed", "CUDA determinism", "CUBLAS_WORKSPACE_CONFIG", "pinned dependencies"]
    }
  ],
  "mlops_lifecycle_governance.regulatory_compliance_ai_act_gdpr": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you architect an MLOps platform to comply with EU AI Act high-risk requirements (risk management, technical documentation, human oversight)?",
      "expected_answer_keywords": ["EU AI Act", "high-risk AI", "technical documentation", "human-in-the-loop", "logging obligations", "GDPR compliance", "audit trail"]
    }
  ],
  "mlops_lifecycle_governance.incident_postmortem_model_failure_runbooks": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you structure an SRE post-mortem runbook for a silent production model failure caused by an upstream data pipeline bug?",
      "expected_answer_keywords": ["post-mortem", "runbook", "silent model failure", "circuit breaker", "fallback model", "root cause analysis", "SRE for ML"]
    }
  ],

  # mlops_experiment_tracking_registry (9)
  "mlops_experiment_tracking_registry.mlflow_tracking_server_backend_setup": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you deploy a production MLflow Tracking Server with PostgreSQL backend-store-uri and S3 default-artifact-root?",
      "expected_answer_keywords": ["MLflow server", "backend-store-uri", "default-artifact-root", "PostgreSQL", "S3 artifact root", "multi-tenancy", "systemd / Docker"]
    }
  ],
  "mlops_experiment_tracking_registry.experiment_run_logging_artifacts": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you log parameters, step-based metrics, and model artifacts using mlflow.log_params and mlflow.log_metrics?",
      "expected_answer_keywords": ["mlflow.log_params", "mlflow.log_metrics", "mlflow.log_artifact", "step metrics", "autologging", "run context"]
    }
  ],
  "mlops_experiment_tracking_registry.model_signatures_input_schemas": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is infer_signature() and schema enforcement critical when saving models to the MLflow Model Registry?",
      "expected_answer_keywords": ["infer_signature", "ModelSignature", "input_example", "schema validation", "prevent signature mismatch", "type safety"]
    }
  ],
  "mlops_experiment_tracking_registry.mlflow_model_registry_lifecycle": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain how models transition through lifecycle stages (None, Staging, Production, Archived) or model aliases in MLflow Model Registry.",
      "expected_answer_keywords": ["Model Registry", "stage transition", "Production", "Staging", "Archived", "model alias", "versioning", "mlflow.register_model"]
    }
  ],
  "mlops_experiment_tracking_registry.weights_biases_experiment_sweeps": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you configure and launch a Bayesian hyperparameter sweep in Weights & Biases using sweep.yaml and wandb agent?",
      "expected_answer_keywords": ["Weights & Biases", "wandb sweep", "sweep.yaml", "wandb agent", "Bayesian search", "metric optimization", "W&B dashboard"]
    }
  ],
  "mlops_experiment_tracking_registry.custom_mlflow_pyfunc_wrappers": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you author a custom mlflow.pyfunc.PythonModel wrapper to encapsulate preprocessing and inference into a single portable artifact?",
      "expected_answer_keywords": ["PythonModel", "mlflow.pyfunc", "load_context", "predict", "encapsulate preprocessing", "portable model artifact"]
    }
  ],
  "mlops_experiment_tracking_registry.artifact_storage_retention_lifecycle": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you design automated S3 artifact retention and lifecycle policies to manage hundreds of terabytes of intermediate training checkpoints?",
      "expected_answer_keywords": ["artifact retention", "S3 lifecycle rules", "checkpoint pruning", "storage cost optimization", "glacier archival", "automated cleanup"]
    }
  ],
  "mlops_experiment_tracking_registry.model_registry_webhook_automation": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you configure MLflow Model Registry webhooks to automatically trigger CI/CD deployment pipelines on model version promotion?",
      "expected_answer_keywords": ["MLflow webhook", "event trigger", "model promotion webhook", "CI/CD integration", "automated deploy pipeline", "GitHub Actions trigger"]
    }
  ],
  "mlops_experiment_tracking_registry.run_comparison_metric_diffing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you use mlflow.search_runs() programmatically to filter and identify champion models based on metric criteria?",
      "expected_answer_keywords": ["mlflow.search_runs", "filter_string", "metric diffing", "automated leaderboard", "top model selection", "programmatic querying"]
    }
  ],

  # mlops_data_feature_management (9)
  "mlops_data_feature_management.feast_feature_store_architecture": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the core abstractions in Feast Feature Store: Entity, FeatureView, BatchSource, and feast apply.",
      "expected_answer_keywords": ["Feast", "Entity", "FeatureView", "BatchSource", "feast apply", "feature_store.yaml", "feature repository"]
    }
  ],
  "mlops_data_feature_management.point_in_time_correct_historical_joins": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Feast get_historical_features execute point-in-time correct (AS-OF) joins to prevent feature lookahead data leakage?",
      "expected_answer_keywords": ["point-in-time join", "time travel join", "get_historical_features", "data leakage prevention", "entity_df", "as-of join"]
    }
  ],
  "mlops_data_feature_management.online_feature_store_redis_dynamo": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does feast materialize populate online Redis stores from offline sources, and how are features retrieved via get_online_features?",
      "expected_answer_keywords": ["feast materialize", "online store", "Redis", "get_online_features", "low-latency retrieval", "feature cache TTL"]
    }
  ],
  "mlops_data_feature_management.on_demand_streaming_feature_views": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "When should you use Feast OnDemandFeatureViews vs Batch FeatureViews for real-time request-time feature computation?",
      "expected_answer_keywords": ["OnDemandFeatureView", "RequestSource", "request-time computation", "real-time transformation", "streaming push source"]
    }
  ],
  "mlops_data_feature_management.dvc_data_versioning_s3_gcs": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does DVC link small .dvc pointer files in Git with multi-gigabyte dataset binaries stored in S3/GCS remote storage?",
      "expected_answer_keywords": ["DVC", ".dvc file", "dvc remote", "dvc push", "dvc pull", "S3 remote storage", "content-addressable hash"]
    }
  ],
  "mlops_data_feature_management.dvc_pipeline_stages_dvc_yaml": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you author a multi-stage dvc.yaml file defining dependencies (deps), outputs (outs), and parameters (params)?",
      "expected_answer_keywords": ["dvc.yaml", "dvc repro", "deps", "outs", "params.yaml", "pipeline stages", "dependency graph"]
    }
  ],
  "mlops_data_feature_management.training_serving_feature_skew_mitigation": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does a centralized Feature Store eliminate Training-Serving Skew across batch training and real-time inference?",
      "expected_answer_keywords": ["training-serving skew", "single source of truth", "shared feature definition", "consistency", "feature parity", "identical transformation"]
    }
  ],
  "mlops_data_feature_management.hopsworks_feature_store_enterprise": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "What enterprise capabilities do platforms like Hopsworks or Tecton offer over lightweight open-source feature stores?",
      "expected_answer_keywords": ["Hopsworks", "Tecton", "enterprise feature store", "feature catalog", "RBAC access control", "automated feature monitoring", "feature lineage"]
    }
  ],
  "mlops_data_feature_management.dataset_checksums_immutability_archival": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you guarantee cryptographic dataset immutability using SHA-256 checksums and S3 Object Lock for regulatory compliance?",
      "expected_answer_keywords": ["dataset immutability", "SHA-256", "S3 Object Lock", "WORM storage", "compliance auditing", "tamper-proof dataset"]
    }
  ],

  # mlops_pipeline_orchestration (9)
  "mlops_pipeline_orchestration.kubeflow_pipelines_kfp_v2_dsl": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you author containerized pipeline components in Kubeflow Pipelines v2 using @dsl.component and compile to pipeline.yaml?",
      "expected_answer_keywords": ["Kubeflow Pipelines", "KFP v2", "@dsl.component", "@dsl.pipeline", "kfp.compiler", "Input[Artifact]", "Output[Model]"]
    }
  ],
  "mlops_pipeline_orchestration.flyte_orchestration_type_safety": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Flyte enforce compile-time and runtime type safety on workflow inputs and outputs using @task and @workflow decorators?",
      "expected_answer_keywords": ["Flyte", "@task", "@workflow", "Flytekit", "type safety", "FlyteFile", "FlyteDirectory", "strong typing"]
    }
  ],
  "mlops_pipeline_orchestration.argo_workflows_declarative_k8s": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you define a declarative multi-step ML DAG in Argo Workflows using WorkflowTemplate and DAG templates?",
      "expected_answer_keywords": ["Argo Workflows", "WorkflowTemplate", "DAG template", "CRD", "artifact repository", "K8s native", "steps"]
    }
  ],
  "mlops_pipeline_orchestration.pipeline_step_caching_memoization": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does pipeline step caching (memoization) prevent redundant execution of expensive data preparation steps in Kubeflow and Flyte?",
      "expected_answer_keywords": ["memoization", "step caching", "enable_caching", "cache_key", "skip redundant execution", "hash inputs"]
    }
  ],
  "mlops_pipeline_orchestration.gpu_resource_allocation_node_affinity": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure container GPU limits, nodeAffinity, and tolerations in a Kubeflow pipeline step to target dedicated GPU node pools?",
      "expected_answer_keywords": ["nvidia.com/gpu", "nodeAffinity", "tolerations", "taints", "GPU node pool", "resource requests and limits"]
    }
  ],
  "mlops_pipeline_orchestration.airflow_for_ml_operators_sensors": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do Airflow cloud provider operators (SageMakerOperator, VertexAIOperator) trigger and monitor managed training jobs?",
      "expected_answer_keywords": ["Airflow for ML", "SageMakerOperator", "VertexAIOperator", "cloud ML trigger", "Airflow sensor", "asynchronous job monitoring"]
    }
  ],
  "mlops_pipeline_orchestration.pipeline_error_handling_retry_policies": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure exponential backoff retries and on_exit cleanup handlers in Kubeflow Pipelines and Argo Workflows?",
      "expected_answer_keywords": ["retry policy", "exponential backoff", "on_exit handler", "pipeline cleanup", "failure notification", "fault tolerance"]
    }
  ],
  "mlops_pipeline_orchestration.distributed_training_operators_k8s_kubeflow": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does the Kubeflow Training Operator manage PyTorchJob multi-node distributed training and coordinate with Volcano gang scheduling?",
      "expected_answer_keywords": ["Training Operator", "PyTorchJob", "Volcano gang scheduling", "master-worker pods", "all-or-nothing scheduling", "multi-node training"]
    }
  ],
  "mlops_pipeline_orchestration.metaflow_production_deployments_argo": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you compile and deploy Netflix Metaflow workflows to Argo Workflows for scheduled enterprise production execution?",
      "expected_answer_keywords": ["Metaflow", "argo-workflows create", "production scheduling", "FlowSpec export", "seamless deployment", "Argo execution"]
    }
  ],

  # mlops_model_packaging_containerization (9)
  "mlops_model_packaging_containerization.docker_multistage_gpu_builds": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you write a multi-stage Dockerfile using nvidia/cuda runtime and devel images to minimize the final container size?",
      "expected_answer_keywords": ["Dockerfile", "multi-stage build", "nvidia/cuda", "devel build stage", "runtime final stage", "non-root user", "slim container"]
    }
  ],
  "mlops_model_packaging_containerization.bentoml_model_packaging_framework": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you package a model service with BentoML using bentofile.yaml and containerize it into an OCI-compliant image?",
      "expected_answer_keywords": ["BentoML", "bentoml.Service", "bentofile.yaml", "bento build", "bentoml.containerize", "runner definition"]
    }
  ],
  "mlops_model_packaging_containerization.triton_model_repository_configuration": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Describe the directory structure and config.pbtxt configuration for an ONNX model served on Triton Inference Server.",
      "expected_answer_keywords": ["Triton repository", "config.pbtxt", "model.onnx", "platform: onnxruntime_onnx", "max_batch_size", "input/output tensor dimensions"]
    }
  ],
  "mlops_model_packaging_containerization.onnx_torchscript_artifact_packaging": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is serializing models to ONNX or TorchScript preferred over raw Python pickle for production serving environments?",
      "expected_answer_keywords": ["ONNX", "TorchScript", "pickle security vulnerabilities", "C++ inference runtime", "cross-platform portability", "optimized execution"]
    }
  ],
  "mlops_model_packaging_containerization.container_registry_vulnerability_scanning": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you integrate Trivy container vulnerability scanning and Cosign image signing into an automated ML packaging pipeline?",
      "expected_answer_keywords": ["Trivy", "CVE vulnerability scan", "Cosign", "image signing", "container security gate", "ECR / Harbor"]
    }
  ],
  "mlops_model_packaging_containerization.conda_poetry_lockfile_pinning": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is strict lockfile pinning (poetry.lock, uv.lock) required to achieve hermetic builds in containerized ML deployments?",
      "expected_answer_keywords": ["poetry.lock", "uv.lock", "hermetic build", "dependency pinning", "reproducible builds", "deterministic environment"]
    }
  ],
  "mlops_model_packaging_containerization.nvidia_container_toolkit_cuda_compatibility": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain CUDA forward compatibility and how the NVIDIA Container Toolkit exposes host GPU drivers to containerized workloads.",
      "expected_answer_keywords": ["NVIDIA Container Toolkit", "CUDA forward compatibility", "libnvidia-container", "driver injection", "--gpus all", "host driver compatibility"]
    }
  ],
  "mlops_model_packaging_containerization.model_artifact_packaging_formats_safetensors": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How do SafeTensors provide secure zero-copy deserialization compared to standard PyTorch .pth weight checkpoints?",
      "expected_answer_keywords": ["SafeTensors", "zero-copy deserialization", "prevent arbitrary code execution", "pickle exploit prevention", "fast memory mapping"]
    }
  ],
  "mlops_model_packaging_containerization.caching_wheel_compilation_speedups": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you use BuildKit cache mounts and pre-compiled wheel binaries to reduce ML Docker build times from 30 minutes to 2 minutes?",
      "expected_answer_keywords": ["BuildKit", "--mount=type=cache", "pip cache mount", "pre-compiled wheel", "flash-attn pre-build", "Docker build optimization"]
    }
  ],

  # mlops_model_serving_infrastructure (9)
  "mlops_model_serving_infrastructure.kserve_inferenceservice_crd": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you deploy a model on Kubernetes using KServe InferenceService CRD with storageUri pointing to S3?",
      "expected_answer_keywords": ["KServe", "InferenceService", "storageUri", "predictor", "Knative", "scale-to-zero", "K8s manifest"]
    }
  ],
  "mlops_model_serving_infrastructure.seldon_core_advanced_graphs": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you construct a complex multi-model inference graph in Seldon Core with a custom Combiner and Router?",
      "expected_answer_keywords": ["Seldon Core", "SeldonDeployment", "inference graph", "Combiner", "Router", "multi-model pipeline", "predictive graph"]
    }
  ],
  "mlops_model_serving_infrastructure.ray_serve_distributed_inference": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Ray Serve manage actor replica scaling and dynamic request batching using @serve.deployment?",
      "expected_answer_keywords": ["Ray Serve", "@serve.deployment", "actor replicas", "dynamic batching", "fractional GPU allocation", "distributed serving"]
    }
  ],
  "mlops_model_serving_infrastructure.vllm_tgi_high_throughput_llm_serving": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain how vLLM's PagedAttention and continuous batching achieve 10x higher throughput over naive Hugging Face pipeline serving.",
      "expected_answer_keywords": ["vLLM", "PagedAttention", "continuous batching", "KV cache fragmentation", "virtual memory paging", "high throughput LLM serving"]
    }
  ],
  "mlops_model_serving_infrastructure.gpu_autoscaling_keda_prometheus": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you configure KEDA with Prometheus ScaledObjects to autoscale GPU model replicas based on inference queue latency rather than CPU usage?",
      "expected_answer_keywords": ["KEDA", "PrometheusScaledObject", "queue latency scaler", "DCGM metrics", "rapid scale-up", "HPA for GPU"]
    }
  ],
  "mlops_model_serving_infrastructure.dynamic_batching_triton_inference": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does dynamic batching in Triton Inference Server combine concurrent user requests into a single tensor batch to saturate GPUs?",
      "expected_answer_keywords": ["dynamic batching", "Triton", "max_queue_delay_microseconds", "max_batch_size", "GPU saturation", "batch latency trade-off"]
    }
  ],
  "mlops_model_serving_infrastructure.istio_service_mesh_traffic_splitting": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure Istio VirtualService and DestinationRule to route 10% of production traffic to a Canary model deployment?",
      "expected_answer_keywords": ["Istio", "VirtualService", "DestinationRule", "traffic weight", "Canary routing", "mirror traffic", "Service Mesh"]
    }
  ],
  "mlops_model_serving_infrastructure.inference_caching_semantic_redis": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does inference caching in Redis reduce latency and cloud compute costs for repeated prediction requests?",
      "expected_answer_keywords": ["inference cache", "Redis", "sub-millisecond latency", "cache hit ratio", "cost reduction", "hash key caching"]
    }
  ],
  "mlops_model_serving_infrastructure.cold_start_latency_reduction_gpu": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "What strategies eliminate GPU cold start latency in serverless inference (DaemonSet image pre-pulling, memory-mapped weights, warm pools)?",
      "expected_answer_keywords": ["cold start reduction", "DaemonSet image pre-pull", "mmap weights", "warm pools", "fast model hydration", "serverless GPU"]
    }
  ],

  # mlops_ci_cd_continuous_training (9)
  "mlops_ci_cd_continuous_training.cml_github_actions_pull_request_reports": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you use CML (Continuous Machine Learning) in GitHub Actions to train a benchmark model and post metrics and loss plots as PR comments?",
      "expected_answer_keywords": ["CML", "cml send-comment", "GitHub Actions", "PR model evaluation", "automated training in CI", "markdown metrics report"]
    }
  ],
  "mlops_ci_cd_continuous_training.model_validation_gates_threshold_checks": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do automated validation gates in CI pipelines block model deployment if accuracy drops below baseline or latency exceeds SLA?",
      "expected_answer_keywords": ["validation gate", "threshold check", "block deployment", "accuracy SLA", "latency threshold check", "automated quality gate"]
    }
  ],
  "mlops_ci_cd_continuous_training.champion_challenger_evaluation_framework": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you design a Champion-Challenger validation step that compares a newly trained Challenger model against the production Champion on held-out live data?",
      "expected_answer_keywords": ["Champion-Challenger", "Champion model", "Challenger model", "held-out evaluation", "statistical superiority", "model promotion gate"]
    }
  ],
  "mlops_ci_cd_continuous_training.automated_continuous_training_triggers": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do event-driven webhooks triggered by data drift alerts initiate automated Continuous Training (CT) pipeline runs in Kubeflow/Airflow?",
      "expected_answer_keywords": ["Continuous Training", "CT trigger", "event-driven retraining", "drift webhook trigger", "automated pipeline invocation", "idempotency"]
    }
  ],
  "mlops_ci_cd_continuous_training.canary_blue_green_model_rollouts": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you automate progressive Canary model rollouts (1% -> 10% -> 50% -> 100%) using Argo Rollouts with Prometheus metric analysis?",
      "expected_answer_keywords": ["Argo Rollouts", "Canary rollout", "AnalysisTemplate", "Prometheus metric check", "progressive traffic shifting", "automated promotion"]
    }
  ],
  "mlops_ci_cd_continuous_training.automated_rollback_health_probes": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do Argo Rollouts or KServe health probes automatically abort a rollout and revert traffic to the previous version when 5xx errors spike?",
      "expected_answer_keywords": ["automated rollback", "health probes", "5xx error spike", "abort rollout", "instant traffic reversion", "fail-safe"]
    }
  ],
  "mlops_ci_cd_continuous_training.data_pipeline_unit_integration_testing": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you write pytest test suites and mock feature transformers to validate data preprocessing logic in CI before running training jobs?",
      "expected_answer_keywords": ["pytest", "mock feature transformer", "unit testing ML", "synthetic test data", "Great Expectations in CI", "data preprocessing test"]
    }
  ],
  "mlops_ci_cd_continuous_training.gitops_for_ml_argo_flux": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you implement GitOps for ML using Argo CD to synchronize declarative KServe and Seldon manifests from Git to multi-cluster environments?",
      "expected_answer_keywords": ["GitOps", "Argo CD", "Flux", "declarative manifest", "Git single source of truth", "multi-cluster sync", "automated reconciliation"]
    }
  ],
  "mlops_ci_cd_continuous_training.infrastructure_ci_cd_terraform_github_actions": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you design a GitHub Actions workflow that executes terraform plan on PRs and terraform apply on main to provision cloud ML compute?",
      "expected_answer_keywords": ["Terraform CI/CD", "terraform plan PR", "terraform apply main", "GitHub Actions IaC", "automated cloud provisioning", "state locking"]
    }
  ],

  # mlops_monitoring_drift_observability (9)
  "mlops_monitoring_drift_observability.prometheus_grafana_ml_metrics_scraping": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you expose Prometheus metrics (Histogram for latency, Counter for requests/errors) in a Python model serving application and visualize them in Grafana?",
      "expected_answer_keywords": ["Prometheus", "prometheus_client", "Histogram", "Counter", "Grafana dashboard", "metrics endpoint", "ServiceMonitor"]
    }
  ],
  "mlops_monitoring_drift_observability.evidently_ai_automated_drift_dashboards": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you write an automated script using Evidently AI to generate DataDriftPreset reports comparing current production inference to reference training data?",
      "expected_answer_keywords": ["Evidently AI", "DataDriftPreset", "reference vs current data", "Report", "HTML export", "drift visualization"]
    }
  ],
  "mlops_monitoring_drift_observability.statistical_drift_tests_ks_psi_wasserstein": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the formula for Population Stability Index (PSI) and how PSI values (< 0.1, 0.1-0.2, > 0.2) guide model retraining decisions.",
      "expected_answer_keywords": ["PSI", "Population Stability Index", "sum((Actual - Expected) * ln(Actual/Expected))", "PSI thresholds", "drift detection", "retraining trigger"]
    }
  ],
  "mlops_monitoring_drift_observability.prediction_output_distribution_monitoring": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why is monitoring the distribution of predicted probabilities (prediction drift) crucial when true ground truth labels are not immediately available?",
      "expected_answer_keywords": ["prediction drift", "predicted probability distribution", "early warning signal", "no ground truth required", "entropy shift", "confidence monitoring"]
    }
  ],
  "mlops_monitoring_drift_observability.delayed_ground_truth_performance_estimation": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does NannyML's Confidence-based Performance Estimation (CBPE) estimate production metric drops (e.g. ROC-AUC decay) without ground truth labels?",
      "expected_answer_keywords": ["NannyML", "CBPE", "Confidence-based Performance Estimation", "delayed labels", "unlabeled accuracy estimation", "calibrated probabilities"]
    }
  ],
  "mlops_monitoring_drift_observability.alertmanager_webhook_incident_triggers": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you author PrometheusRule alert definitions and configure Alertmanager to dispatch high-priority alerts to PagerDuty when model P99 latency spikes?",
      "expected_answer_keywords": ["Alertmanager", "PrometheusRule", "PagerDuty integration", "latency alert threshold", "for: 5m", "severity: critical", "alert routing"]
    }
  ],
  "mlops_monitoring_drift_observability.model_logging_payload_capture_fluentd": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure FluentBit / Kafka to asynchronously capture inference requests and responses to S3 data lakes without impacting serving latency?",
      "expected_answer_keywords": ["FluentBit", "Fluentd", "asynchronous logging", "Kafka payload capture", "S3 data lake", "zero latency impact", "inference audit log"]
    }
  ],
  "mlops_monitoring_drift_observability.outlier_out_of_distribution_alerting": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you build real-time Out-of-Distribution (OOD) monitoring using Mahalanobis distance on embedding spaces to flag anomalous inputs?",
      "expected_answer_keywords": ["OOD monitoring", "Mahalanobis distance", "embedding anomaly detection", "real-time alert", "input guardrail", "flag anomalous payload"]
    }
  ],
  "mlops_monitoring_drift_observability.automated_model_retraining_trigger_integration": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you architect a closed-loop self-healing MLOps system where drift detection alerts trigger automated retraining and validation in Kubeflow?",
      "expected_answer_keywords": ["closed-loop MLOps", "drift-triggered retraining", "self-healing ML", "webhook integration", "automated retraining pipeline", "Kubeflow trigger"]
    }
  ],

  # mlops_infrastructure_iac_cloud (9)
  "mlops_infrastructure_iac_cloud.terraform_ml_infrastructure_modules": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you structure reusable Terraform modules to provision EKS/GKE clusters, S3 artifact buckets, and PostgreSQL databases for ML platforms?",
      "expected_answer_keywords": ["Terraform module", "EKS / GKE IaC", "S3 bucket provisioning", "RDS PostgreSQL", "remote state", "HCL", "infrastructure as code"]
    }
  ],
  "mlops_infrastructure_iac_cloud.kubernetes_gpu_device_plugin_setup": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you install and verify the NVIDIA GPU Operator / k8s-device-plugin on a Kubernetes cluster to expose nvidia.com/gpu resources?",
      "expected_answer_keywords": ["NVIDIA GPU Operator", "k8s-device-plugin", "nvidia.com/gpu", "kubectl describe node", "GPU allocatable resources", "DaemonSet"]
    }
  ],
  "mlops_infrastructure_iac_cloud.karpenter_just_in_time_gpu_node_provisioning": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you configure Karpenter NodePools to dynamically provision GPU instances (e.g. g5.2xlarge, p4d.24xlarge) directly in response to pending pod requirements?",
      "expected_answer_keywords": ["Karpenter", "NodePool", "EC2NodeClass", "just-in-time GPU provisioning", "instance type selection", "consolidation", "spot and on-demand"]
    }
  ],
  "mlops_infrastructure_iac_cloud.iam_roles_service_accounts_irsa_security": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does IAM Roles for Service Accounts (IRSA / Workload Identity) provide secure least-privilege cloud access to ML pods without hardcoding API keys?",
      "expected_answer_keywords": ["IRSA", "Workload Identity", "ServiceAccount", "OIDC provider", "least privilege", "no hardcoded credentials", "temporary STS tokens"]
    }
  ],
  "mlops_infrastructure_iac_cloud.helm_charts_mlops_platform_deployment": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you customize values.yaml files when deploying MLOps platforms (MLflow, KServe, Prometheus) via Helm?",
      "expected_answer_keywords": ["Helm", "values.yaml", "helm upgrade --install", "custom values", "K8s package management", "chart configuration"]
    }
  ],
  "mlops_infrastructure_iac_cloud.cluster_networking_ingress_cert_manager": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure Ingress-NGINX and cert-manager to automatically provision Let's Encrypt TLS certificates for model prediction endpoints?",
      "expected_answer_keywords": ["Ingress-NGINX", "cert-manager", "Let's Encrypt", "TLS certificate", "ClusterIssuer", "secure endpoint routing"]
    }
  ],
  "mlops_infrastructure_iac_cloud.persistent_volumes_nfs_fast_model_loading": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why is mounting Amazon FSx for Lustre or local NVMe storage preferred over standard S3 download for multi-gigabyte deep learning checkpoint loading?",
      "expected_answer_keywords": ["FSx for Lustre", "NVMe storage", "high throughput POSIX", "fast checkpoint loading", "avoid S3 bottleneck", "PersistentVolume"]
    }
  ],
  "mlops_infrastructure_iac_cloud.multi_tenant_cluster_isolation_namespaces": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you enforce ResourceQuotas, LimitRanges, and NetworkPolicies to isolate ML workloads across multiple data science teams on a shared Kubernetes cluster?",
      "expected_answer_keywords": ["ResourceQuota", "LimitRange", "NetworkPolicy", "namespace isolation", "multi-tenant cluster", "prevent resource hogging"]
    }
  ],
  "mlops_infrastructure_iac_cloud.multi_region_cloud_disaster_recovery": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you design an active-passive multi-region disaster recovery architecture for an enterprise ML platform to satisfy strict RTO and RPO requirements?",
      "expected_answer_keywords": ["Disaster Recovery", "active-passive", "cross-region S3 replication", "Route 53 DNS failover", "RTO", "RPO", "failover runbook"]
    }
  ],

  # mlops_cost_finops_resource_optimization (9)
  "mlops_cost_finops_resource_optimization.multi_instance_gpu_mig_partitioning": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does NVIDIA Multi-Instance GPU (MIG) partition an 80GB A100 GPU into isolated hardware instances with dedicated memory and compute for multiple pods?",
      "expected_answer_keywords": ["MIG", "Multi-Instance GPU", "A100 partitioning", "hardware isolation", "dedicated memory slices", "nvidia.com/mig-*", "QoS guarantee"]
    }
  ],
  "mlops_cost_finops_resource_optimization.gpu_time_slicing_sharing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure NVIDIA GPU time-slicing in Kubernetes to oversubscribe non-MIG GPUs (e.g. T4/L4) across multiple lightweight inference pods?",
      "expected_answer_keywords": ["GPU time-slicing", "fractional GPU sharing", "timeSlicing.resources", "oversubscription", "T4 / L4 sharing", "cost reduction"]
    }
  ],
  "mlops_cost_finops_resource_optimization.spot_instance_orchestration_checkpoints": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you build a resilient training pipeline on AWS Spot instances that listens for 2-minute termination notices and saves checkpoints to S3?",
      "expected_answer_keywords": ["Spot instances", "2-minute termination notice", "spot interruption handler", "automated checkpoint to S3", "fault-tolerant training", "cost savings"]
    }
  ],
  "mlops_cost_finops_resource_optimization.gpu_utilization_profiling_dcgm": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you use NVIDIA Data Center GPU Manager (DCGM) metrics to identify underutilized GPU allocations and tensor core idle time?",
      "expected_answer_keywords": ["DCGM", "DCGM_FI_DEV_GPU_UTIL", "tensor core activity", "memory bandwidth", "underutilized GPU detection", "zombie allocation"]
    }
  ],
  "mlops_cost_finops_resource_optimization.finops_cost_allocation_kubecost": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you use Kubecost and AWS cost allocation tags to calculate and report the exact cost-per-inference for different deployed ML models?",
      "expected_answer_keywords": ["Kubecost", "cost allocation tags", "cost-per-inference", "team chargeback", "FinOps", "cloud spend attribution"]
    }
  ],
  "mlops_cost_finops_resource_optimization.inference_right_sizing_cpu_vs_gpu": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "When is it more cost-effective to deploy an inference model on high-memory Intel Xeon CPUs (AVX-512) or AWS Inferentia rather than expensive NVIDIA GPUs?",
      "expected_answer_keywords": ["right-sizing", "CPU inference", "AVX-512", "AWS Inferentia", "cost-performance benchmarking", "low RPS efficiency"]
    }
  ],
  "mlops_cost_finops_resource_optimization.auto_termination_idle_compute_clusters": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you configure auto-termination and scale-to-zero controllers to shut down idle development Jupyter notebook pods after 1 hour of inactivity?",
      "expected_answer_keywords": ["auto-termination", "idle pod reaper", "scale-to-zero", "inactivity timer", "cost governance", "scheduled shutdown"]
    }
  ],
  "mlops_cost_finops_resource_optimization.model_compaction_for_lower_gpu_tier": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does compressing an LLM from FP16 (32GB VRAM) to INT4 (8GB VRAM) allow it to run on a single affordable T4/L4 GPU instead of an A100?",
      "expected_answer_keywords": ["model compaction", "INT4 / INT8 quantization", "VRAM reduction", "run on L4 / T4", "avoid expensive A100", "hardware cost reduction"]
    }
  ],
  "mlops_cost_finops_resource_optimization.cloud_savings_plans_reserved_instances": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you formulate a multi-year FinOps commitment strategy combining Compute Savings Plans, Reserved Instances, and Spot for an ML platform?",
      "expected_answer_keywords": ["Savings Plans", "Reserved Instances", "EC2 Capacity Blocks", "FinOps commitment strategy", "baseline vs peak workload", "cost optimization"]
    }
  ]
}

assessment_data = {
  "source_id": "assessment",
  "name": "MLOps Engineering Adaptive Technical Assessment",
  "description": "Comprehensive technical question bank and adaptive testing engine for evaluating MLOps Engineer candidate proficiency across all 90 composite subskills.",
  "trigger_conditions": {
    "rules": [
      "When a subskill has status 'not_yet_evidenced' (confidence = 0.0) for a target role level",
      "When a subskill has status 'insufficient_evidence' and confidence < 0.4",
      "When CV/LinkedIn claims a skill but GitHub code has no supporting implementation",
      "When a skill is critical for the target role (importance >= 0.80) and evidence is ambiguous"
    ]
  },
  "question_types": [
    { "type": "conceptual", "strength": 0.6, "description": "Tests deep theoretical, architecture and MLOps platform understanding." },
    { "type": "scenario", "strength": 0.8, "description": "Tests practical problem-solving, pipeline design, and infrastructure troubleshooting." },
    { "type": "practical_task", "strength": 1.0, "description": "Hands-on implementation task validating production MLOps manifests." }
  ],
  "sample_questions_by_composite_key": questions_by_key
}

with open(os.path.join(evidence_dir, 'assessment.json'), 'w', encoding='utf-8') as f:
  json.dump(assessment_data, f, indent=2)

print(f"Generated complete evidence files in {evidence_dir}")
print(f"Total questions mapped in assessment.json: {len(questions_by_key)}")
