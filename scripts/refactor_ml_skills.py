import json
import os

base = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
ml_skills_dir = os.path.join(base, "skills", "machine-learning")
ml_roles_dir = os.path.join(base, "roles", "machine-learning")
ml_evidence_dir = os.path.join(base, "evidence", "machine-learning")

# ─────────────────────────────────────────────────────────────
# 1. DEFINE 3 NEW SKILLS
# ─────────────────────────────────────────────────────────────

# Skill 8: Computer Vision & Deep Learning
skill_cv = {
  "skill_id": "ml_computer_vision_deep_learning",
  "name": "Computer Vision & Visual Deep Learning",
  "description": "Architectures, loss functions, augmentations, and modern neural vision modeling from CNNs to Vision Transformers.",
  "category": "machine-learning",
  "subskills": [
    {
      "id": "cnn_architectures_resnet_convnext",
      "name": "CNN Architectures & Modern Backbones (ResNet, ConvNeXt)",
      "description": "Residual connections, bottleneck blocks, depthwise separable convolutions, and modern ConvNeXt/EfficientNet backbones.",
      "keywords": ["ResNet", "ConvNeXt", "EfficientNet", "Residual Connections", "Bottleneck", "CNN"]
    },
    {
      "id": "vision_transformers_vit_swin",
      "name": "Vision Transformers (ViT, Swin, Patch Embeddings)",
      "description": "Patch partitioning, linear projection of flattened patches, multi-head self-attention on images, Swin hierarchical shifted windows.",
      "keywords": ["ViT", "Vision Transformer", "Swin Transformer", "Patch Embedding", "Self-Attention Vision"]
    },
    {
      "id": "object_detection_yolo_faster_rcnn",
      "name": "Object Detection & Localization (YOLO, Faster R-CNN)",
      "description": "Anchor boxes, region proposal networks (RPN), single-stage vs two-stage detectors, Non-Maximum Suppression (NMS), and mAP calculation.",
      "keywords": ["YOLO", "Faster R-CNN", "RPN", "Non-Maximum Suppression", "NMS", "Object Detection", "mAP"]
    },
    {
      "id": "semantic_instance_segmentation_unet_mask_rcnn",
      "name": "Semantic & Instance Segmentation (U-Net, Mask R-CNN)",
      "description": "Encoder-decoder architectures with skip connections, pixel-level classification, RoIAlign, and mask prediction heads.",
      "keywords": ["U-Net", "Mask R-CNN", "Semantic Segmentation", "Instance Segmentation", "Skip Connections", "RoIAlign"]
    },
    {
      "id": "image_data_augmentation_albumentations",
      "name": "Image Augmentation & Synthetic Perturbation (Albumentations)",
      "description": "Geometric transformations, color jittering, CutMix, MixUp, AutoAugment, and RandAugment for vision regularization.",
      "keywords": ["Albumentations", "CutMix", "MixUp", "AutoAugment", "Image Augmentation", "Data Augmentation"]
    },
    {
      "id": "transfer_learning_feature_extraction",
      "name": "Vision Transfer Learning & Backbone Fine-Tuning",
      "description": "Pretrained ImageNet weights, progressive unfreezing, discriminative learning rates, and linear probing vs end-to-end fine-tuning.",
      "keywords": ["Transfer Learning", "Fine-Tuning", "Pretrained Weights", "Feature Extraction", "Linear Probing"]
    },
    {
      "id": "loss_functions_focal_dice_iou",
      "name": "Vision Loss Functions (Focal Loss, Dice Loss, IoU Loss)",
      "description": "Class imbalance handling in dense prediction, Focal loss for hard examples, Dice loss, and Generalized IoU loss.",
      "keywords": ["Focal Loss", "Dice Loss", "IoU Loss", "GIoU", "Loss Functions Vision"]
    },
    {
      "id": "self_supervised_vision_clip_dino",
      "name": "Self-Supervised & Multimodal Vision (CLIP, DINO, SimCLR)",
      "description": "Contrastive image-text pretraining, self-distillation without labels (DINO v1/v2), and representation learning.",
      "keywords": ["CLIP", "DINO", "SimCLR", "Contrastive Learning", "Self-Supervised Vision"]
    },
    {
      "id": "video_spatial_temporal_modeling",
      "name": "Spatial-Temporal Video & Sequence Modeling",
      "description": "3D Convolutions (C3D, I3D), VideoMAE, temporal attention, and action recognition pipelines.",
      "keywords": ["3D CNN", "VideoMAE", "Action Recognition", "Temporal Modeling", "Optical Flow"]
    }
  ],
  "levels": {
    "junior": {
      "expected_subskills": [
        "cnn_architectures_resnet_convnext",
        "image_data_augmentation_albumentations",
        "transfer_learning_feature_extraction"
      ]
    },
    "mid": {
      "expected_subskills": [
        "vision_transformers_vit_swin",
        "object_detection_yolo_faster_rcnn",
        "loss_functions_focal_dice_iou"
      ]
    },
    "senior": {
      "expected_subskills": [
        "semantic_instance_segmentation_unet_mask_rcnn",
        "self_supervised_vision_clip_dino",
        "video_spatial_temporal_modeling"
      ]
    }
  },
  "evidence": {
    "github": [
      {
        "signal": "Uses Albumentations and torchvision transforms for image pipeline",
        "detection": "content_analysis",
        "pattern": "albumentations|torchvision.transforms|CutMix|MixUp",
        "strength": 0.6,
        "maps_to": ["ml_computer_vision_deep_learning.image_data_augmentation_albumentations"]
      },
      {
        "signal": "Implements ResNet, ConvNeXt, or ViT backbone models",
        "detection": "content_analysis",
        "pattern": "timm.create_model|models.resnet|ConvNeXt|ViT|VisionTransformer",
        "strength": 0.6,
        "maps_to": [
          "ml_computer_vision_deep_learning.cnn_architectures_resnet_convnext",
          "ml_computer_vision_deep_learning.vision_transformers_vit_swin"
        ]
      },
      {
        "signal": "Trains YOLO or Faster R-CNN object detection pipelines",
        "detection": "content_analysis",
        "pattern": "ultralytics|yolov8|yolov5|fasterrcnn_resnet50_fpn",
        "strength": 0.6,
        "maps_to": ["ml_computer_vision_deep_learning.object_detection_yolo_faster_rcnn"]
      }
    ]
  }
}

