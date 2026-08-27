import os
import json

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'machine-learning')
evidence_dir = os.path.join(base_dir, 'evidence', 'machine-learning')
roles_dir = os.path.join(base_dir, 'roles', 'machine-learning')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

skills = {}

# 1. ml_mathematics_foundations
skills["ml_mathematics_foundations"] = {
  "skill_id": "ml_mathematics_foundations",
  "name": "Mathematics, Linear Algebra & Optimization",
  "category": "mathematics",
  "description": "Mathematical foundations for machine learning: linear algebra, multivariable calculus, gradients, Jacobians/Hessians, probability distributions, Bayesian inference, and optimization algorithms.",
  "subskills": [
    {
      "id": "matrix_operations_decompositions",
      "name": "Linear Algebra & Matrix Decompositions",
      "description": "Vectors, matrices, dot products, eigenvalues, eigenvectors, Singular Value Decomposition (SVD), QR decomposition, and matrix rank.",
      "keywords": ["SVD", "eigenvalue", "eigenvector", "Singular Value Decomposition", "matrix multiplication", "dot product", "matrix rank", "determinant", "orthogonal matrix"]
    },
    {
      "id": "calculus_gradients_hessians",
      "name": "Multivariate Calculus, Gradients & Jacobians",
      "description": "Partial derivatives, chain rule in multivariate calculus, gradient vectors, Jacobian matrices, Hessian matrices, and Taylor approximations.",
      "keywords": ["partial derivative", "chain rule", "gradient vector", "Jacobian", "Hessian", "Taylor series", "directional derivative", "convexity"]
    },
    {
      "id": "probability_distributions_bayes",
      "name": "Probability Distributions & Bayesian Inference",
      "description": "Gaussian/Normal, Bernoulli, Poisson, Exponential distributions, Bayes theorem, prior/posterior/likelihood, and Maximum A Posteriori (MAP).",
      "keywords": ["Bayes theorem", "prior", "posterior", "likelihood", "Gaussian distribution", "MAP", "Bernoulli", "conditional probability", "expectation", "variance"]
    },
    {
      "id": "maximum_likelihood_estimation",
      "name": "Maximum Likelihood Estimation (MLE)",
      "description": "Log-likelihood formulation, finding optimal parameter estimators analytically and numerically, and relationship to cross-entropy loss.",
      "keywords": ["MLE", "Maximum Likelihood Estimation", "log-likelihood", "score function", "estimator", "cross-entropy", "parameter estimation"]
    },
    {
      "id": "first_order_optimization_sgd_adam",
      "name": "First-Order Optimization (GD, SGD, Momentum, Adam)",
      "description": "Batch Gradient Descent, Stochastic Gradient Descent (SGD), Mini-batch GD, Momentum, RMSprop, Adam, AdamW, and learning rate dynamics.",
      "keywords": ["SGD", "Mini-batch GD", "Adam", "AdamW", "RMSprop", "Momentum", "learning rate", "gradient descent", "saddle points", "local minima"]
    },
    {
      "id": "second_order_constrained_optimization",
      "name": "Second-Order & Constrained Optimization",
      "description": "Newton-Raphson, quasi-Newton (BFGS / L-BFGS), Lagrange multipliers, KKT conditions, and primal-dual optimization.",
      "keywords": ["L-BFGS", "Newton-Raphson", "Lagrange multipliers", "KKT conditions", "primal dual", "constrained optimization", "second-order optimization"]
    },
    {
      "id": "information_theory_entropy",
      "name": "Information Theory, Entropy & KL Divergence",
      "description": "Shannon entropy, joint entropy, conditional entropy, mutual information, cross-entropy, and Kullback-Leibler (KL) divergence.",
      "keywords": ["Shannon entropy", "KL divergence", "Kullback-Leibler", "cross-entropy", "mutual information", "information gain", "relative entropy"]
    },
    {
      "id": "statistical_hypothesis_testing",
      "name": "Statistical Hypothesis Testing & A/B Testing Math",
      "description": "Null/alternative hypothesis, p-values, z-test, t-test, ANOVA, Chi-Square test, Type I / Type II errors, and power analysis.",
      "keywords": ["p-value", "hypothesis testing", "t-test", "z-test", "Chi-Square", "Type I error", "Type II error", "statistical significance", "power analysis"]
    },
    {
      "id": "loss_functions_mathematics",
      "name": "Loss Functions & Convexity Analysis",
      "description": "MSE, MAE, Huber loss, Hinge loss, Focal loss, Triplet loss, Bregman divergences, and verifying objective function convexity.",
      "keywords": ["loss function", "Huber loss", "Hinge loss", "Focal loss", "MSE", "MAE", "convexity", "strict convexity", "Lipschitz continuity"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Designed custom loss functions and derived analytical optimization solutions for ML models",
        "strength": 0.5,
        "maps_to": ["ml_mathematics_foundations.first_order_optimization_sgd_adam", "ml_mathematics_foundations.loss_functions_mathematics", "ml_mathematics_foundations.matrix_operations_decompositions"]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsed for Machine Learning Mathematics, Linear Algebra, and Statistics",
        "strength": 0.3,
        "maps_to": ["ml_mathematics_foundations.probability_distributions_bayes", "ml_mathematics_foundations.calculus_gradients_hessians"]
      }
    ],
    "github": [
      {
        "pattern": "*loss*.py|*optim*.py|*math*.py|notebooks/*derivation*.ipynb",
        "strength": 1.0,
        "maps_to": [
          "ml_mathematics_foundations.matrix_operations_decompositions",
          "ml_mathematics_foundations.calculus_gradients_hessians",
          "ml_mathematics_foundations.probability_distributions_bayes",
          "ml_mathematics_foundations.maximum_likelihood_estimation",
          "ml_mathematics_foundations.first_order_optimization_sgd_adam",
          "ml_mathematics_foundations.second_order_constrained_optimization",
          "ml_mathematics_foundations.information_theory_entropy",
          "ml_mathematics_foundations.statistical_hypothesis_testing",
          "ml_mathematics_foundations.loss_functions_mathematics"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes ML Mathematics, Linear Algebra & Optimization Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_mathematics_foundations.matrix_operations_decompositions",
          "ml_mathematics_foundations.calculus_gradients_hessians",
          "ml_mathematics_foundations.probability_distributions_bayes",
          "ml_mathematics_foundations.maximum_likelihood_estimation",
          "ml_mathematics_foundations.first_order_optimization_sgd_adam",
          "ml_mathematics_foundations.second_order_constrained_optimization",
          "ml_mathematics_foundations.information_theory_entropy",
          "ml_mathematics_foundations.statistical_hypothesis_testing",
          "ml_mathematics_foundations.loss_functions_mathematics"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["matrix_operations_decompositions", "calculus_gradients_hessians", "probability_distributions_bayes"],
      "description": "Understands matrix algebra, computes partial gradients using chain rule, and works with standard probability distributions."
    },
    "mid": {
      "expected_subskills": ["maximum_likelihood_estimation", "first_order_optimization_sgd_adam", "statistical_hypothesis_testing", "loss_functions_mathematics"],
      "description": "Formulates MLE problems, tunes first-order optimizers (Adam/SGD), runs statistical hypothesis tests, and selects appropriate loss functions."
    },
    "senior": {
      "expected_subskills": ["second_order_constrained_optimization", "information_theory_entropy"],
      "description": "Applies second-order optimization and quasi-Newton methods, analyzes information-theoretic KL divergence, and proves algorithmic convexity."
    }
  }
}

# 2. ml_classical_algorithms
skills["ml_classical_algorithms"] = {
  "skill_id": "ml_classical_algorithms",
  "name": "Classical Supervised & Unsupervised Algorithms",
  "category": "algorithms",
  "description": "Implementation, mathematical mechanics, and tuning of classical machine learning algorithms: Linear/Logistic Regression, Tree Ensembles (XGBoost, LightGBM, CatBoost), SVMs, Naive Bayes, KNN, and Unsupervised Clustering.",
  "subskills": [
    {
      "id": "linear_logistic_regression_regularization",
      "name": "Linear & Logistic Regression with L1/L2 Regularization",
      "description": "Ordinary Least Squares, Ridge (L2), Lasso (L1), ElasticNet, odds ratios, sigmoid activation, and log-odds interpretation.",
      "keywords": ["Linear Regression", "Logistic Regression", "Ridge", "Lasso", "ElasticNet", "L1 regularization", "L2 regularization", "sigmoid", "OLS", "sparsity"]
    },
    {
      "id": "decision_trees_splitting_criteria",
      "name": "Decision Trees & Splitting Criteria (Gini, Entropy)",
      "description": "CART, ID3, C4.5, Gini impurity, Information Gain, tree pruning (pre-pruning, cost-complexity post-pruning), and decision boundary behavior.",
      "keywords": ["Decision Tree", "CART", "Gini impurity", "Information Gain", "entropy", "tree pruning", "cost-complexity pruning", "max_depth", "min_samples_split"]
    },
    {
      "id": "random_forests_bagging",
      "name": "Random Forests & Bagging Ensembles",
      "description": "Bootstrap aggregating (bagging), out-of-bag (OOB) error estimation, feature subspace sampling, and variance reduction.",
      "keywords": ["Random Forest", "Bagging", "Bootstrap aggregating", "OOB error", "out-of-bag", "ensemble", "variance reduction", "feature subsampling"]
    },
    {
      "id": "gradient_boosting_xgboost_lightgbm_catboost",
      "name": "Gradient Boosting (XGBoost, LightGBM, CatBoost)",
      "description": "Residual fitting, shrinkage, XGBoost exact/histogram split, LightGBM GOSS & EFB (Leaf-wise), CatBoost symmetric trees & target statistics.",
      "keywords": ["XGBoost", "LightGBM", "CatBoost", "Gradient Boosting", "GBDT", "GOSS", "EFB", "histogram-based", "leaf-wise", "depth-wise", "learning_rate"]
    },
    {
      "id": "support_vector_machines_kernels",
      "name": "Support Vector Machines & Kernel Trick",
      "description": "Max-margin hyperplanes, soft margin (C parameter), kernel trick (RBF, Polynomial, Linear), dual formulation, and support vectors.",
      "keywords": ["SVM", "Support Vector Machine", "RBF kernel", "kernel trick", "max margin", "slack variable", "hyperplane", "dual problem", "support vectors"]
    },
    {
      "id": "naive_bayes_knn",
      "name": "Naive Bayes Classifiers & K-Nearest Neighbors (KNN)",
      "description": "Gaussian/Multinomial/Bernoulli Naive Bayes, conditional independence assumption, KNN distance metrics (Euclidean, Manhattan, Cosine), and KD-Tree / Ball Tree indexing.",
      "keywords": ["Naive Bayes", "KNN", "K-Nearest Neighbors", "conditional independence", "KD-Tree", "Ball Tree", "Euclidean distance", "Cosine distance"]
    },
    {
      "id": "kmeans_hierarchical_clustering",
      "name": "K-Means & Hierarchical Clustering",
      "description": "K-Means Lloyd's algorithm, K-Means++, Elbow method, Silhouette score, Agglomerative clustering, linkage criteria (Ward, Complete, Single), and dendrograms.",
      "keywords": ["K-Means", "K-Means++", "Elbow method", "Silhouette score", "Hierarchical Clustering", "Agglomerative", "dendrogram", "linkage Ward"]
    },
    {
      "id": "density_clustering_dbscan_hdbscan",
      "name": "Density-Based Clustering (DBSCAN & HDBSCAN)",
      "description": "Core points, border points, noise points, eps and min_samples parameters, HDBSCAN varying density clustering, and non-spherical clusters.",
      "keywords": ["DBSCAN", "HDBSCAN", "core points", "eps", "min_samples", "density clustering", "noise points", "non-spherical clusters"]
    },
    {
      "id": "pca_dimensionality_reduction",
      "name": "Principal Component Analysis (PCA) & t-SNE / UMAP",
      "description": "Variance maximization, covariance matrix eigendecomposition, scree plot, explained variance ratio, t-SNE, and UMAP for non-linear manifold projection.",
      "keywords": ["PCA", "Principal Component Analysis", "explained variance ratio", "scree plot", "t-SNE", "UMAP", "dimensionality reduction", "manifold learning"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Trained and deployed high-performance XGBoost and LightGBM models for production prediction",
        "strength": 0.5,
        "maps_to": ["ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost", "ml_classical_algorithms.random_forests_bagging", "ml_classical_algorithms.linear_logistic_regression_regularization"]
      }
    ],
    "linkedin": [
      {
        "signal": "Skill endorsements in Scikit-Learn, XGBoost, and Machine Learning Algorithms",
        "strength": 0.3,
        "maps_to": ["ml_classical_algorithms.decision_trees_splitting_criteria", "ml_classical_algorithms.kmeans_hierarchical_clustering"]
      }
    ],
    "github": [
      {
        "pattern": "*xgboost*|*lightgbm*|*sklearn*|models/**/*.py|notebooks/*model*.ipynb",
        "strength": 1.0,
        "maps_to": [
          "ml_classical_algorithms.linear_logistic_regression_regularization",
          "ml_classical_algorithms.decision_trees_splitting_criteria",
          "ml_classical_algorithms.random_forests_bagging",
          "ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost",
          "ml_classical_algorithms.support_vector_machines_kernels",
          "ml_classical_algorithms.naive_bayes_knn",
          "ml_classical_algorithms.kmeans_hierarchical_clustering",
          "ml_classical_algorithms.density_clustering_dbscan_hdbscan",
          "ml_classical_algorithms.pca_dimensionality_reduction"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Classical Supervised & Unsupervised Machine Learning Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_classical_algorithms.linear_logistic_regression_regularization",
          "ml_classical_algorithms.decision_trees_splitting_criteria",
          "ml_classical_algorithms.random_forests_bagging",
          "ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost",
          "ml_classical_algorithms.support_vector_machines_kernels",
          "ml_classical_algorithms.naive_bayes_knn",
          "ml_classical_algorithms.kmeans_hierarchical_clustering",
          "ml_classical_algorithms.density_clustering_dbscan_hdbscan",
          "ml_classical_algorithms.pca_dimensionality_reduction"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["linear_logistic_regression_regularization", "decision_trees_splitting_criteria", "naive_bayes_knn"],
      "description": "Applies linear and logistic regressions with L1/L2 regularization, trains decision trees, and implements KNN and Naive Bayes."
    },
    "mid": {
      "expected_subskills": ["random_forests_bagging", "gradient_boosting_xgboost_lightgbm_catboost", "kmeans_hierarchical_clustering", "pca_dimensionality_reduction"],
      "description": "Tunes tree ensembles (Random Forest, XGBoost, LightGBM), performs K-Means clustering, and reduces dimensions with PCA."
    },
    "senior": {
      "expected_subskills": ["support_vector_machines_kernels", "density_clustering_dbscan_hdbscan"],
      "description": "Formulates kernel SVM optimizations, solves complex non-spherical clustering problems with HDBSCAN, and designs custom ensemble architectures."
    }
  }
}

# 3. ml_feature_engineering_preprocessing
skills["ml_feature_engineering_preprocessing"] = {
  "skill_id": "ml_feature_engineering_preprocessing",
  "name": "Feature Engineering, Preprocessing & Selection",
  "category": "data_preparation",
  "description": "Data preprocessing, handling missing values, categorical encoding strategies, feature scaling, outlier detection, interaction features, feature selection techniques, and scikit-learn pipeline construction.",
  "subskills": [
    {
      "id": "missing_data_imputation_strategies",
      "name": "Missing Data Imputation Strategies (MICE, KNN, Simple)",
      "description": "MCAR, MAR, MNAR mechanisms, mean/median/mode imputation, KNNImputer, MICE (IterativeImputer), and indicator columns for missingness.",
      "keywords": ["imputation", "KNNImputer", "IterativeImputer", "MICE", "SimpleImputer", "MCAR", "MAR", "MNAR", "missingness indicator"]
    },
    {
      "id": "categorical_encoding_target_ohe_embeddings",
      "name": "Categorical Encoding (Target, One-Hot, Ordinal, Frequency)",
      "description": "One-Hot Encoding, Ordinal/Label Encoding, Target/Mean Encoding with smoothing/regularization, Frequency Encoding, and Category Embeddings.",
      "keywords": ["One-Hot Encoding", "Target Encoding", "Mean Encoding", "Ordinal Encoding", "Frequency Encoding", "smoothing", "target leakage", "high cardinality"]
    },
    {
      "id": "feature_scaling_power_transformations",
      "name": "Feature Scaling & Power Transformations",
      "description": "StandardScaler, MinMaxScaler, RobustScaler (outlier-resistant), Box-Cox transformation, Yeo-Johnson transformation, and log transforms.",
      "keywords": ["StandardScaler", "MinMaxScaler", "RobustScaler", "Box-Cox", "Yeo-Johnson", "log transform", "normalizing", "scaling"]
    },
    {
      "id": "outlier_detection_treatment",
      "name": "Outlier Detection & Treatment (IQR, Isolation Forest)",
      "description": "Z-score, IQR capping/winsorization, Isolation Forest, Local Outlier Factor (LOF), EllipticEnvelope, and domain-specific thresholds.",
      "keywords": ["Isolation Forest", "IQR", "winsorization", "capping", "Local Outlier Factor", "LOF", "z-score", "outlier detection", "EllipticEnvelope"]
    },
    {
      "id": "interaction_polynomial_features",
      "name": "Interaction Terms & Polynomial Feature Generation",
      "description": "PolynomialFeatures, crossing categorical features, multiplicative interaction terms, ratios, and domain-engineered features.",
      "keywords": ["PolynomialFeatures", "feature crossing", "interaction terms", "feature creation", "ratio features", "domain features"]
    },
    {
      "id": "temporal_datetime_cyclical_features",
      "name": "Temporal, Datetime & Cyclical Feature Encoding",
      "description": "Extracting datetime components (hour, day, week, month), sine/cosine cyclical encoding, rolling aggregations, and lag features.",
      "keywords": ["cyclical encoding", "sine cosine encoding", "lag features", "rolling window", "datetime features", "time-based features"]
    },
    {
      "id": "text_nlp_feature_extraction_tfidf_embeddings",
      "name": "Text Feature Extraction (TF-IDF, Bag-of-Words, Word2Vec)",
      "description": "CountVectorizer, TfidfVectorizer (sublinear tf, n-grams, min_df/max_df), Word2Vec, and dense embedding feature extraction.",
      "keywords": ["TF-IDF", "TfidfVectorizer", "CountVectorizer", "n-grams", "Bag of Words", "Word2Vec", "text features", "sublinear_tf"]
    },
    {
      "id": "feature_selection_filter_wrapper_embedded",
      "name": "Feature Selection (Filter, Wrapper & Embedded Methods)",
      "description": "Filter methods (VarianceThreshold, ANOVA F-test, Mutual Information), Wrapper methods (RFE, SequentialFeatureSelector), and Embedded methods (L1 Lasso, tree feature importances).",
      "keywords": ["feature selection", "RFE", "Recursive Feature Elimination", "VarianceThreshold", "Mutual Information", "SelectKBest", "SequentialFeatureSelector", "L1 selection"]
    },
    {
      "id": "sklearn_pipelines_columntransformer",
      "name": "Scikit-Learn Pipelines & ColumnTransformer",
      "description": "Building leak-free Pipeline and ColumnTransformer workflows, custom BaseEstimator / TransformerMixin classes, and pipeline serialization.",
      "keywords": ["Pipeline", "ColumnTransformer", "TransformerMixin", "BaseEstimator", "fit_transform", "data leakage prevention", "sklearn.pipeline"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Engineered automated feature transformation pipelines using Scikit-Learn ColumnTransformer and target encoding",
        "strength": 0.5,
        "maps_to": ["ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings", "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer", "ml_feature_engineering_preprocessing.feature_selection_filter_wrapper_embedded"]
      }
    ],
    "linkedin": [
      {
        "signal": "Feature Engineering & Data Preprocessing endorsements",
        "strength": 0.3,
        "maps_to": ["ml_feature_engineering_preprocessing.feature_scaling_power_transformations", "ml_feature_engineering_preprocessing.missing_data_imputation_strategies"]
      }
    ],
    "github": [
      {
        "pattern": "*feature*.py|*preprocess*.py|*pipeline*.py|transformers/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "ml_feature_engineering_preprocessing.missing_data_imputation_strategies",
          "ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings",
          "ml_feature_engineering_preprocessing.feature_scaling_power_transformations",
          "ml_feature_engineering_preprocessing.outlier_detection_treatment",
          "ml_feature_engineering_preprocessing.interaction_polynomial_features",
          "ml_feature_engineering_preprocessing.temporal_datetime_cyclical_features",
          "ml_feature_engineering_preprocessing.text_nlp_feature_extraction_tfidf_embeddings",
          "ml_feature_engineering_preprocessing.feature_selection_filter_wrapper_embedded",
          "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Feature Engineering, Preprocessing & Selection Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_feature_engineering_preprocessing.missing_data_imputation_strategies",
          "ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings",
          "ml_feature_engineering_preprocessing.feature_scaling_power_transformations",
          "ml_feature_engineering_preprocessing.outlier_detection_treatment",
          "ml_feature_engineering_preprocessing.interaction_polynomial_features",
          "ml_feature_engineering_preprocessing.temporal_datetime_cyclical_features",
          "ml_feature_engineering_preprocessing.text_nlp_feature_extraction_tfidf_embeddings",
          "ml_feature_engineering_preprocessing.feature_selection_filter_wrapper_embedded",
          "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["missing_data_imputation_strategies", "feature_scaling_power_transformations", "text_nlp_feature_extraction_tfidf_embeddings"],
      "description": "Performs data cleaning, implements imputation strategies, scales numerical features, and extracts basic TF-IDF text features."
    },
    "mid": {
      "expected_subskills": ["categorical_encoding_target_ohe_embeddings", "outlier_detection_treatment", "temporal_datetime_cyclical_features", "sklearn_pipelines_columntransformer"],
      "description": "Prevents target leakage with smoothed target encoding, detects outliers with Isolation Forests, encodes cyclical time features, and builds end-to-end ColumnTransformer pipelines."
    },
    "senior": {
      "expected_subskills": ["interaction_polynomial_features", "feature_selection_filter_wrapper_embedded"],
      "description": "Designs automated feature selection systems (RFE/Boruta), constructs high-order domain interaction terms, and builds production feature engineering engines."
    }
  }
}

# 4. ml_model_evaluation_validation
skills["ml_model_evaluation_validation"] = {
  "skill_id": "ml_model_evaluation_validation",
  "name": "Model Evaluation, Cross-Validation & Diagnostics",
  "category": "validation",
  "description": "Rigorous validation strategies (K-Fold, Stratified, TimeSeriesSplit), classification & regression metrics, ROC-AUC, Precision-Recall curves, probability calibration, bias-variance tradeoff, and data leakage diagnostics.",
  "subskills": [
    {
      "id": "cross_validation_strategies_leakage",
      "name": "Cross-Validation Strategies & Leakage Prevention",
      "description": "K-Fold, StratifiedKFold, GroupKFold, TimeSeriesSplit, Purged/Embargoed CV for financial/temporal data, and preventing train-test data leakage.",
      "keywords": ["K-Fold", "StratifiedKFold", "GroupKFold", "TimeSeriesSplit", "cross-validation", "data leakage", "train test split", "purging", "embargo"]
    },
    {
      "id": "classification_metrics_pr_roc",
      "name": "Classification Metrics (ROC-AUC, PR-AUC, F1, Log-Loss)",
      "description": "Confusion matrix, Precision, Recall, Specificity, F1-Score, F-beta, ROC Curve & AUC, Precision-Recall Curve & Average Precision, and Log-Loss.",
      "keywords": ["ROC-AUC", "PR-AUC", "Precision", "Recall", "F1-Score", "F-beta", "Log-Loss", "Confusion Matrix", "Average Precision", "Specificity"]
    },
    {
      "id": "regression_metrics_residual_analysis",
      "name": "Regression Metrics & Residual Diagnostics",
      "description": "MSE, RMSE, MAE, MAPE, SMAPE, R-squared (R2), Adjusted R2, homoscedasticity vs heteroscedasticity, and residual Q-Q plots.",
      "keywords": ["RMSE", "MAE", "MAPE", "R-squared", "Adjusted R2", "residual plot", "heteroscedasticity", "Q-Q plot", "error distribution"]
    },
    {
      "id": "probability_calibration_platt_isotonic",
      "name": "Probability Calibration (Platt Scaling, Isotonic Regression)",
      "description": "Calibration curves / reliability diagrams, Brier score, Platt scaling (logistic calibration), and non-parametric Isotonic Regression.",
      "keywords": ["calibration curve", "Platt scaling", "Isotonic Regression", "reliability diagram", "Brier score", "predicted probability", "CalibratedClassifierCV"]
    },
    {
      "id": "bias_variance_tradeoff_learning_curves",
      "name": "Bias-Variance Tradeoff & Learning Curves",
      "description": "Decomposing error into bias, variance, and irreducible noise, plotting learning curves to diagnose underfitting vs overfitting.",
      "keywords": ["bias-variance tradeoff", "learning curve", "underfitting", "overfitting", "high bias", "high variance", "training curve", "validation curve"]
    },
    {
      "id": "imbalanced_data_handling_smote",
      "name": "Imbalanced Learning (SMOTE, Class Weights, Focal Loss)",
      "description": "Random oversampling/undersampling, SMOTE (Synthetic Minority Over-sampling Technique), ADASYN, class_weight='balanced', and cost-sensitive learning.",
      "keywords": ["SMOTE", "ADASYN", "imbalanced data", "class_weight", "undersampling", "oversampling", "cost-sensitive", "minority class"]
    },
    {
      "id": "threshold_tuning_cost_matrices",
      "name": "Decision Threshold Tuning & Cost-Benefit Matrices",
      "description": "Selecting optimal classification thresholds based on business cost matrices (cost of False Positive vs False Negative) rather than default 0.5.",
      "keywords": ["threshold tuning", "cost matrix", "optimal threshold", "business impact", "False Positive cost", "False Negative cost", "decision boundary"]
    },
    {
      "id": "ranking_recommendation_metrics",
      "name": "Ranking & Retrieval Metrics (NDCG, MAP, MRR)",
      "description": "Evaluating search and recommendation models: Normalized Discounted Cumulative Gain (NDCG@K), Mean Average Precision (MAP@K), and Mean Reciprocal Rank (MRR).",
      "keywords": ["NDCG", "MAP@K", "MRR", "Mean Reciprocal Rank", "ranking metrics", "top-k metrics", "Precision@K", "Recall@K"]
    },
    {
      "id": "ab_testing_online_evaluation",
      "name": "Online Model Evaluation & A/B Testing Design",
      "description": "Designing online A/B tests, sample size determination, minimum detectable effect (MDE), counterfactual evaluation, and shadow deployment metrics.",
      "keywords": ["A/B testing", "MDE", "minimum detectable effect", "sample size", "online evaluation", "shadow deployment", "counterfactual", "statistical power"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Designed custom metric evaluation pipelines with Stratified TimeSeriesSplit and probability calibration",
        "strength": 0.5,
        "maps_to": ["ml_model_evaluation_validation.cross_validation_strategies_leakage", "ml_model_evaluation_validation.classification_metrics_pr_roc", "ml_model_evaluation_validation.probability_calibration_platt_isotonic"]
      }
    ],
    "linkedin": [
      {
        "signal": "Model Evaluation, Validation & Statistical Testing endorsements",
        "strength": 0.3,
        "maps_to": ["ml_model_evaluation_validation.regression_metrics_residual_analysis", "ml_model_evaluation_validation.bias_variance_tradeoff_learning_curves"]
      }
    ],
    "github": [
      {
        "pattern": "*eval*.py|*metrics*.py|*validate*.py|evaluation/**/*.py",
        "strength": 1.0,
        "maps_to": [
          "ml_model_evaluation_validation.cross_validation_strategies_leakage",
          "ml_model_evaluation_validation.classification_metrics_pr_roc",
          "ml_model_evaluation_validation.regression_metrics_residual_analysis",
          "ml_model_evaluation_validation.probability_calibration_platt_isotonic",
          "ml_model_evaluation_validation.bias_variance_tradeoff_learning_curves",
          "ml_model_evaluation_validation.imbalanced_data_handling_smote",
          "ml_model_evaluation_validation.threshold_tuning_cost_matrices",
          "ml_model_evaluation_validation.ranking_recommendation_metrics",
          "ml_model_evaluation_validation.ab_testing_online_evaluation"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Evaluation, Cross-Validation & Diagnostics Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_model_evaluation_validation.cross_validation_strategies_leakage",
          "ml_model_evaluation_validation.classification_metrics_pr_roc",
          "ml_model_evaluation_validation.regression_metrics_residual_analysis",
          "ml_model_evaluation_validation.probability_calibration_platt_isotonic",
          "ml_model_evaluation_validation.bias_variance_tradeoff_learning_curves",
          "ml_model_evaluation_validation.imbalanced_data_handling_smote",
          "ml_model_evaluation_validation.threshold_tuning_cost_matrices",
          "ml_model_evaluation_validation.ranking_recommendation_metrics",
          "ml_model_evaluation_validation.ab_testing_online_evaluation"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["classification_metrics_pr_roc", "regression_metrics_residual_analysis", "bias_variance_tradeoff_learning_curves"],
      "description": "Calculates standard classification and regression metrics, generates ROC/PR curves, and analyzes learning curves for overfitting."
    },
    "mid": {
      "expected_subskills": ["cross_validation_strategies_leakage", "probability_calibration_platt_isotonic", "imbalanced_data_handling_smote", "threshold_tuning_cost_matrices"],
      "description": "Designs leak-free cross-validation splits, calibrates model probabilities (Platt/Isotonic), handles extreme imbalance (SMOTE), and tunes decision thresholds."
    },
    "senior": {
      "expected_subskills": ["ranking_recommendation_metrics", "ab_testing_online_evaluation"],
      "description": "Establishes online A/B testing frameworks, evaluates ranking models with NDCG/MAP, and designs statistical validation standards across company models."
    }
  }
}

# 5. ml_deep_learning_architectures
skills["ml_deep_learning_architectures"] = {
  "skill_id": "ml_deep_learning_architectures",
  "name": "Deep Learning Architectures & Frameworks (PyTorch / TF)",
  "category": "deep_learning",
  "description": "Deep learning fundamentals, PyTorch autograd and modules, CNNs, Sequence models (RNN/LSTM/GRU), Transformer self-attention mechanisms, Autoencoders, and custom layers/loss implementations.",
  "subskills": [
    {
      "id": "pytorch_core_autograd_nn_module",
      "name": "PyTorch Core, Tensors, Autograd & nn.Module",
      "description": "Tensors, GPU memory allocation (cuda), autograd computation graph, forward pass, backward pass, zero_grad(), and torch.nn.Module.",
      "keywords": ["PyTorch", "autograd", "nn.Module", "forward pass", "backward()", "optimizer.zero_grad()", "torch.Tensor", "cuda", "computation graph"]
    },
    {
      "id": "feedforward_regularization_batchnorm_dropout",
      "name": "Feedforward Networks, BatchNorm & Dropout",
      "description": "Multi-Layer Perceptrons (MLP), activations (ReLU, GELU, Swish), Batch Normalization, Layer Normalization, and Dropout regularization.",
      "keywords": ["MLP", "BatchNorm", "LayerNorm", "Dropout", "ReLU", "GELU", "Swish", "activation function", "weight initialization", "He initialization"]
    },
    {
      "id": "convolutional_neural_networks_cnn",
      "name": "Convolutional Neural Networks (CNNs) & Computer Vision",
      "description": "2D/3D Convolutions, kernels, stride, padding, pooling, ResNet residual blocks, ConvNeXt, and receptive field mechanics.",
      "keywords": ["CNN", "Convolution", "ResNet", "residual connection", "stride", "padding", "pooling", "ConvNeXt", "kernel", "receptive field"]
    },
    {
      "id": "recurrent_networks_lstm_gru",
      "name": "Recurrent Neural Networks (RNN, LSTM & GRU)",
      "description": "Vanishing/exploding gradient in RNNs, LSTM cell states, gates (forget, input, output), GRU update/reset gates, and bidirectional RNNs.",
      "keywords": ["RNN", "LSTM", "GRU", "cell state", "forget gate", "vanishing gradient", "gradient clipping", "bidirectional LSTM", "sequence modeling"]
    },
    {
      "id": "transformer_self_attention_mechanisms",
      "name": "Transformer Architecture & Scaled Dot-Product Attention",
      "description": "Self-attention formula QK^T / sqrt(d_k), Multi-Head Attention, positional encodings (Sinusoidal, RoPE), and Encoder-Decoder blocks.",
      "keywords": ["Transformer", "Self-Attention", "Multi-Head Attention", "Scaled Dot-Product", "RoPE", "positional encoding", "Encoder", "Decoder", "Attention map"]
    },
    {
      "id": "autoencoders_variational_ae",
      "name": "Autoencoders & Variational Autoencoders (VAE)",
      "description": "Bottleneck representations, reconstruction loss, Variational Autoencoders (VAE), latent space distribution, and reparameterization trick.",
      "keywords": ["Autoencoder", "VAE", "Variational Autoencoder", "latent space", "reparameterization trick", "KL divergence loss", "reconstruction loss", "bottleneck"]
    },
    {
      "id": "custom_layers_loss_functions_pytorch",
      "name": "Custom PyTorch Layers & Differentiable Loss Functions",
      "description": "Writing custom torch.autograd.Function with explicit forward/backward methods, custom loss functions, and parameterized module layers.",
      "keywords": ["custom loss", "torch.autograd.Function", "custom layer", "forward backward implementation", "differentiable", "parameter registration"]
    },
    {
      "id": "deep_learning_training_loop_lightning",
      "name": "Training Loops, PyTorch Lightning & Callbacks",
      "description": "Structuring clean training loops, PyTorch Lightning LightningModule & Trainer, EarlyStopping, ModelCheckpoint, and mixed-precision (AMP).",
      "keywords": ["PyTorch Lightning", "LightningModule", "Trainer", "EarlyStopping", "ModelCheckpoint", "AMP", "automatic mixed precision", "training loop"]
    },
    {
      "id": "distributed_training_ddp_fsdp",
      "name": "Distributed Training (DDP, FSDP & DeepSpeed)",
      "description": "DistributedDataParallel (DDP), gradient all-reduce, Fully Sharded Data Parallel (FSDP), ZeRO stages in DeepSpeed, and multi-GPU scaling.",
      "keywords": ["DDP", "DistributedDataParallel", "FSDP", "DeepSpeed", "ZeRO", "all-reduce", "multi-GPU", "gradient accumulation", "distributed training"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Built custom deep learning architectures in PyTorch with distributed training (DDP) across GPU clusters",
        "strength": 0.5,
        "maps_to": ["ml_deep_learning_architectures.pytorch_core_autograd_nn_module", "ml_deep_learning_architectures.distributed_training_ddp_fsdp", "ml_deep_learning_architectures.transformer_self_attention_mechanisms"]
      }
    ],
    "linkedin": [
      {
        "signal": "PyTorch, Deep Learning, and Neural Networks specialist endorsements",
        "strength": 0.3,
        "maps_to": ["ml_deep_learning_architectures.feedforward_regularization_batchnorm_dropout", "ml_deep_learning_architectures.convolutional_neural_networks_cnn"]
      }
    ],
    "github": [
      {
        "pattern": "*torch*.py|*model*.py|*nn*.py|train.py|models/**/*.pt|models/**/*.pth",
        "strength": 1.0,
        "maps_to": [
          "ml_deep_learning_architectures.pytorch_core_autograd_nn_module",
          "ml_deep_learning_architectures.feedforward_regularization_batchnorm_dropout",
          "ml_deep_learning_architectures.convolutional_neural_networks_cnn",
          "ml_deep_learning_architectures.recurrent_networks_lstm_gru",
          "ml_deep_learning_architectures.transformer_self_attention_mechanisms",
          "ml_deep_learning_architectures.autoencoders_variational_ae",
          "ml_deep_learning_architectures.custom_layers_loss_functions_pytorch",
          "ml_deep_learning_architectures.deep_learning_training_loop_lightning",
          "ml_deep_learning_architectures.distributed_training_ddp_fsdp"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Deep Learning Architectures & PyTorch Frameworks Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_deep_learning_architectures.pytorch_core_autograd_nn_module",
          "ml_deep_learning_architectures.feedforward_regularization_batchnorm_dropout",
          "ml_deep_learning_architectures.convolutional_neural_networks_cnn",
          "ml_deep_learning_architectures.recurrent_networks_lstm_gru",
          "ml_deep_learning_architectures.transformer_self_attention_mechanisms",
          "ml_deep_learning_architectures.autoencoders_variational_ae",
          "ml_deep_learning_architectures.custom_layers_loss_functions_pytorch",
          "ml_deep_learning_architectures.deep_learning_training_loop_lightning",
          "ml_deep_learning_architectures.distributed_training_ddp_fsdp"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["pytorch_core_autograd_nn_module", "feedforward_regularization_batchnorm_dropout", "deep_learning_training_loop_lightning"],
      "description": "Writes PyTorch tensors and modules, configures standard layers (BatchNorm, Dropout), and manages training loops with PyTorch Lightning."
    },
    "mid": {
      "expected_subskills": ["convolutional_neural_networks_cnn", "recurrent_networks_lstm_gru", "autoencoders_variational_ae", "custom_layers_loss_functions_pytorch"],
      "description": "Constructs CNNs and LSTMs/GRUs, writes custom loss functions and autograd layers, and builds Variational Autoencoders."
    },
    "senior": {
      "expected_subskills": ["transformer_self_attention_mechanisms", "distributed_training_ddp_fsdp"],
      "description": "Architects custom Transformer multi-head attention systems and scales multi-GPU distributed training using DDP, FSDP, and DeepSpeed."
    }
  }
}

# 6. ml_hyperparameter_optimization
skills["ml_hyperparameter_optimization"] = {
  "skill_id": "ml_hyperparameter_optimization",
  "name": "Hyperparameter Optimization & Tuning",
  "category": "experimentation",
  "description": "Automated hyperparameter search strategies: Grid Search, Random Search, Bayesian Optimization (Optuna, Hyperopt, TPE), early stopping pruning, Multi-Fidelity tuning, and learning rate scheduling.",
  "subskills": [
    {
      "id": "grid_random_search_tuning",
      "name": "Grid Search & Randomized Search",
      "description": "Exhaustive parameter grids with GridSearchCV, RandomizedSearchCV probability distributions, budget allocation, and search space definition.",
      "keywords": ["GridSearchCV", "RandomizedSearchCV", "parameter grid", "search space", "exhaustive search", "random sampling", "Scikit-Learn tuning"]
    },
    {
      "id": "bayesian_optimization_tpe_optuna",
      "name": "Bayesian Optimization & Optuna TPE Sampler",
      "description": "Tree-structured Parzen Estimators (TPE), Gaussian Process surrogate models, Expected Improvement (EI), and study optimization with Optuna.",
      "keywords": ["Optuna", "TPE", "Tree-structured Parzen Estimator", "Bayesian Optimization", "Expected Improvement", "study.optimize", "suggest_float", "suggest_int"]
    },
    {
      "id": "early_stopping_pruning_strategies",
      "name": "Early Stopping & Automated Trial Pruning",
      "description": "Median pruner, Hyperband, Successive Halving (ASHA), trial.should_prune(), and terminating unpromising hyperparameter trials early.",
      "keywords": ["pruning", "Hyperband", "ASHA", "Successive Halving", "MedianPruner", "trial.should_prune()", "early stopping", "resource conservation"]
    },
    {
      "id": "learning_rate_schedulers_warmup",
      "name": "Learning Rate Schedulers & Warmup Dynamics",
      "description": "Cosine Annealing, OneCycleLR, ExponentialLR, ReduceLROnPlateau, linear warmup steps, and cyclic learning rates.",
      "keywords": ["CosineAnnealingLR", "OneCycleLR", "ReduceLROnPlateau", "warmup steps", "learning rate scheduler", "cyclic learning rate", "lr_finder"]
    },
    {
      "id": "multi_objective_optimization",
      "name": "Multi-Objective Hyperparameter Optimization",
      "description": "Pareto frontiers, simultaneously optimizing accuracy vs latency vs model size, and non-dominated sorting in Optuna.",
      "keywords": ["multi-objective", "Pareto frontier", "Pareto optimal", "accuracy vs latency", "non-dominated sorting", "NSGA-II", "Optuna directions"]
    },
    {
      "id": "distributed_hyperparameter_tuning_ray",
      "name": "Distributed Hyperparameter Tuning (Ray Tune)",
      "description": "Scaling tuning across clusters using Ray Tune, population-based training (PBT), distributed trial scheduling, and checkpoint synchronization.",
      "keywords": ["Ray Tune", "Population Based Training", "PBT", "distributed tuning", "Ray cluster", "trial concurrency", "search algorithm"]
    },
    {
      "id": "search_space_design_hyperparameter_types",
      "name": "Search Space Design & Parameter Sensitivity",
      "description": "Log-scale sampling for learning rates/regularization, categorical choices, conditional hyperparameter spaces, and Sobol sensitivity analysis.",
      "keywords": ["log-scale sampling", "conditional search space", "parameter sensitivity", "Sobol indices", "hyperparameter importance", "Optuna visualization"]
    },
    {
      "id": "k_fold_integrated_hpo",
      "name": "Nested Cross-Validation for Hyperparameter Selection",
      "description": "Inner loop for hyperparameter tuning, outer loop for unbiased generalization performance estimation, and avoiding optimism bias.",
      "keywords": ["Nested CV", "inner loop", "outer loop", "unbiased evaluation", "optimism bias", "nested cross-validation", "model selection"]
    },
    {
      "id": "experiment_tracking_wandb_mlflow_hpo",
      "name": "HPO Experiment Tracking & Sweep Logging (W&B, MLflow)",
      "description": "Logging hyperparameter sweeps in Weights & Biases (W&B) or MLflow, parallel coordinates plots, correlation charts, and artifact linking.",
      "keywords": ["Weights & Biases", "W&B sweeps", "MLflow experiments", "parallel coordinates", "hyperparameter tracking", "sweep config", "run artifacts"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Implemented Bayesian hyperparameter tuning with Optuna and Ray Tune, improving model AUC while halving compute costs",
        "strength": 0.5,
        "maps_to": ["ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna", "ml_hyperparameter_optimization.early_stopping_pruning_strategies", "ml_hyperparameter_optimization.multi_objective_optimization"]
      }
    ],
    "linkedin": [
      {
        "signal": "Hyperparameter Optimization, Optuna, and Ray Tune endorsements",
        "strength": 0.3,
        "maps_to": ["ml_hyperparameter_optimization.grid_random_search_tuning", "ml_hyperparameter_optimization.learning_rate_schedulers_warmup"]
      }
    ],
    "github": [
      {
        "pattern": "*optuna*|*sweep*|*tune*.py|configs/*hpo*.yml",
        "strength": 1.0,
        "maps_to": [
          "ml_hyperparameter_optimization.grid_random_search_tuning",
          "ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna",
          "ml_hyperparameter_optimization.early_stopping_pruning_strategies",
          "ml_hyperparameter_optimization.learning_rate_schedulers_warmup",
          "ml_hyperparameter_optimization.multi_objective_optimization",
          "ml_hyperparameter_optimization.distributed_hyperparameter_tuning_ray",
          "ml_hyperparameter_optimization.search_space_design_hyperparameter_types",
          "ml_hyperparameter_optimization.k_fold_integrated_hpo",
          "ml_hyperparameter_optimization.experiment_tracking_wandb_mlflow_hpo"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Hyperparameter Optimization & Tuning Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_hyperparameter_optimization.grid_random_search_tuning",
          "ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna",
          "ml_hyperparameter_optimization.early_stopping_pruning_strategies",
          "ml_hyperparameter_optimization.learning_rate_schedulers_warmup",
          "ml_hyperparameter_optimization.multi_objective_optimization",
          "ml_hyperparameter_optimization.distributed_hyperparameter_tuning_ray",
          "ml_hyperparameter_optimization.search_space_design_hyperparameter_types",
          "ml_hyperparameter_optimization.k_fold_integrated_hpo",
          "ml_hyperparameter_optimization.experiment_tracking_wandb_mlflow_hpo"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["grid_random_search_tuning", "learning_rate_schedulers_warmup", "experiment_tracking_wandb_mlflow_hpo"],
      "description": "Performs grid and random searches, configures learning rate schedulers (Cosine/ReduceLROnPlateau), and tracks runs in MLflow/W&B."
    },
    "mid": {
      "expected_subskills": ["bayesian_optimization_tpe_optuna", "early_stopping_pruning_strategies", "search_space_design_hyperparameter_types", "k_fold_integrated_hpo"],
      "description": "Conducts Bayesian optimization with Optuna TPE samplers, configures ASHA/Hyperband pruning, and performs nested cross-validation."
    },
    "senior": {
      "expected_subskills": ["multi_objective_optimization", "distributed_hyperparameter_tuning_ray"],
      "description": "Architects multi-objective Pareto optimization (accuracy vs latency) and scales distributed hyperparameter sweeps across clusters with Ray Tune."
    }
  }
}

# 7. ml_model_deployment_serving
skills["ml_model_deployment_serving"] = {
  "skill_id": "ml_model_deployment_serving",
  "name": "Model Serving & Inference Infrastructure",
  "category": "deployment",
  "description": "Deploying machine learning models in production: REST/gRPC microservices (FastAPI), Triton Inference Server, ONNX Runtime, TorchScript, dynamic batching, and low-latency serving.",
  "subskills": [
    {
      "id": "fastapi_rest_model_microservices",
      "name": "FastAPI & REST Model Microservices",
      "description": "Building high-performance async prediction endpoints with FastAPI, Pydantic request/response schemas, dependency injection, and health checks.",
      "keywords": ["FastAPI", "Pydantic", "REST endpoint", "async prediction", "model serving", "microservice", "health check", "JSON payload"]
    },
    {
      "id": "grpc_protobuf_high_throughput_serving",
      "name": "gRPC & Protocol Buffers for Low-Latency Serving",
      "description": "Defining Proto service definitions, streaming predictions, low-latency binary serialization, and bidirectional gRPC communication.",
      "keywords": ["gRPC", "Protobuf", "Protocol Buffers", "binary serialization", "low-latency", "streaming prediction", "stub", "RPC"]
    },
    {
      "id": "triton_inference_server_management",
      "name": "Triton Inference Server & Model Repositories",
      "description": "NVIDIA Triton Inference Server, config.pbtxt model repository layout, multi-model concurrent execution, and dynamic batching.",
      "keywords": ["Triton", "NVIDIA Triton", "config.pbtxt", "model repository", "dynamic batching", "concurrent model execution", "ensemble scheduler"]
    },
    {
      "id": "onnx_runtime_export_inference",
      "name": "ONNX Export & ONNX Runtime (ORT) Execution",
      "description": "Exporting PyTorch/Scikit-Learn models to Open Neural Network Exchange (ONNX), dynamic axes, and running inference with ONNX Runtime.",
      "keywords": ["ONNX", "ONNX Runtime", "torch.onnx.export", "dynamic axes", "ORT", "cross-platform inference", "onnxruntime-gpu"]
    },
    {
      "id": "torchscript_trace_script_deployment",
      "name": "TorchScript (Tracing & Scripting) for C++ Integration",
      "description": "torch.jit.trace vs torch.jit.script, removing Python runtime dependency, and loading serialized models in high-performance C++ runtimes.",
      "keywords": ["TorchScript", "torch.jit.trace", "torch.jit.script", "C++ inference", "libtorch", "no-Python runtime", "JIT compilation"]
    },
    {
      "id": "batch_vs_realtime_serving_architectures",
      "name": "Batch vs Real-Time vs Streaming Inference Patterns",
      "description": "Offline batch scoring at scale (Spark/Ray), online request-response serving, streaming event-driven inference, and cached predictions.",
      "keywords": ["batch scoring", "real-time inference", "streaming inference", "offline prediction", "online scoring", "feature caching", "Redis cache"]
    },
    {
      "id": "dynamic_batching_concurrency_control",
      "name": "Dynamic Batching, Queuing & Concurrency Control",
      "description": "Grouping concurrent real-time requests into GPU/CPU batches, max_queue_delay_microseconds, and worker thread pool concurrency.",
      "keywords": ["dynamic batching", "max_batch_size", "queue delay", "batch latency", "concurrency control", "throughput optimization", "worker threads"]
    },
    {
      "id": "model_canary_shadow_ab_deployment",
      "name": "Deployment Strategies (Canary, Blue/Green, Shadow Deployments)",
      "description": "Canary rollouts, Blue/Green deployments, Shadow / Dark launch (duplicating traffic for evaluation), and automated rollbacks on error spikes.",
      "keywords": ["Canary deployment", "Blue-Green deployment", "Shadow deployment", "dark launch", "traffic splitting", "automated rollback", "Seldon Core", "KServe"]
    },
    {
      "id": "latency_profiling_load_testing",
      "name": "Latency Profiling (P95/P99) & Load Testing (Locust)",
      "description": "Benchmarking inference endpoints with Locust / wrk, measuring P50/P95/P99 latency, profiling cold start, and memory leak testing under stress.",
      "keywords": ["P95 latency", "P99 latency", "Locust", "load testing", "benchmark", "cold start", "stress testing", "throughput RPS"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Deployed production models on Triton Inference Server with dynamic batching and ONNX Runtime achieving sub-10ms P99 latency",
        "strength": 0.5,
        "maps_to": ["ml_model_deployment_serving.triton_inference_server_management", "ml_model_deployment_serving.onnx_runtime_export_inference", "ml_model_deployment_serving.latency_profiling_load_testing"]
      }
    ],
    "linkedin": [
      {
        "signal": "Model Deployment, FastAPI, and Triton Inference Server endorsements",
        "strength": 0.3,
        "maps_to": ["ml_model_deployment_serving.fastapi_rest_model_microservices", "ml_model_deployment_serving.batch_vs_realtime_serving_architectures"]
      }
    ],
    "github": [
      {
        "pattern": "*serve*.py|*app*.py|*triton*|service/**/*.py|config.pbtxt|*.onnx",
        "strength": 1.0,
        "maps_to": [
          "ml_model_deployment_serving.fastapi_rest_model_microservices",
          "ml_model_deployment_serving.grpc_protobuf_high_throughput_serving",
          "ml_model_deployment_serving.triton_inference_server_management",
          "ml_model_deployment_serving.onnx_runtime_export_inference",
          "ml_model_deployment_serving.torchscript_trace_script_deployment",
          "ml_model_deployment_serving.batch_vs_realtime_serving_architectures",
          "ml_model_deployment_serving.dynamic_batching_concurrency_control",
          "ml_model_deployment_serving.model_canary_shadow_ab_deployment",
          "ml_model_deployment_serving.latency_profiling_load_testing"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Serving & Inference Infrastructure Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_model_deployment_serving.fastapi_rest_model_microservices",
          "ml_model_deployment_serving.grpc_protobuf_high_throughput_serving",
          "ml_model_deployment_serving.triton_inference_server_management",
          "ml_model_deployment_serving.onnx_runtime_export_inference",
          "ml_model_deployment_serving.torchscript_trace_script_deployment",
          "ml_model_deployment_serving.batch_vs_realtime_serving_architectures",
          "ml_model_deployment_serving.dynamic_batching_concurrency_control",
          "ml_model_deployment_serving.model_canary_shadow_ab_deployment",
          "ml_model_deployment_serving.latency_profiling_load_testing"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["fastapi_rest_model_microservices", "batch_vs_realtime_serving_architectures", "onnx_runtime_export_inference"],
      "description": "Wraps models into FastAPI prediction endpoints, exports models to ONNX, and implements batch scoring jobs."
    },
    "mid": {
      "expected_subskills": ["grpc_protobuf_high_throughput_serving", "torchscript_trace_script_deployment", "model_canary_shadow_ab_deployment", "latency_profiling_load_testing"],
      "description": "Implements gRPC model services, compiles models with TorchScript, runs Locust load tests, and coordinates Canary/Shadow deployments."
    },
    "senior": {
      "expected_subskills": ["triton_inference_server_management", "dynamic_batching_concurrency_control"],
      "description": "Architects enterprise Triton multi-model inference clusters, configures hardware dynamic batching, and guarantees sub-10ms P99 SLAs."
    }
  }
}

# 8. ml_model_optimization_compression
skills["ml_model_optimization_compression"] = {
  "skill_id": "ml_model_optimization_compression",
  "name": "Model Compression, Quantization & Acceleration",
  "category": "optimization",
  "description": "Reducing model size and latency without sacrificing accuracy: Post-Training Quantization (PTQ), Quantization-Aware Training (QAT), Structured/Unstructured Pruning, Knowledge Distillation, TensorRT, and hardware compilation.",
  "subskills": [
    {
      "id": "post_training_quantization_ptq",
      "name": "Post-Training Quantization (PTQ - INT8 / FP16)",
      "description": "Quantization mechanics (scale, zero-point, dynamic vs static quantization), calibration datasets, and converting FP32 weights to INT8.",
      "keywords": ["PTQ", "Post-Training Quantization", "INT8", "FP16", "scale factor", "zero-point", "dynamic quantization", "static quantization", "calibration"]
    },
    {
      "id": "quantization_aware_training_qat",
      "name": "Quantization-Aware Training (QAT)",
      "description": "Simulating fake quantization during backpropagation, straight-through estimators (STE), and retaining full accuracy at INT8 precision.",
      "keywords": ["QAT", "Quantization-Aware Training", "fake quantization", "straight-through estimator", "STE", "torch.ao.quantization", "accuracy preservation"]
    },
    {
      "id": "structural_unstructured_weight_pruning",
      "name": "Weight Pruning (Structured & Unstructured)",
      "description": "Magnitude-based pruning, L1-norm channel pruning, structured pruning for hardware acceleration, iterative prune-and-finetune schedules.",
      "keywords": ["pruning", "weight pruning", "structured pruning", "unstructured pruning", "channel pruning", "sparsity", "fine-tuning", "torch.nn.utils.prune"]
    },
    {
      "id": "knowledge_distillation_teacher_student",
      "name": "Knowledge Distillation (Teacher-Student Frameworks)",
      "description": "Soft targets, temperature scaling, Kullback-Leibler distillation loss, feature map distillation, and training compact student models.",
      "keywords": ["Knowledge Distillation", "teacher model", "student model", "soft targets", "temperature", "distillation loss", "model compression"]
    },
    {
      "id": "tensorrt_gpu_acceleration",
      "name": "NVIDIA TensorRT GPU Acceleration & Kernel Fusion",
      "description": "Building TensorRT engines from ONNX, layer fusion, kernel auto-tuning, precision calibration (FP16/INT8), and execution profiles.",
      "keywords": ["TensorRT", "layer fusion", "kernel auto-tuning", "TRT engine", "NVIDIA GPU acceleration", "polygraphy", "trtexec"]
    },
    {
      "id": "openvino_cpu_optimization",
      "name": "Intel OpenVINO & CPU Inference Acceleration",
      "description": "Optimizing neural networks for x86 Intel CPUs, VNNI / AVX-512 instructions, OpenVINO Model Optimizer, and asynchronous execution.",
      "keywords": ["OpenVINO", "AVX-512", "VNNI", "Model Optimizer", "Intel CPU acceleration", "heterogeneous plugin", "inference engine"]
    },
    {
      "id": "model_compilation_torch_compile_tvm",
      "name": "Model Compilation (torch.compile & Apache TVM)",
      "description": "PyTorch 2.0 torch.compile, TorchDynamo, AOTAutograd, Inductor backend, graph capture, and Apache TVM tensor compilation.",
      "keywords": ["torch.compile", "TorchDynamo", "TorchInductor", "AOTAutograd", "Apache TVM", "graph capture", "JIT compilation", "PyTorch 2.0"]
    },
    {
      "id": "low_rank_matrix_factorization_weights",
      "name": "Low-Rank Weight Factorization & LoRA Mechanics",
      "description": "Decomposing heavy weight matrices using SVD or low-rank adapters (LoRA / QLoRA rank matrices A and B), parameter reduction.",
      "keywords": ["Low-Rank Factorization", "LoRA", "SVD decomposition", "rank reduction", "weight matrix decomposition", "adapter parameter reduction"]
    },
    {
      "id": "memory_bandwidth_cache_optimization",
      "name": "Memory Bandwidth, Cache Locality & Kernel Tuning",
      "description": "Analyzing memory-bound vs compute-bound layers (Roofline model), SRAM cache utilization, and FlashAttention I/O awareness.",
      "keywords": ["Roofline model", "memory-bound", "compute-bound", "SRAM", "cache locality", "FlashAttention", "IO awareness", "kernel fusion"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Optimized neural network inference via INT8 Quantization and TensorRT compilation, reducing latency by 4x",
        "strength": 0.5,
        "maps_to": ["ml_model_optimization_compression.post_training_quantization_ptq", "ml_model_optimization_compression.tensorrt_gpu_acceleration", "ml_model_optimization_compression.knowledge_distillation_teacher_student"]
      }
    ],
    "linkedin": [
      {
        "signal": "Model Quantization, TensorRT, and Model Compression endorsements",
        "strength": 0.3,
        "maps_to": ["ml_model_optimization_compression.structural_unstructured_weight_pruning", "ml_model_optimization_compression.model_compilation_torch_compile_tvm"]
      }
    ],
    "github": [
      {
        "pattern": "*quant*.py|*prune*.py|*distill*.py|*tensorrt*|*compile*.py",
        "strength": 1.0,
        "maps_to": [
          "ml_model_optimization_compression.post_training_quantization_ptq",
          "ml_model_optimization_compression.quantization_aware_training_qat",
          "ml_model_optimization_compression.structural_unstructured_weight_pruning",
          "ml_model_optimization_compression.knowledge_distillation_teacher_student",
          "ml_model_optimization_compression.tensorrt_gpu_acceleration",
          "ml_model_optimization_compression.openvino_cpu_optimization",
          "ml_model_optimization_compression.model_compilation_torch_compile_tvm",
          "ml_model_optimization_compression.low_rank_matrix_factorization_weights",
          "ml_model_optimization_compression.memory_bandwidth_cache_optimization"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Compression, Quantization & Acceleration Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_model_optimization_compression.post_training_quantization_ptq",
          "ml_model_optimization_compression.quantization_aware_training_qat",
          "ml_model_optimization_compression.structural_unstructured_weight_pruning",
          "ml_model_optimization_compression.knowledge_distillation_teacher_student",
          "ml_model_optimization_compression.tensorrt_gpu_acceleration",
          "ml_model_optimization_compression.openvino_cpu_optimization",
          "ml_model_optimization_compression.model_compilation_torch_compile_tvm",
          "ml_model_optimization_compression.low_rank_matrix_factorization_weights",
          "ml_model_optimization_compression.memory_bandwidth_cache_optimization"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["post_training_quantization_ptq", "model_compilation_torch_compile_tvm", "openvino_cpu_optimization"],
      "description": "Applies post-training dynamic quantization (PTQ) and compiles standard PyTorch models with torch.compile."
    },
    "mid": {
      "expected_subskills": ["structural_unstructured_weight_pruning", "knowledge_distillation_teacher_student", "low_rank_matrix_factorization_weights", "quantization_aware_training_qat"],
      "description": "Trains student models via Knowledge Distillation, prunes weights with iterative finetuning, and implements QAT fake quantization."
    },
    "senior": {
      "expected_subskills": ["tensorrt_gpu_acceleration", "memory_bandwidth_cache_optimization"],
      "description": "Builds optimized TensorRT engines with custom layer fusions and optimizes hardware memory bandwidth using the Roofline model."
    }
  }
}

# 9. ml_monitoring_drift_observability
skills["ml_monitoring_drift_observability"] = {
  "skill_id": "ml_monitoring_drift_observability",
  "name": "Model Monitoring, Explainability & Drift Detection",
  "category": "observability",
  "description": "Production model observability: detecting Data Drift, Concept Drift, prediction drift, statistical divergence (PSI, KS-test), explainable AI (SHAP, LIME), performance decay, and automated alerting.",
  "subskills": [
    {
      "id": "data_covariate_drift_detection",
      "name": "Data Drift & Covariate Shift Detection",
      "description": "Detecting distribution shifts in input features P(X), Kolmogorov-Smirnov test (KS-test), Population Stability Index (PSI), and Wasserstein distance.",
      "keywords": ["data drift", "covariate shift", "PSI", "Population Stability Index", "KS-test", "Kolmogorov-Smirnov", "Wasserstein distance", "P(X) shift"]
    },
    {
      "id": "concept_prior_drift_detection",
      "name": "Concept Drift & Prior Shift P(Y|X) / P(Y)",
      "description": "Detecting relationship shifts between features and targets P(Y|X), prior probability shifts P(Y), sudden vs gradual vs seasonal drift.",
      "keywords": ["concept drift", "prior shift", "P(Y|X)", "P(Y)", "seasonal drift", "gradual drift", "relationship change", "degraded accuracy"]
    },
    {
      "id": "evidently_ai_whylogs_monitoring_tooling",
      "name": "Drift Monitoring Frameworks (Evidently AI, whylogs)",
      "description": "Automated drift reports and test suites in Evidently AI, statistical data profiling with whylogs, and real-time dashboarding.",
      "keywords": ["Evidently AI", "whylogs", "drift report", "data profile", "statistical tests", "test suite", "drift dashboard", "monitoring report"]
    },
    {
      "id": "shap_shapley_feature_attribution",
      "name": "SHAP (SHapley Additive exPlanations) & Feature Attribution",
      "description": "Game-theoretic Shapley values, TreeSHAP, KernelSHAP, summary plots, waterfall plots, dependence plots, and local/global explainability.",
      "keywords": ["SHAP", "TreeSHAP", "KernelSHAP", "Shapley values", "feature attribution", "waterfall plot", "summary plot", "dependence plot", "local explanation"]
    },
    {
      "id": "lime_local_interpretable_explanations",
      "name": "LIME (Local Interpretable Model-agnostic Explanations)",
      "description": "Perturbation-based local surrogate models, interpretable feature representations, and explaining individual black-box predictions.",
      "keywords": ["LIME", "local surrogate", "model agnostic", "perturbation", "black box explanation", "interpretable features"]
    },
    {
      "id": "performance_decay_ground_truth_delay",
      "name": "Performance Decay & Delayed Ground Truth Handling",
      "description": "Tracking metrics with delayed labels, proxy performance estimation (NannyML), confidence degradation, and business impact estimation.",
      "keywords": ["delayed ground truth", "performance estimation", "NannyML", "confidence decay", "accuracy drop", "feedback loop", "proxy metrics"]
    },
    {
      "id": "adversarial_anomaly_out_of_distribution_ood",
      "name": "Out-of-Distribution (OOD) & Adversarial Input Detection",
      "description": "Mahalanobis distance, energy-based OOD scores, detecting corrupted/adversarial payloads before feeding into model inference.",
      "keywords": ["OOD", "Out-of-Distribution", "Mahalanobis distance", "adversarial input", "energy score", "input validation", "anomaly rejection"]
    },
    {
      "id": "fairness_bias_demographic_parity",
      "name": "Model Fairness, Disparate Impact & Bias Auditing",
      "description": "Demographic parity, Equalized Odds, disparate impact ratio, Fairlearn / AIF360, and auditing protected attributes.",
      "keywords": ["Fairness", "Fairlearn", "AIF360", "Demographic Parity", "Equalized Odds", "disparate impact", "bias audit", "protected attributes"]
    },
    {
      "id": "ml_alerting_automated_incident_response",
      "name": "ML Alerting Rules & Automated Incident Response",
      "description": "Defining metric threshold alert rules in Prometheus/Grafana, automated fallback model triggering, and retraining pipeline invocation.",
      "keywords": ["ML alerting", "Prometheus", "Grafana", "fallback model", "incident response", "automated retraining trigger", "alertmanager"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Implemented real-time data drift monitoring with Evidently AI and integrated SHAP explainability into production APIs",
        "strength": 0.5,
        "maps_to": ["ml_monitoring_drift_observability.data_covariate_drift_detection", "ml_monitoring_drift_observability.shap_shapley_feature_attribution", "ml_monitoring_drift_observability.evidently_ai_whylogs_monitoring_tooling"]
      }
    ],
    "linkedin": [
      {
        "signal": "Model Monitoring, Explainable AI (SHAP), and Data Drift endorsements",
        "strength": 0.3,
        "maps_to": ["ml_monitoring_drift_observability.concept_prior_drift_detection", "ml_monitoring_drift_observability.lime_local_interpretable_explanations"]
      }
    ],
    "github": [
      {
        "pattern": "*monitor*.py|*drift*.py|*shap*.py|*explain*.py|reports/**/*.html",
        "strength": 1.0,
        "maps_to": [
          "ml_monitoring_drift_observability.data_covariate_drift_detection",
          "ml_monitoring_drift_observability.concept_prior_drift_detection",
          "ml_monitoring_drift_observability.evidently_ai_whylogs_monitoring_tooling",
          "ml_monitoring_drift_observability.shap_shapley_feature_attribution",
          "ml_monitoring_drift_observability.lime_local_interpretable_explanations",
          "ml_monitoring_drift_observability.performance_decay_ground_truth_delay",
          "ml_monitoring_drift_observability.adversarial_anomaly_out_of_distribution_ood",
          "ml_monitoring_drift_observability.fairness_bias_demographic_parity",
          "ml_monitoring_drift_observability.ml_alerting_automated_incident_response"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes Model Monitoring, Explainability & Drift Detection Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_monitoring_drift_observability.data_covariate_drift_detection",
          "ml_monitoring_drift_observability.concept_prior_drift_detection",
          "ml_monitoring_drift_observability.evidently_ai_whylogs_monitoring_tooling",
          "ml_monitoring_drift_observability.shap_shapley_feature_attribution",
          "ml_monitoring_drift_observability.lime_local_interpretable_explanations",
          "ml_monitoring_drift_observability.performance_decay_ground_truth_delay",
          "ml_monitoring_drift_observability.adversarial_anomaly_out_of_distribution_ood",
          "ml_monitoring_drift_observability.fairness_bias_demographic_parity",
          "ml_monitoring_drift_observability.ml_alerting_automated_incident_response"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["data_covariate_drift_detection", "shap_shapley_feature_attribution", "lime_local_interpretable_explanations"],
      "description": "Computes KS-test and PSI for drift, generates SHAP/LIME explanation plots for stakeholder transparency."
    },
    "mid": {
      "expected_subskills": ["concept_prior_drift_detection", "evidently_ai_whylogs_monitoring_tooling", "performance_decay_ground_truth_delay", "fairness_bias_demographic_parity"],
      "description": "Configures Evidently AI test suites, tracks performance with delayed labels, and conducts bias audits using Fairlearn."
    },
    "senior": {
      "expected_subskills": ["adversarial_anomaly_out_of_distribution_ood", "ml_alerting_automated_incident_response"],
      "description": "Architects Out-of-Distribution (OOD) protection gates and implements automated alerting with fallback model routing."
    }
  }
}

# 10. ml_pipelines_orchestration
skills["ml_pipelines_orchestration"] = {
  "skill_id": "ml_pipelines_orchestration",
  "name": "ML Pipelines, Feature Stores & MLOps",
  "category": "mlops",
  "description": "End-to-end MLOps: experiment tracking and model registry (MLflow), pipeline orchestration (Kubeflow Pipelines, Metaflow), feature stores (Feast), data version control (DVC), and automated CI/CD for machine learning (CML).",
  "subskills": [
    {
      "id": "mlflow_tracking_model_registry",
      "name": "MLflow Tracking, Model Registry & Artifacts",
      "description": "Logging parameters, metrics, and model artifacts with mlflow.log_*, model signatures, Model Registry stages (Staging, Production, Archived), and version transitions.",
      "keywords": ["MLflow", "Model Registry", "mlflow.log_metric", "mlflow.log_param", "model signature", "mlflow.pyfunc", "model stage", "artifact store"]
    },
    {
      "id": "dvc_data_version_control",
      "name": "Data Version Control (DVC) & Reproducibility",
      "description": "Version controlling gigabyte datasets and model weights using Git and remote storage (S3/GCS) with DVC, dvc.yaml pipeline stages.",
      "keywords": ["DVC", "dvc.yaml", "dvc repro", "dvc push", "dvc pull", "data versioning", "remote storage", "reproducibility", ".dvc"]
    },
    {
      "id": "feature_store_feast_architecture",
      "name": "Feature Stores (Feast) - Online & Offline Stores",
      "description": "Feature definitions, entities, offline store for historical point-in-time correct training joins, and low-latency online store (Redis) for real-time inference.",
      "keywords": ["Feast", "Feature Store", "offline store", "online store", "point-in-time join", "time-travel feature join", "entity", "feature view", "Redis"]
    },
    {
      "id": "kubeflow_pipelines_kfp_components",
      "name": "Kubeflow Pipelines (KFP) & Component Design",
      "description": "Containerized pipeline components in Kubeflow, @dsl.pipeline, @dsl.component, input/output artifacts, pipeline compiling, and KFP on Kubernetes.",
      "keywords": ["Kubeflow", "KFP", "Kubeflow Pipelines", "@dsl.component", "@dsl.pipeline", "pipeline compilation", "kfp.v2", "containerized pipeline"]
    },
    {
      "id": "metaflow_human_centric_ml_workflows",
      "name": "Metaflow Human-Centric ML Workflows",
      "description": "Developing ML workflows with Metaflow @step, branching, foreach parallel execution, resuming failed runs, and AWS/Kubernetes integration.",
      "keywords": ["Metaflow", "@step", "FlowSpec", "foreach", "self.next", "Metaflow artifacts", "Netflix Metaflow", "step resumption"]
    },
    {
      "id": "ci_cd_cml_continuous_machine_learning",
      "name": "Continuous Machine Learning (CML) & GitHub Actions",
      "description": "Automated training on PRs, generating markdown model evaluation report comments in pull requests using CML and GitHub Actions.",
      "keywords": ["CML", "Continuous Machine Learning", "Iterative CML", "PR model report", "cml send-comment", "GitHub Actions for ML", "automated benchmark PR"]
    },
    {
      "id": "automated_continuous_training_ct_triggers",
      "name": "Continuous Training (CT) Triggers & Retraining Loops",
      "description": "Event-driven vs schedule-based automated retraining triggers, model gate evaluation against current production model, and automated deployment.",
      "keywords": ["Continuous Training", "CT", "retraining trigger", "champion challenger", "model gate", "automated retraining", "production promotion"]
    },
    {
      "id": "docker_gpu_containers_cuda_drivers",
      "name": "GPU Containerization (Docker, NVIDIA Container Toolkit)",
      "description": "Configuring Dockerfiles with CUDA/cuDNN base images, NVIDIA Container Toolkit (--gpus all), multi-stage builds for ML, and CUDA compatibility.",
      "keywords": ["NVIDIA Container Toolkit", "--gpus all", "CUDA base image", "cuDNN", "Dockerfile for ML", "GPU container", "CUDA driver compatibility"]
    },
    {
      "id": "model_catalog_governance_lineage",
      "name": "Model Governance, Lineage & Compliance Cards",
      "description": "Documenting Model Cards (intended use, training dataset, limitations), model lineage from raw data commit to production binary, and audit trails.",
      "keywords": ["Model Card", "model governance", "model lineage", "audit trail", "compliance", "training data provenance", "intended use"]
    }
  ],
  "evidence_patterns": {
    "cv": [
      {
        "signal": "Built end-to-end MLOps platform using MLflow, Feast Feature Store, and Kubeflow Pipelines with automated Continuous Training",
        "strength": 0.5,
        "maps_to": ["ml_pipelines_orchestration.mlflow_tracking_model_registry", "ml_pipelines_orchestration.feature_store_feast_architecture", "ml_pipelines_orchestration.kubeflow_pipelines_kfp_components"]
      }
    ],
    "linkedin": [
      {
        "signal": "MLOps, MLflow, and Kubeflow specialist endorsements",
        "strength": 0.3,
        "maps_to": ["ml_pipelines_orchestration.dvc_data_version_control", "ml_pipelines_orchestration.ci_cd_cml_continuous_machine_learning"]
      }
    ],
    "github": [
      {
        "pattern": "*mlflow*|*pipeline*.py|dvc.yaml|feature_store.yaml|kfp*.py",
        "strength": 1.0,
        "maps_to": [
          "ml_pipelines_orchestration.mlflow_tracking_model_registry",
          "ml_pipelines_orchestration.dvc_data_version_control",
          "ml_pipelines_orchestration.feature_store_feast_architecture",
          "ml_pipelines_orchestration.kubeflow_pipelines_kfp_components",
          "ml_pipelines_orchestration.metaflow_human_centric_ml_workflows",
          "ml_pipelines_orchestration.ci_cd_cml_continuous_machine_learning",
          "ml_pipelines_orchestration.automated_continuous_training_ct_triggers",
          "ml_pipelines_orchestration.docker_gpu_containers_cuda_drivers",
          "ml_pipelines_orchestration.model_catalog_governance_lineage"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes ML Pipelines, Feature Stores & MLOps Technical Assessment",
        "strength": 1.0,
        "maps_to": [
          "ml_pipelines_orchestration.mlflow_tracking_model_registry",
          "ml_pipelines_orchestration.dvc_data_version_control",
          "ml_pipelines_orchestration.feature_store_feast_architecture",
          "ml_pipelines_orchestration.kubeflow_pipelines_kfp_components",
          "ml_pipelines_orchestration.metaflow_human_centric_ml_workflows",
          "ml_pipelines_orchestration.ci_cd_cml_continuous_machine_learning",
          "ml_pipelines_orchestration.automated_continuous_training_ct_triggers",
          "ml_pipelines_orchestration.docker_gpu_containers_cuda_drivers",
          "ml_pipelines_orchestration.model_catalog_governance_lineage"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["mlflow_tracking_model_registry", "dvc_data_version_control", "docker_gpu_containers_cuda_drivers"],
      "description": "Logs runs and models to MLflow, version controls datasets with DVC, and builds GPU Docker containers."
    },
    "mid": {
      "expected_subskills": ["feature_store_feast_architecture", "kubeflow_pipelines_kfp_components", "ci_cd_cml_continuous_machine_learning", "metaflow_human_centric_ml_workflows"],
      "description": "Operates Feast feature stores, authors Kubeflow / Metaflow pipelines, and automates PR evaluation reports with CML."
    },
    "senior": {
      "expected_subskills": ["automated_continuous_training_ct_triggers", "model_catalog_governance_lineage"],
      "description": "Architects enterprise Continuous Training (CT) feedback loops, champion/challenger gates, and governs corporate model compliance."
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
    "role_id": "machine_learning",
    "level": "junior",
    "title": "Junior Machine Learning Engineer",
    "description": "Entry-level machine learning engineering position focused on data preprocessing, feature engineering, training classical algorithms (Scikit-Learn, XGBoost), basic PyTorch neural networks, model evaluation metrics, and experiment tracking under guidance.",
    "experience_range": "0-2 years",
    "skills": [
      {
        "skill_id": "ml_feature_engineering_preprocessing",
        "importance": 0.95,
        "rationale": "High-quality data preparation, imputation, scaling, and feature encoding are non-negotiable foundations for model quality."
      },
      {
        "skill_id": "ml_classical_algorithms",
        "importance": 0.90,
        "rationale": "Strong grasp of regression, decision trees, random forests, and gradient boosting algorithms."
      },
      {
        "skill_id": "ml_model_evaluation_validation",
        "importance": 0.90,
        "rationale": "Accurate calculation of ROC-AUC, PR-AUC, F1 metrics, and diagnosing bias-variance tradeoff."
      },
      {
        "skill_id": "ml_deep_learning_architectures",
        "importance": 0.80,
        "rationale": "Building and training basic neural networks with PyTorch and PyTorch Lightning."
      },
      {
        "skill_id": "ml_mathematics_foundations",
        "importance": 0.75,
        "rationale": "Understanding gradient descent, linear algebra matrix operations, and probability distributions."
      },
      {
        "skill_id": "ml_pipelines_orchestration",
        "importance": 0.70,
        "rationale": "Tracking runs with MLflow, dataset versioning with DVC, and containerizing with Docker."
      },
      {
        "skill_id": "ml_hyperparameter_optimization",
        "importance": 0.65,
        "rationale": "Executing grid/random searches and learning rate schedulers."
      },
      {
        "skill_id": "ml_model_deployment_serving",
        "importance": 0.60,
        "rationale": "Wrapping models into FastAPI prediction endpoints and exporting to ONNX."
      },
      {
        "skill_id": "ml_monitoring_drift_observability",
        "importance": 0.55,
        "rationale": "Calculating statistical drift metrics (PSI, KS-test) and generating SHAP feature plots."
      },
      {
        "skill_id": "ml_model_optimization_compression",
        "importance": 0.45,
        "rationale": "Applying standard post-training quantization and torch.compile."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.35, "description": "Insufficient foundational understanding of machine learning algorithms and preprocessing." },
        "partially_ready": { "min": 0.35, "max": 0.60, "description": "Able to train standard baseline models but lacks production pipeline and evaluation rigor." },
        "ready": { "min": 0.60, "max": 0.85, "description": "Solid junior engineer capable of engineering features, training ML models, and tracking experiments under guidance." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceeds junior expectations with strong deep learning skills and production API deployment knowledge." }
      }
    }
  },
  "mid": {
    "role_id": "machine_learning",
    "level": "mid",
    "title": "Mid-Level Machine Learning Engineer",
    "description": "Mid-level machine learning engineering position focused on building production-grade ML systems, deep learning architectures (CNN, LSTM, Transformers), Bayesian hyperparameter optimization (Optuna), model serving microservices (gRPC/TorchScript), data/concept drift monitoring, and feature store integration.",
    "experience_range": "2-5 years",
    "skills": [
      {
        "skill_id": "ml_classical_algorithms",
        "importance": 0.95,
        "rationale": "Expert tuning and custom ensembling of gradient boosted trees (XGBoost, LightGBM, CatBoost)."
      },
      {
        "skill_id": "ml_deep_learning_architectures",
        "importance": 0.90,
        "rationale": "Developing custom PyTorch architectures, loss functions, and CNN/sequence models."
      },
      {
        "skill_id": "ml_model_evaluation_validation",
        "importance": 0.90,
        "rationale": "Designing leak-free cross-validation, probability calibration, and business threshold tuning."
      },
      {
        "skill_id": "ml_model_deployment_serving",
        "importance": 0.85,
        "rationale": "Building robust model serving services, TorchScript export, load testing, and Canary deployments."
      },
      {
        "skill_id": "ml_hyperparameter_optimization",
        "importance": 0.85,
        "rationale": "Conducting Bayesian optimization with Optuna TPE samplers and pruning unpromising trials."
      },
      {
        "skill_id": "ml_pipelines_orchestration",
        "importance": 0.85,
        "rationale": "Building automated training pipelines with Kubeflow/Metaflow and integrating Feast feature stores."
      },
      {
        "skill_id": "ml_monitoring_drift_observability",
        "importance": 0.80,
        "rationale": "Implementing Evidently AI drift monitoring, delayed ground truth tracking, and SHAP explainability."
      },
      {
        "skill_id": "ml_feature_engineering_preprocessing",
        "importance": 0.80,
        "rationale": "Constructing complex ColumnTransformer pipelines and handling severe class imbalance."
      },
      {
        "skill_id": "ml_mathematics_foundations",
        "importance": 0.75,
        "rationale": "Formulating MLE objectives, tuning Adam/AdamW optimizers, and conducting hypothesis tests."
      },
      {
        "skill_id": "ml_model_optimization_compression",
        "importance": 0.70,
        "rationale": "Applying Knowledge Distillation, weight pruning, and Quantization-Aware Training (QAT)."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.40, "description": "Lacks production ML deployment experience or deep understanding of optimization." },
        "partially_ready": { "min": 0.40, "max": 0.65, "description": "Competent model builder but needs supervision on production serving and drift monitoring." },
        "ready": { "min": 0.65, "max": 0.88, "description": "Fully autonomous ML engineer delivering production-grade models, robust serving APIs, and MLOps workflows." },
        "exceeds": { "min": 0.88, "max": 1.0, "description": "Demonstrates advanced technical leadership in distributed training, hardware acceleration, and system design." }
      }
    }
  },
  "senior": {
    "role_id": "machine_learning",
    "level": "senior",
    "title": "Senior Machine Learning Engineer / ML Architect",
    "description": "Senior technical leadership position driving end-to-end machine learning strategy: distributed multi-GPU training (DDP/FSDP), high-throughput Triton serving clusters, INT8 quantization & TensorRT compilation, automated Continuous Training (CT) feedback loops, Out-of-Distribution security, and enterprise ML governance.",
    "experience_range": "5+ years",
    "skills": [
      {
        "skill_id": "ml_deep_learning_architectures",
        "importance": 0.95,
        "rationale": "Architecting Transformer self-attention mechanisms and scaling multi-GPU distributed training (DDP/FSDP)."
      },
      {
        "skill_id": "ml_model_deployment_serving",
        "importance": 0.95,
        "rationale": "Architecting Triton multi-model inference clusters with dynamic batching and sub-10ms P99 latency."
      },
      {
        "skill_id": "ml_model_optimization_compression",
        "importance": 0.95,
        "rationale": "Building TensorRT engines, memory bandwidth kernel tuning, and hardware acceleration."
      },
      {
        "skill_id": "ml_pipelines_orchestration",
        "importance": 0.90,
        "rationale": "Establishing enterprise Continuous Training loops, champion/challenger gates, and model governance."
      },
      {
        "skill_id": "ml_monitoring_drift_observability",
        "importance": 0.90,
        "rationale": "Architecting Out-of-Distribution (OOD) protection gates, model bias auditing, and automated incident response."
      },
      {
        "skill_id": "ml_hyperparameter_optimization",
        "importance": 0.85,
        "rationale": "Scaling distributed tuning with Ray Tune and multi-objective Pareto optimization (accuracy vs latency)."
      },
      {
        "skill_id": "ml_mathematics_foundations",
        "importance": 0.85,
        "rationale": "Second-order optimization, KL divergence analysis, and custom loss mathematical formulations."
      },
      {
        "skill_id": "ml_classical_algorithms",
        "importance": 0.85,
        "rationale": "Non-spherical density clustering (HDBSCAN), kernel methods, and custom ensemble algorithms."
      },
      {
        "skill_id": "ml_model_evaluation_validation",
        "importance": 0.85,
        "rationale": "Company-wide online A/B testing design and ranking/retrieval evaluation frameworks."
      },
      {
        "skill_id": "ml_feature_engineering_preprocessing",
        "importance": 0.80,
        "rationale": "Designing automated feature selection engines and high-dimensional interaction pipelines."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Each skill score is multiplied by its importance weight. Final score is the sum of weighted scores divided by sum of weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.45, "description": "Does not meet the architectural depth, distributed scaling, or acceleration leadership required for senior roles." },
        "partially_ready": { "min": 0.45, "max": 0.70, "description": "Strong pipeline practitioner but lacks hardware acceleration (TensorRT), distributed DDP, or enterprise MLOps architecture." },
        "ready": { "min": 0.70, "max": 0.90, "description": "Proven senior ML engineer with comprehensive platform architecture, distributed tuning, and production acceleration mastery." },
        "exceeds": { "min": 0.90, "max": 1.0, "description": "World-class ML architect capable of building multi-billion parameter inference systems and enterprise AI platforms." }
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
  "name": "CV / Resume Parser - Machine Learning Engineering",
  "description": "Extraction and scoring rules for Machine Learning Engineer CVs/Resumes based on section base strengths and keyword associations.",
  "sections": [
    {
      "section_id": "work_experience",
      "name": "Work Experience",
      "base_strength": 0.5,
      "description": "Professional machine learning roles, modeling projects, and production deployments.",
      "signal_extractors": [
        {
          "pattern": "PyTorch|TorchScript|DDP|DeepSpeed|FSDP",
          "strength": 0.5,
          "maps_to": [
            "ml_deep_learning_architectures.pytorch_core_autograd_nn_module",
            "ml_deep_learning_architectures.transformer_self_attention_mechanisms",
            "ml_deep_learning_architectures.distributed_training_ddp_fsdp"
          ]
        },
        {
          "pattern": "XGBoost|LightGBM|CatBoost|Scikit-Learn|Random Forest",
          "strength": 0.5,
          "maps_to": [
            "ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost",
            "ml_classical_algorithms.random_forests_bagging",
            "ml_classical_algorithms.linear_logistic_regression_regularization"
          ]
        },
        {
          "pattern": "Triton Inference Server|ONNX Runtime|FastAPI|gRPC",
          "strength": 0.5,
          "maps_to": [
            "ml_model_deployment_serving.triton_inference_server_management",
            "ml_model_deployment_serving.onnx_runtime_export_inference",
            "ml_model_deployment_serving.fastapi_rest_model_microservices"
          ]
        },
        {
          "pattern": "TensorRT|Quantization|INT8|Pruning|Knowledge Distillation",
          "strength": 0.5,
          "maps_to": [
            "ml_model_optimization_compression.tensorrt_gpu_acceleration",
            "ml_model_optimization_compression.post_training_quantization_ptq",
            "ml_model_optimization_compression.knowledge_distillation_teacher_student"
          ]
        },
        {
          "pattern": "Optuna|Ray Tune|Hyperparameter Optimization|Bayesian Optimization",
          "strength": 0.5,
          "maps_to": [
            "ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna",
            "ml_hyperparameter_optimization.early_stopping_pruning_strategies",
            "ml_hyperparameter_optimization.distributed_hyperparameter_tuning_ray"
          ]
        },
        {
          "pattern": "MLflow|Kubeflow|Feast|DVC|Continuous Training",
          "strength": 0.5,
          "maps_to": [
            "ml_pipelines_orchestration.mlflow_tracking_model_registry",
            "ml_pipelines_orchestration.feature_store_feast_architecture",
            "ml_pipelines_orchestration.kubeflow_pipelines_kfp_components"
          ]
        },
        {
          "pattern": "Evidently AI|SHAP|LIME|Data Drift|Concept Drift",
          "strength": 0.5,
          "maps_to": [
            "ml_monitoring_drift_observability.data_covariate_drift_detection",
            "ml_monitoring_drift_observability.shap_shapley_feature_attribution",
            "ml_monitoring_drift_observability.evidently_ai_whylogs_monitoring_tooling"
          ]
        },
        {
          "pattern": "Feature Engineering|ColumnTransformer|Target Encoding|Imputation",
          "strength": 0.5,
          "maps_to": [
            "ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings",
            "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer",
            "ml_feature_engineering_preprocessing.missing_data_imputation_strategies"
          ]
        },
        {
          "pattern": "Cross-Validation|ROC-AUC|PR-AUC|Calibration|A/B Testing",
          "strength": 0.5,
          "maps_to": [
            "ml_model_evaluation_validation.cross_validation_strategies_leakage",
            "ml_model_evaluation_validation.classification_metrics_pr_roc",
            "ml_model_evaluation_validation.probability_calibration_platt_isotonic"
          ]
        },
        {
          "pattern": "Linear Algebra|Optimization|SGD|Adam|MLE|Loss Functions",
          "strength": 0.5,
          "maps_to": [
            "ml_mathematics_foundations.first_order_optimization_sgd_adam",
            "ml_mathematics_foundations.loss_functions_mathematics",
            "ml_mathematics_foundations.matrix_operations_decompositions"
          ]
        }
      ]
    },
    {
      "section_id": "projects",
      "name": "Projects",
      "base_strength": 0.5,
      "description": "Machine learning open-source repositories and research implementations."
    },
    {
      "section_id": "skills_list",
      "name": "Skills List",
      "base_strength": 0.3,
      "description": "Self-reported ML skills and libraries."
    },
    {
      "section_id": "education",
      "name": "Education & Certifications",
      "base_strength": 0.3,
      "description": "Degrees and professional ML certifications."
    }
  ]
}

with open(os.path.join(evidence_dir, 'cv.json'), 'w', encoding='utf-8') as f:
  json.dump(cv_data, f, indent=2)

# 2. linkedin.json
linkedin_data = {
  "source_id": "linkedin",
  "name": "LinkedIn Profile Signals - Machine Learning Engineering",
  "description": "Signals and skill endorsements extracted from candidate LinkedIn profiles.",
  "sections": [
    {
      "section_id": "experience",
      "base_strength": 0.5,
      "description": "Professional experience in Machine Learning Engineer, MLOps Engineer, or Research Engineer roles."
    },
    {
      "section_id": "headline_summary",
      "base_strength": 0.3,
      "description": "Profile headline and summary keywords."
    },
    {
      "section_id": "skills_endorsements",
      "base_strength": 0.3,
      "description": "Endorsed skills related to PyTorch, Scikit-Learn, XGBoost, Model Serving, and MLOps."
    },
    {
      "section_id": "recommendations",
      "base_strength": 0.5,
      "description": "Colleague recommendations validating machine learning capabilities."
    }
  ]
}

with open(os.path.join(evidence_dir, 'linkedin.json'), 'w', encoding='utf-8') as f:
  json.dump(linkedin_data, f, indent=2)

# 3. github.json
github_data = {
  "source_id": "github",
  "name": "GitHub Repository Analysis - Machine Learning Engineering",
  "description": "Automated code and pipeline scanning rules for validating Machine Learning Engineer implementations.",
  "preprocessing_pipeline": {
    "steps": [
      {
        "step": 1,
        "name": "repository_metadata",
        "description": "Inspects languages, dependencies, and commit cadence."
      },
      {
        "step": 2,
        "name": "file_tree_scan",
        "description": "Scans for training scripts, PyTorch models, inference servers, and MLOps configs.",
        "target_files": [
          { "pattern": "train*.py|models/**/*.py|*.pt|*.pth", "skill": "ml_deep_learning_architectures", "priority": "high" },
          { "pattern": "*xgboost*|*lightgbm*|*sklearn*.py", "skill": "ml_classical_algorithms", "priority": "high" },
          { "pattern": "config.pbtxt|*triton*|serve*.py|*.onnx", "skill": "ml_model_deployment_serving", "priority": "high" },
          { "pattern": "*optuna*|*sweep*.py|configs/*hpo*.yml", "skill": "ml_hyperparameter_optimization", "priority": "high" },
          { "pattern": "dvc.yaml|*mlflow*|feature_store.yaml|kfp*.py", "skill": "ml_pipelines_orchestration", "priority": "high" },
          { "pattern": "*drift*.py|*shap*.py|*evidently*", "skill": "ml_monitoring_drift_observability", "priority": "high" },
          { "pattern": "*tensorrt*|*quant*.py|*prune*.py", "skill": "ml_model_optimization_compression", "priority": "high" },
          { "pattern": "*preprocess*.py|*pipeline*.py", "skill": "ml_feature_engineering_preprocessing", "priority": "high" },
          { "pattern": "*eval*.py|*metrics*.py", "skill": "ml_model_evaluation_validation", "priority": "high" }
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
  # ml_mathematics_foundations (9)
  "ml_mathematics_foundations.matrix_operations_decompositions": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the geometric and mathematical interpretation of Singular Value Decomposition (SVD): A = U * Sigma * V^T?",
      "expected_answer_keywords": ["rotation", "scaling", "orthonormal eigenvectors", "singular values", "left singular vectors", "right singular vectors", "matrix decomposition"]
    }
  ],
  "ml_mathematics_foundations.calculus_gradients_hessians": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the difference between a Jacobian matrix and a Hessian matrix in multivariable optimization?",
      "expected_answer_keywords": ["Jacobian first derivatives", "Hessian second derivatives", "curvature", "gradient vector", "vector-valued function", "convexity"]
    }
  ],
  "ml_mathematics_foundations.probability_distributions_bayes": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "State Bayes' Theorem and explain how prior probability is updated by evidence likelihood to yield posterior probability.",
      "expected_answer_keywords": ["Bayes theorem", "P(A|B)", "prior", "posterior", "likelihood", "marginal likelihood", "evidence"]
    }
  ],
  "ml_mathematics_foundations.maximum_likelihood_estimation": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Why do we maximize the log-likelihood rather than the raw likelihood product in MLE parameter estimation?",
      "expected_answer_keywords": ["log-likelihood", "turn products into sums", "numerical underflow", "monotonic transformation", "derivative simplification"]
    }
  ],
  "ml_mathematics_foundations.first_order_optimization_sgd_adam": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does the Adam optimizer combine the principles of Momentum (first moment) and RMSprop (second moment) with bias correction?",
      "expected_answer_keywords": ["exponential moving average", "first moment mean", "second moment uncentered variance", "bias correction", "adaptive learning rate", "Adam"]
    }
  ],
  "ml_mathematics_foundations.second_order_constrained_optimization": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "How does L-BFGS approximate the inverse Hessian matrix without storing the full O(N^2) matrix in memory?",
      "expected_answer_keywords": ["L-BFGS", "quasi-Newton", "implicit Hessian inverse", "curvature vectors s and y", "memory efficient", "two-loop recursion"]
    }
  ],
  "ml_mathematics_foundations.information_theory_entropy": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain why Kullback-Leibler (KL) divergence is non-symmetric: D_KL(P || Q) != D_KL(Q || P), and its implication in VAE loss functions.",
      "expected_answer_keywords": ["KL divergence", "non-symmetric", "relative entropy", "mode-seeking vs mean-seeking", "VAE regularization", "prior distribution"]
    }
  ],
  "ml_mathematics_foundations.statistical_hypothesis_testing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "What is the difference between Type I error (alpha) and Type II error (beta) in ML statistical significance tests, and what determines statistical power (1 - beta)?",
      "expected_answer_keywords": ["Type I false positive", "Type II false negative", "alpha", "beta", "statistical power", "sample size", "effect size"]
    }
  ],
  "ml_mathematics_foundations.loss_functions_mathematics": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does Focal Loss modify standard Cross-Entropy Loss to prevent easy background examples from overwhelming gradient updates?",
      "expected_answer_keywords": ["Focal Loss", "modulating factor (1 - p_t)^gamma", "focus on hard examples", "cross-entropy", "class imbalance", "down-weight easy examples"]
    }
  ],

  # ml_classical_algorithms (9)
  "ml_classical_algorithms.linear_logistic_regression_regularization": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why does L1 regularization (Lasso) produce sparse weight vectors while L2 regularization (Ridge) only shrinks weights toward zero?",
      "expected_answer_keywords": ["L1 diamond constraint", "L2 circular constraint", "corner solution on axes", "sparsity", "feature selection", "penalty term"]
    }
  ],
  "ml_classical_algorithms.decision_trees_splitting_criteria": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Compare Gini Impurity and Entropy/Information Gain as splitting criteria in Decision Trees.",
      "expected_answer_keywords": ["Gini impurity", "Entropy", "Information Gain", "computational complexity", "logarithm vs squares", "CART vs C4.5"]
    }
  ],
  "ml_classical_algorithms.random_forests_bagging": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does Random Forest decorrelate individual trees through feature subsampling (max_features = sqrt(p))?",
      "expected_answer_keywords": ["feature subsampling", "decorrelate trees", "variance reduction", "dominant feature avoidance", "bagging", "ensemble"]
    }
  ],
  "ml_classical_algorithms.gradient_boosting_xgboost_lightgbm_catboost": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Compare XGBoost, LightGBM (GOSS & EFB), and CatBoost (ordered target statistics) in terms of split finding and categorical handling.",
      "expected_answer_keywords": ["LightGBM GOSS", "EFB", "histogram-based", "leaf-wise", "CatBoost ordered target statistics", "XGBoost exact split", "regularized residuals"]
    }
  ],
  "ml_classical_algorithms.support_vector_machines_kernels": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain the Kernel Trick in SVMs and how the Radial Basis Function (RBF) maps data implicitly into infinite-dimensional Hilbert space.",
      "expected_answer_keywords": ["kernel trick", "RBF kernel", "Mercer's theorem", "inner product", "infinite dimensional", "dual formulation", "support vectors"]
    }
  ],
  "ml_classical_algorithms.naive_bayes_knn": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What fundamental conditional independence assumption does Naive Bayes make, and why does it still work well in high-dimensional text classification?",
      "expected_answer_keywords": ["conditional independence", "P(x_i | y)", "naive assumption", "decision boundary robustness", "zero-frequency Laplace smoothing"]
    }
  ],
  "ml_classical_algorithms.kmeans_hierarchical_clustering": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does K-Means++ smart centroid initialization overcome the local optima pitfalls of random initialization?",
      "expected_answer_keywords": ["K-Means++", "distance probability D(x)^2", "spread out centroids", "local minima", "clustering initialization"]
    }
  ],
  "ml_classical_algorithms.density_clustering_dbscan_hdbscan": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Why does DBSCAN succeed on arbitrary non-spherical clusters with noise where K-Means fails, and how does HDBSCAN eliminate the fixed epsilon threshold?",
      "expected_answer_keywords": ["DBSCAN", "HDBSCAN", "varying density", "non-spherical clusters", "core points", "noise rejection", "hierarchical density tree"]
    }
  ],
  "ml_classical_algorithms.pca_dimensionality_reduction": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does Principal Component Analysis (PCA) find orthogonal axes that maximize variance using the sample covariance matrix?",
      "expected_answer_keywords": ["covariance matrix", "eigenvalues", "eigenvectors", "orthogonal projection", "maximum variance", "dimensionality reduction"]
    }
  ],

  # ml_feature_engineering_preprocessing (9)
  "ml_feature_engineering_preprocessing.missing_data_imputation_strategies": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the difference between MCAR, MAR, and MNAR missingness, and when MICE (IterativeImputer) is preferred over simple median imputation.",
      "expected_answer_keywords": ["MCAR", "MAR", "MNAR", "MICE", "IterativeImputer", "multivariate relationships", "median imputation bias"]
    }
  ],
  "ml_feature_engineering_preprocessing.categorical_encoding_target_ohe_embeddings": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you implement Target Encoding on high-cardinality features without causing target leakage and overfitting?",
      "expected_answer_keywords": ["target leakage", "smoothing weight m", "out-of-fold target encoding", "additive noise", "global mean blend"]
    }
  ],
  "ml_feature_engineering_preprocessing.feature_scaling_power_transformations": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "When should you use RobustScaler instead of StandardScaler, and what do Yeo-Johnson / Box-Cox transformations achieve?",
      "expected_answer_keywords": ["RobustScaler", "median and IQR", "outlier resistance", "StandardScaler mean/variance", "Yeo-Johnson negative values", "Box-Cox normality"]
    }
  ],
  "ml_feature_engineering_preprocessing.outlier_detection_treatment": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does an Isolation Forest isolate anomalies using random partitioning trees, and why are anomalies isolated with shorter path lengths?",
      "expected_answer_keywords": ["Isolation Forest", "random partition", "average path length", "few splits to isolate", "anomaly score", "multivariate outliers"]
    }
  ],
  "ml_feature_engineering_preprocessing.interaction_polynomial_features": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do feature crossing and polynomial interaction terms allow linear models to capture non-linear decision boundaries?",
      "expected_answer_keywords": ["feature crossing", "interaction terms", "x1 * x2", "non-linear boundary", "PolynomialFeatures", "expressive power"]
    }
  ],
  "ml_feature_engineering_preprocessing.temporal_datetime_cyclical_features": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why should cyclical features like hour-of-day (0-23) be encoded using sin and cos transforms rather than raw integer values?",
      "expected_answer_keywords": ["cyclical encoding", "sin and cos", "circular continuity", "hour 23 close to hour 0", "distance distortion", "trigonometric mapping"]
    }
  ],
  "ml_feature_engineering_preprocessing.text_nlp_feature_extraction_tfidf_embeddings": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Explain the formula and purpose of Term Frequency-Inverse Document Frequency (TF-IDF) in down-weighting common corpus terms.",
      "expected_answer_keywords": ["TF-IDF", "Term Frequency", "Inverse Document Frequency", "log(N / df)", "down-weight stop words", "informative terms"]
    }
  ],
  "ml_feature_engineering_preprocessing.feature_selection_filter_wrapper_embedded": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Compare Filter methods (Mutual Information), Wrapper methods (RFE), and Embedded methods (Lasso/Tree importance) for feature selection.",
      "expected_answer_keywords": ["Filter fast model-agnostic", "Wrapper RFE computationally expensive", "Embedded Lasso L1", "feature selection trade-offs", "multicollinearity"]
    }
  ],
  "ml_feature_engineering_preprocessing.sklearn_pipelines_columntransformer": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why does fitting scalers and encoders inside a Scikit-Learn Pipeline object prevent train-test data leakage during cross-validation?",
      "expected_answer_keywords": ["Pipeline", "ColumnTransformer", "fit on train fold only", "transform on test fold", "leakage prevention", "reproducible pipeline"]
    }
  ],

  # ml_model_evaluation_validation (9)
  "ml_model_evaluation_validation.cross_validation_strategies_leakage": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why is standard K-Fold cross-validation invalid for time-series forecasting, and how does TimeSeriesSplit preserve chronological order?",
      "expected_answer_keywords": ["TimeSeriesSplit", "lookahead bias", "temporal ordering", "train on past predict future", "expanding window", "purging"]
    }
  ],
  "ml_model_evaluation_validation.classification_metrics_pr_roc": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is the Precision-Recall AUC (PR-AUC) much more informative than ROC-AUC when evaluating highly imbalanced classification datasets (e.g. 0.1% positive fraud)?",
      "expected_answer_keywords": ["PR-AUC", "ROC-AUC", "True Negative inflation", "imbalanced data", "False Positive impact", "Precision focus"]
    }
  ],
  "ml_model_evaluation_validation.regression_metrics_residual_analysis": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What does heteroscedasticity in a regression residual plot indicate, and how does it violate standard OLS linear regression assumptions?",
      "expected_answer_keywords": ["heteroscedasticity", "non-constant variance", "funnel shape residual plot", "OLS assumption violation", "weighted least squares", "log transform"]
    }
  ],
  "ml_model_evaluation_validation.probability_calibration_platt_isotonic": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why do tree-based ensembles (XGBoost) often output uncalibrated probabilities, and how does Platt Scaling (logistic calibration) resolve this?",
      "expected_answer_keywords": ["uncalibrated probabilities", "Platt scaling", "logistic sigmoid fit", "Isotonic Regression", "reliability diagram", "Brier score"]
    }
  ],
  "ml_model_evaluation_validation.bias_variance_tradeoff_learning_curves": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you identify high bias (underfitting) vs high variance (overfitting) by looking at training vs validation loss curves?",
      "expected_answer_keywords": ["high bias high train error", "high variance large train-validation gap", "overfitting", "underfitting", "learning curve convergence"]
    }
  ],
  "ml_model_evaluation_validation.imbalanced_data_handling_smote": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does SMOTE synthesize new minority class samples along KNN line segments, and why must SMOTE only be applied to training folds?",
      "expected_answer_keywords": ["SMOTE", "k-nearest neighbors interpolation", "synthetic instances", "data leakage prevention", "fit on training fold only", "minority class"]
    }
  ],
  "ml_model_evaluation_validation.threshold_tuning_cost_matrices": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "If a False Negative costs $500 and a False Positive costs $10, how do you tune the classification decision threshold away from the default 0.5?",
      "expected_answer_keywords": ["cost matrix", "threshold tuning", "minimize expected cost", "lower threshold for high recall", "cost of FN vs FP", "expected value optimization"]
    }
  ],
  "ml_model_evaluation_validation.ranking_recommendation_metrics": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "Explain the formula for Normalized Discounted Cumulative Gain (NDCG@K) and why logarithmic position discounting is crucial.",
      "expected_answer_keywords": ["NDCG@K", "DCG", "IDCG", "logarithmic position discount", "relevance score", "ranking evaluation", "top positions weight"]
    }
  ],
  "ml_model_evaluation_validation.ab_testing_online_evaluation": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you calculate the required sample size and duration for an online ML A/B test given alpha=0.05, beta=0.20, and a Minimum Detectable Effect (MDE)?",
      "expected_answer_keywords": ["MDE", "Minimum Detectable Effect", "sample size calculation", "statistical power", "traffic split", "variance estimation", "significance level"]
    }
  ],

  # ml_deep_learning_architectures (9)
  "ml_deep_learning_architectures.pytorch_core_autograd_nn_module": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does PyTorch's dynamic computation graph (autograd) compute gradients during backward(), and why is optimizer.zero_grad() necessary?",
      "expected_answer_keywords": ["autograd", "dynamic computation graph", "backward()", "gradient accumulation", "optimizer.zero_grad()", "leaf nodes", "requires_grad"]
    }
  ],
  "ml_deep_learning_architectures.feedforward_regularization_batchnorm_dropout": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What is the difference in behavior between Batch Normalization and Dropout during model.train() vs model.eval() modes?",
      "expected_answer_keywords": ["model.train() vs model.eval()", "BatchNorm running mean/var", "Dropout disabled during eval", "inverted dropout scaling", "internal covariate shift"]
    }
  ],
  "ml_deep_learning_architectures.convolutional_neural_networks_cnn": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why do ResNet skip/residual connections: F(x) + x, prevent vanishing gradients in 100+ layer deep convolutional networks?",
      "expected_answer_keywords": ["residual connection", "skip connection", "identity mapping", "gradient highway", "F(x) + x", "vanishing gradient prevention", "ResNet"]
    }
  ],
  "ml_deep_learning_architectures.recurrent_networks_lstm_gru": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Explain the role of the Forget Gate and Cell State in Long Short-Term Memory (LSTM) networks for retaining long-range dependencies.",
      "expected_answer_keywords": ["Forget Gate", "Cell State", "additive update", "sigmoid gate", "long-range dependencies", "LSTM", "vanishing gradient mitigation"]
    }
  ],
  "ml_deep_learning_architectures.transformer_self_attention_mechanisms": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Derive the Scaled Dot-Product Attention equation: Softmax(QK^T / sqrt(d_k))V, and explain why scaling by sqrt(d_k) prevents vanishing gradients.",
      "expected_answer_keywords": ["Scaled Dot-Product", "QK^T / sqrt(d_k)", "Softmax", "d_k scaling", "extremely small gradients in softmax", "large magnitude dot products", "Self-Attention"]
    }
  ],
  "ml_deep_learning_architectures.autoencoders_variational_ae": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Why is the Reparameterization Trick: z = mu + sigma * epsilon, essential for backpropagation in Variational Autoencoders (VAEs)?",
      "expected_answer_keywords": ["Reparameterization trick", "z = mu + sigma * epsilon", "stochastic sampling", "differentiable", "backpropagation", "VAE", "latent vector"]
    }
  ],
  "ml_deep_learning_architectures.custom_layers_loss_functions_pytorch": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you implement a custom PyTorch autograd function with static forward() and backward() methods?",
      "expected_answer_keywords": ["torch.autograd.Function", "forward(ctx, ...)", "backward(ctx, grad_output)", "ctx.save_for_backward", "custom derivative", "autograd extension"]
    }
  ],
  "ml_deep_learning_architectures.deep_learning_training_loop_lightning": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How does PyTorch Lightning decouple engineering boilerplate (device placement, AMP, logging) from research model code in LightningModule?",
      "expected_answer_keywords": ["PyTorch Lightning", "LightningModule", "Trainer", "training_step", "validation_step", "configure_optimizers", "automatic mixed precision"]
    }
  ],
  "ml_deep_learning_architectures.distributed_training_ddp_fsdp": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain the architectural difference between DistributedDataParallel (DDP) gradient all-reduce and Fully Sharded Data Parallel (FSDP) parameter sharding.",
      "expected_answer_keywords": ["DDP all-reduce", "FSDP sharding", "ZeRO stage 3", "sharded parameters", "gradients and optimizer states", "GPU memory reduction", "distributed training"]
    }
  ],

  # ml_hyperparameter_optimization (9)
  "ml_hyperparameter_optimization.grid_random_search_tuning": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why does Randomized Search explore high-dimensional hyperparameter spaces with low effective dimensionality much more efficiently than Grid Search?",
      "expected_answer_keywords": ["RandomizedSearchCV", "GridSearchCV", "effective dimensionality", "unique values per dimension", "curse of dimensionality", "random distribution"]
    }
  ],
  "ml_hyperparameter_optimization.bayesian_optimization_tpe_optuna": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Optuna's Tree-structured Parzen Estimator (TPE) use the ratio l(x)/g(x) of good vs bad trials to propose candidate hyperparameters?",
      "expected_answer_keywords": ["Optuna", "TPE", "Tree-structured Parzen Estimator", "l(x) / g(x)", "Expected Improvement", "Bayesian optimization", "gamma quantile"]
    }
  ],
  "ml_hyperparameter_optimization.early_stopping_pruning_strategies": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does the Asynchronous Successive Halving Algorithm (ASHA) prune underperforming hyperparameter trials dynamically?",
      "expected_answer_keywords": ["ASHA", "Successive Halving", "Hyperband", "trial pruning", "bracket promotion", "early stopping", "resource allocation"]
    }
  ],
  "ml_hyperparameter_optimization.learning_rate_schedulers_warmup": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Why is a linear learning rate warmup phase combined with Cosine Annealing effective during the initial epochs of neural network training?",
      "expected_answer_keywords": ["warmup phase", "Cosine Annealing", "stabilize initial random gradients", "avoid early divergence", "smooth decay", "learning rate schedule"]
    }
  ],
  "ml_hyperparameter_optimization.multi_objective_optimization": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you use Optuna multi-objective optimization with NSGA-II to find the Pareto frontier between model accuracy and inference latency?",
      "expected_answer_keywords": ["Pareto frontier", "multi-objective", "NSGA-II", "accuracy vs latency trade-off", "non-dominated solutions", "directions=['maximize', 'minimize']"]
    }
  ],
  "ml_hyperparameter_optimization.distributed_hyperparameter_tuning_ray": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does Population Based Training (PBT) in Ray Tune dynamically mutate hyperparameters (e.g. learning rate) during a single training run?",
      "expected_answer_keywords": ["Ray Tune", "Population Based Training", "PBT", "explore and exploit", "copy weights from top performers", "mutate hyperparameters", "distributed workers"]
    }
  ],
  "ml_hyperparameter_optimization.search_space_design_hyperparameter_types": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "Why must learning rates and regularization penalties be sampled on a logarithmic scale (suggest_float(log=True))?",
      "expected_answer_keywords": ["logarithmic scale", "order of magnitude", "suggest_float(log=True)", "equal sampling probability across 1e-4 and 1e-2", "scale invariance"]
    }
  ],
  "ml_hyperparameter_optimization.k_fold_integrated_hpo": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain why Nested Cross-Validation (inner loop for tuning, outer loop for testing) is necessary to report an unbiased performance estimate.",
      "expected_answer_keywords": ["Nested Cross-Validation", "inner loop hyperparameter selection", "outer loop generalization estimate", "optimism bias", "unbiased evaluation"]
    }
  ],
  "ml_hyperparameter_optimization.experiment_tracking_wandb_mlflow_hpo": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do Parallel Coordinates plots in Weights & Biases (W&B) or MLflow visualize multi-hyperparameter correlations with model loss?",
      "expected_answer_keywords": ["Parallel Coordinates", "W&B sweeps", "MLflow experiments", "hyperparameter correlation", "visualize multi-dimensional tuning", "loss minimization path"]
    }
  ],

  # ml_model_deployment_serving (9)
  "ml_model_deployment_serving.fastapi_rest_model_microservices": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you build a high-concurrency async prediction API using FastAPI with Pydantic validation and startup model caching?",
      "expected_answer_keywords": ["FastAPI", "Pydantic", "lifespan / startup event", "async def", "model in-memory caching", "request validation", "REST API"]
    }
  ],
  "ml_model_deployment_serving.grpc_protobuf_high_throughput_serving": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why is gRPC over HTTP/2 significantly faster than JSON REST for high-throughput machine learning inference payloads?",
      "expected_answer_keywords": ["gRPC", "HTTP/2 multiplexing", "Protocol Buffers", "binary serialization", "low CPU serialization overhead", "streaming RPC"]
    }
  ],
  "ml_model_deployment_serving.triton_inference_server_management": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you configure dynamic batching and instance groups in a Triton config.pbtxt file to maximize GPU utilization under varying load?",
      "expected_answer_keywords": ["Triton", "config.pbtxt", "dynamic_batching", "max_queue_delay_microseconds", "instance_group", "KIND_GPU", "GPU saturation"]
    }
  ],
  "ml_model_deployment_serving.onnx_runtime_export_inference": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How do you export a PyTorch model to ONNX using torch.onnx.export and specify dynamic batch dimensions in dynamic_axes?",
      "expected_answer_keywords": ["torch.onnx.export", "dynamic_axes", "dynamic batch size", "ONNX Runtime", "InferenceSession", "input_names", "output_names"]
    }
  ],
  "ml_model_deployment_serving.torchscript_trace_script_deployment": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "When should you use torch.jit.script over torch.jit.trace to serialize a PyTorch model containing dynamic control flow (if/else, loops)?",
      "expected_answer_keywords": ["torch.jit.script", "torch.jit.trace", "dynamic control flow", "AST inspection", "tracing fixed control flow", "C++ deployment", "TorchScript"]
    }
  ],
  "ml_model_deployment_serving.batch_vs_realtime_serving_architectures": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "Compare Offline Batch Scoring (Spark/Ray), Online Real-Time Serving (FastAPI/Triton), and Nearline Streaming Inference.",
      "expected_answer_keywords": ["batch scoring", "real-time serving", "streaming inference", "throughput vs latency trade-off", "pre-computed predictions", "event-driven"]
    }
  ],
  "ml_model_deployment_serving.dynamic_batching_concurrency_control": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does server-side dynamic batching assemble independent concurrent requests into a single tensor batch without exceeding latency deadlines?",
      "expected_answer_keywords": ["dynamic batching", "request queuing", "max_queue_delay", "batch dimension concatenation", "tensor splitting", "latency threshold"]
    }
  ],
  "ml_model_deployment_serving.model_canary_shadow_ab_deployment": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain how Shadow Deployment (Dark Launch) mirrors live production traffic to a candidate model without affecting client responses.",
      "expected_answer_keywords": ["Shadow deployment", "dark launch", "mirror live traffic", "fire-and-forget", "zero user impact", "production validation", "Seldon / KServe"]
    }
  ],
  "ml_model_deployment_serving.latency_profiling_load_testing": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you use Locust to profile the P95 and P99 latency percentiles of a model microservice under 1,000 concurrent RPS?",
      "expected_answer_keywords": ["Locust", "P95 latency", "P99 latency", "RPS", "concurrency testing", "cold start spikes", "stress testing", "latency distribution"]
    }
  ],

  # ml_model_optimization_compression (9)
  "ml_model_optimization_compression.post_training_quantization_ptq": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does Post-Training Quantization (PTQ) convert FP32 weights and activations to INT8 using scale and zero-point calibration?",
      "expected_answer_keywords": ["PTQ", "INT8", "scale factor", "zero-point", "affine quantization", "calibration dataset", "4x memory reduction"]
    }
  ],
  "ml_model_optimization_compression.quantization_aware_training_qat": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Quantization-Aware Training (QAT) model quantization noise during the forward pass while using Straight-Through Estimators (STE) in backward pass?",
      "expected_answer_keywords": ["QAT", "Quantization-Aware Training", "fake quantization", "Straight-Through Estimator", "STE", "round function derivative", "accuracy recovery"]
    }
  ],
  "ml_model_optimization_compression.structural_unstructured_weight_pruning": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Why does structured channel pruning yield immediate speedups on standard GPUs whereas unstructured sparse pruning requires specialized sparse hardware?",
      "expected_answer_keywords": ["structured pruning", "unstructured pruning", "channel pruning", "dense matrix dimensions", "sparse tensor overhead", "hardware acceleration"]
    }
  ],
  "ml_model_optimization_compression.knowledge_distillation_teacher_student": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "In Knowledge Distillation, how does temperature scaling T > 1 soften target probability distributions to transfer dark knowledge to the student model?",
      "expected_answer_keywords": ["Knowledge Distillation", "temperature scaling", "soft targets", "dark knowledge", "KL divergence", "student model", "teacher logits"]
    }
  ],
  "ml_model_optimization_compression.tensorrt_gpu_acceleration": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How does NVIDIA TensorRT perform vertical and horizontal layer fusion (e.g. Conv + BatchNorm + ReLU into a single kernel) to reduce memory bandwidth roundtrips?",
      "expected_answer_keywords": ["TensorRT", "layer fusion", "Conv+BatchNorm+ReLU", "kernel fusion", "SRAM memory bandwidth", "TRT engine compilation", "GPU kernel launch overhead"]
    }
  ],
  "ml_model_optimization_compression.openvino_cpu_optimization": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does Intel OpenVINO utilize AVX-512 and VNNI instruction sets to accelerate INT8 neural network inference on modern CPUs?",
      "expected_answer_keywords": ["OpenVINO", "AVX-512", "VNNI", "vector neural network instructions", "CPU inference acceleration", "Intel Model Optimizer"]
    }
  ],
  "ml_model_optimization_compression.model_compilation_torch_compile_tvm": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does PyTorch 2.0 torch.compile capture graphs with TorchDynamo and generate optimized kernel C++/Triton code with TorchInductor?",
      "expected_answer_keywords": ["torch.compile", "TorchDynamo", "TorchInductor", "Triton code generation", "graph capture", "PyTorch 2.0", "kernel fusion"]
    }
  ],
  "ml_model_optimization_compression.low_rank_matrix_factorization_weights": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does low-rank matrix decomposition replace a dense W (d x k) weight matrix with two low-rank matrices A (d x r) and B (r x k) where r << min(d, k)?",
      "expected_answer_keywords": ["low-rank decomposition", "W = A * B", "rank r", "parameter reduction", "SVD factorization", "LoRA", "FLOP reduction"]
    }
  ],
  "ml_model_optimization_compression.memory_bandwidth_cache_optimization": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "Explain the Roofline Model (Arithmetic Intensity vs Memory Bandwidth) and how FlashAttention reorganizes Softmax computation to be I/O-aware.",
      "expected_answer_keywords": ["Roofline model", "Arithmetic Intensity", "memory-bound vs compute-bound", "FlashAttention", "SRAM tiling", "HBM memory access reduction"]
    }
  ],

  # ml_monitoring_drift_observability (9)
  "ml_monitoring_drift_observability.data_covariate_drift_detection": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does the Population Stability Index (PSI) quantify covariate shift between baseline training data and production inference data?",
      "expected_answer_keywords": ["PSI", "Population Stability Index", "covariate shift", "binning distributions", "PSI < 0.1 stable", "distribution divergence"]
    }
  ],
  "ml_monitoring_drift_observability.concept_prior_drift_detection": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "What is the difference between Covariate Shift P(X), Concept Drift P(Y|X), and Prior Probability Shift P(Y)?",
      "expected_answer_keywords": ["Covariate Shift P(X)", "Concept Drift P(Y|X)", "Prior Shift P(Y)", "relationship change", "input distribution change", "target distribution change"]
    }
  ],
  "ml_monitoring_drift_observability.evidently_ai_whylogs_monitoring_tooling": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you integrate Evidently AI or whylogs into an automated pipeline to generate HTML drift reports and trigger Slack alerts on drift detection?",
      "expected_answer_keywords": ["Evidently AI", "whylogs", "DataDriftPreset", "statistical tests", "HTML report", "automated test suite", "drift alert"]
    }
  ],
  "ml_monitoring_drift_observability.shap_shapley_feature_attribution": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "What game-theoretic properties (efficiency, symmetry, additivity) make SHAP values mathematically sound for local feature attribution?",
      "expected_answer_keywords": ["SHAP", "Shapley values", "game theory", "efficiency", "symmetry", "additivity", "local feature attribution", "TreeSHAP"]
    }
  ],
  "ml_monitoring_drift_observability.lime_local_interpretable_explanations": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does LIME explain a complex black-box model prediction by training an interpretable sparse linear surrogate on perturbed neighborhood samples?",
      "expected_answer_keywords": ["LIME", "local surrogate", "perturbed samples", "exponential kernel weighting", "interpretable linear model", "model agnostic"]
    }
  ],
  "ml_monitoring_drift_observability.performance_decay_ground_truth_delay": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "In domains where ground truth labels arrive with months of delay (e.g. loan defaults), how can you estimate model performance degradation using confidence scores?",
      "expected_answer_keywords": ["delayed ground truth", "CBPE", "confidence-based performance estimation", "NannyML", "proxy metrics", "prediction distribution shift"]
    }
  ],
  "ml_monitoring_drift_observability.adversarial_anomaly_out_of_distribution_ood": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do Mahalanobis distance and deep feature embeddings detect Out-of-Distribution (OOD) test samples before generating misleading model predictions?",
      "expected_answer_keywords": ["OOD detection", "Mahalanobis distance", "penultimate layer embeddings", "covariance matrix", "anomaly threshold", "reject uncertain inputs"]
    }
  ],
  "ml_monitoring_drift_observability.fairness_bias_demographic_parity": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "Explain the trade-off between Demographic Parity P(Y_hat=1 | A=0) = P(Y_hat=1 | A=1) and Equalized Odds in algorithmic bias auditing.",
      "expected_answer_keywords": ["Demographic Parity", "Equalized Odds", "TPR and FPR equality", "protected attribute", "Fairlearn", "fairness-accuracy trade-off", "disparate impact"]
    }
  ],
  "ml_monitoring_drift_observability.ml_alerting_automated_incident_response": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you architect a Prometheus/Grafana alerting rule that automatically redirects production traffic to a heuristic fallback model when inference error spikes?",
      "expected_answer_keywords": ["Prometheus", "Grafana alert", "Alertmanager", "fallback model redirect", "circuit breaker", "automated incident response", "error rate spike"]
    }
  ],

  # ml_pipelines_orchestration (9)
  "ml_pipelines_orchestration.mlflow_tracking_model_registry": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you log parameters, metrics, and PyFunc model artifacts with MLflow, and manage model stage transitions (Staging -> Production)?",
      "expected_answer_keywords": ["MLflow", "mlflow.log_params", "mlflow.log_metrics", "mlflow.pyfunc.log_model", "Model Registry", "transition_model_version_stage", "model signature"]
    }
  ],
  "ml_pipelines_orchestration.dvc_data_version_control": [
    {
      "level": "junior",
      "type": "conceptual",
      "question": "How does Data Version Control (DVC) link large dataset pointers in Git with remote cloud storage (S3/GCS) using content-addressable hash files?",
      "expected_answer_keywords": ["DVC", "dvc.yaml", ".dvc file", "content-addressable hash", "dvc push", "dvc pull", "S3 remote storage", "Git dataset pointer"]
    }
  ],
  "ml_pipelines_orchestration.feature_store_feast_architecture": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How does Feast Feature Store provide point-in-time correct historical joins for training while serving low-latency online features from Redis?",
      "expected_answer_keywords": ["Feast", "offline store", "online store", "point-in-time join", "time travel join", "prevent training-serving skew", "Redis", "FeatureView"]
    }
  ],
  "ml_pipelines_orchestration.kubeflow_pipelines_kfp_components": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you author containerized ML pipeline components in Kubeflow Pipelines (KFP) using the @dsl.component decorator and pass artifacts?",
      "expected_answer_keywords": ["Kubeflow Pipelines", "KFP", "@dsl.component", "@dsl.pipeline", "Input[Artifact]", "Output[Model]", "containerized execution", "kfp compiler"]
    }
  ],
  "ml_pipelines_orchestration.metaflow_human_centric_ml_workflows": [
    {
      "level": "mid",
      "type": "conceptual",
      "question": "How does Netflix Metaflow structure DAG steps with @step, foreach branch parallelism, and artifact persistence across AWS batch jobs?",
      "expected_answer_keywords": ["Metaflow", "FlowSpec", "@step", "foreach", "artifact persistence", "self.next", "cloud compute offloading"]
    }
  ],
  "ml_pipelines_orchestration.ci_cd_cml_continuous_machine_learning": [
    {
      "level": "mid",
      "type": "scenario",
      "question": "How do you configure Continuous Machine Learning (CML) and GitHub Actions to train a benchmark model on pull requests and post performance metrics as a PR comment?",
      "expected_answer_keywords": ["CML", "Continuous Machine Learning", "GitHub Actions", "cml send-comment", "PR benchmark report", "automated model test in CI", "markdown report"]
    }
  ],
  "ml_pipelines_orchestration.automated_continuous_training_ct_triggers": [
    {
      "level": "senior",
      "type": "scenario",
      "question": "How do you design a Continuous Training (CT) pipeline with Champion/Challenger validation gates before promoting a newly retrained model to production?",
      "expected_answer_keywords": ["Continuous Training", "CT", "Champion-Challenger", "validation gate", "automated retraining", "production promotion", "statistically superior metric"]
    }
  ],
  "ml_pipelines_orchestration.docker_gpu_containers_cuda_drivers": [
    {
      "level": "junior",
      "type": "scenario",
      "question": "How do you write a multi-stage Dockerfile utilizing NVIDIA CUDA base images and NVIDIA Container Toolkit for secure GPU-accelerated model training?",
      "expected_answer_keywords": ["NVIDIA Container Toolkit", "Dockerfile for ML", "CUDA base image", "multi-stage build", "non-root user", "cuDNN", "--gpus all"]
    }
  ],
  "ml_pipelines_orchestration.model_catalog_governance_lineage": [
    {
      "level": "senior",
      "type": "conceptual",
      "question": "What components must be included in a standardized Model Card (intended use, training dataset provenance, quantitative metrics, ethical limitations) for regulatory compliance?",
      "expected_answer_keywords": ["Model Card", "training data provenance", "intended use", "limitations", "ethical audit", "model governance", "reproducibility lineage"]
    }
  ]
}

