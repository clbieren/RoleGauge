import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "data-analyst")
evidence_dir = os.path.join(base_dir, "evidence", "data-analyst")

# 1. da_excel
da_excel = {
  "skill_id": "da_excel",
  "name": "Excel & Spreadsheets",
  "category": "analysis",
  "description": "Advanced Excel techniques for data manipulation, summarization, and reporting.",
  "subskills": [
    {
      "id": "basic_formulas",
      "name": "Basic Formulas",
      "description": "Using SUM, AVERAGE, COUNT, IF, AND, OR for basic cell calculations.",
      "keywords": ["SUM", "AVERAGE", "COUNT", "IF", "AND", "OR", "formula"]
    },
    {
      "id": "pivot_tables",
      "name": "Pivot Tables",
      "description": "Summarizing large datasets, creating calculated fields, and using slicers.",
      "keywords": ["Pivot Table", "Slicer", "Calculated Field", "Pivot Chart"]
    },
    {
      "id": "data_formatting",
      "name": "Data Formatting",
      "description": "Formatting text, numbers, dates, and using text-to-columns.",
      "keywords": ["Text to Columns", "Data Formatting", "Number Format", "Date Format"]
    },
    {
      "id": "vlookup_index_match",
      "name": "VLOOKUP/INDEX-MATCH",
      "description": "Looking up and merging data across sheets using VLOOKUP, HLOOKUP, XLOOKUP, or INDEX/MATCH.",
      "keywords": ["VLOOKUP", "INDEX", "MATCH", "XLOOKUP", "HLOOKUP"]
    },
    {
      "id": "data_validation",
      "name": "Data Validation",
      "description": "Creating dropdown lists and restricting cell inputs to ensure data integrity.",
      "keywords": ["Data Validation", "Dropdown List", "Input Restriction"]
    },
    {
      "id": "conditional_formatting",
      "name": "Conditional Formatting",
      "description": "Applying color scales, data bars, and formula-based formatting rules.",
      "keywords": ["Conditional Formatting", "Color Scale", "Data Bar", "Highlight Cells Rules"]
    },
    {
      "id": "macros_vba",
      "name": "Macros & VBA",
      "description": "Automating repetitive Excel tasks using recorded Macros and VBA scripting.",
      "keywords": ["Macro", "VBA", "Visual Basic", "Automate"]
    },
    {
      "id": "power_query",
      "name": "Power Query",
      "description": "Connecting to external data sources, merging, appending, and transforming data via Power Query.",
      "keywords": ["Power Query", "Get & Transform", "M Code", "Merge Queries", "Append Queries"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "VBA scripts present",
        "detection": "file_presence",
        "pattern": "\\.vba$|\\.bas$",
        "strength": 0.8,
        "maps_to": ["da_excel.macros_vba"]
      }
    ],
    "cv": [
      {
        "signal": "Mentioned Pivot Tables, VLOOKUP, or Power Query",
        "strength": 0.6,
        "maps_to": ["da_excel.pivot_tables", "da_excel.vlookup_index_match", "da_excel.power_query"]
      }
    ],
    "linkedin": [
      {
        "signal": "Advanced Excel or VBA endorsed",
        "strength": 0.5,
        "maps_to": ["da_excel.macros_vba", "da_excel.vlookup_index_match"]
      }
    ],
    "assessment": [
      {
        "signal": "Can construct a dynamic INDEX/MATCH formula across multiple sheets",
        "strength": 1.0,
        "maps_to": ["da_excel.vlookup_index_match"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["basic_formulas", "pivot_tables", "data_formatting"],
      "description": "Can perform basic daily reporting and summarization."
    },
    "mid": {
      "expected_subskills": ["vlookup_index_match", "data_validation", "conditional_formatting"],
      "description": "Can handle complex lookups and create interactive, validated templates."
    },
    "senior": {
      "expected_subskills": ["macros_vba", "power_query"],
      "description": "Can automate data pipelines and build robust VBA applications within Excel."
    }
  }
}

# 2. da_data_visualization
da_data_visualization = {
  "skill_id": "da_data_visualization",
  "name": "Data Visualization",
  "category": "analysis",
  "description": "Visualizing data effectively and building dashboards.",
  "subskills": [
    {
      "id": "chart_types",
      "name": "Basic Chart Types",
      "description": "Choosing appropriate charts (bar, line, scatter, pie) for the data.",
      "keywords": ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Histogram"]
    },
    {
      "id": "basic_dashboards",
      "name": "Basic Dashboards",
      "description": "Creating simple dashboards in Excel or basic BI tools.",
      "keywords": ["Dashboard", "Report", "Visual Summary"]
    },
    {
      "id": "color_theory",
      "name": "Color Theory",
      "description": "Applying color palettes effectively for accessibility and emphasis.",
      "keywords": ["Color Palette", "Accessibility", "Colorblind safe", "Contrast"]
    },
    {
      "id": "interactive_plots",
      "name": "Interactive Plots (Plotly)",
      "description": "Building interactive visualizations using libraries like Plotly or Bokeh.",
      "keywords": ["Plotly", "Bokeh", "Interactive Chart", "Hover effects"]
    },
    {
      "id": "bi_tools",
      "name": "BI Tools (Tableau/PowerBI)",
      "description": "Developing enterprise dashboards using Tableau, Power BI, Looker, etc.",
      "keywords": ["Tableau", "Power BI", "Looker", "DAX", "Calculated Field"]
    },
    {
      "id": "storytelling",
      "name": "Data Storytelling",
      "description": "Structuring visual narratives to drive business decisions.",
      "keywords": ["Data Storytelling", "Narrative", "Business Impact", "Insights"]
    },
    {
      "id": "custom_visualizations",
      "name": "Custom Visualizations",
      "description": "Creating highly customized visuals beyond standard chart types.",
      "keywords": ["Custom Visuals", "Sankey Diagram", "Network Graph", "Geospatial"]
    },
    {
      "id": "d3_js_advanced",
      "name": "D3.js / Advanced",
      "description": "Programming bespoke, low-level web visualizations using D3.js.",
      "keywords": ["D3.js", "SVG", "Canvas", "Web Visualization"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Python script using interactive visualization libraries",
        "detection": "dependency_extraction",
        "pattern": "plotly|bokeh|altair",
        "strength": 0.8,
        "maps_to": ["da_data_visualization.interactive_plots"]
      },
      {
        "signal": "Usage of D3.js",
        "detection": "content_analysis",
        "pattern": "d3\\.select|d3\\.scale",
        "strength": 0.9,
        "maps_to": ["da_data_visualization.d3_js_advanced"]
      }
    ],
    "cv": [
      {
        "signal": "Experience with Tableau or Power BI",
        "strength": 0.7,
        "maps_to": ["da_data_visualization.bi_tools"]
      }
    ],
    "linkedin": [
      {
        "signal": "Data Visualization or BI tools endorsed",
        "strength": 0.5,
        "maps_to": ["da_data_visualization.bi_tools", "da_data_visualization.chart_types"]
      }
    ],
    "assessment": [
      {
        "signal": "Can design a dashboard layout selecting the correct chart types for KPIs",
        "strength": 1.0,
        "maps_to": ["da_data_visualization.bi_tools", "da_data_visualization.storytelling"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["chart_types", "basic_dashboards", "color_theory"],
      "description": "Can produce standard charts and assemble basic reports."
    },
    "mid": {
      "expected_subskills": ["interactive_plots", "bi_tools", "storytelling"],
      "description": "Can build interactive enterprise BI dashboards and tell a cohesive data story."
    },
    "senior": {
      "expected_subskills": ["custom_visualizations", "d3_js_advanced"],
      "description": "Can architect custom visualization solutions and bespoke visual components."
    }
  }
}

# 3. da_programming
da_programming = {
  "skill_id": "da_programming",
  "name": "Programming for Data Analysis",
  "category": "programming",
  "description": "Python/R programming fundamentals and data manipulation libraries.",
  "subskills": [
    {
      "id": "variables_types",
      "name": "Variables & Types",
      "description": "Understanding core data types (int, string, bool).",
      "keywords": ["Variables", "Data Types", "int", "string", "bool"]
    },
    {
      "id": "loops_conditionals",
      "name": "Loops & Conditionals",
      "description": "Control flow using for, while, if, elif, else.",
      "keywords": ["for loop", "while loop", "if statement", "control flow"]
    },
    {
      "id": "functions",
      "name": "Functions",
      "description": "Writing reusable code blocks using def or lambda.",
      "keywords": ["def", "function", "lambda", "return"]
    },
    {
      "id": "pandas_basics",
      "name": "Pandas Basics",
      "description": "Data manipulation using pandas DataFrames and Series.",
      "keywords": ["pandas", "DataFrame", "Series", "pd.merge", "groupby"]
    },
    {
      "id": "numpy_arrays",
      "name": "Numpy Arrays",
      "description": "Vectorized operations and linear algebra using NumPy.",
      "keywords": ["numpy", "ndarray", "vectorization", "np.array"]
    },
    {
      "id": "data_structures",
      "name": "Data Structures",
      "description": "Using lists, dictionaries, sets, and tuples efficiently.",
      "keywords": ["list", "dictionary", "set", "tuple", "hash map"]
    },
    {
      "id": "code_optimization",
      "name": "Code Optimization",
      "description": "Writing memory-efficient and fast execution code (list comprehensions, generators).",
      "keywords": ["list comprehension", "generator", "yield", "timeit", "optimization"]
    },
    {
      "id": "oop_concepts",
      "name": "OOP Concepts",
      "description": "Object-oriented programming principles (classes, inheritance, methods).",
      "keywords": ["class", "object", "inheritance", "self", "__init__"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Python Pandas usage",
        "detection": "content_analysis",
        "pattern": "import pandas as pd",
        "strength": 0.8,
        "maps_to": ["da_programming.pandas_basics"]
      },
      {
        "signal": "Python OOP usage",
        "detection": "content_analysis",
        "pattern": "class \\w+\\(.*\\):",
        "strength": 0.7,
        "maps_to": ["da_programming.oop_concepts"]
      }
    ],
    "cv": [
      {
        "signal": "Python data analysis mentioned",
        "strength": 0.6,
        "maps_to": ["da_programming.pandas_basics"]
      }
    ],
    "linkedin": [
      {
        "signal": "Python endorsed",
        "strength": 0.5,
        "maps_to": ["da_programming.pandas_basics", "da_programming.functions"]
      }
    ],
    "assessment": [
      {
        "signal": "Can write an optimized pandas data transformation pipeline",
        "strength": 1.0,
        "maps_to": ["da_programming.pandas_basics", "da_programming.code_optimization"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["variables_types", "loops_conditionals", "functions"],
      "description": "Can write basic scripts for data tasks."
    },
    "mid": {
      "expected_subskills": ["pandas_basics", "numpy_arrays", "data_structures"],
      "description": "Can perform complex data manipulation and vectorized operations."
    },
    "senior": {
      "expected_subskills": ["code_optimization", "oop_concepts"],
      "description": "Can write production-ready, object-oriented, and optimized analysis code."
    }
  }
}

# 4. da_data_cleaning
da_data_cleaning = {
  "skill_id": "da_data_cleaning",
  "name": "Data Cleaning & Preprocessing",
  "category": "data_engineering",
  "description": "Cleaning messy data, handling outliers, and preparing for analysis.",
  "subskills": [
    {
      "id": "missing_values",
      "name": "Handling Missing Values",
      "description": "Identifying and dropping/filling Null/NaN values.",
      "keywords": ["dropna", "fillna", "isnull", "NaN", "missing data"]
    },
    {
      "id": "deduplication",
      "name": "Deduplication",
      "description": "Removing duplicate records.",
      "keywords": ["drop_duplicates", "duplicated", "unique"]
    },
    {
      "id": "data_type_casting",
      "name": "Type Casting",
      "description": "Converting strings to dates, floats to ints, etc.",
      "keywords": ["astype", "to_datetime", "to_numeric", "type casting"]
    },
    {
      "id": "outlier_detection",
      "name": "Outlier Detection",
      "description": "Identifying anomalies using IQR or Z-score.",
      "keywords": ["outlier", "IQR", "Z-score", "anomaly detection"]
    },
    {
      "id": "regex_cleaning",
      "name": "Regex Cleaning",
      "description": "Using Regular Expressions for complex text extraction/cleaning.",
      "keywords": ["regex", "re.sub", "re.match", "pattern matching"]
    },
    {
      "id": "string_manipulation",
      "name": "String Manipulation",
      "description": "Cleaning text data (strip, lower, replace).",
      "keywords": ["str.strip", "str.lower", "str.replace", "text cleaning"]
    },
    {
      "id": "imputation_strategies",
      "name": "Advanced Imputation",
      "description": "Using KNN or regression for missing data imputation.",
      "keywords": ["KNN Imputer", "SimpleImputer", "Multivariate Imputation"]
    },
    {
      "id": "feature_scaling",
      "name": "Feature Scaling",
      "description": "Standardizing or normalizing numeric features.",
      "keywords": ["StandardScaler", "MinMaxScaler", "Normalization", "Standardization"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Pandas data cleaning methods",
        "detection": "content_analysis",
        "pattern": "\\.dropna\\(|\\.fillna\\(|\\.drop_duplicates\\(",
        "strength": 0.8,
        "maps_to": ["da_data_cleaning.missing_values", "da_data_cleaning.deduplication"]
      },
      {
        "signal": "Usage of regex module",
        "detection": "content_analysis",
        "pattern": "import re\\n",
        "strength": 0.7,
        "maps_to": ["da_data_cleaning.regex_cleaning"]
      }
    ],
    "cv": [
      {
        "signal": "Data cleaning/wrangling experience mentioned",
        "strength": 0.6,
        "maps_to": ["da_data_cleaning.missing_values", "da_data_cleaning.string_manipulation"]
      }
    ],
    "linkedin": [
      {
        "signal": "Data Wrangling endorsed",
        "strength": 0.5,
        "maps_to": ["da_data_cleaning.missing_values"]
      }
    ],
    "assessment": [
      {
        "signal": "Can design an imputation strategy for a dataset with 30% missing values",
        "strength": 1.0,
        "maps_to": ["da_data_cleaning.imputation_strategies"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["missing_values", "deduplication", "data_type_casting"],
      "description": "Can handle basic inconsistencies and nulls in standard datasets."
    },
    "mid": {
      "expected_subskills": ["outlier_detection", "regex_cleaning", "string_manipulation"],
      "description": "Can clean unstructured text data and detect statistical outliers."
    },
    "senior": {
      "expected_subskills": ["imputation_strategies", "feature_scaling"],
      "description": "Can prepare datasets for ML models using advanced imputation and scaling."
    }
  }
}

# 5. da_statistical_analysis
da_statistical_analysis = {
  "skill_id": "da_statistical_analysis",
  "name": "Statistical Analysis",
  "category": "analysis",
  "description": "Applying statistics to interpret data.",
  "subskills": [
    {
      "id": "descriptive_stats",
      "name": "Descriptive Statistics",
      "description": "Mean, median, mode, variance, standard deviation.",
      "keywords": ["Mean", "Median", "Variance", "Standard Deviation", "describe"]
    },
    {
      "id": "probability_basics",
      "name": "Probability Basics",
      "description": "Basic probability concepts and conditional probability.",
      "keywords": ["Probability", "Bayes", "Conditional Probability"]
    },
    {
      "id": "distributions",
      "name": "Distributions",
      "description": "Normal, Binomial, Poisson distributions.",
      "keywords": ["Normal Distribution", "Binomial", "Poisson", "Skewness", "Kurtosis"]
    },
    {
      "id": "hypothesis_testing",
      "name": "Hypothesis Testing",
      "description": "T-tests, ANOVA, Chi-Square, p-values.",
      "keywords": ["Hypothesis Test", "p-value", "T-test", "ANOVA", "Null Hypothesis"]
    },
    {
      "id": "correlation",
      "name": "Correlation",
      "description": "Pearson, Spearman correlation coefficients.",
      "keywords": ["Correlation", "Pearson", "Spearman", "Covariance"]
    },
    {
      "id": "ab_testing",
      "name": "A/B Testing",
      "description": "Designing and evaluating A/B tests for product changes.",
      "keywords": ["A/B Testing", "Experiment Design", "Control Group", "Sample Size"]
    },
    {
      "id": "regression_analysis",
      "name": "Regression Analysis",
      "description": "Linear and logistic regression for inference.",
      "keywords": ["Linear Regression", "Logistic Regression", "R-squared", "Coefficients"]
    },
    {
      "id": "time_series_analysis",
      "name": "Time Series",
      "description": "ARIMA, seasonality, moving averages.",
      "keywords": ["Time Series", "ARIMA", "Seasonality", "Moving Average"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Statsmodels or scipy.stats usage",
        "detection": "dependency_extraction",
        "pattern": "statsmodels|scipy\\.stats",
        "strength": 0.8,
        "maps_to": ["da_statistical_analysis.hypothesis_testing", "da_statistical_analysis.regression_analysis"]
      }
    ],
    "cv": [
      {
        "signal": "Statistical analysis or A/B testing experience",
        "strength": 0.6,
        "maps_to": ["da_statistical_analysis.ab_testing", "da_statistical_analysis.hypothesis_testing"]
      }
    ],
    "linkedin": [
      {
        "signal": "Statistics endorsed",
        "strength": 0.5,
        "maps_to": ["da_statistical_analysis.descriptive_stats"]
      }
    ],
    "assessment": [
      {
        "signal": "Can interpret a p-value in the context of an A/B test",
        "strength": 1.0,
        "maps_to": ["da_statistical_analysis.ab_testing", "da_statistical_analysis.hypothesis_testing"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["descriptive_stats", "probability_basics"],
      "description": "Can summarize data distributions and central tendencies."
    },
    "mid": {
      "expected_subskills": ["distributions", "hypothesis_testing", "correlation"],
      "description": "Can perform significance testing and evaluate correlations."
    },
    "senior": {
      "expected_subskills": ["ab_testing", "regression_analysis", "time_series_analysis"],
      "description": "Can design robust experiments and perform predictive/inferential regression."
    }
  }
}

# 6. da_machine_learning
da_machine_learning = {
  "skill_id": "da_machine_learning",
  "name": "Machine Learning & Big Data",
  "category": "analysis",
  "description": "ML concepts, model building, and Big Data processing frameworks.",
  "subskills": [
    {
      "id": "concept_understanding",
      "name": "ML Concepts",
      "description": "Understanding supervised vs unsupervised, bias-variance tradeoff.",
      "keywords": ["Supervised Learning", "Unsupervised Learning", "Bias-Variance", "Overfitting"]
    },
    {
      "id": "train_test_split",
      "name": "Train/Test Split",
      "description": "Splitting data and cross-validation.",
      "keywords": ["train_test_split", "Cross Validation", "K-Fold"]
    },
    {
      "id": "scikit_learn_basics",
      "name": "Scikit-Learn Basics",
      "description": "Using sklearn APIs (fit, predict, transform).",
      "keywords": ["sklearn", "fit", "predict", "Pipeline"]
    },
    {
      "id": "classification_models",
      "name": "Classification Models",
      "description": "Random Forests, XGBoost, Decision Trees.",
      "keywords": ["Random Forest", "XGBoost", "Decision Tree", "Logistic Regression"]
    },
    {
      "id": "clustering",
      "name": "Clustering",
      "description": "K-Means, DBSCAN, Hierarchical.",
      "keywords": ["K-Means", "Clustering", "DBSCAN"]
    },
    {
      "id": "model_evaluation",
      "name": "Model Evaluation",
      "description": "Accuracy, Precision, Recall, F1, ROC-AUC.",
      "keywords": ["Precision", "Recall", "F1 Score", "ROC", "AUC", "Confusion Matrix"]
    },
    {
      "id": "big_data_hadoop",
      "name": "Hadoop Ecosystem",
      "description": "Processing large datasets using HDFS, MapReduce, Hive.",
      "keywords": ["Hadoop", "HDFS", "MapReduce", "Hive", "EMR"]
    },
    {
      "id": "big_data_spark",
      "name": "Apache Spark / PySpark",
      "description": "Distributed data processing using Spark DataFrames.",
      "keywords": ["Spark", "PySpark", "RDD", "Spark DataFrame"]
    },
    {
      "id": "hyperparameter_tuning",
      "name": "Hyperparameter Tuning",
      "description": "GridSearchCV, RandomSearchCV.",
      "keywords": ["GridSearchCV", "RandomizedSearchCV", "Hyperopt"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Scikit-learn usage",
        "detection": "dependency_extraction",
        "pattern": "scikit-learn|sklearn",
        "strength": 0.8,
        "maps_to": ["da_machine_learning.scikit_learn_basics"]
      },
      {
        "signal": "PySpark usage",
        "detection": "content_analysis",
        "pattern": "from pyspark\\.sql import SparkSession",
        "strength": 0.9,
        "maps_to": ["da_machine_learning.big_data_spark"]
      }
    ],
    "cv": [
      {
        "signal": "Machine learning projects or Big Data experience mentioned",
        "strength": 0.6,
        "maps_to": ["da_machine_learning.classification_models", "da_machine_learning.big_data_hadoop"]
      }
    ],
    "linkedin": [
      {
        "signal": "Spark/Hadoop or ML endorsed",
        "strength": 0.6,
        "maps_to": ["da_machine_learning.big_data_spark", "da_machine_learning.concept_understanding"]
      }
    ],
    "assessment": [
      {
        "signal": "Can evaluate a classification model's performance on imbalanced data",
        "strength": 1.0,
        "maps_to": ["da_machine_learning.model_evaluation"]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": ["concept_understanding", "train_test_split", "scikit_learn_basics"],
      "description": "Understands ML basics and can use scikit-learn APIs."
    },
    "mid": {
      "expected_subskills": ["classification_models", "clustering", "model_evaluation"],
      "description": "Can build and evaluate standard classification and clustering models."
    },
    "senior": {
      "expected_subskills": ["big_data_hadoop", "big_data_spark", "hyperparameter_tuning"],
      "description": "Can tune complex models and process massive datasets using distributed computing frameworks."
    }
  }
}

for sk_dict in [da_excel, da_data_visualization, da_programming, da_data_cleaning, da_statistical_analysis, da_machine_learning]:
    with open(os.path.join(skills_dir, f"{sk_dict['skill_id']}.json"), "w", encoding="utf-8") as f:
        json.dump(sk_dict, f, indent=2)

print("Remaining files enriched successfully.")