# Skill 9: Time Series & Forecasting
skill_ts = {
  "skill_id": "ml_time_series_forecasting",
  "name": "Time Series Analysis & Forecasting",
  "description": "Decomposition, stationarity, classical statistical models, tree-based lag engineering, and deep temporal architectures.",
  "category": "machine-learning",
  "subskills": [
    {
      "id": "time_series_decomposition_trend_seasonality",
      "name": "Time Series Decomposition & Additive/Multiplicative Components",
      "description": "Decomposing temporal signals into trend, seasonal, cyclical, and irregular/noise components using classical and STL decomposition.",
      "keywords": ["STL Decomposition", "Trend", "Seasonality", "Additive Model", "Multiplicative Model"]
    },
    {
      "id": "stationarity_differencing_unit_root_tests",
      "name": "Stationarity Transformations & Unit Root Testing (ADF, KPSS)",
      "description": "Checking covariance stationarity, Augmented Dickey-Fuller (ADF) test, KPSS test, fractional differencing, and Box-Cox transforms.",
      "keywords": ["ADF Test", "KPSS Test", "Stationarity", "Differencing", "Unit Root", "Box-Cox"]
    },
    {
      "id": "statistical_forecasting_arima_sarima",
      "name": "Statistical Univariate Forecasting (ARIMA, SARIMA, Auto-ARIMA)",
      "description": "Autoregressive (AR), Moving Average (MA), seasonal integration (SARIMA), ACF/PACF interpretation, and Box-Jenkins methodology.",
      "keywords": ["ARIMA", "SARIMA", "Auto-ARIMA", "ACF", "PACF", "Box-Jenkins"]
    },
    {
      "id": "exponential_smoothing_holt_winters",
      "name": "Exponential Smoothing & State Space Models (Holt-Winters, ETS)",
      "description": "Simple Exponential Smoothing (SES), Holt's linear trend, Holt-Winters seasonal exponential smoothing, and ETS state space formulation.",
      "keywords": ["Holt-Winters", "Exponential Smoothing", "ETS", "Damped Trend"]
    },
    {
      "id": "machine_learning_time_series_lag_features",
      "name": "Tree-Based Forecasting & Lag/Rolling Feature Engineering",
      "description": "Autoregressive lag creation, rolling mean/std/min/max windows, expanding features, cyclical calendar encodings with LightGBM/XGBoost.",
      "keywords": ["Lag Features", "Rolling Window", "Expanding Window", "Cyclical Features", "Direct Forecasting", "Recursive Forecasting"]
    },
    {
      "id": "deep_learning_forecasting_lstm_tcn",
      "name": "Sequential Neural Forecasting (LSTM, GRU, TCN, N-BEATS)",
      "description": "Recurrent architectures for temporal modeling, Temporal Convolutional Networks (dilated causal convolutions), and N-BEATS basis expansions.",
      "keywords": ["LSTM Forecasting", "GRU", "TCN", "Temporal Convolutional Network", "N-BEATS", "NeuralProphet"]
    },
    {
      "id": "temporal_fusion_transformers_patchtst",
      "name": "Transformer Forecasting Architectures (TFT, PatchTST, Informer)",
      "description": "Self-attention on time series, Temporal Fusion Transformer for static/dynamic metadata gating, PatchTST channel independence.",
      "keywords": ["Temporal Fusion Transformer", "TFT", "PatchTST", "Informer", "Autoformer"]
    },
    {
      "id": "time_series_cross_validation_backtesting",
      "name": "Temporal Validation & Backtesting Strategies (TimeSeriesSplit)",
      "description": "Preventing future data leakage with TimeSeriesSplit, rolling origin evaluation, blocked cross-validation, and expanding window backtesting.",
      "keywords": ["TimeSeriesSplit", "Rolling Origin", "Backtesting", "Walk-Forward Validation", "Data Leakage Temporal"]
    },
    {
      "id": "evaluation_metrics_mape_smape_wape",
      "name": "Forecast Accuracy Metrics & Diagnostics (MAPE, WAPE, Pinball)",
      "description": "Mean Absolute Percentage Error (MAPE), symmetric MAPE, Weighted Absolute Percentage Error (WAPE), MASE, and Pinball loss for quantiles.",
      "keywords": ["MAPE", "sMAPE", "WAPE", "MASE", "Pinball Loss", "Quantile Loss"]
    }
  ],
  "levels": {
    "junior": {
      "expected_subskills": [
        "time_series_decomposition_trend_seasonality",
        "stationarity_differencing_unit_root_tests",
        "evaluation_metrics_mape_smape_wape"
      ]
    },
    "mid": {
      "expected_subskills": [
        "statistical_forecasting_arima_sarima",
        "exponential_smoothing_holt_winters",
        "machine_learning_time_series_lag_features"
      ]
    },
    "senior": {
      "expected_subskills": [
        "deep_learning_forecasting_lstm_tcn",
        "temporal_fusion_transformers_patchtst",
        "time_series_cross_validation_backtesting"
      ]
    }
  },
  "evidence": {
    "github": [
      {
        "signal": "Uses statsmodels or prophet for time series analysis",
        "detection": "content_analysis",
        "pattern": "statsmodels.tsa|prophet|Prophet|pmdarima|auto_arima",
        "strength": 0.6,
        "maps_to": [
          "ml_time_series_forecasting.statistical_forecasting_arima_sarima",
          "ml_time_series_forecasting.stationarity_differencing_unit_root_tests"
        ]
      },
      {
        "signal": "Implements neural or lag-based time series pipelines with TimeSeriesSplit",
        "detection": "content_analysis",
        "pattern": "TimeSeriesSplit|rolling_origin|neuralforecast|darts.models|pytorch_forecasting",
        "strength": 0.6,
        "maps_to": [
          "ml_time_series_forecasting.machine_learning_time_series_lag_features",
          "ml_time_series_forecasting.time_series_cross_validation_backtesting"
        ]
      }
    ]
  }
}