assessment_data = {
  "source_id": "assessment",
  "name": "Machine Learning Engineering Adaptive Technical Assessment",
  "description": "Comprehensive technical question bank and adaptive testing engine for evaluating Machine Learning Engineer candidate proficiency across all 90 composite subskills.",
  "trigger_conditions": {
    "rules": [
      "When a subskill has status 'not_yet_evidenced' (confidence = 0.0) for a target role level",
      "When a subskill has status 'insufficient_evidence' and confidence < 0.4",
      "When CV/LinkedIn claims a skill but GitHub code has no supporting implementation",
      "When a skill is critical for the target role (importance >= 0.80) and evidence is ambiguous"
    ]
  },
  "question_types": [
    { "type": "conceptual", "strength": 0.6, "description": "Tests deep theoretical, mathematical and algorithmic understanding." },
    { "type": "scenario", "strength": 0.8, "description": "Tests practical problem-solving, debugging, and production engineering." },
    { "type": "practical_task", "strength": 1.0, "description": "Hands-on implementation task validating production ML code." }
  ],
  "sample_questions_by_composite_key": questions_by_key
}

with open(os.path.join(evidence_dir, 'assessment.json'), 'w', encoding='utf-8') as f:
  json.dump(assessment_data, f, indent=2)

print(f"Generated complete evidence files in {evidence_dir}")
print(f"Total questions mapped in assessment.json: {len(questions_by_key)}")
