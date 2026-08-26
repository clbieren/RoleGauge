import os
import json

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge-base'))

# Ensure directories
os.makedirs(os.path.join(base_dir, 'skills', 'ai-engineer'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'roles', 'ai-engineer'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'evidence', 'ai-engineer'), exist_ok=True)

CRITICAL_NOTE_DA = "Data Analyst'in ML'i tahmine dayalı klasik modelleme (regresyon, sınıflandırma, kümeleme) ve büyük veri işlemedir; AI Engineer, üretken/büyük dil modellerini (LLM) uygulamalara RAG, agent ve prompt engineering yoluyla entegre etme disiplinidir — farklı matematiksel temel, farklı araç seti, farklı problem sınıfı."

CRITICAL_NOTE_SEC = "Cyber Security (Siber Güvenlik) geleneksel altyapı, ağ güvenliği, sızma testleri, IAM ve OS/bulut zafiyetlerine odaklanırken; AI Safety, Ethics & Deployment disiplini LLM'lere özgü prompt injection, jailbreaking, halüsinasyon azaltma, guardrails, model önyargısı (bias/fairness), alignment (hizalama) ve üretken yapay zeka gizlilik/telif uyumluluğuna odaklanır — farklı tehdit yüzeyi, farklı hafifletme teknikleri, farklı uzmanlık alanı."