# Skill 10: Experimentation & Research Methodology
skill_exp = {
  "skill_id": "ml_experimentation_research_methodology",
  "name": "ML Experimentation & Research Methodology",
  "description": "Scientific hypothesis testing, experimental design, baseline modeling, ablation studies, error slicing, and reproducible discovery.",
  "category": "machine-learning",
  "subskills": [
    {
      "id": "hypothesis_formulation_scientific_method",
      "name": "Scientific Hypothesis Formulation & Problem Structuring",
      "description": "Translating ambiguous business/scientific problems into testable ML hypotheses with clear dependent/independent variables.",
      "keywords": ["Hypothesis Testing", "Problem Framing", "Scientific Method", "Research Design"]
    },
    {
      "id": "ab_testing_design_power_analysis",
      "name": "Experimental Design & Statistical Power Analysis",
      "description": "Sample size determination, minimum detectable effect (MDE), significance level (alpha), statistical power (1-beta), and randomized trials.",
      "keywords": ["Power Analysis", "Sample Size", "MDE", "Randomized Controlled Trial", "A/B Testing Design"]
    },
    {
      "id": "statistical_significance_p_values_confidence_intervals",
      "name": "Statistical Significance, P-values & Multiple Testing",
      "description": "Parametric/non-parametric tests (t-test, Mann-Whitney U, ANOVA), Bonferroni/FDR corrections, and bootstrapping confidence intervals.",
      "keywords": ["P-value", "Confidence Interval", "T-test", "Mann-Whitney", "Bonferroni", "FDR", "Bootstrapping"]
    },
    {
      "id": "baseline_model_selection_heuristics",
      "name": "Baseline Model Formulation & Simple Benchmark Heuristics",
      "description": "Establishing zero-cost baselines (majority class, mean/median, heuristic rules) to rigorously justify model complexity increases.",
      "keywords": ["Baseline Model", "Heuristic Benchmark", "DummyClassifier", "DummyRegressor", "Benchmark"]
    },
    {
      "id": "error_analysis_confusion_matrix_slicing",
      "name": "Cohort Error Analysis & Data Slicing Diagnostics",
      "description": "Residual inspection, error taxonomy categorization, slice-based evaluation to identify systemic failure modes in subpopulations.",
      "keywords": ["Error Analysis", "Data Slicing", "Failure Modes", "Residual Analysis", "Model Diagnostics"]
    },
    {
      "id": "ablation_studies_feature_attribution",
      "name": "Ablation Studies & Model Component Isolation",
      "description": "Systematic removal of architectural components, regularizers, or feature subsets to isolate causal performance drivers.",
      "keywords": ["Ablation Study", "Component Isolation", "Sensitivity Analysis", "Feature Ablation"]
    },
    {
      "id": "research_reproducibility_deterministic_seeds",
      "name": "Research Reproducibility, Deterministic Seeds & Environment Pinning",
      "description": "Deterministic CUDA execution, random seed management across NumPy/PyTorch/Python, environment pinning for exact replication.",
      "keywords": ["Reproducibility", "Deterministic Seed", "torch.manual_seed", "CUDNN Deterministic"]
    },
    {
      "id": "metric_selection_tradeoff_analysis",
      "name": "Primary vs Guardrail Metrics & Strategic Trade-off Analysis",
      "description": "Selecting primary optimization objectives vs guardrail/constraint metrics (e.g. latency vs accuracy, precision vs recall trade-offs).",
      "keywords": ["Guardrail Metrics", "Metric Tradeoff", "Pareto Frontier", "Objective Function"]
    },
    {
      "id": "literature_review_state_of_the_art_benchmarking",
      "name": "SOTA Literature Review & Standardized Benchmarking",
      "description": "Tracking ArXiv research, evaluating models on benchmark suites (GLUE, SuperGLUE, ImageNet, MMLU), and reproducing papers.",
      "keywords": ["Literature Review", "Benchmark Datasets", "SOTA", "Research Reproduction"]
    }
  ],
  "levels": {
    "junior": {
      "expected_subskills": [
        "hypothesis_formulation_scientific_method",
        "baseline_model_selection_heuristics",
        "research_reproducibility_deterministic_seeds"
      ]
    },
    "mid": {
      "expected_subskills": [
        "ab_testing_design_power_analysis",
        "statistical_significance_p_values_confidence_intervals",
        "error_analysis_confusion_matrix_slicing"
      ]
    },
    "senior": {
      "expected_subskills": [
        "ablation_studies_feature_attribution",
        "metric_selection_tradeoff_analysis",
        "literature_review_state_of_the_art_benchmarking"
      ]
    }
  },
  "evidence": {
    "github": [
      {
        "signal": "Sets deterministic seeds and documents experimental ablations",
        "detection": "content_analysis",
        "pattern": "manual_seed|np.random.seed|torch.cuda.manual_seed_all|ablation_study",
        "strength": 0.6,
        "maps_to": [
          "ml_experimentation_research_methodology.research_reproducibility_deterministic_seeds",
          "ml_experimentation_research_methodology.ablation_studies_feature_attribution"
        ]
      },
      {
        "signal": "Implements statistical hypothesis testing or power analysis",
        "detection": "content_analysis",
        "pattern": "scipy.stats.ttest|statsmodels.stats.power|scipy.stats.mannwhitneyu",
        "strength": 0.6,
        "maps_to": [
          "ml_experimentation_research_methodology.statistical_significance_p_values_confidence_intervals",
          "ml_experimentation_research_methodology.ab_testing_design_power_analysis"
        ]
      }
    ]
  }
}

# ─────────────────────────────────────────────────────────────
# 2. WRITE NEW SKILL FILES & DELETE OLD ONES
# ─────────────────────────────────────────────────────────────
old_skills = [
    "ml_model_deployment_serving.json",
    "ml_monitoring_drift_observability.json",
    "ml_pipelines_orchestration.json"
]
for old_f in old_skills:
    old_p = os.path.join(ml_skills_dir, old_f)
    if os.path.exists(old_p):
        os.remove(old_p)
        print(f"[REMOVED OLD SKILL] {old_f}")

with open(os.path.join(ml_skills_dir, "ml_computer_vision_deep_learning.json"), "w", encoding="utf-8") as f:
    json.dump(skill_cv, f, indent=2, ensure_ascii=False)
print("[CREATED NEW SKILL] ml_computer_vision_deep_learning.json")

with open(os.path.join(ml_skills_dir, "ml_time_series_forecasting.json"), "w", encoding="utf-8") as f:
    json.dump(skill_ts, f, indent=2, ensure_ascii=False)
print("[CREATED NEW SKILL] ml_time_series_forecasting.json")

with open(os.path.join(ml_skills_dir, "ml_experimentation_research_methodology.json"), "w", encoding="utf-8") as f:
    json.dump(skill_exp, f, indent=2, ensure_ascii=False)