# -------------------------------------------------------------
# 1. AI Engineer Skills Definitions
# -------------------------------------------------------------
ai_skills = [
    # ---------------------------------------------------------
    # Skill 1: ai_llm_fundamentals
    # ---------------------------------------------------------
    {
        "skill_id": "ai_llm_fundamentals",
        "name": "Large Language Model Fundamentals & Architecture",
        "category": "ai_core",
        "description": f"Foundation models, transformer architectures, tokenization, pre-training vs fine-tuning (LoRA, QLoRA, PEFT), inference mechanics, sampling parameters, context windows, and quantitative evaluation benchmarks. ÖNEMLİ AYRIM: {CRITICAL_NOTE_DA}",
        "subskills": [
            {
                "id": "tokenization_bpe_sentencepiece",
                "name": "Tokenization Algorithms & Token Economics",
                "description": "Understanding subword tokenization algorithms (Byte-Pair Encoding, WordPiece, SentencePiece, tiktoken), token-to-word ratios across languages, context window consumption, and token cost modeling.",
                "keywords": ["tokenization", "Byte-Pair Encoding (BPE)", "tiktoken", "SentencePiece", "token-to-word ratio", "context limit budget", "cl100k_base", "o200k_base"]
            },
            {
                "id": "llm_inference_sampling_parameters",
                "name": "LLM Sampling Parameters & Generation Control",
                "description": "Controlling LLM output generation using hyperparameters: temperature, top-p (nucleus sampling), top-k, frequency penalty, presence penalty, stop sequences, and logit bias.",
                "keywords": ["temperature", "top_p / nucleus sampling", "top_k", "frequency_penalty", "presence_penalty", "stop sequences", "logit_bias", "deterministic decoding (greedy)"]
            },
            {
                "id": "foundation_models_api_integration",
                "name": "Foundation Model SDKs & Multi-Provider API Integration",
                "description": "Consuming proprietary LLM APIs (OpenAI, Anthropic Claude, Google Gemini) using official SDKs, streaming completions (SSE), rate limiting, exponential backoff, and unified wrappers (LiteLLM).",
                "keywords": ["OpenAI API", "Anthropic Claude SDK", "Google GenerativeAI", "LiteLLM client", "streaming completions (SSE)", "model fallback routing", "exponential backoff", "rate limit handling"]
            },
            {
                "id": "transformer_architecture_attention",
                "name": "Transformer Architecture, Self-Attention & KV Cache",
                "description": "Inner mechanics of decoder-only transformer models: self-attention, multi-head attention (MHA), grouped-query attention (GQA), rotary positional embeddings (RoPE), KV cache memory dynamics, and FLOPs scaling.",
                "keywords": ["self-attention mechanism", "Grouped-Query Attention (GQA)", "Multi-Head Attention (MHA)", "Rotary Position Embedding (RoPE)", "KV cache memory sizing", "decoder-only architecture"]
            },
            {
                "id": "fine_tuning_peft_lora_qlora",
                "name": "Parameter-Efficient Fine-Tuning (PEFT, LoRA & QLoRA)",
                "description": "Supervised fine-tuning (SFT) mathematical theory and mechanics: low-rank adaptation decomposition (ΔW = B·A), rank (r) and alpha (α) scaling, QLoRA 4-bit NormalFloat (NF4), double quantization, and adapter merging.",
                "keywords": ["PEFT", "LoRA (Low-Rank Adaptation)", "QLoRA", "low-rank decomposition (B·A)", "NF4 quantization theory", "lora_rank / lora_alpha", "adapter weights merging", "gradient checkpointing"]
            },
            {
                "id": "structured_outputs_json_schema",
                "name": "Structured Outputs, JSON Schema & Instructor",
                "description": "Enforcing deterministic structured JSON output from LLMs using JSON Schema response formats, Pydantic models, Instructor library, and Outlines constrained grammar decoding.",
                "keywords": ["structured outputs", "response_format json_schema", "Pydantic response validation", "Instructor library", "Outlines grammar constraint", "strict mode schema", "function calling structured output"]
            },
            {
                "id": "context_window_scaling_techniques",
                "name": "Context Window Scaling & Long-Context Dynamics",
                "description": "Long-context LLM mechanics: FlashAttention-2/3, context window extension (YaRN, RoPE interpolation), Needle-In-A-Haystack (NIAH) retrieval degradation, and lost-in-the-middle positioning effects.",
                "keywords": ["FlashAttention-2", "FlashAttention-3", "Needle In A Haystack (NIAH)", "lost-in-the-middle phenomenon", "RoPE scaling / YaRN", "effective context length", "context compression"]
            },
            {
                "id": "model_evaluation_benchmarks_metrics",
                "name": "LLM Evaluation Benchmarks & Quantitative Quality Metrics",
                "description": "Evaluating model capabilities using standardized benchmarks (MMLU, GSM8K, HumanEval, MT-Bench, Chatbot Arena Elo), automated metrics (Perplexity, BLEU, ROUGE, exact match), and LLM-as-a-judge statistical bias mitigation.",
                "keywords": ["MMLU benchmark", "GSM8K math reasoning", "HumanEval code benchmark", "Chatbot Arena Elo rating", "Perplexity (PPL)", "LLM-as-a-judge evaluation", "MT-Bench multi-turn evaluation", "win-rate statistical significance"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "OpenAI, Anthropic, or LiteLLM SDK client usage and streaming completions",
                    "detection": "content_analysis",
                    "pattern": "from (openai|anthropic|litellm) import|OpenAI\\(|Anthropic\\(|completion\\(|ChatOpenAI\\(|stream=True",
                    "strength": 0.8,
                    "maps_to": ["ai_llm_fundamentals.foundation_models_api_integration", "ai_llm_fundamentals.llm_inference_sampling_parameters"]
                },
                {
                    "signal": "Instructor or Pydantic structured output extraction and JSON schema enforcement",
                    "detection": "content_analysis",
                    "pattern": "instructor\\.from_openai|instructor\\.patch|response_format=\\{\"type\": \"json_object\"\\}|response_model=|class .*\\(BaseModel\\):",
                    "strength": 0.85,
                    "maps_to": ["ai_llm_fundamentals.structured_outputs_json_schema"]
                },
                {
                    "signal": "PEFT or LoRA configuration and low-rank adapter training code",
                    "detection": "content_analysis",
                    "pattern": "from peft import LoraConfig|get_peft_model|prepare_model_for_kbit_training|LoraConfig\\(",
                    "strength": 0.9,
                    "maps_to": ["ai_llm_fundamentals.fine_tuning_peft_lora_qlora"]
                },
                {
                    "signal": "Benchmark evaluation scripts and perplexity or accuracy measurement",
                    "detection": "content_analysis",
                    "pattern": "lm_eval|evaluate_perplexity|torch\\.exp\\(loss\\)|mmlu_eval|mt_bench|calculate_win_rate",
                    "strength": 0.85,
                    "maps_to": ["ai_llm_fundamentals.model_evaluation_benchmarks_metrics", "ai_llm_fundamentals.context_window_scaling_techniques"]
                }
            ],
            "cv": [
                {
                    "signal": "Evaluated foundation models using standard benchmarks (MMLU, GSM8K, MT-Bench) and automated LLM-as-a-judge pipelines",
                    "strength": 0.85,
                    "maps_to": ["ai_llm_fundamentals.model_evaluation_benchmarks_metrics", "ai_llm_fundamentals.structured_outputs_json_schema"]
                },
                {
                    "signal": "Implemented mathematical parameter-efficient fine-tuning (LoRA/QLoRA) and long-context FlashAttention scaling",
                    "strength": 0.9,
                    "maps_to": ["ai_llm_fundamentals.fine_tuning_peft_lora_qlora", "ai_llm_fundamentals.transformer_architecture_attention", "ai_llm_fundamentals.context_window_scaling_techniques"]
                },
                {
                    "signal": "Integrated multi-provider LLM pipelines (OpenAI, Anthropic Claude, Gemini) with LiteLLM and token optimization",
                    "strength": 0.8,
                    "maps_to": ["ai_llm_fundamentals.foundation_models_api_integration", "ai_llm_fundamentals.tokenization_bpe_sentencepiece", "ai_llm_fundamentals.llm_inference_sampling_parameters"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Large Language Models (LLM), OpenAI API, or Generative AI endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_llm_fundamentals.foundation_models_api_integration", "ai_llm_fundamentals.tokenization_bpe_sentencepiece"]
                },
                {
                    "signal": "Job experience describing LLM architecture research, transformer optimization, or prompt token economics",
                    "strength": 0.85,
                    "maps_to": ["ai_llm_fundamentals.transformer_architecture_attention", "ai_llm_fundamentals.fine_tuning_peft_lora_qlora", "ai_llm_fundamentals.model_evaluation_benchmarks_metrics"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "tokenization_bpe_sentencepiece",
                    "llm_inference_sampling_parameters",
                    "foundation_models_api_integration"
                ],
                "description": "Understands tokenization economics and sampling hyperparameters, and integrates proprietary LLM APIs via standard SDKs."
            },
            "mid": {
                "expected_subskills": [
                    "transformer_architecture_attention",
                    "fine_tuning_peft_lora_qlora",
                    "structured_outputs_json_schema"
                ],
                "description": "Applies PEFT/LoRA low-rank theory, understands attention mechanics and KV cache dynamics, and enforces strict structured outputs via Pydantic/Instructor."
            },
            "senior": {
                "expected_subskills": [
                    "context_window_scaling_techniques",
                    "model_evaluation_benchmarks_metrics"
                ],
                "description": "Manages long-context FlashAttention scaling, evaluates models against MMLU/MT-Bench benchmarks, and mitigates LLM-as-a-judge evaluation bias."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 2: ai_prompt_engineering
    # ---------------------------------------------------------
    {
        "skill_id": "ai_prompt_engineering",
        "name": "Prompt Engineering & Context Construction",
        "category": "ai_core",
        "description": "Systematic prompt design, in-context learning, reasoning frameworks (CoT, ToT, ReAct), few-shot exemplar curation, dynamic prompt templating, metaprompts, automated prompt optimization (DSPy), and output calibration.",
        "subskills": [
            {
                "id": "zero_shot_few_shot_prompting",
                "name": "Zero-Shot & Few-Shot In-Context Learning",
                "description": "Structuring zero-shot prompts, authoring system instructions, role conditioning, and selecting balanced few-shot exemplars with clear input-output boundaries.",
                "keywords": ["zero-shot prompting", "few-shot in-context learning", "system prompt", "role conditioning", "exemplar selection", "input-output demonstration", "prompt prefixing"]
            },
            {
                "id": "prompt_templating_dynamic_injection",
                "name": "Dynamic Prompt Templating (Jinja2 & LangChain)",
                "description": "Authoring dynamic and reusable prompt templates with variable injection, partial formatting, Jinja2 conditional rendering, and LangChain/LlamaIndex ChatPromptTemplate.",
                "keywords": ["PromptTemplate", "ChatPromptTemplate", "Jinja2 template rendering", "partial variable formatting", "SystemMessage / HumanMessage", "dynamic context insertion"]
            },
            {
                "id": "output_formatting_constraints",
                "name": "Output Formatting & Delimiter Engineering",
                "description": "Enforcing output format adherence (Markdown, XML tags, YAML, JSON) using structural delimiters (```, <instructions>, <context>), avoiding markdown fences leakage, and negative constraints.",
                "keywords": ["XML delimiters (<context>, <query>)", "markdown formatting constraint", "negative constraints", "format adherence", "delimiter isolation", "structural boundaries"]
            },
            {
                "id": "chain_of_thought_reasoning",
                "name": "Chain-of-Thought & Self-Consistency Reasoning",
                "description": "Implementing Chain-of-Thought (CoT) prompting ('Think step-by-step'), Least-to-Most prompting, and Self-Consistency decoding with majority voting across multiple sample paths.",
                "keywords": ["Chain-of-Thought (CoT)", "zero-shot CoT ('Let's think step by step')", "Self-Consistency decoding", "majority voting", "Least-to-Most prompting", "step-by-step reasoning trace"]
            },
            {
                "id": "tree_of_thoughts_advanced_reasoning",
                "name": "Tree of Thoughts (ToT) & Graph Reasoning",
                "description": "Designing multi-path exploration and heuristic search reasoning architectures: Tree of Thoughts (ToT), Graph of Thoughts (GoT), thought generation, evaluation states, and backtracking.",
                "keywords": ["Tree of Thoughts (ToT)", "Graph of Thoughts (GoT)", "thought generator", "state evaluation", "beam search prompting", "backtracking heuristic"]
            },
            {
                "id": "metaprompting_system_architecture",
                "name": "Enterprise Metaprompting & System Prompt Design",
                "description": "Architecting comprehensive enterprise metaprompts, role definitions, tone of voice, tool-use guidance, fallback policies, context budget allocation, and self-correcting prompt instructions.",
                "keywords": ["metaprompting", "system prompt architecture", "enterprise prompt guidelines", "context budget allocation", "self-correcting prompt", "fallback behavior instructions"]
            },
            {
                "id": "automated_prompt_optimization_dspy",
                "name": "Automated Prompt Optimization (DSPy & TextGrad)",
                "description": "Programmatic prompt engineering and automated compiler optimization using DSPy (Signatures, Modules, Teleprompters like BootstrapFewShot, MIPRO) and gradient-like text optimization (TextGrad).",
                "keywords": ["DSPy framework", "dspy.Signature", "dspy.Module", "dspy.BootstrapFewShot", "MIPRO teleprompter", "compiled prompt program", "TextGrad", "automated prompt tuning"]
            },
            {
                "id": "prompt_evaluation_benchmarking",
                "name": "Prompt Evaluation & LLM-as-a-Judge Benchmarking",
                "description": "Evaluating prompt performance using LLM-as-a-Judge methodologies, pairwise comparison, automated prompt regression testing, and evaluation harness tools (Promptfoo, Langfuse).",
                "keywords": ["LLM-as-a-Judge", "Promptfoo", "pairwise evaluation", "prompt regression testing", "Elo rating for prompts", "G-Eval", "prompt versioning"]
            },
            {
                "id": "adversarial_prompt_resilience",
                "name": "Prompt Injection Resilience & Sandwich Defense",
                "description": "Hardening prompts against prompt injection, jailbreaking, and goal hijacking using sandwich defense, XML tag isolation, instruction-data separation, and output canary verification.",
                "keywords": ["sandwich defense", "instruction-data separation", "canary tokens", "prompt injection defense", "system prompt leak prevention", "XML tag wrapping"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "LangChain or custom Jinja2 prompt templates with message structures",
                    "detection": "content_analysis",
                    "pattern": "ChatPromptTemplate\\.from_messages|PromptTemplate\\(template=|SystemMessagePromptTemplate|HumanMessagePromptTemplate",
                    "strength": 0.8,
                    "maps_to": ["ai_prompt_engineering.prompt_templating_dynamic_injection", "ai_prompt_engineering.zero_shot_few_shot_prompting", "ai_prompt_engineering.output_formatting_constraints"]
                },
                {
                    "signal": "DSPy signatures, modules, and teleprompter compilation code",
                    "detection": "content_analysis",
                    "pattern": "import dspy|class .*\\(dspy\\.Signature\\):|dspy\\.Predict\\(|dspy\\.ChainOfThought\\(|BootstrapFewShotWithRandomSearch|dspy\\.MIPRO",
                    "strength": 0.95,
                    "maps_to": ["ai_prompt_engineering.automated_prompt_optimization_dspy"]
                },
                {
                    "signal": "Promptfoo configuration or automated prompt evaluation scripts",
                    "detection": "file_presence",
                    "pattern": "promptfooconfig\\.ya?ml|promptfoo\\.json",
                    "strength": 0.9,
                    "maps_to": ["ai_prompt_engineering.prompt_evaluation_benchmarking"]
                },
                {
                    "signal": "Chain-of-thought, self-consistency, or XML delimited system prompts in code",
                    "detection": "content_analysis",
                    "pattern": "<instructions>|<context>|Let's think step by step|reasoning_steps|self_consistency",
                    "strength": 0.8,
                    "maps_to": ["ai_prompt_engineering.chain_of_thought_reasoning", "ai_prompt_engineering.output_formatting_constraints", "ai_prompt_engineering.adversarial_prompt_resilience"]
                }
            ],
            "cv": [
                {
                    "signal": "Optimized production prompt pipelines using DSPy, MIPRO teleprompters, and Promptfoo regression suites",
                    "strength": 0.9,
                    "maps_to": ["ai_prompt_engineering.automated_prompt_optimization_dspy", "ai_prompt_engineering.prompt_evaluation_benchmarking"]
                },
                {
                    "signal": "Architected complex prompt systems with Chain-of-Thought, Tree of Thoughts, and defensive formatting",
                    "strength": 0.85,
                    "maps_to": ["ai_prompt_engineering.chain_of_thought_reasoning", "ai_prompt_engineering.tree_of_thoughts_advanced_reasoning", "ai_prompt_engineering.metaprompting_system_architecture"]
                },
                {
                    "signal": "Implemented few-shot in-context learning with dynamic exemplar retrieval and injection protection",
                    "strength": 0.8,
                    "maps_to": ["ai_prompt_engineering.zero_shot_few_shot_prompting", "ai_prompt_engineering.prompt_templating_dynamic_injection", "ai_prompt_engineering.adversarial_prompt_resilience"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Prompt Engineering, In-Context Learning, or Prompt Optimization endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_prompt_engineering.zero_shot_few_shot_prompting", "ai_prompt_engineering.prompt_templating_dynamic_injection"]
                },
                {
                    "signal": "Job experience describing DSPy prompt compilation, LLM-as-a-judge benchmarking, or reasoning chains",
                    "strength": 0.85,
                    "maps_to": ["ai_prompt_engineering.automated_prompt_optimization_dspy", "ai_prompt_engineering.prompt_evaluation_benchmarking", "ai_prompt_engineering.chain_of_thought_reasoning"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "zero_shot_few_shot_prompting",
                    "prompt_templating_dynamic_injection",
                    "output_formatting_constraints"
                ],
                "description": "Authors zero/few-shot prompts, designs reusable dynamic prompt templates, and enforces strict delimiter output formatting."
            },
            "mid": {
                "expected_subskills": [
                    "chain_of_thought_reasoning",
                    "tree_of_thoughts_advanced_reasoning",
                    "metaprompting_system_architecture"
                ],
                "description": "Implements Chain-of-Thought and Tree of Thoughts reasoning architectures, and designs production enterprise metaprompts."
            },
            "senior": {
                "expected_subskills": [
                    "automated_prompt_optimization_dspy",
                    "prompt_evaluation_benchmarking",
                    "adversarial_prompt_resilience"
                ],
                "description": "Compiles prompts programmatically with DSPy, establishes LLM-as-a-judge evaluation pipelines, and hardens systems against prompt attacks."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 3: ai_embeddings_vector_db
    # ---------------------------------------------------------
    {
        "skill_id": "ai_embeddings_vector_db",
        "name": "Embeddings, Similarity Search & Vector Databases",
        "category": "ai_core",
        "description": "Dense and sparse vector representations, embedding models (OpenAI, Cohere, BGE, Nomic), distance metrics, approximate nearest neighbor (ANN) indexing (HNSW, IVF), vector databases (Pinecone, ChromaDB, Weaviate, Qdrant, pgvector), hybrid search (BM25 + Dense), and ColBERT late-interaction.",
        "subskills": [
            {
                "id": "dense_embeddings_generation",
                "name": "Dense Embedding Generation & Embedding Models",
                "description": "Generating dense semantic embeddings using OpenAI (text-embedding-3-small/large), Cohere, HuggingFace sentence-transformers (BGE, Nomic), dimension truncation, and batch embedding pipelines.",
                "keywords": ["text-embedding-3", "SentenceTransformer", "BGE embeddings", "Cohere embed-v3", "embedding dimensions", "batch embedding generation", "vector normalization"]
            },
            {
                "id": "distance_metrics_similarity",
                "name": "Vector Distance Metrics & Similarity Calculation",
                "description": "Calculating similarity and distance in high-dimensional vector spaces: Cosine Similarity, Dot Product (Inner Product), Euclidean Distance (L2), and Manhattan distance with normalized vectors.",
                "keywords": ["cosine similarity", "dot product (inner product)", "Euclidean distance (L2)", "Manhattan distance (L1)", "vector magnitude normalization", "high-dimensional geometry"]
            },
            {
                "id": "chromadb_local_vector_storage",
                "name": "Local Vector Storage & Querying (ChromaDB & FAISS)",
                "description": "Setting up local and embedded vector search engines using ChromaDB and FAISS: collection creation, document/metadata indexing, querying by embedding, and persistence management.",
                "keywords": ["ChromaDB client", "chromadb.PersistentClient", "collection.add / collection.query", "FAISS IndexFlatL2 / IndexHNSWFlat", "local vector store", "metadata filtering"]
            },
            {
                "id": "cloud_vector_db_pinecone_weaviate_qdrant",
                "name": "Managed Cloud Vector DBs (Pinecone, Weaviate & Qdrant)",
                "description": "Architecting production vector stores with Pinecone (serverless indexes, namespaces), Weaviate (schema collections, multi-tenancy), Qdrant (payload indexing), and Milvus.",
                "keywords": ["Pinecone client", "pinecone.Index", "namespaces", "Weaviate client", "QdrantClient", "payload indexing", "Milvus", "serverless vector index"]
            },
            {
                "id": "pgvector_relational_integration",
                "name": "Relational Vector Search with PostgreSQL & pgvector",
                "description": "Integrating vector search into PostgreSQL using pgvector extension: VECTOR column types, cosine distance operator (<=>), IVFFlat / HNSW index creation, and hybrid SQL relational filtering.",
                "keywords": ["pgvector", "CREATE EXTENSION vector", "VECTOR(1536)", "cosine distance operator <=>", "HNSW index pgvector", "IVFFlat index", "SQL JOIN with vector search"]
            },
            {
                "id": "ann_indexing_hnsw_ivf",
                "name": "Approximate Nearest Neighbor (ANN) Indexing & HNSW",
                "description": "Tuning Approximate Nearest Neighbor (ANN) algorithms: Hierarchical Navigable Small World (HNSW: M, ef_construction, ef_search), Inverted File Index (IVF: nlist, nprobe), and memory vs latency trade-offs.",
                "keywords": ["HNSW (Hierarchical Navigable Small World)", "M parameter", "efConstruction / efSearch", "Inverted File Index (IVF)", "nlist / nprobe", "ANN recall vs latency trade-off"]
            },
            {
                "id": "hybrid_search_sparse_dense_bm25",
                "name": "Hybrid Search (Dense + Sparse BM25) & Reciprocal Rank Fusion",
                "description": "Implementing hybrid search combining dense semantic vectors with sparse lexical search (BM25, SPLADE) and merging ranked candidate lists using Reciprocal Rank Fusion (RRF) and alpha weighting.",
                "keywords": ["hybrid search", "BM25 keyword search", "SPLADE sparse embeddings", "Reciprocal Rank Fusion (RRF)", "hybrid alpha weighting (dense vs sparse)", "lexical-semantic retrieval"]
            },
            {
                "id": "late_interaction_colbert",
                "name": "Late-Interaction Multi-Vector Search (ColBERT & RAGatouille)",
                "description": "Implementing token-level multi-vector late-interaction retrieval using ColBERTv2 and RAGatouille, token embeddings calculation, MaxSim operator, and dense indexing.",
                "keywords": ["ColBERTv2", "RAGatouille", "late-interaction retrieval", "MaxSim operator", "token-level multi-vector index", "fine-grained semantic matching"]
            },
            {
                "id": "embedding_finetuning_domain_adaptation",
                "name": "Embedding Fine-Tuning & Matryoshka Embeddings (MRL)",
                "description": "Fine-tuning embedding models for domain adaptation using contrastive loss (MultipleNegativesRankingLoss), Triplet Loss, and training Matryoshka Representation Learning (MRL) embeddings.",
                "keywords": ["embedding fine-tuning", "SentenceTransformers training", "MultipleNegativesRankingLoss", "Matryoshka Representation Learning (MRL)", "triplet loss", "contrastive learning"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Pinecone, ChromaDB, Weaviate, or Qdrant vector database initialization and query code",
                    "detection": "content_analysis",
                    "pattern": "pinecone\\.Pinecone|chromadb\\.Client|chromadb\\.PersistentClient|weaviate\\.connect_to|QdrantClient|from langchain_community\\.vectorstores import",
                    "strength": 0.85,
                    "maps_to": ["ai_embeddings_vector_db.cloud_vector_db_pinecone_weaviate_qdrant", "ai_embeddings_vector_db.chromadb_local_vector_storage"]
                },
                {
                    "signal": "OpenAI or SentenceTransformers embedding generation pipeline",
                    "detection": "content_analysis",
                    "pattern": "from sentence_transformers import SentenceTransformer|openai\\.embeddings\\.create|OpenAIEmbeddings\\(|HuggingFaceEmbeddings\\(",
                    "strength": 0.8,
                    "maps_to": ["ai_embeddings_vector_db.dense_embeddings_generation", "ai_embeddings_vector_db.distance_metrics_similarity"]
                },
                {
                    "signal": "pgvector SQL migration scripts or SQLAlchemy vector column definitions",
                    "detection": "content_analysis",
                    "pattern": "CREATE EXTENSION.*vector|from pgvector\\.sqlalchemy import Vector|Column\\(Vector\\(|<=>",
                    "strength": 0.9,
                    "maps_to": ["ai_embeddings_vector_db.pgvector_relational_integration"]
                },
                {
                    "signal": "ColBERT or RAGatouille multi-vector retrieval integration",
                    "detection": "content_analysis",
                    "pattern": "from ragatouille import RAGPretrainedModel|RAGatouille|colbert",
                    "strength": 0.9,
                    "maps_to": ["ai_embeddings_vector_db.late_interaction_colbert"]
                }
            ],
            "cv": [
                {
                    "signal": "Engineered enterprise vector search infrastructure using Pinecone, Qdrant, and pgvector with HNSW indexing",
                    "strength": 0.9,
                    "maps_to": ["ai_embeddings_vector_db.cloud_vector_db_pinecone_weaviate_qdrant", "ai_embeddings_vector_db.pgvector_relational_integration", "ai_embeddings_vector_db.ann_indexing_hnsw_ivf"]
                },
                {
                    "signal": "Implemented hybrid search combining BM25 sparse search with dense embeddings via Reciprocal Rank Fusion (RRF)",
                    "strength": 0.9,
                    "maps_to": ["ai_embeddings_vector_db.hybrid_search_sparse_dense_bm25", "ai_embeddings_vector_db.dense_embeddings_generation"]
                },
                {
                    "signal": "Fine-tuned domain-specific embedding models with Matryoshka Representation Learning (MRL) and ColBERT",
                    "strength": 0.85,
                    "maps_to": ["ai_embeddings_vector_db.embedding_finetuning_domain_adaptation", "ai_embeddings_vector_db.late_interaction_colbert"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Vector Databases, Pinecone, Embeddings, or Semantic Search endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_embeddings_vector_db.cloud_vector_db_pinecone_weaviate_qdrant", "ai_embeddings_vector_db.dense_embeddings_generation"]
                },
                {
                    "signal": "Job experience describing vector index optimization (HNSW), hybrid search, or pgvector integration",
                    "strength": 0.85,
                    "maps_to": ["ai_embeddings_vector_db.ann_indexing_hnsw_ivf", "ai_embeddings_vector_db.hybrid_search_sparse_dense_bm25", "ai_embeddings_vector_db.pgvector_relational_integration"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "dense_embeddings_generation",
                    "distance_metrics_similarity",
                    "chromadb_local_vector_storage"
                ],
                "description": "Generates dense embeddings with OpenAI/SentenceTransformers, calculates vector distances, and manages local ChromaDB/FAISS stores."
            },
            "mid": {
                "expected_subskills": [
                    "cloud_vector_db_pinecone_weaviate_qdrant",
                    "pgvector_relational_integration",
                    "ann_indexing_hnsw_ivf"
                ],
                "description": "Configures managed cloud vector DBs (Pinecone, Qdrant), integrates pgvector into PostgreSQL, and tunes HNSW/IVF indexing parameters."
            },
            "senior": {
                "expected_subskills": [
                    "hybrid_search_sparse_dense_bm25",
                    "late_interaction_colbert",
                    "embedding_finetuning_domain_adaptation"
                ],
                "description": "Implements hybrid BM25+Dense search with RRF, deploys ColBERT late-interaction indexing, and fine-tunes domain-specific Matryoshka embeddings."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 4: ai_rag_implementation
    # ---------------------------------------------------------
    {
        "skill_id": "ai_rag_implementation",
        "name": "Retrieval-Augmented Generation (RAG) Architecture",
        "category": "ai_core",
        "description": f"End-to-end Retrieval-Augmented Generation (RAG) architectures, document parsing/chunking pipelines, semantic chunking, multi-stage retrieval, re-ranking (Cross-Encoders, Cohere Rerank), query transformations (HyDE, Multi-Query), GraphRAG, and RAG evaluation (RAGAS, TruLens). ÖNEMLİ AYRIM: {CRITICAL_NOTE_DA}",
        "subskills": [
            {
                "id": "document_parsing_chunking_strategies",
                "name": "Document Parsing & Fixed-Size Chunking",
                "description": "Ingesting and parsing heterogeneous documents (PDF, Markdown, DOCX, HTML) using Unstructured, PyMuPDF, or LlamaParse, applying fixed-size chunking with sliding window overlap, and enriching metadata.",
                "keywords": ["document parsing", "PyMuPDF / pdfplumber", "LlamaParse", "fixed-size chunking", "chunk_overlap", "metadata extraction", "CharacterTextSplitter"]
            },
            {
                "id": "basic_rag_pipeline_langchain_llamaindex",
                "name": "Baseline RAG Pipelines (LangChain & LlamaIndex)",
                "description": "Building baseline RAG pipelines using LangChain (create_retrieval_chain, LCEL) and LlamaIndex (VectorStoreIndex, QueryEngine, RetrieverQueryEngine) connecting retriever to LLM generator.",
                "keywords": ["LangChain LCEL", "create_retrieval_chain", "LlamaIndex VectorStoreIndex", "QueryEngine", "VectorIndexRetriever", "RetrievalQA", "context prompt pipeline"]
            },
            {
                "id": "context_stuffing_citation_generation",
                "name": "Context Assembly & Citation Footnoting",
                "description": "Assembling retrieved chunks into context windows, generating verified citation footnotes with source document metadata, and handling out-of-domain / ungrounded query fallback responses.",
                "keywords": ["citation generation", "source attribution", "context stuffing", "fallback 'I don't know' response", "grounded answers", "metadata source tracking"]
            },
            {
                "id": "semantic_recursive_chunking",
                "name": "Semantic & Hierarchical Parent-Document Chunking",
                "description": "Implementing advanced chunking techniques: RecursiveCharacterTextSplitter, Semantic Chunking (split by embedding distance threshold), and Hierarchical / ParentDocumentRetriever (small chunk for retrieval, large chunk for generation).",
                "keywords": ["RecursiveCharacterTextSplitter", "SemanticChunker", "ParentDocumentRetriever", "hierarchical chunking", "summary index retrieval", "sentence boundary splitting"]
            },
            {
                "id": "query_transformation_hyde_multiquery",
                "name": "Query Transformation (HyDE, Multi-Query & Step-Back)",
                "description": "Formulating query transformations: Hypothetical Document Embeddings (HyDE), Multi-Query expansion with LLMs, Step-Back prompting, and sub-question decomposition.",
                "keywords": ["Hypothetical Document Embeddings (HyDE)", "MultiQueryRetriever", "Step-Back prompting", "sub-question query engine", "query rewriting", "query expansion"]
            },
            {
                "id": "reranking_cross_encoders",
                "name": "Multi-Stage Retrieval & Cross-Encoder Re-ranking",
                "description": "Implementing two-stage retrieval architectures: initial high-recall vector search followed by Cross-Encoder re-ranking (Cohere Rerank, BGE-Reranker, FlashRank) to filter irrelevant chunks.",
                "keywords": ["cross-encoder reranker", "Cohere Rerank API", "BGE-Reranker", "FlashRank", "two-stage retrieval", "re-ranking top-k precision", "ContextualCompressionRetriever"]
            },
            {
                "id": "graph_rag_knowledge_graphs",
                "name": "GraphRAG & Knowledge Graph Augmented Retrieval",
                "description": "Constructing GraphRAG architectures: automated entity/relationship extraction from text with LLMs, Neo4j / NetworkX graph storage, community detection, and multi-hop graph traversal retrieval.",
                "keywords": ["GraphRAG", "Knowledge Graph RAG", "Neo4j Cypher query", "entity-relation extraction", "community summarization", "multi-hop graph reasoning", "NetworkX"]
            },
            {
                "id": "agentic_corrective_rag_crag_self_rag",
                "name": "Agentic, Corrective (CRAG) & Self-RAG Architectures",
                "description": "Architecting dynamic RAG loops with agentic decision-making: Corrective RAG (CRAG) with confidence thresholding, Self-RAG (self-reflection on relevance/groundedness), and web search fallback (Tavily/SerpAPI).",
                "keywords": ["Corrective RAG (CRAG)", "Self-RAG", "reflection tokens", "Adaptive RAG routing", "Tavily web search fallback", "agentic retrieval loop", "retrieval self-correction"]
            },
            {
                "id": "rag_evaluation_ragas_trulens",
                "name": "RAG Evaluation Frameworks (RAGAS & TruLens)",
                "description": "Evaluating RAG pipelines quantitatively using RAGAS and TruLens: Faithfulness, Answer Relevance, Context Precision, Context Recall, Context Entities Score, and synthetic test set generation.",
                "keywords": ["RAGAS framework", "TruLens RAG Triad", "faithfulness metric", "answer_relevancy", "context_precision", "context_recall", "synthetic test generation (TestsetGenerator)"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "LangChain or LlamaIndex RAG retrieval pipeline and chain composition",
                    "detection": "content_analysis",
                    "pattern": "create_retrieval_chain|RetrievalQA\\.from_chain_type|VectorStoreIndex\\.from_documents|as_query_engine\\(|ContextualCompressionRetriever",
                    "strength": 0.85,
                    "maps_to": ["ai_rag_implementation.basic_rag_pipeline_langchain_llamaindex", "ai_rag_implementation.document_parsing_chunking_strategies", "ai_rag_implementation.context_stuffing_citation_generation"]
                },
                {
                    "signal": "Cohere reranking, cross-encoder, or ParentDocumentRetriever implementation",
                    "detection": "content_analysis",
                    "pattern": "CohereRerank|from sentence_transformers import CrossEncoder|ParentDocumentRetriever|SemanticChunker|RecursiveCharacterTextSplitter",
                    "strength": 0.9,
                    "maps_to": ["ai_rag_implementation.reranking_cross_encoders", "ai_rag_implementation.semantic_recursive_chunking"]
                },
                {
                    "signal": "RAGAS or TruLens RAG evaluation evaluation scripts",
                    "detection": "content_analysis",
                    "pattern": "from ragas import evaluate|from ragas\\.metrics import faithfulness|from trulens_eval import TruChain|TestsetGenerator",
                    "strength": 0.95,
                    "maps_to": ["ai_rag_implementation.rag_evaluation_ragas_trulens"]
                },
                {
                    "signal": "GraphRAG or Corrective RAG (CRAG) pipeline implementation",
                    "detection": "content_analysis",
                    "pattern": "from langchain_community\\.graphs import Neo4jGraph|GraphRAG|crag|self_rag",
                    "strength": 0.9,
                    "maps_to": ["ai_rag_implementation.graph_rag_knowledge_graphs", "ai_rag_implementation.agentic_corrective_rag_crag_self_rag"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected enterprise RAG systems with hybrid search, Cohere re-ranking, and Parent-Document retrieval",
                    "strength": 0.9,
                    "maps_to": ["ai_rag_implementation.basic_rag_pipeline_langchain_llamaindex", "ai_rag_implementation.semantic_recursive_chunking", "ai_rag_implementation.reranking_cross_encoders"]
                },
                {
                    "signal": "Built Corrective RAG (CRAG) and GraphRAG knowledge graphs with automated RAGAS evaluation pipelines",
                    "strength": 0.9,
                    "maps_to": ["ai_rag_implementation.agentic_corrective_rag_crag_self_rag", "ai_rag_implementation.graph_rag_knowledge_graphs", "ai_rag_implementation.rag_evaluation_ragas_trulens"]
                },
                {
                    "signal": "Implemented query expansion with HyDE, Multi-Query, and dynamic source citation attribution",
                    "strength": 0.85,
                    "maps_to": ["ai_rag_implementation.query_transformation_hyde_multiquery", "ai_rag_implementation.context_stuffing_citation_generation", "ai_rag_implementation.document_parsing_chunking_strategies"]
                }
            ],
            "linkedin": [
                {
                    "signal": "RAG (Retrieval-Augmented Generation), LangChain, or LlamaIndex endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_rag_implementation.basic_rag_pipeline_langchain_llamaindex", "ai_rag_implementation.document_parsing_chunking_strategies"]
                },
                {
                    "signal": "Job experience describing RAGAS evaluation, GraphRAG, re-ranking pipelines, or semantic chunking",
                    "strength": 0.85,
                    "maps_to": ["ai_rag_implementation.rag_evaluation_ragas_trulens", "ai_rag_implementation.graph_rag_knowledge_graphs", "ai_rag_implementation.reranking_cross_encoders"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "document_parsing_chunking_strategies",
                    "basic_rag_pipeline_langchain_llamaindex",
                    "context_stuffing_citation_generation"
                ],
                "description": "Parses documents with fixed-size chunks, builds baseline RAG pipelines in LangChain/LlamaIndex, and injects verified citations."
            },
            "mid": {
                "expected_subskills": [
                    "semantic_recursive_chunking",
                    "query_transformation_hyde_multiquery",
                    "reranking_cross_encoders"
                ],
                "description": "Implements semantic and parent-document chunking, applies HyDE query rewriting, and integrates Cross-Encoder/Cohere re-ranking."
            },
            "senior": {
                "expected_subskills": [
                    "graph_rag_knowledge_graphs",
                    "agentic_corrective_rag_crag_self_rag",
                    "rag_evaluation_ragas_trulens"
                ],
                "description": "Architects GraphRAG knowledge graphs, implements self-correcting agentic RAG (CRAG), and benchmarks faithfulness via RAGAS/TruLens."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 5: ai_agents_orchestration
    # ---------------------------------------------------------
    {
        "skill_id": "ai_agents_orchestration",
        "name": "AI Agents, Multi-Agent Systems & Tool Orchestration",
        "category": "ai_core",
        "description": "Autonomous LLM agents, cognitive architectures, function calling and tool use, ReAct execution loops, memory systems (short-term, long-term, semantic, episodic), multi-agent frameworks (LangGraph, CrewAI, AutoGen), human-in-the-loop (HITL), and task planning.",
        "subskills": [
            {
                "id": "function_calling_tool_definitions",
                "name": "Function Calling & Tool Schema Definitions",
                "description": "Defining tools and JSON schemas for LLM function calling (OpenAI tools parameter, Pydantic tool definitions, LangChain @tool decorator), parameter validation, and local execution.",
                "keywords": ["function calling", "@tool decorator", "OpenAI tools parameter", "tool JSON schema", "Pydantic tool args schema", "tool execution handler"]
            },
            {
                "id": "react_agent_loop_execution",
                "name": "ReAct Agent Loop & Thought-Action-Observation",
                "description": "Implementing and debugging the ReAct (Reasoning + Acting) loop: Thought -> Action -> Action Input -> Observation -> Final Answer cycle, handling parsing errors and infinite loops.",
                "keywords": ["ReAct framework", "Thought-Action-Observation cycle", "Action Input parsing", "AgentExecutor", "max_iterations limit", "infinite loop mitigation"]
            },
            {
                "id": "conversational_memory_management",
                "name": "Agent Conversational & Working Memory",
                "description": "Managing agent short-term and working memory: ConversationBufferMemory, ConversationSummaryMemory, sliding window token limiters, and structured scratchpad state.",
                "keywords": ["ConversationBufferMemory", "ConversationSummaryBufferMemory", "sliding window memory", "agent scratchpad", "working memory", "message history trimming"]
            },
            {
                "id": "stateful_agent_graphs_langgraph",
                "name": "Stateful Agent Graphs with LangGraph",
                "description": "Building cyclical, stateful agent graphs using LangGraph: StateGraph, TypedDict state schema, Nodes, conditional Edges, state persistence (MemorySaver, SqliteSaver checkpointer), and time travel.",
                "keywords": ["LangGraph", "StateGraph", "TypedDict state", "conditional edges", "END node", "MemorySaver checkpointer", "time travel debugging", "cyclical agent flow"]
            },
            {
                "id": "crewai_role_based_collaboration",
                "name": "Role-Based Multi-Agent Collaboration (CrewAI)",
                "description": "Orchestrating multi-agent systems with CrewAI: Agent definitions (role, goal, backstory, verbose), Task assignments, Processes (Sequential, Hierarchical with Manager LLM), and inter-agent delegation.",
                "keywords": ["CrewAI", "Agent(role, goal, backstory)", "Task(description, expected_output)", "Crew(process=Process.hierarchical)", "manager_llm", "inter-agent delegation"]
            },
            {
                "id": "autogen_conversable_agents",
                "name": "Conversable Multi-Agent Systems (AutoGen & AG2)",
                "description": "Developing conversable multi-agent architectures using Microsoft AutoGen / AG2: AssistantAgent, UserProxyAgent, GroupChatManager, sandboxed Docker code execution, and termination conditions.",
                "keywords": ["Microsoft AutoGen / AG2", "AssistantAgent", "UserProxyAgent", "GroupChat / GroupChatManager", "code_execution_config (Docker)", "is_termination_msg"]
            },
            {
                "id": "hierarchical_planning_decomposition",
                "name": "Hierarchical Task Planning & Subgoal Decomposition",
                "description": "Implementing hierarchical planning and goal decomposition: Plan-and-Solve prompting, dynamic DAG task generation, dependency resolution, failure recovery, and replanning.",
                "keywords": ["Plan-and-Solve prompting", "DAG task planner", "subgoal decomposition", "agent replanning on error", "dynamic step execution", "hierarchical planning"]
            },
            {
                "id": "human_in_the_loop_hitl_workflows",
                "name": "Human-In-The-Loop (HITL) Workflows & Approval Gates",
                "description": "Designing enterprise Human-in-the-Loop (HITL) safety workflows: interrupt patterns before high-stakes tool execution (e.g. database mutations, payment triggers), resume tokens, and state inspection.",
                "keywords": ["Human-in-the-Loop (HITL)", "interrupt_before / interrupt_after", "approval checkpoint", "high-stakes tool gate", "state resumption", "human review workflow"]
            },
            {
                "id": "episodic_semantic_long_term_memory",
                "name": "Long-Term Episodic & Semantic Memory (MemGPT / Letta)",
                "description": "Implementing long-term agent memory architectures: MemGPT / Letta tiered memory (core memory, recall memory, archival memory), episodic experience retrieval, and self-editing user profiles.",
                "keywords": ["MemGPT / Letta", "core memory (persona, human)", "archival memory (vector)", "recall memory (conversation)", "episodic memory reflection", "self-updating memory"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "LangGraph StateGraph, Nodes, checkpointer, and conditional edge definitions",
                    "detection": "content_analysis",
                    "pattern": "from langgraph\\.graph import StateGraph, END|workflow\\.add_node|workflow\\.add_conditional_edges|MemorySaver\\(\\)|SqliteSaver",
                    "strength": 0.9,
                    "maps_to": ["ai_agents_orchestration.stateful_agent_graphs_langgraph", "ai_agents_orchestration.human_in_the_loop_hitl_workflows"]
                },
                {
                    "signal": "CrewAI multi-agent crew, tasks, and agent definitions",
                    "detection": "content_analysis",
                    "pattern": "from crewai import Agent, Task, Crew, Process|backstory=|expected_output=|Crew\\(agents=",
                    "strength": 0.9,
                    "maps_to": ["ai_agents_orchestration.crewai_role_based_collaboration"]
                },
                {
                    "signal": "AutoGen / AG2 ConversableAgent, GroupChat, or AssistantAgent code",
                    "detection": "content_analysis",
                    "pattern": "import autogen|AssistantAgent|UserProxyAgent|GroupChatManager|register_function",
                    "strength": 0.9,
                    "maps_to": ["ai_agents_orchestration.autogen_conversable_agents"]
                },
                {
                    "signal": "OpenAI function calling tool definitions with @tool decorator or Pydantic schemas",
                    "detection": "content_analysis",
                    "pattern": "@tool|from langchain_core\\.tools import tool|tools=\\[.*\\], tool_choice=|AgentExecutor",
                    "strength": 0.8,
                    "maps_to": ["ai_agents_orchestration.function_calling_tool_definitions", "ai_agents_orchestration.react_agent_loop_execution", "ai_agents_orchestration.conversational_memory_management"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected multi-agent autonomous workflows using LangGraph state graphs with human-in-the-loop approval gates",
                    "strength": 0.9,
                    "maps_to": ["ai_agents_orchestration.stateful_agent_graphs_langgraph", "ai_agents_orchestration.human_in_the_loop_hitl_workflows", "ai_agents_orchestration.hierarchical_planning_decomposition"]
                },
                {
                    "signal": "Built collaborative agent teams with CrewAI and AutoGen for automated research and code generation",
                    "strength": 0.9,
                    "maps_to": ["ai_agents_orchestration.crewai_role_based_collaboration", "ai_agents_orchestration.autogen_conversable_agents"]
                },
                {
                    "signal": "Integrated MemGPT long-term tiered memory and custom function calling tools for enterprise LLM agents",
                    "strength": 0.85,
                    "maps_to": ["ai_agents_orchestration.episodic_semantic_long_term_memory", "ai_agents_orchestration.function_calling_tool_definitions", "ai_agents_orchestration.react_agent_loop_execution"]
                }
            ],
            "linkedin": [
                {
                    "signal": "AI Agents, Multi-Agent Systems, LangGraph, or AutoGen endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_agents_orchestration.stateful_agent_graphs_langgraph", "ai_agents_orchestration.function_calling_tool_definitions"]
                },
                {
                    "signal": "Job experience describing CrewAI orchestration, LangGraph checkpointers, or autonomous agent loops",
                    "strength": 0.85,
                    "maps_to": ["ai_agents_orchestration.crewai_role_based_collaboration", "ai_agents_orchestration.stateful_agent_graphs_langgraph", "ai_agents_orchestration.hierarchical_planning_decomposition"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "function_calling_tool_definitions",
                    "react_agent_loop_execution",
                    "conversational_memory_management"
                ],
                "description": "Defines tool schemas for function calling, implements ReAct execution loops, and manages short-term buffer memory."
            },
            "mid": {
                "expected_subskills": [
                    "stateful_agent_graphs_langgraph",
                    "crewai_role_based_collaboration",
                    "autogen_conversable_agents"
                ],
                "description": "Constructs cyclical state graphs in LangGraph, orchestrates multi-agent teams with CrewAI, and sets up AutoGen group chats."
            },
            "senior": {
                "expected_subskills": [
                    "hierarchical_planning_decomposition",
                    "human_in_the_loop_hitl_workflows",
                    "episodic_semantic_long_term_memory"
                ],
                "description": "Designs hierarchical DAG task planners, implements enterprise HITL approval checkpoints, and manages MemGPT long-term memory."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 6: ai_multimodal_applications
    # ---------------------------------------------------------
    {
        "skill_id": "ai_multimodal_applications",
        "name": "Multimodal AI & Vision-Language Applications",
        "category": "ai_core",
        "description": "Multimodal LLMs (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro), vision-language processing, document OCR / visual understanding, audio/speech AI (Whisper, TTS, realtime voice APIs), image generation (Stable Diffusion, FLUX, DALL-E 3), video understanding, multimodal embeddings (CLIP), and ColPali visual RAG.",
        "subskills": [
            {
                "id": "vision_llm_api_image_analysis",
                "name": "Vision LLMs & Visual Question Answering",
                "description": "Ingesting and analyzing images with Vision-Language Models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, LLaVA) using Base64 encoding, high-detail image tiling, and visual reasoning.",
                "keywords": ["GPT-4o vision", "Claude 3.5 Sonnet vision", "base64 image payload", "image_url type", "detail: high/low", "Visual Question Answering (VQA)", "LLaVA"]
            },
            {
                "id": "speech_to_text_whisper_integration",
                "name": "Speech-to-Text Transcription (Whisper & Faster-Whisper)",
                "description": "Transcribing audio streams and files using OpenAI Whisper and faster-whisper (CTranslate2): word-level timestamps, language detection, VAD chunking, and handling background noise.",
                "keywords": ["OpenAI Whisper API", "faster-whisper", "CTranslate2", "word-level timestamps", "voice activity detection (VAD)", "audio chunking (pydub)", "transcribe audio"]
            },
            {
                "id": "text_to_speech_voice_synthesis",
                "name": "Text-to-Speech & Voice Synthesis (ElevenLabs & OpenAI TTS)",
                "description": "Synthesizing natural voice from text using ElevenLabs API and OpenAI TTS: voice cloning parameters, stability/clarity tuning, SSML formatting, and audio chunk streaming.",
                "keywords": ["ElevenLabs API", "OpenAI TTS (tts-1-hd)", "voice synthesis", "streaming audio chunks", "voice cloning", "stability / similarity_boost", "latency optimization"]
            },
            {
                "id": "visual_document_understanding_ocr",
                "name": "Visual Document Parsing & Table Extraction",
                "description": "Extracting structured data, tables, and key-value fields from complex scanned PDF documents, invoices, and receipts using vision LLMs, bounding box coordinates, and visual layout understanding.",
                "keywords": ["visual document parsing", "table extraction from image", "invoice parsing VLM", "bounding box coordinates [ymin, xmin, ymax, xmax]", "receipt OCR with LLM", "visual layout analysis"]
            },
            {
                "id": "multimodal_embeddings_clip",
                "name": "Cross-Modal Embeddings & Joint Search (CLIP & SigLIP)",
                "description": "Computing joint text-image embeddings using CLIP (OpenAI / OpenCLIP) and SigLIP: calculating cross-modal cosine similarity, zero-shot image classification, and text-to-image semantic search.",
                "keywords": ["CLIP (Contrastive Language-Image Pretraining)", "SigLIP", "OpenCLIP", "text-image similarity", "cross-modal embeddings", "zero-shot image classification"]
            },
            {
                "id": "image_generation_sd_flux_dalle",
                "name": "Programmatic Image Generation (FLUX, Stable Diffusion & DALL-E)",
                "description": "Generating and editing images programmatically using DALL-E 3 API, HuggingFace Diffusers library (FLUX.1, Stable Diffusion XL), ControlNet conditioning, and inpainting masks.",
                "keywords": ["DALL-E 3 API", "HuggingFace Diffusers", "Stable Diffusion XL (SDXL)", "FLUX.1 pipeline", "ControlNet conditioning", "inpainting / outpainting mask", "prompt weighting"]
            },
            {
                "id": "realtime_multimodal_voice_websocket",
                "name": "Realtime Bidirectional Voice Streaming (WebSockets & WebRTC)",
                "description": "Architecting low-latency, bidirectional audio streaming voice agents using OpenAI Realtime API (WebSockets), WebRTC, client-side Voice Activity Detection (VAD), and turn-taking interrupt handling.",
                "keywords": ["OpenAI Realtime API", "WebSocket audio streaming", "WebRTC audio channel", "server-side VAD (voice activity detection)", "low-latency audio response", "turn-taking interruption"]
            },
            {
                "id": "video_understanding_temporal_reasoning",
                "name": "Video Understanding & Temporal Event Reasoning",
                "description": "Processing video inputs for LLMs: frame extraction algorithms (uniform sampling, scene-change detection), Gemini 1.5 Pro native video ingestion, audio transcript synchronization, and temporal event detection.",
                "keywords": ["video understanding", "Gemini 1.5 Pro video upload", "frame sampling (cv2.VideoCapture)", "scene change detection", "temporal event timestamping", "audio-video multimodal fusion"]
            },
            {
                "id": "multimodal_rag_colpali_visual_retrieval",
                "name": "Visual Document RAG & ColPali Multi-Vector Indexing",
                "description": "Implementing end-to-end OCR-free Multimodal RAG with ColPali (PaliGemma-based late interaction): embedding high-resolution page screenshot patches directly into multi-vector indexes for visual layout retrieval.",
                "keywords": ["ColPali", "PaliGemma VLM", "visual document RAG", "OCR-free retrieval", "page screenshot patch embedding", "multi-vector visual retrieval", "byaldi library"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Vision LLM API call with image payload (GPT-4o, Claude, or Gemini)",
                    "detection": "content_analysis",
                    "pattern": "\"type\": \"image_url\"|base64\\.b64encode|image/jpeg;base64|genai\\.upload_file|from diffusers import",
                    "strength": 0.85,
                    "maps_to": ["ai_multimodal_applications.vision_llm_api_image_analysis", "ai_multimodal_applications.visual_document_understanding_ocr", "ai_multimodal_applications.image_generation_sd_flux_dalle"]
                },
                {
                    "signal": "Whisper audio transcription or ElevenLabs TTS synthesis code",
                    "detection": "content_analysis",
                    "pattern": "from faster_whisper import WhisperModel|openai\\.audio\\.transcriptions\\.create|from elevenlabs import|elevenlabs\\.generate",
                    "strength": 0.85,
                    "maps_to": ["ai_multimodal_applications.speech_to_text_whisper_integration", "ai_multimodal_applications.text_to_speech_voice_synthesis"]
                },
                {
                    "signal": "CLIP / OpenCLIP cross-modal embedding model loading and inference",
                    "detection": "content_analysis",
                    "pattern": "import open_clip|clip\\.load\\(|from transformers import CLIPProcessor, CLIPModel",
                    "strength": 0.9,
                    "maps_to": ["ai_multimodal_applications.multimodal_embeddings_clip"]
                },
                {
                    "signal": "ColPali visual RAG or OpenAI Realtime API WebSocket client implementation",
                    "detection": "content_analysis",
                    "pattern": "from colpali_engine import|from byaldi import RAGMultiModalModel|wss://api\\.openai\\.com/v1/realtime|session\\.update.*voice",
                    "strength": 0.95,
                    "maps_to": ["ai_multimodal_applications.multimodal_rag_colpali_visual_retrieval", "ai_multimodal_applications.realtime_multimodal_voice_websocket", "ai_multimodal_applications.video_understanding_temporal_reasoning"]
                }
            ],
            "cv": [
                {
                    "signal": "Built multimodal applications integrating GPT-4o vision, Whisper STT, and ElevenLabs voice streaming",
                    "strength": 0.85,
                    "maps_to": ["ai_multimodal_applications.vision_llm_api_image_analysis", "ai_multimodal_applications.speech_to_text_whisper_integration", "ai_multimodal_applications.text_to_speech_voice_synthesis"]
                },
                {
                    "signal": "Architected real-time WebSocket voice agents with OpenAI Realtime API and WebRTC low-latency streaming",
                    "strength": 0.9,
                    "maps_to": ["ai_multimodal_applications.realtime_multimodal_voice_websocket", "ai_multimodal_applications.video_understanding_temporal_reasoning"]
                },
                {
                    "signal": "Implemented OCR-free visual document RAG using ColPali and cross-modal search with CLIP embeddings",
                    "strength": 0.9,
                    "maps_to": ["ai_multimodal_applications.multimodal_rag_colpali_visual_retrieval", "ai_multimodal_applications.multimodal_embeddings_clip", "ai_multimodal_applications.visual_document_understanding_ocr"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Multimodal AI, Computer Vision, Speech AI, or Whisper endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_multimodal_applications.vision_llm_api_image_analysis", "ai_multimodal_applications.speech_to_text_whisper_integration"]
                },
                {
                    "signal": "Job experience describing ColPali visual retrieval, Realtime Voice APIs, or CLIP embedding search",
                    "strength": 0.85,
                    "maps_to": ["ai_multimodal_applications.multimodal_rag_colpali_visual_retrieval", "ai_multimodal_applications.realtime_multimodal_voice_websocket", "ai_multimodal_applications.multimodal_embeddings_clip"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "vision_llm_api_image_analysis",
                    "speech_to_text_whisper_integration",
                    "text_to_speech_voice_synthesis"
                ],
                "description": "Integrates vision LLM APIs with image payloads, transcribes audio with Whisper, and synthesizes speech with ElevenLabs/TTS."
            },
            "mid": {
                "expected_subskills": [
                    "visual_document_understanding_ocr",
                    "multimodal_embeddings_clip",
                    "image_generation_sd_flux_dalle"
                ],
                "description": "Extracts structured tables from scanned documents, generates CLIP cross-modal embeddings, and controls image generation pipelines."
            },
            "senior": {
                "expected_subskills": [
                    "realtime_multimodal_voice_websocket",
                    "video_understanding_temporal_reasoning",
                    "multimodal_rag_colpali_visual_retrieval"
                ],
                "description": "Architects real-time bidirectional WebSocket voice agents, ingests video streams, and deploys OCR-free ColPali visual RAG."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 7: ai_safety_ethics_deployment
    # ---------------------------------------------------------
    {
        "skill_id": "ai_safety_ethics_deployment",
        "name": "AI Safety, Guardrails, Ethics & Production Deployment",
        "category": "ai_core",
        "description": f"LLM security, prompt injection defense, red teaming, hallucination detection, guardrails frameworks (Guardrails AI, NeMo Guardrails, Llama Guard), bias and fairness evaluation, AI ethics & GDPR/EU AI Act compliance, observability and tracing (Langfuse, LangSmith), and production AI gateways (LiteLLM). ÖNEMLİ AYRIM: {CRITICAL_NOTE_SEC}",
        "subskills": [
            {
                "id": "prompt_injection_jailbreak_defense",
                "name": "Prompt Injection & Jailbreak Attack Defense",
                "description": "Identifying and defending against direct prompt injections, indirect prompt injections from untrusted external sources (web/RAG), system prompt leaking, and multi-turn jailbreak attempts.",
                "keywords": ["prompt injection (direct & indirect)", "jailbreak defense", "system prompt extraction mitigation", "OWASP Top 10 for LLM - LLM01", "untrusted input sanitization"]
            },
            {
                "id": "llm_observability_tracing_langfuse",
                "name": "LLM Observability, Tracing & Cost Accounting (Langfuse & LangSmith)",
                "description": "Implementing production observability for LLM applications: trace trees, nested span tracking, token usage breakdown, latency monitoring, cost calculation, and logging via Langfuse or LangSmith.",
                "keywords": ["Langfuse client", "LangSmith tracing", "OpenInference OpenTelemetry", "token usage analytics", "cost per trace accounting", "latency monitoring spans"]
            },
            {
                "id": "pii_masking_anonymization_presidio",
                "name": "PII Detection, Anonymization & Data Privacy",
                "description": "Detecting, masking, and anonymizing Personally Identifiable Information (PII: emails, SSNs, credit cards, names) in prompts and completions using Microsoft Presidio and reversible tokenizers before API calls.",
                "keywords": ["Microsoft Presidio Analyzer", "Presidio Anonymizer", "PII masking", "anonymization / pseudonymization", "GDPR data compliance", "sensitive entity redaction"]
            },
            {
                "id": "guardrails_nemo_guardrails_ai",
                "name": "Deterministic Guardrails (NeMo Guardrails & Guardrails AI)",
                "description": "Implementing deterministic runtime guardrails on LLM inputs and outputs using NeMo Guardrails (Colang dialog flows, safety rails), Guardrails AI (validators for SQL, toxicity, valid JSON), and Llama Guard.",
                "keywords": ["NeMo Guardrails", "Colang rails syntax", "Guardrails AI", "Guard.use_many", "Llama Guard safety classifier", "input moderation rail", "output hallucination rail"]
            },
            {
                "id": "hallucination_detection_metrics",
                "name": "Hallucination Detection, G-Eval & DeepEval",
                "description": "Detecting and quantifying model hallucinations: SelfCheckGPT (sampling consistency without ground truth), DeepEval hallucination metric, G-Eval framework, and citation factual consistency checking.",
                "keywords": ["hallucination detection", "SelfCheckGPT", "DeepEval framework", "G-Eval metric", "factual consistency score", "groundedness verification"]
            },
            {
                "id": "llm_security_red_teaming_garak",
                "name": "Automated LLM Red Teaming & Vulnerability Scanning (Garak & PyRIT)",
                "description": "Running automated red teaming assessments and vulnerability scans on LLM pipelines using Garak (LLM vulnerability scanner), Microsoft PyRIT, and auditing against OWASP Top 10 for LLM Applications.",
                "keywords": ["Garak LLM scanner", "Microsoft PyRIT", "automated red teaming", "OWASP Top 10 for LLMs", "vulnerability probing", "adversarial safety benchmarking"]
            },
            {
                "id": "model_alignment_rlhf_dpo_ethics",
                "name": "AI Alignment (RLHF, DPO) & Bias/Fairness Metrics",
                "description": "Understanding and applying AI alignment methods: Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimization (DPO), Constitutional AI, and measuring demographic bias and fairness.",
                "keywords": ["AI alignment theory", "Direct Preference Optimization (DPO)", "RLHF reward modeling", "Constitutional AI", "demographic parity / fairness metrics", "bias mitigation", "KTO alignment"]
            },
            {
                "id": "eu_ai_act_compliance_governance",
                "name": "Enterprise AI Governance & EU AI Act Compliance",
                "description": "Ensuring regulatory compliance for AI systems: EU AI Act risk categorization (unacceptable, high, limited, minimal risk), model documentation cards, transparency disclosures, and audit trail logging.",
                "keywords": ["EU AI Act compliance", "risk tier classification (High-Risk AI)", "Model Cards for Model Reporting", "transparency obligations", "AI watermarking / C2PA", "audit trail logging"]
            },
            {
                "id": "production_gateway_rate_limiting_litellm",
                "name": "Production AI Gateways, Rate Limiting & Semantic Caching",
                "description": "Deploying scalable enterprise AI gateways: LiteLLM Proxy / Portkey for virtual key management, provider failover routing, token rate-limiting, and Redis-backed semantic caching (GPTCache).",
                "keywords": ["LiteLLM Proxy", "Portkey AI Gateway", "virtual key budget limits", "semantic cache (GPTCache / Redis)", "provider fallback routing", "token rate limiting (TPM / RPM)"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Langfuse or LangSmith observability client and tracing integration",
                    "detection": "content_analysis",
                    "pattern": "from langfuse import Langfuse|from langfuse\\.callback import CallbackHandler|os\\.environ\\[\"LANGCHAIN_TRACING_V2\"\\]|openinference",
                    "strength": 0.85,
                    "maps_to": ["ai_safety_ethics_deployment.llm_observability_tracing_langfuse"]
                },
                {
                    "signal": "Microsoft Presidio PII analyzer or anonymizer implementation",
                    "detection": "content_analysis",
                    "pattern": "from presidio_analyzer import AnalyzerEngine|from presidio_anonymizer import AnonymizerEngine|AnalyzerEngine\\(\\)",
                    "strength": 0.9,
                    "maps_to": ["ai_safety_ethics_deployment.pii_masking_anonymization_presidio"]
                },
                {
                    "signal": "Guardrails AI or NeMo Guardrails configuration and validator usage",
                    "detection": "content_analysis",
                    "pattern": "from guardrails import Guard|from nemoguardrails import RailsConfig, LLMRails|Guard\\.from_rail|guardrails_config",
                    "strength": 0.9,
                    "maps_to": ["ai_safety_ethics_deployment.guardrails_nemo_guardrails_ai", "ai_safety_ethics_deployment.prompt_injection_jailbreak_defense"]
                },
                {
                    "signal": "DeepEval or Garak red teaming and evaluation script",
                    "detection": "content_analysis",
                    "pattern": "from deepeval import evaluate|from deepeval\\.metrics import HallucinationMetric|import garak|garak\\.probes",
                    "strength": 0.9,
                    "maps_to": ["ai_safety_ethics_deployment.hallucination_detection_metrics", "ai_safety_ethics_deployment.llm_security_red_teaming_garak"]
                },
                {
                    "signal": "LiteLLM Proxy or GPTCache semantic cache configuration",
                    "detection": "content_analysis",
                    "pattern": "litellm_settings|from gptcache import Cache|portkey|proxy_server",
                    "strength": 0.85,
                    "maps_to": ["ai_safety_ethics_deployment.production_gateway_rate_limiting_litellm"]
                }
            ],
            "cv": [
                {
                    "signal": "Implemented production LLM guardrails using NeMo Guardrails and Guardrails AI with PII anonymization via Presidio",
                    "strength": 0.9,
                    "maps_to": ["ai_safety_ethics_deployment.guardrails_nemo_guardrails_ai", "ai_safety_ethics_deployment.pii_masking_anonymization_presidio", "ai_safety_ethics_deployment.prompt_injection_jailbreak_defense"]
                },
                {
                    "signal": "Established enterprise LLM observability with Langfuse and automated red-teaming security scans with Garak/DeepEval",
                    "strength": 0.9,
                    "maps_to": ["ai_safety_ethics_deployment.llm_observability_tracing_langfuse", "ai_safety_ethics_deployment.llm_security_red_teaming_garak", "ai_safety_ethics_deployment.hallucination_detection_metrics"]
                },
                {
                    "signal": "Managed EU AI Act compliance, DPO alignment, and deployed LiteLLM proxy gateways with semantic caching",
                    "strength": 0.85,
                    "maps_to": ["ai_safety_ethics_deployment.eu_ai_act_compliance_governance", "ai_safety_ethics_deployment.model_alignment_rlhf_dpo_ethics", "ai_safety_ethics_deployment.production_gateway_rate_limiting_litellm"]
                }
            ],
            "linkedin": [
                {
                    "signal": "AI Safety, LLM Guardrails, Langfuse, or AI Ethics endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_safety_ethics_deployment.guardrails_nemo_guardrails_ai", "ai_safety_ethics_deployment.llm_observability_tracing_langfuse"]
                },
                {
                    "signal": "Job experience describing automated LLM red-teaming, EU AI Act compliance, or LiteLLM proxy architectures",
                    "strength": 0.85,
                    "maps_to": ["ai_safety_ethics_deployment.llm_security_red_teaming_garak", "ai_safety_ethics_deployment.eu_ai_act_compliance_governance", "ai_safety_ethics_deployment.production_gateway_rate_limiting_litellm"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "prompt_injection_jailbreak_defense",
                    "llm_observability_tracing_langfuse",
                    "pii_masking_anonymization_presidio"
                ],
                "description": "Defends against basic prompt injections, integrates Langfuse tracing for token/cost monitoring, and masks PII with Presidio."
            },
            "mid": {
                "expected_subskills": [
                    "guardrails_nemo_guardrails_ai",
                    "hallucination_detection_metrics",
                    "llm_security_red_teaming_garak"
                ],
                "description": "Configures NeMo/Guardrails AI safety rails, detects hallucinations with DeepEval/SelfCheckGPT, and runs automated Garak red-teaming."
            },
            "senior": {
                "expected_subskills": [
                    "model_alignment_rlhf_dpo_ethics",
                    "eu_ai_act_compliance_governance",
                    "production_gateway_rate_limiting_litellm"
                ],
                "description": "Guides DPO/RLHF alignment & fairness, governs EU AI Act compliance audits, and scales LiteLLM AI gateway infrastructure."
            }
        }
    },

    # ---------------------------------------------------------
    # Skill 8: ai_open_source_models
    # ---------------------------------------------------------
    {
        "skill_id": "ai_open_source_models",
        "name": "Open-Source Models, Ecosystem & Self-Hosting",
        "category": "ai_core",
        "description": "Modern open-weights foundation model ecosystem (Llama 3, DeepSeek-V3/R1 MoE, Qwen 2.5, Mistral), Hugging Face Hub & model card governance, open-weight licensing models (Apache 2.0 vs Llama Community), open vs proprietary TCO/data sovereignty trade-offs, local desktop & edge inference (Ollama, llama.cpp, GGUF, MLX), practical open fine-tuning toolchains (Unsloth, Axolotl, TRL), advanced post-training quantization (AWQ, GPTQ, EXL2, FP8), and enterprise high-throughput self-hosted serving clusters (vLLM PagedAttention, TGI, TensorRT-LLM).",
        "subskills": [
            {
                "id": "huggingface_hub_ecosystem",
                "name": "Hugging Face Hub, Model Repositories & Model Cards",
                "description": "Navigating and utilizing Hugging Face Hub: model repositories, dataset loading, Model Cards, Hub API, git-lfs checkpoints, Spaces, and transformers pipeline/AutoModel integration.",
                "keywords": ["Hugging Face Hub", "huggingface_hub API", "Model Cards", "hf datasets", "snapshot_download", "model repository structure", "Inference Endpoints", "AutoModelForCausalLM", "git-lfs weights"]
            },
            {
                "id": "open_model_licensing_governance",
                "name": "Open-Weight Licensing & Usage Governance",
                "description": "Understanding open-source vs open-weights licensing models: permissive licenses (Apache 2.0, MIT) versus restricted community licenses (Llama 3 Community License, DeepSeek License, Qwen License, commercial threshold restrictions, downstream derivative governance).",
                "keywords": ["Apache 2.0 license", "MIT license", "Llama 3 Community License", "commercial user threshold (700M MAU)", "open-weights vs open-source", "model attribution", "acceptable use policy (AUP)", "synthetic data distillation restrictions"]
            },
            {
                "id": "open_vs_proprietary_tradeoffs",
                "name": "Open-Weight vs Proprietary Model Trade-Off & TCO Analysis",
                "description": "Evaluating total cost of ownership (TCO: GPU hardware amortization, electricity, ops overhead vs token pricing), data sovereignty/privacy compliance (GDPR, HIPAA, on-prem isolation), latency SLAs, vendor lock-in mitigation, and customization feasibility.",
                "keywords": ["TCO (Total Cost of Ownership)", "data sovereignty / GDPR compliance", "on-premise isolation / air-gapped", "GPU capital expenditure (CapEx) vs OpEx", "vendor lock-in mitigation", "SLA guarantee vs self-hosted reliability", "customization flexibility"]
            },
            {
                "id": "open_weight_model_families",
                "name": "Open-Weight Model Architectures (Llama, DeepSeek, Qwen, Mistral)",
                "description": "Architecture paradigms and trade-offs across modern open-weight families: Meta Llama 3.x, DeepSeek-V3/R1 (Multi-Head Latent Attention - MLA, DeepSeekMoE, reasoning tokens), Alibaba Qwen 2.5, Mistral/Mixtral sparse Mixture-of-Experts (MoE), Gemma, and Phi.",
                "keywords": ["Meta Llama 3.x", "DeepSeek-V3 / DeepSeek-R1", "Multi-Head Latent Attention (MLA)", "Mixture of Experts (MoE)", "Qwen 2.5 series", "Mistral / Mixtral 8x7B / 8x22B", "Gemma 2", "router gate load balancing"]
            },
            {
                "id": "local_desktop_edge_runtime",
                "name": "Local Desktop & Edge Model Runtimes (Ollama, llama.cpp, GGUF, MLX)",
                "description": "Running quantized open models locally on developer machines and edge hardware: Ollama CLI/server API, llama.cpp C/C++ engine, GGUF file format conversion, Apple Silicon unified memory acceleration with MLX, and LM Studio.",
                "keywords": ["Ollama local CLI/server", "llama.cpp engine", "GGUF format", "Modelfile customization", "Apple Silicon MLX framework", "CPU/GPU layer offloading (-ngl)", "LM Studio", "edge device deployment"]
            },
            {
                "id": "open_model_finetuning_recipes",
                "name": "Open Model Fine-Tuning Frameworks (Axolotl, Unsloth & TRL)",
                "description": "Practical fine-tuning toolchains for open-weights models: Unsloth fast Triton kernels, Axolotl declarative YAML configurations, HuggingFace TRL (SFTTrainer/DPOTrainer), dataset format preparation (Alpaca, ShareGPT, ChatML).",
                "keywords": ["Unsloth fast LoRA/QLoRA", "Axolotl YAML recipes", "HuggingFace TRL (SFTTrainer)", "ChatML format", "ShareGPT dataset formatting", "Triton GPU kernels", "gradient accumulation & checkpointing", "custom tokenizer padding tokens"]
            },
            {
                "id": "model_quantization_awq_gptq_exl2",
                "name": "Production Model Quantization (AWQ, GPTQ, EXL2 & BitsAndBytes)",
                "description": "Post-training quantization (PTQ) techniques for open-weights serving: AWQ (Activation-aware Weight Quantization), GPTQ second-order calibration, EXL2 high-speed inference format, FP8 / INT4 precision calibration, and perplexity degradation testing.",
                "keywords": ["AWQ (Activation-aware Weight Quantization)", "GPTQ calibration dataset", "EXL2 format", "FP8 E4M3/E5M2 precision", "bitsandbytes NF4/INT8", "quantization perplexity loss", "Tensor Core INT4/FP8 GEMM acceleration"]
            },
            {
                "id": "enterprise_open_serving_vllm",
                "name": "Enterprise High-Throughput Open Model Serving (vLLM, TGI & TensorRT-LLM)",
                "description": "Architecting production-grade, distributed open-source model serving clusters: vLLM engine with PagedAttention and continuous batching, HuggingFace TGI, NVIDIA TensorRT-LLM, multi-GPU Tensor Parallelism (TP), chunked prefill, and OpenAI-compatible API endpoints.",
                "keywords": ["vLLM serving engine", "PagedAttention memory paging", "Continuous Batching / iteration-level scheduling", "HuggingFace TGI (Text Generation Inference)", "NVIDIA TensorRT-LLM", "Tensor Parallelism (TP) NCCL", "Chunked Prefill", "OpenAI-compatible vLLM server"]
            }
        ],
        "evidence": {
            "github": [
                {
                    "signal": "Hugging Face Hub API, Model Cards, or snapshot downloads",
                    "detection": "content_analysis",
                    "pattern": "from huggingface_hub import|snapshot_download|hf_hub_download|AutoModelForCausalLM\\.from_pretrained|AutoTokenizer\\.from_pretrained",
                    "strength": 0.85,
                    "maps_to": ["ai_open_source_models.huggingface_hub_ecosystem", "ai_open_source_models.open_weight_model_families"]
                },
                {
                    "signal": "Ollama API, llama.cpp GGUF loading, or MLX Apple Silicon scripts",
                    "detection": "content_analysis",
                    "pattern": "import ollama|ollama\\.chat|ollama\\.generate|llama_cpp|Llama\\(model_path|from mlx_lm import",
                    "strength": 0.9,
                    "maps_to": ["ai_open_source_models.local_desktop_edge_runtime"]
                },
                {
                    "signal": "Unsloth, Axolotl, or HuggingFace TRL fine-tuning scripts and recipes",
                    "detection": "content_analysis",
                    "pattern": "from unsloth import FastLanguageModel|import axolotl|from trl import SFTTrainer, DPOTrainer|SFTConfig",
                    "strength": 0.9,
                    "maps_to": ["ai_open_source_models.open_model_finetuning_recipes"]
                },
                {
                    "signal": "AWQ or AutoGPTQ quantization scripts and calibration runs",
                    "detection": "content_analysis",
                    "pattern": "from awq import AutoAWQForCausalLM|from auto_gptq import AutoGPTQForCausalLM|BitsAndBytesConfig",
                    "strength": 0.9,
                    "maps_to": ["ai_open_source_models.model_quantization_awq_gptq_exl2"]
                },
                {
                    "signal": "vLLM or TGI high-throughput production serving configuration",
                    "detection": "content_analysis",
                    "pattern": "from vllm import LLM, SamplingParams|AsyncLLMEngine|vllm serve|--tensor-parallel-size",
                    "strength": 0.95,
                    "maps_to": ["ai_open_source_models.enterprise_open_serving_vllm"]
                }
            ],
            "cv": [
                {
                    "signal": "Architected and maintained high-throughput enterprise LLM serving clusters with vLLM PagedAttention and multi-GPU tensor parallelism",
                    "strength": 0.95,
                    "maps_to": ["ai_open_source_models.enterprise_open_serving_vllm", "ai_open_source_models.model_quantization_awq_gptq_exl2"]
                },
                {
                    "signal": "Fine-tuned open-weights models (Llama 3, DeepSeek, Qwen) using Unsloth, Axolotl, and HuggingFace TRL for domain-specific tasks",
                    "strength": 0.9,
                    "maps_to": ["ai_open_source_models.open_model_finetuning_recipes", "ai_open_source_models.open_weight_model_families"]
                },
                {
                    "signal": "Deployed quantized models locally and on edge hardware with Ollama, llama.cpp (GGUF), and Apple Silicon MLX",
                    "strength": 0.85,
                    "maps_to": ["ai_open_source_models.local_desktop_edge_runtime", "ai_open_source_models.model_quantization_awq_gptq_exl2"]
                },
                {
                    "signal": "Conducted TCO, data sovereignty, and open-weights licensing analyses (Apache 2.0 vs Llama Community) for private on-prem AI migration",
                    "strength": 0.85,
                    "maps_to": ["ai_open_source_models.open_vs_proprietary_tradeoffs", "ai_open_source_models.open_model_licensing_governance", "ai_open_source_models.huggingface_hub_ecosystem"]
                }
            ],
            "linkedin": [
                {
                    "signal": "Open Source AI, Hugging Face, Ollama, vLLM, or Llama endorsed",
                    "strength": 0.5,
                    "maps_to": ["ai_open_source_models.huggingface_hub_ecosystem", "ai_open_source_models.local_desktop_edge_runtime"]
                },
                {
                    "signal": "Job experience deploying open-weights models with vLLM, fine-tuning via Unsloth/Axolotl, or on-prem LLM architectures",
                    "strength": 0.85,
                    "maps_to": ["ai_open_source_models.enterprise_open_serving_vllm", "ai_open_source_models.open_model_finetuning_recipes", "ai_open_source_models.open_weight_model_families"]
                }
            ]
        },
        "levels": {
            "junior": {
                "expected_subskills": [
                    "huggingface_hub_ecosystem",
                    "open_model_licensing_governance",
                    "open_vs_proprietary_tradeoffs"
                ],
                "description": "Utilizes Hugging Face Hub, evaluates open-weights licensing (Apache 2.0 vs Llama Community), and assesses TCO/privacy trade-offs."
            },
            "mid": {
                "expected_subskills": [
                    "open_weight_model_families",
                    "local_desktop_edge_runtime",
                    "open_model_finetuning_recipes"
                ],
                "description": "Runs local models with Ollama/llama.cpp (GGUF), understands open model architectures (Llama, DeepSeek MoE), and fine-tunes via Unsloth/Axolotl."
            },
            "senior": {
                "expected_subskills": [
                    "model_quantization_awq_gptq_exl2",
                    "enterprise_open_serving_vllm"
                ],
                "description": "Architects high-throughput vLLM serving clusters (PagedAttention, tensor parallelism) and executes post-training quantization (AWQ/GPTQ/FP8)."
            }
        }
    }
]

# Write skill json files
for skill in ai_skills:
    file_path = os.path.join(base_dir, 'skills', 'ai-engineer', f"{skill['skill_id']}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill, f, indent=2, ensure_ascii=False)
    print(f"Written skill: {skill['skill_id']}.json")

# -------------------------------------------------------------
# 2. AI Engineer Roles Definitions (Junior, Mid, Senior)
# -------------------------------------------------------------
roles_data = {
    "junior": {
        "role_id": "ai_engineer",
        "level": "junior",
        "title": "Junior AI Engineer",
        "description": "Entry-level AI Engineer focused on integrating foundation model APIs, crafting dynamic prompt templates, exploring open-source models with Hugging Face and Ollama, setting up vector databases, and assembling baseline RAG pipelines with basic observability.",
        "experience_range": "0-2 years",
        "skills": [
            {"skill_id": "ai_llm_fundamentals", "importance": 0.95, "rationale": "Core understanding of tokenization, sampling hyperparameters, and API SDK consumption."},
            {"skill_id": "ai_prompt_engineering", "importance": 0.90, "rationale": "Core ability to author few-shot prompts, dynamic Jinja2 templates, and formatted outputs."},
            {"skill_id": "ai_embeddings_vector_db", "importance": 0.85, "rationale": "Core vector generation, distance similarity calculations, and ChromaDB/FAISS storage."},
            {"skill_id": "ai_rag_implementation", "importance": 0.85, "rationale": "Core document chunking, LangChain/LlamaIndex baseline retrieval chains, and citations."},
            {"skill_id": "ai_open_source_models", "importance": 0.80, "rationale": "Understanding Hugging Face Hub, open-weights licensing vs proprietary APIs, and basic Ollama local setup."},
            {"skill_id": "ai_safety_ethics_deployment", "importance": 0.60, "rationale": "Basic awareness of prompt injection, PII masking with Presidio, and Langfuse tracing."},
            {"skill_id": "ai_agents_orchestration", "importance": 0.55, "rationale": "Basic understanding of function calling tool schemas and simple ReAct loops."},
            {"skill_id": "ai_multimodal_applications", "importance": 0.50, "rationale": "Basic integration of vision LLMs and Whisper speech-to-text APIs."}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Standard weighted scoring evaluating junior AI engineering foundations.",
            "thresholds": {}
        }
    },
    "mid": {
        "role_id": "ai_engineer",
        "level": "mid",
        "title": "Mid-level AI Engineer",
        "description": "Mid-level AI Engineer capable of implementing advanced RAG (semantic chunking, HyDE, re-ranking), fine-tuning open-weights models with LoRA/QLoRA/Unsloth, orchestrating stateful agent workflows (LangGraph, CrewAI), and configuring production guardrails.",
        "experience_range": "2-5 years",
        "skills": [
            {"skill_id": "ai_rag_implementation", "importance": 0.95, "rationale": "Core proficiency in multi-stage retrieval, cross-encoder re-ranking, and query transformations."},
            {"skill_id": "ai_agents_orchestration", "importance": 0.90, "rationale": "Core implementation of LangGraph state machines, CrewAI multi-agent teams, and tool calling."},
            {"skill_id": "ai_embeddings_vector_db", "importance": 0.90, "rationale": "Core cloud vector database indexing (Pinecone, Qdrant), pgvector, and HNSW tuning."},
            {"skill_id": "ai_llm_fundamentals", "importance": 0.85, "rationale": "Supervised fine-tuning theory with LoRA/QLoRA, KV caching dynamics, and Pydantic structured output."},
            {"skill_id": "ai_open_source_models", "importance": 0.85, "rationale": "Running open-weights models locally with Ollama/llama.cpp, fine-tuning recipes (Axolotl/Unsloth), and open model architectures."},
            {"skill_id": "ai_prompt_engineering", "importance": 0.85, "rationale": "Advanced reasoning prompts (CoT, ToT) and enterprise metaprompt architecture."},
            {"skill_id": "ai_safety_ethics_deployment", "importance": 0.80, "rationale": "Runtime guardrails (NeMo, Guardrails AI), hallucination metrics, and Garak red teaming."},
            {"skill_id": "ai_multimodal_applications", "importance": 0.70, "rationale": "Visual document table extraction, CLIP embeddings, and image generation pipelines."}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Standard weighted scoring evaluating autonomous implementation of advanced RAG, open-source LLMs, and agent architectures.",
            "thresholds": {}
        }
    },
    "senior": {
        "role_id": "ai_engineer",
        "level": "senior",
        "title": "Senior AI Engineer",
        "description": "Senior AI Engineer and Architect leading enterprise GenAI systems: GraphRAG, autonomous multi-agent planning, vLLM high-throughput distributed serving clusters, DSPy prompt compilation, ColPali multimodal RAG, and AI safety/EU AI Act governance.",
        "experience_range": "5+ years",
        "skills": [
            {"skill_id": "ai_agents_orchestration", "importance": 0.95, "rationale": "Architecting autonomous hierarchical multi-agent systems, MemGPT long-term memory, and enterprise HITL."},
            {"skill_id": "ai_rag_implementation", "importance": 0.95, "rationale": "Architecting GraphRAG knowledge graphs, Corrective RAG (CRAG), and quantitative RAGAS benchmarking."},
            {"skill_id": "ai_open_source_models", "importance": 0.90, "rationale": "Architecting enterprise vLLM serving clusters (PagedAttention, multi-GPU TP), AWQ/GPTQ quantization, and TCO/sovereignty trade-offs."},
            {"skill_id": "ai_safety_ethics_deployment", "importance": 0.90, "rationale": "AI alignment (DPO/RLHF), EU AI Act regulatory governance, and LiteLLM gateway caching infrastructure."},
            {"skill_id": "ai_llm_fundamentals", "importance": 0.85, "rationale": "Transformer architecture, KV cache memory scaling, FlashAttention, structured schema outputs, and quantitative benchmark evaluation."},
            {"skill_id": "ai_embeddings_vector_db", "importance": 0.85, "rationale": "Hybrid search (BM25+Dense with RRF), ColBERT late-interaction, and Matryoshka embedding fine-tuning."},
            {"skill_id": "ai_prompt_engineering", "importance": 0.85, "rationale": "Automated prompt optimization with DSPy, MIPRO teleprompters, and LLM-as-a-judge evaluation."},
            {"skill_id": "ai_multimodal_applications", "importance": 0.80, "rationale": "Realtime WebSocket voice agents, temporal video reasoning, and OCR-free ColPali visual RAG."}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Standard weighted scoring assessing production architecture, reliability, scale, and governance.",
            "thresholds": {}
        }
    }
}

for level_key, data in roles_data.items():
    file_path = os.path.join(base_dir, 'roles', 'ai-engineer', f"{level_key}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Written role: roles/ai-engineer/{level_key}.json")

# -------------------------------------------------------------
# 3. Evidence: github.json, cv.json, linkedin.json
# -------------------------------------------------------------
github_evidence = {
    "source_id": "github",
    "name": "GitHub Repository Analysis - AI Engineer",
    "description": "Global parsing rules for AI Engineer repositories across Python and TypeScript codebases. NOTE: Specific evidence mappings (regex patterns and maps_to composite keys) are stored within individual skill files under evidence.github. The validate_composite_keys.py script scans both locations to verify coverage.",
    "preprocessing_pipeline": {
        "steps": [
            {
                "step": 1,
                "name": "file_tree_scan",
                "target_files": [
                    {
                        "pattern": "requirements\\.txt|pyproject\\.toml|Pipfile|setup\\.py|package\\.json",
                        "skills": [
                            "ai_llm_fundamentals",
                            "ai_open_source_models",
                            "ai_embeddings_vector_db",
                            "ai_rag_implementation",
                            "ai_agents_orchestration",
                            "ai_safety_ethics_deployment"
                        ],
                        "priority": "high",
                        "notes": "Python and Node dependency manifests containing GenAI libraries (langchain, llama-index, openai, anthropic, chromadb, pinecone-client, vllm, litellm, dspy-ai, guardrails-ai, deepeval, langfuse, unsloth, huggingface-hub)"
                    },
                    {
                        "pattern": "\\.py$|\\.ipynb$",
                        "skills": [
                            "ai_llm_fundamentals",
                            "ai_open_source_models",
                            "ai_prompt_engineering",
                            "ai_embeddings_vector_db",
                            "ai_rag_implementation",
                            "ai_agents_orchestration",
                            "ai_multimodal_applications",
                            "ai_safety_ethics_deployment"
                        ],
                        "priority": "high",
                        "notes": "Core Python scripts and Jupyter notebooks implementing LLM chains, agent graphs, RAG retrievers, open-source fine-tuning recipes, and prompt templates"
                    },
                    {
                        "pattern": "promptfooconfig\\.ya?ml|\\.promptfoo|nemoguardrails/|guardrails/|litellm_config\\.ya?ml",
                        "skills": [
                            "ai_prompt_engineering",
                            "ai_safety_ethics_deployment"
                        ],
                        "priority": "high",
                        "notes": "Configuration files for prompt evaluation (Promptfoo), safety guardrails (NeMo), and AI gateways (LiteLLM)"
                    },
                    {
                        "pattern": "\\.env\\.example|docker-compose\\.ya?ml|Dockerfile|Modelfile",
                        "skills": [
                            "ai_embeddings_vector_db",
                            "ai_llm_fundamentals",
                            "ai_open_source_models",
                            "ai_safety_ethics_deployment"
                        ],
                        "priority": "medium",
                        "notes": "Infrastructure definitions for vector databases (Qdrant, Weaviate, Milvus, pgvector), local model inference (vLLM, Ollama, Modelfile), and API gateways"
                    }
                ]
            },
            {
                "step": 2,
                "name": "dependency_extraction",
                "source_manifests": [
                    "requirements.txt",
                    "pyproject.toml",
                    "package.json"
                ],
                "relevant_dependencies": {
                    "ai_llm_fundamentals": [
                        "openai",
                        "anthropic",
                        "google-generativeai",
                        "litellm",
                        "peft",
                        "transformers",
                        "instructor",
                        "tiktoken"
                    ],
                    "ai_open_source_models": [
                        "huggingface-hub",
                        "transformers",
                        "accelerate",
                        "vllm",
                        "ollama",
                        "unsloth",
                        "axolotl",
                        "trl",
                        "llama-cpp-python",
                        "autoawq",
                        "auto-gptq",
                        "bitsandbytes",
                        "mlx-lm"
                    ],
                    "ai_prompt_engineering": [
                        "dspy-ai",
                        "promptfoo",
                        "jinja2",
                        "textgrad"
                    ],
                    "ai_embeddings_vector_db": [
                        "sentence-transformers",
                        "chromadb",
                        "pinecone-client",
                        "weaviate-client",
                        "qdrant-client",
                        "pymilvus",
                        "pgvector",
                        "faiss-cpu",
                        "ragatouille"
                    ],
                    "ai_rag_implementation": [
                        "langchain",
                        "llama-index",
                        "ragas",
                        "trulens-eval",
                        "unstructured",
                        "pypdf",
                        "neo4j",
                        "cohere"
                    ],
                    "ai_agents_orchestration": [
                        "langgraph",
                        "crewai",
                        "pyautogen",
                        "letta",
                        "memgpt"
                    ],
                    "ai_multimodal_applications": [
                        "faster-whisper",
                        "elevenlabs",
                        "open-clip-torch",
                        "diffusers",
                        "colpali-engine",
                        "byaldi",
                        "opencv-python"
                    ],
                    "ai_safety_ethics_deployment": [
                        "guardrails-ai",
                        "nemoguardrails",
                        "presidio-analyzer",
                        "presidio-anonymizer",
                        "langfuse",
                        "langsmith",
                        "deepeval",
                        "garak"
                    ]
                }
            },
            {
                "step": 3,
                "name": "config_file_scan",
                "target_configs": [
                    "promptfooconfig.yaml",
                    "litellm_config.yaml",
                    "config.colang",
                    "docker-compose.yml",
                    "pyproject.toml",
                    "Modelfile"
                ]
            }
        ]
    },
    "ai_analysis_instructions": {
        "tasks": [
            "Map detected signals to composite keys ({skill_id}.{subskill_id}) using patterns defined in ai-engineer skill files",
            "Inspect requirements.txt and pyproject.toml for modern GenAI frameworks (LangGraph, DSPy, vLLM, LiteLLM, Qdrant, RAGAS, Unsloth)",
            "Check RAG implementation — presence of hybrid search, cross-encoder re-ranking, and semantic chunking vs naive splitters",
            "Evaluate agent architectures — cyclical LangGraph state graphs with checkpointers vs simple single-shot ReAct chains",
            "Assess open source & self-hosting — presence of vLLM serving configs, Ollama Modelfiles, and Unsloth/Axolotl fine-tuning recipes",
            "Assess safety & observability — presence of Langfuse/LangSmith tracing, Presidio PII masking, and NeMo/Guardrails AI integration"
        ]
    }
}

with open(os.path.join(base_dir, 'evidence', 'ai-engineer', 'github.json'), 'w', encoding='utf-8') as f:
    json.dump(github_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ai-engineer/github.json")

# cv.json
cv_evidence = {
    "source_id": "cv",
    "name": "CV / Resume Analysis - AI Engineer",
    "description": "Signals extracted from the user's CV/resume to evidence AI Engineer skills. CV data provides self-reported technical achievements that must be cross-validated with GitHub repositories and assessment sources.",
    "extraction_rules": {
        "description": "How to extract and weight information from CV content for AI Engineer roles.",
        "sections": [
            {
                "section": "skills_list",
                "description": "Explicit list of technologies, frameworks, vector DBs, and LLM toolkits in skills section.",
                "base_strength": 0.3,
                "notes": "Low strength alone. Listing 'LangChain' or 'RAG' requires verification against project details."
            },
            {
                "section": "work_experience",
                "description": "Job descriptions describing AI engineering achievements, RAG deployments, and multi-agent systems.",
                "base_strength": 0.5,
                "quality_indicators": [
                    "Specific LLM architectures and frameworks mentioned (e.g. 'architected multi-agent system with LangGraph, vLLM serving, and Qdrant hybrid search')",
                    "Quantifiable GenAI metrics (reduced hallucination rate by 35% using Corrective RAG and Cohere re-ranking, reduced token costs by 45% via semantic caching)",
                    "Action verbs indicating hands-on AI leadership (architected, fine-tuned, deployed, orchestrated, evaluated, hardened)",
                    "Production scale indicators (serving 10M+ daily LLM tokens, 100k+ QPS vector similarity searches)"
                ]
            },
            {
                "section": "projects",
                "description": "Personal or open-source GenAI projects demonstrating technical depth.",
                "base_strength": 0.4,
                "notes": "Higher strength if linked to GitHub with clean LangGraph code, DSPy optimization, and automated RAGAS test suites."
            },
            {
                "section": "certifications",
                "description": "Professional Generative AI and Cloud ML certifications.",
                "base_strength": 0.2,
                "recognized_certifications": {
                    "ai_certifications": [
                        "DeepLearning.AI LangChain / LangGraph Certification",
                        "AWS Certified Machine Learning - Specialty",
                        "Google Cloud Professional Machine Learning Engineer",
                        "Databricks Generative AI Engineer"
                    ]
                }
            }
        ]
    },
    "signal_mapping": {
        "description": "How CV mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
        "patterns": [
            {
                "pattern": "Architected end-to-end RAG pipelines with semantic chunking, Cohere re-ranking, and Pinecone/Qdrant vector databases",
                "maps_to": [
                    "ai_rag_implementation.basic_rag_pipeline_langchain_llamaindex",
                    "ai_rag_implementation.semantic_recursive_chunking",
                    "ai_rag_implementation.reranking_cross_encoders",
                    "ai_embeddings_vector_db.cloud_vector_db_pinecone_weaviate_qdrant"
                ],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Fine-tuned open-weights models (Llama 3, DeepSeek) using Unsloth/Axolotl and deployed with vLLM PagedAttention clusters",
                "maps_to": [
                    "ai_open_source_models.enterprise_open_serving_vllm",
                    "ai_open_source_models.open_model_finetuning_recipes",
                    "ai_open_source_models.model_quantization_awq_gptq_exl2"
                ],
                "strength_modifier": 1.2
            },
            {
                "pattern": "Orchestrated autonomous multi-agent systems using LangGraph, CrewAI, and custom tool function calling",
                "maps_to": [
                    "ai_agents_orchestration.stateful_agent_graphs_langgraph",
                    "ai_agents_orchestration.crewai_role_based_collaboration",
                    "ai_agents_orchestration.function_calling_tool_definitions"
                ],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Optimized production prompt pipelines using DSPy teleprompters and LLM-as-a-judge benchmarking with Promptfoo",
                "maps_to": [
                    "ai_prompt_engineering.automated_prompt_optimization_dspy",
                    "ai_prompt_engineering.prompt_evaluation_benchmarking",
                    "ai_prompt_engineering.chain_of_thought_reasoning"
                ],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Implemented hybrid search combining BM25 and dense embeddings with Reciprocal Rank Fusion (RRF) in PostgreSQL pgvector",
                "maps_to": [
                    "ai_embeddings_vector_db.hybrid_search_sparse_dense_bm25",
                    "ai_embeddings_vector_db.pgvector_relational_integration",
                    "ai_embeddings_vector_db.ann_indexing_hnsw_ivf"
                ],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Built multimodal applications using GPT-4o vision, Whisper audio transcription, and ElevenLabs speech synthesis",
                "maps_to": [
                    "ai_multimodal_applications.vision_llm_api_image_analysis",
                    "ai_multimodal_applications.speech_to_text_whisper_integration",
                    "ai_multimodal_applications.text_to_speech_voice_synthesis"
                ],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Enforced production LLM guardrails using NeMo Guardrails, Microsoft Presidio PII masking, and Langfuse tracing",
                "maps_to": [
                    "ai_safety_ethics_deployment.guardrails_nemo_guardrails_ai",
                    "ai_safety_ethics_deployment.pii_masking_anonymization_presidio",
                    "ai_safety_ethics_deployment.llm_observability_tracing_langfuse"
                ],
                "strength_modifier": 1.1
            },
            {
                "pattern": "Evaluated RAG systems using RAGAS metrics and constructed GraphRAG knowledge graphs with Neo4j",
                "maps_to": [
                    "ai_rag_implementation.rag_evaluation_ragas_trulens",
                    "ai_rag_implementation.graph_rag_knowledge_graphs",
                    "ai_rag_implementation.agentic_corrective_rag_crag_self_rag"
                ],
                "strength_modifier": 1.2
            }
        ]
    },
    "important_notes": [
        "Distinguish AI Engineer (LLMs, RAG, Agents, Prompting) from Data Analyst (da_machine_learning: regression, classification, tabular modeling)",
        "Distinguish AI Safety (prompt injection, jailbreak, guardrails, hallucinations) from traditional Cyber Security (network, IAM, OS CVEs)",
        "Cross-validate self-reported GenAI metrics with code in GitHub and assessment results"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'ai-engineer', 'cv.json'), 'w', encoding='utf-8') as f:
    json.dump(cv_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ai-engineer/cv.json")

# linkedin.json
linkedin_evidence = {
    "source_id": "linkedin",
    "name": "LinkedIn Profile Analysis - AI Engineer",
    "description": "Signals extracted from LinkedIn profiles to evidence AI Engineer skills.",
    "extraction_rules": {
        "sections": [
            {
                "section": "headline_summary",
                "description": "Profile headline and summary section.",
                "base_strength": 0.2,
                "notes": "Look for specialization (e.g. 'Senior AI Engineer | LLMs | LangGraph | RAG | vLLM')."
            },
            {
                "section": "experience",
                "description": "Work experience entries with job titles and project descriptions.",
                "base_strength": 0.4,
                "quality_indicators": [
                    "AI-specific job titles (AI Engineer, Generative AI Architect, LLM Engineer, Machine Learning Systems Engineer)",
                    "Technologies described (LangChain, LangGraph, LlamaIndex, vLLM, Pinecone, Qdrant, DSPy, LoRA, Hugging Face)",
                    "Scale and production impact of GenAI applications"
                ]
            },
            {
                "section": "skills_endorsements",
                "description": "Skills listed with endorsements.",
                "base_strength": 0.15
            },
            {
                "section": "recommendations",
                "description": "Written peer and manager recommendations.",
                "base_strength": 0.3
            }
        ]
    },
    "signal_mapping": {
        "description": "How LinkedIn mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
        "patterns": [
            {
                "pattern": "LinkedIn skills endorsement for 'Large Language Models (LLM)' or 'Generative AI'",
                "maps_to": [
                    "ai_llm_fundamentals.foundation_models_api_integration",
                    "ai_llm_fundamentals.tokenization_bpe_sentencepiece"
                ],
                "strength_modifier": 0.33
            },
            {
                "pattern": "LinkedIn skills endorsement for 'Prompt Engineering' or 'LangChain'",
                "maps_to": [
                    "ai_prompt_engineering.prompt_templating_dynamic_injection",
                    "ai_prompt_engineering.zero_shot_few_shot_prompting"
                ],
                "strength_modifier": 0.33
            },
            {
                "pattern": "LinkedIn skills endorsement for 'Vector Databases' or 'Pinecone'",
                "maps_to": [
                    "ai_embeddings_vector_db.cloud_vector_db_pinecone_weaviate_qdrant",
                    "ai_embeddings_vector_db.dense_embeddings_generation"
                ],
                "strength_modifier": 0.33
            },
            {
                "pattern": "Job experience describing building production RAG systems with LlamaIndex and hybrid vector search",
                "maps_to": [
                    "ai_rag_implementation.basic_rag_pipeline_langchain_llamaindex",
                    "ai_embeddings_vector_db.hybrid_search_sparse_dense_bm25",
                    "ai_rag_implementation.semantic_recursive_chunking"
                ],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing deploying open-weights models with vLLM, Ollama runtimes, and Hugging Face Hub integration",
                "maps_to": [
                    "ai_open_source_models.enterprise_open_serving_vllm",
                    "ai_open_source_models.local_desktop_edge_runtime",
                    "ai_open_source_models.huggingface_hub_ecosystem"
                ],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing LangGraph multi-agent architectures, checkpointers, and human-in-the-loop workflows",
                "maps_to": [
                    "ai_agents_orchestration.stateful_agent_graphs_langgraph",
                    "ai_agents_orchestration.human_in_the_loop_hitl_workflows",
                    "ai_agents_orchestration.function_calling_tool_definitions"
                ],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing LLM guardrails, PII masking with Presidio, and Langfuse tracing",
                "maps_to": [
                    "ai_safety_ethics_deployment.guardrails_nemo_guardrails_ai",
                    "ai_safety_ethics_deployment.pii_masking_anonymization_presidio",
                    "ai_safety_ethics_deployment.llm_observability_tracing_langfuse"
                ],
                "strength_modifier": 1.0
            },
            {
                "pattern": "Job experience describing multimodal Vision-Language integration, Whisper speech transcription, or ColPali visual RAG",
                "maps_to": [
                    "ai_multimodal_applications.vision_llm_api_image_analysis",
                    "ai_multimodal_applications.speech_to_text_whisper_integration",
                    "ai_multimodal_applications.multimodal_rag_colpali_visual_retrieval"
                ],
                "strength_modifier": 1.0
            }
        ]
    },
    "important_notes": [
        "ALL extracted signals MUST be mapped to COMPOSITE KEYS ({skill_id}.{subskill_id})",
        "LinkedIn endorsements have low evidential value on their own; cross-validate with code and technical assessments"
    ]
}

with open(os.path.join(base_dir, 'evidence', 'ai-engineer', 'linkedin.json'), 'w', encoding='utf-8') as f:
    json.dump(linkedin_evidence, f, indent=2, ensure_ascii=False)
print("Written evidence/ai-engineer/linkedin.json")

print("\nSkills, roles, and github/cv/linkedin evidence generation complete.")