print("[CREATED NEW SKILL] ml_experimentation_research_methodology.json")

# ─────────────────────────────────────────────────────────────
# 3. UPDATE ROLES (junior.json, mid.json, senior.json)
# ─────────────────────────────────────────────────────────────
new_skill_ids = [
    {"skill_id": "ml_computer_vision_deep_learning", "importance": 0.8},
    {"skill_id": "ml_time_series_forecasting", "importance": 0.8},
    {"skill_id": "ml_experimentation_research_methodology", "importance": 0.85}
]
old_skill_id_set = {
    "ml_model_deployment_serving",
    "ml_monitoring_drift_observability",
    "ml_pipelines_orchestration"
}

for rfile in ["junior.json", "mid.json", "senior.json"]:
    rpath = os.path.join(ml_roles_dir, rfile)
    with open(rpath, "r", encoding="utf-8") as f:
        rdata = json.load(f)
    
    updated_skills = [s for s in rdata.get("skills", []) if s.get("skill_id") not in old_skill_id_set]
    for ns in new_skill_ids:
        updated_skills.append(ns)
    rdata["skills"] = updated_skills
    
    with open(rpath, "w", encoding="utf-8") as f:
        json.dump(rdata, f, indent=2, ensure_ascii=False)
    print(f"[UPDATED ROLE] {rfile}")

# ─────────────────────────────────────────────────────────────
# 4. UPDATE EVIDENCE (github.json & cv.json)
# ─────────────────────────────────────────────────────────────
github_path = os.path.join(ml_evidence_dir, "github.json")
with open(github_path, "r", encoding="utf-8") as f:
    gdata = json.load(f)

# Update dependency mappings
deps = gdata.get("preprocessing_pipeline", {}).get("steps", [])
for step in deps:
    if step.get("name") == "dependency_extraction":
        rd = step.get("relevant_dependencies", {})
        for old_k in old_skill_id_set:
            if old_k in rd:
                del rd[old_k]
        rd["ml_computer_vision_deep_learning"] = ["torchvision", "albumentations", "timm", "ultralytics", "opencv-python"]
        rd["ml_time_series_forecasting"] = ["statsmodels", "prophet", "pmdarima", "darts", "neuralforecast"]
        rd["ml_experimentation_research_methodology"] = ["scipy", "statsmodels"]

with open(github_path, "w", encoding="utf-8") as f:
    json.dump(gdata, f, indent=2, ensure_ascii=False)
print("[UPDATED EVIDENCE] github.json")

# Update cv.json
cv_path = os.path.join(ml_evidence_dir, "cv.json")
with open(cv_path, "r", encoding="utf-8") as f:
    cvdata = json.load(f)

# Replace patterns
cv_patterns = [
    {
      "pattern": "PyTorch|TorchScript|DDP|DeepSpeed|FSDP",
      "maps_to": [
        "ml_deep_learning_architectures.pytorch_core_autograd_nn_module",
        "ml_deep_learning_architectures.transformer_self_attention_mechanisms",
        "ml_deep_learning_architectures.distributed_training_ddp_fsdp"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "XGBoost|LightGBM|CatBoost|Scikit-Learn|Random Forest",
      "maps_to": [
        "ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost",
        "ml_classical_algorithms.random_forests_bagging",
        "ml_classical_algorithms.linear_logistic_regression_regularization"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "Computer Vision|CNN|ResNet|Vision Transformer|YOLO|Object Detection|Albumentations",
      "maps_to": [
        "ml_computer_vision_deep_learning.cnn_architectures_resnet_convnext",
        "ml_computer_vision_deep_learning.vision_transformers_vit_swin",
        "ml_computer_vision_deep_learning.object_detection_yolo_faster_rcnn",
        "ml_computer_vision_deep_learning.image_data_augmentation_albumentations"
      ],
      "strength_modifier": 1.1
    },
    {
      "pattern": "Time Series Forecasting|ARIMA|SARIMA|Prophet|Temporal Fusion Transformer|TimeSeriesSplit",
      "maps_to": [
        "ml_time_series_forecasting.statistical_forecasting_arima_sarima",
        "ml_time_series_forecasting.machine_learning_time_series_lag_features",
        "ml_time_series_forecasting.temporal_fusion_transformers_patchtst",
        "ml_time_series_forecasting.time_series_cross_validation_backtesting"
      ],
      "strength_modifier": 1.1
    },
    {
      "pattern": "A/B Testing|Power Analysis|Hypothesis Testing|Ablation Studies|Error Analysis",
      "maps_to": [
        "ml_experimentation_research_methodology.ab_testing_design_power_analysis",
        "ml_experimentation_research_methodology.statistical_significance_p_values_confidence_intervals",
        "ml_experimentation_research_methodology.ablation_studies_feature_attribution",
        "ml_experimentation_research_methodology.error_analysis_confusion_matrix_slicing"
      ],
      "strength_modifier": 1.1
    },
    {
      "pattern": "TensorRT|Quantization|INT8|Pruning|Knowledge Distillation",
      "maps_to": [
        "ml_model_optimization_compression.tensorrt_gpu_acceleration",
        "ml_model_optimization_compression.post_training_quantization_ptq",
        "ml_model_optimization_compression.knowledge_distillation_teacher_student"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "Optuna|Ray Tune|Hyperparameter Optimization|Bayesian Optimization",
      "maps_to": [
        "ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna",
        "ml_hyperparameter_optimization.early_stopping_pruning_strategies",
        "ml_hyperparameter_optimization.distributed_hyperparameter_tuning_ray"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "Feature Engineering|ColumnTransformer|Target Encoding|Imputation",
      "maps_to": [
        "ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings",
        "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer",
        "ml_feature_engineering_preprocessing.missing_data_imputation_strategies"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "Cross-Validation|ROC-AUC|PR-AUC|Calibration|A/B Testing",
      "maps_to": [
        "ml_model_evaluation_validation.cross_validation_strategies_leakage",
        "ml_model_evaluation_validation.classification_metrics_pr_roc",
        "ml_model_evaluation_validation.probability_calibration_platt_isotonic"
      ],
      "strength_modifier": 1.0
    },
    {
      "pattern": "Linear Algebra|Optimization|SGD|Adam|MLE|Loss Functions",
      "maps_to": [
        "ml_mathematics_foundations.first_order_optimization_sgd_adam",
        "ml_mathematics_foundations.loss_functions_mathematics",
        "ml_mathematics_foundations.matrix_operations_decompositions"
      ],
      "strength_modifier": 1.0
    }
]

cvdata["signal_mapping"]["patterns"] = cv_patterns
with open(cv_path, "w", encoding="utf-8") as f:
    json.dump(cvdata, f, indent=2, ensure_ascii=False)
print("[UPDATED EVIDENCE] cv.json")

# ─────────────────────────────────────────────────────────────
# 5. UPDATE ASSESSMENT (assessment.json)
# ─────────────────────────────────────────────────────────────
ass_path = os.path.join(ml_evidence_dir, "assessment.json")
with open(ass_path, "r", encoding="utf-8") as f:
    assdata = json.load(f)

q_map = assdata.get("sample_questions_by_composite_key", {})

# Remove old keys
for k in list(q_map.keys()):
    if any(k.startswith(f"{old_id}.") for old_id in old_skill_id_set):
        del q_map[k]

# Add questions for 3 new skills (27 new subskills)
new_questions = {
    # CV
    "ml_computer_vision_deep_learning.cnn_architectures_resnet_convnext": [
        {
            "question": "How do residual skip connections in ResNet resolve the vanishing gradient problem in very deep CNNs?",
            "expected_answer_keywords": ["identity mapping", "residual connection", "vanishing gradient", "gradient highway", "f(x) + x"]
        }
    ],
    "ml_computer_vision_deep_learning.vision_transformers_vit_swin": [
        {
            "question": "Explain how Vision Transformers (ViT) divide an image into patches and process them using self-attention compared to convolutional inductive bias.",
            "expected_answer_keywords": ["patch embedding", "linear projection", "self-attention", "inductive bias", "global context"]
        }
    ],
    "ml_computer_vision_deep_learning.object_detection_yolo_faster_rcnn": [
        {
            "question": "What is Non-Maximum Suppression (NMS) in object detection and how does IoU thresholding filter overlapping bounding boxes?",
            "expected_answer_keywords": ["non-maximum suppression", "nms", "iou", "bounding box", "confidence score", "overlap"]
        }
    ],
    "ml_computer_vision_deep_learning.semantic_instance_segmentation_unet_mask_rcnn": [
        {
            "question": "How does U-Net's skip connection structure preserve fine-grained spatial localization for pixel-level semantic segmentation?",
            "expected_answer_keywords": ["skip connections", "encoder-decoder", "spatial resolution", "localization", "pixel classification"]
        }
    ],
    "ml_computer_vision_deep_learning.image_data_augmentation_albumentations": [
        {
            "question": "How do CutMix and MixUp regularization techniques improve vision model generalization and robustness against adversarial perturbations?",
            "expected_answer_keywords": ["cutmix", "mixup", "linear interpolation", "regularization", "generalization", "data augmentation"]
        }
    ],
    "ml_computer_vision_deep_learning.transfer_learning_feature_extraction": [
        {
            "question": "What is the strategic trade-off between linear probing (frozen backbone) and end-to-end fine-tuning on a small custom dataset?",
            "expected_answer_keywords": ["linear probing", "fine-tuning", "overfitting", "feature extraction", "learning rate", "frozen layers"]
        }
    ],
    "ml_computer_vision_deep_learning.loss_functions_focal_dice_iou": [
        {
            "question": "How does Focal Loss dynamically down-weight easy examples to address extreme foreground-background class imbalance in dense object detection?",
            "expected_answer_keywords": ["focal loss", "class imbalance", "modulating factor", "cross entropy", "easy examples", "hard negatives"]
        }
    ],
    "ml_computer_vision_deep_learning.self_supervised_vision_clip_dino": [
        {
            "question": "Explain how CLIP uses contrastive learning over image-text pairs to achieve zero-shot visual classification.",
            "expected_answer_keywords": ["clip", "contrastive learning", "zero-shot", "cosine similarity", "image-text embedding"]
        }
    ],
    "ml_computer_vision_deep_learning.video_spatial_temporal_modeling": [
        {
            "question": "How do 3D convolutions (C3D/I3D) capture temporal dynamics across consecutive video frames compared to 2D CNNs?",
            "expected_answer_keywords": ["3d convolution", "temporal dimension", "video frames", "spatial temporal", "action recognition"]
        }
    ],
    # Time Series
    "ml_time_series_forecasting.time_series_decomposition_trend_seasonality": [
        {
            "question": "When should an additive decomposition model be chosen over a multiplicative decomposition model for time series data?",
            "expected_answer_keywords": ["additive", "multiplicative", "seasonal variation", "constant magnitude", "proportional to trend"]
        }
    ],
    "ml_time_series_forecasting.stationarity_differencing_unit_root_tests": [
        {
            "question": "How do you interpret conflicting Augmented Dickey-Fuller (ADF) and KPSS unit root test results to establish trend vs difference stationarity?",
            "expected_answer_keywords": ["adf test", "kpss test", "null hypothesis", "stationarity", "unit root", "differencing"]
        }
    ],
    "ml_time_series_forecasting.statistical_forecasting_arima_sarima": [
        {
            "question": "How do Autocorrelation (ACF) and Partial Autocorrelation (PACF) plots guide the selection of AR(p) and MA(q) order parameters in ARIMA modeling?",
            "expected_answer_keywords": ["acf", "pacf", "autoregressive", "moving average", "cut-off", "geometric decay", "arima"]
        }
    ],
    "ml_time_series_forecasting.exponential_smoothing_holt_winters": [
        {
            "question": "Explain the role of level, trend, and seasonal smoothing parameters (alpha, beta, gamma) in the Holt-Winters exponential smoothing model.",
            "expected_answer_keywords": ["holt-winters", "level", "trend", "seasonality", "smoothing parameters", "alpha beta gamma"]
        }
    ],
    "ml_time_series_forecasting.machine_learning_time_series_lag_features": [
        {
            "question": "How do you engineer lag and rolling window features for tabular gradient boosting without causing future data leakage in multi-step forecasting?",
            "expected_answer_keywords": ["lag features", "rolling window", "data leakage", "direct forecasting", "recursive forecasting", "lightgbm"]
        }
    ],
    "ml_time_series_forecasting.deep_learning_forecasting_lstm_tcn": [
        {
            "question": "Why do Temporal Convolutional Networks (TCNs) with dilated causal convolutions often outperform standard RNNs/LSTMs in long-range sequence modeling?",
            "expected_answer_keywords": ["tcn", "dilated convolution", "causal convolution", "receptive field", "vanishing gradient", "parallel training"]
        }
    ],
    "ml_time_series_forecasting.temporal_fusion_transformers_patchtst": [
        {
            "question": "How does the Temporal Fusion Transformer (TFT) utilize variable selection networks and gated residual networks to incorporate static metadata alongside dynamic time series?",
            "expected_answer_keywords": ["temporal fusion transformer", "tft", "variable selection", "gated residual", "static metadata", "self-attention"]
        }
    ],
    "ml_time_series_forecasting.time_series_cross_validation_backtesting": [
        {
            "question": "Why is standard k-fold cross-validation invalid for time series forecasting, and how does expanding window TimeSeriesSplit prevent lookahead bias?",
            "expected_answer_keywords": ["timeseriessplit", "rolling origin", "lookahead bias", "temporal ordering", "backtesting"]
        }
    ],
    "ml_time_series_forecasting.evaluation_metrics_mape_smape_wape": [
        {
            "question": "Why is Mean Absolute Percentage Error (MAPE) problematic when actual values are close to zero, and how does WAPE resolve this issue?",
            "expected_answer_keywords": ["mape", "wape", "division by zero", "asymmetry", "weighted absolute percentage error"]
        }
    ],
    # Experimentation
    "ml_experimentation_research_methodology.hypothesis_formulation_scientific_method": [
        {
            "question": "How do you translate a vague business objective (e.g. 'improve user retention') into a testable machine learning research hypothesis?",
            "expected_answer_keywords": ["hypothesis", "independent variable", "dependent variable", "objective function", "measurable metric"]
        }
    ],
    "ml_experimentation_research_methodology.ab_testing_design_power_analysis": [
        {
            "question": "How does statistical power analysis calculate the minimum sample size needed given an expected Minimum Detectable Effect (MDE) and alpha level?",
            "expected_answer_keywords": ["power analysis", "sample size", "mde", "alpha", "type i error", "type ii error", "statistical power"]
        }
    ],
    "ml_experimentation_research_methodology.statistical_significance_p_values_confidence_intervals": [
        {
            "question": "Why is Bonferroni or False Discovery Rate (FDR) correction necessary when conducting multiple simultaneous hypothesis tests on ML model cohorts?",
            "expected_answer_keywords": ["bonferroni", "false discovery rate", "fdr", "multiple testing", "family-wise error rate", "p-value"]
        }
    ],
    "ml_experimentation_research_methodology.baseline_model_selection_heuristics": [
        {
            "question": "Why is evaluating against zero-cost heuristic or dummy baselines critical before committing to training complex deep neural architectures?",
            "expected_answer_keywords": ["heuristic baseline", "dummy classifier", "model complexity", "benchmark", "occams razor", "roi"]
        }
    ],
    "ml_experimentation_research_methodology.error_analysis_confusion_matrix_slicing": [
        {
            "question": "How does data slicing and subgroup error taxonomy analysis uncover critical model blind spots that aggregate accuracy metrics mask?",
            "expected_answer_keywords": ["data slicing", "error analysis", "subgroups", "disaggregated metrics", "failure modes", "confusion matrix"]
        }
    ],
    "ml_experimentation_research_methodology.ablation_studies_feature_attribution": [
        {
            "question": "What is an ablation study in empirical ML research, and how does systematically removing components isolate causal performance gains?",
            "expected_answer_keywords": ["ablation study", "component isolation", "causal attribution", "feature removal", "empirical validation"]
        }
    ],
    "ml_experimentation_research_methodology.research_reproducibility_deterministic_seeds": [
        {
            "question": "How do you ensure full bitwise reproducibility in PyTorch experiments across random seeds, cuDNN non-deterministic algorithms, and multi-GPU workers?",
            "expected_answer_keywords": ["torch.manual_seed", "cudnn.deterministic", "reproducibility", "random seed", "dataloader worker_init_fn"]
        }
    ],
    "ml_experimentation_research_methodology.metric_selection_tradeoff_analysis": [
        {
            "question": "How do you balance primary optimization metrics against guardrail and operational constraints (such as inference latency and memory footprint)?",
            "expected_answer_keywords": ["primary metric", "guardrail metric", "pareto frontier", "latency constraint", "trade-off analysis"]
        }
    ],
    "ml_experimentation_research_methodology.literature_review_state_of_the_art_benchmarking": [
        {
            "question": "How do you rigorously benchmark a novel architecture against published SOTA papers while avoiding benchmark overfitting and dataset contamination?",
            "expected_answer_keywords": ["sota benchmark", "dataset contamination", "generalization", "leaderboard", "peer review"]
        }
    ]
}

q_map.update(new_questions)
assdata["sample_questions_by_composite_key"] = q_map
with open(ass_path, "w", encoding="utf-8") as f:
    json.dump(assdata, f, indent=2, ensure_ascii=False)
print("[UPDATED EVIDENCE] assessment.json")
