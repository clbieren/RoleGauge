import os
import json
import shutil

base_dir = os.path.abspath('knowledge-base')
skills_dir = os.path.join(base_dir, 'skills', 'blockchain')
evidence_dir = os.path.join(base_dir, 'evidence', 'blockchain-developer')
roles_dir = os.path.join(base_dir, 'roles', 'blockchain-developer')

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

# Remove deprecated/merged blockchain_oracles.json if it exists
old_oracle_file = os.path.join(skills_dir, 'blockchain_oracles.json')
if os.path.exists(old_oracle_file):
    os.remove(old_oracle_file)
    print(f"Removed legacy merged file: {old_oracle_file}")

# ==============================================================================
# 1. BLOCKCHAIN SKILLS DEFINITIONS (8 Skills, 74 Subskills)
# ==============================================================================
skills = {}

# 1. blockchain_fundamentals
skills["blockchain_fundamentals"] = {
  "skill_id": "blockchain_fundamentals",
  "name": "Blockchain Fundamentals & Distributed Systems",
  "category": "blockchain_core",
  "description": "Fundamental concepts of distributed ledgers, peer-to-peer networking, state transition systems, UTXO vs Account models, and cryptographic primitives.",
  "subskills": [
    {
      "id": "what_is_blockchain",
      "name": "Distributed Ledger Technology Foundations",
      "description": "Understanding append-only distributed ledgers, immutability, cryptographic chaining, and centralized vs decentralized paradigms.",
      "keywords": ["distributed ledger", "append-only", "immutability", "cryptographic chain", "decentralization", "trustless", "DLT", "double spending"]
    },
    {
      "id": "decentralization_principles",
      "name": "Decentralization Principles & Game Theory",
      "description": "Nakamoto consensus principles, censorship resistance, game theoretic alignment, and permissionless network participation.",
      "keywords": ["censorship resistance", "permissionless", "game theory", "Nakamoto consensus", "trust minimization", "node distribution"]
    },
    {
      "id": "blockchain_data_structure",
      "name": "Block Architecture & Header Structures",
      "description": "Internal structure of blocks: block header, nonce, difficulty target, timestamp, state root, receipt root, and previous block hash.",
      "keywords": ["block header", "nonce", "difficulty target", "block height", "state root", "receipts root", "transactions root", "parent hash"]
    },
    {
      "id": "utxo_vs_account_model",
      "name": "UTXO vs Account-Based State Models",
      "description": "Comparison between Bitcoin's Unspent Transaction Output (UTXO) model and Ethereum's Account/Nonce state model.",
      "keywords": ["UTXO", "account model", "nonce", "state transition", "unspent output", "coinbase transaction", "account balance"]
    },
    {
      "id": "p2p_network_gossip",
      "name": "P2P Networking & Gossip Protocols",
      "description": "Peer-to-peer communication, node discovery (Kademlia DHT, discv4/discv5), and transaction/block propagation via gossip protocols.",
      "keywords": ["P2P", "gossip protocol", "Kademlia DHT", "discv5", "libp2p", "devp2p", "block propagation", "mempool broadcast"]
    },
    {
      "id": "transaction_lifecycle_mempool",
      "name": "Transaction Lifecycle & Mempool Dynamics",
      "description": "Transaction creation, digital signature verification, mempool propagation, MEV dynamics, replacement-by-fee (RBF), and block inclusion.",
      "keywords": ["mempool", "transaction lifecycle", "RBF", "gas price bidding", "pending transactions", "inclusion delay", "nonce ordering"]
    },
    {
      "id": "cryptographic_hashing_merkle_trees",
      "name": "Cryptographic Hashing & Merkle Trees",
      "description": "SHA-256, Keccak-256, RIPEMD-160, Merkle Trees, Merkle Patricia Tries, and cryptographic proof verification (Merkle proofs).",
      "keywords": ["Keccak-256", "SHA-256", "Merkle tree", "Merkle proof", "Merkle Patricia Trie", "root hash", "cryptographic inclusion proof"]
    },
    {
      "id": "byzantine_fault_tolerance_theory",
      "name": "Byzantine Fault Tolerance (BFT) Theory",
      "description": "The Byzantine Generals Problem, crash fault tolerance vs Byzantine fault tolerance, safety vs liveness, and 33%/51% attack thresholds.",
      "keywords": ["Byzantine Fault Tolerance", "BFT", "safety vs liveness", "FLP impossibility", "51% attack", "33% fault threshold", "finality"]
    },
    {
      "id": "trilemma_tradeoff_analysis",
      "name": "Blockchain Trilemma & Tradeoff Analysis",
      "description": "Analyzing the fundamental tradeoffs between Decentralization, Security, and Scalability across L1 and L2 architectures.",
      "keywords": ["Blockchain Trilemma", "scalability", "decentralization", "security", "L1 vs L2", "block size debate", "throughput limits"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Cryptographic hash functions, Merkle tree implementations, and block parsing scripts",
        "detection": "content_analysis",
        "pattern": "keccak256|sha256|MerkleTree|verifyProof|getMerkleRoot",
        "strength": 0.85,
        "maps_to": [
          "blockchain_fundamentals.cryptographic_hashing_merkle_trees",
          "blockchain_fundamentals.blockchain_data_structure"
        ]
      },
      {
        "signal": "Raw transaction serialization, signature validation, and mempool listeners",
        "detection": "content_analysis",
        "pattern": "signTransaction|serializeTransaction|eth_sendRawTransaction|on\\('pending'",
        "strength": 0.85,
        "maps_to": [
          "blockchain_fundamentals.transaction_lifecycle_mempool",
          "blockchain_fundamentals.utxo_vs_account_model"
        ]
      },
      {
        "signal": "P2P node setup, gossip config, or consensus simulation scripts",
        "detection": "file_presence",
        "pattern": "docker-compose\\.ya?ml|geth\\.toml|reth\\.toml",
        "strength": 0.8,
        "maps_to": [
          "blockchain_fundamentals.p2p_network_gossip",
          "blockchain_fundamentals.byzantine_fault_tolerance_theory",
          "blockchain_fundamentals.trilemma_tradeoff_analysis",
          "blockchain_fundamentals.what_is_blockchain",
          "blockchain_fundamentals.decentralization_principles"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Demonstrated deep understanding of distributed ledger mechanics, Merkle proofs, and consensus economics",
        "strength": 0.6,
        "maps_to": [
          "blockchain_fundamentals.what_is_blockchain",
          "blockchain_fundamentals.decentralization_principles",
          "blockchain_fundamentals.blockchain_data_structure",
          "blockchain_fundamentals.utxo_vs_account_model",
          "blockchain_fundamentals.cryptographic_hashing_merkle_trees"
        ]
      },
      {
        "signal": "Architected low-latency mempool monitors and evaluated BFT consensus models against blockchain trilemma constraints",
        "strength": 0.6,
        "maps_to": [
          "blockchain_fundamentals.p2p_network_gossip",
          "blockchain_fundamentals.transaction_lifecycle_mempool",
          "blockchain_fundamentals.byzantine_fault_tolerance_theory",
          "blockchain_fundamentals.trilemma_tradeoff_analysis"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements and publications in Blockchain Architecture, Distributed Systems, and Cryptography",
        "strength": 0.4,
        "maps_to": [
          "blockchain_fundamentals.what_is_blockchain",
          "blockchain_fundamentals.decentralization_principles",
          "blockchain_fundamentals.blockchain_data_structure",
          "blockchain_fundamentals.utxo_vs_account_model",
          "blockchain_fundamentals.p2p_network_gossip",
          "blockchain_fundamentals.transaction_lifecycle_mempool",
          "blockchain_fundamentals.cryptographic_hashing_merkle_trees",
          "blockchain_fundamentals.byzantine_fault_tolerance_theory",
          "blockchain_fundamentals.trilemma_tradeoff_analysis"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive blockchain fundamentals assessment covering Merkle proofs, mempool dynamics, BFT theory, and Trilemma tradeoffs",
        "strength": 1.0,
        "maps_to": [
          "blockchain_fundamentals.what_is_blockchain",
          "blockchain_fundamentals.decentralization_principles",
          "blockchain_fundamentals.blockchain_data_structure",
          "blockchain_fundamentals.utxo_vs_account_model",
          "blockchain_fundamentals.p2p_network_gossip",
          "blockchain_fundamentals.transaction_lifecycle_mempool",
          "blockchain_fundamentals.cryptographic_hashing_merkle_trees",
          "blockchain_fundamentals.byzantine_fault_tolerance_theory",
          "blockchain_fundamentals.trilemma_tradeoff_analysis"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "what_is_blockchain",
        "decentralization_principles",
        "blockchain_data_structure",
        "utxo_vs_account_model"
      ],
      "description": "Understands block header layouts, UTXO vs Account balance models, and fundamental decentralization principles."
    },
    "mid": {
      "expected_subskills": [
        "p2p_network_gossip",
        "transaction_lifecycle_mempool",
        "cryptographic_hashing_merkle_trees"
      ],
      "description": "Constructs and verifies Merkle inclusion proofs, analyzes mempool transaction propagation, and understands P2P gossip networks."
    },
    "senior": {
      "expected_subskills": [
        "byzantine_fault_tolerance_theory",
        "trilemma_tradeoff_analysis"
      ],
      "description": "Evaluates BFT consensus resilience under adversary conditions and models architectural tradeoffs across the blockchain trilemma."
    }
  }
}

# 2. blockchain_core_concepts
skills["blockchain_core_concepts"] = {
  "skill_id": "blockchain_core_concepts",
  "name": "Blockchain Cryptography & Consensus Core",
  "category": "blockchain_core",
  "description": "Cryptographic foundations, digital signatures (ECDSA, Ed25519, BLS), key derivation, wallet mechanics, token economics, hard/soft forks, and advanced consensus algorithms.",
  "subskills": [
    {
      "id": "asymmetric_cryptography_signatures",
      "name": "Asymmetric Cryptography & Digital Signatures",
      "description": "Elliptic curve cryptography (secp256k1, Ed25519, BLS signature aggregation), public/private key pairs, and signature verification (ecrecover).",
      "keywords": ["ECDSA", "secp256k1", "Ed25519", "BLS signatures", "ecrecover", "public key", "private key", "signature malleability"]
    },
    {
      "id": "crypto_wallets_key_management",
      "name": "Hierarchical Deterministic (HD) Wallets & Key Derivation",
      "description": "BIP-39 mnemonic seeds, BIP-32/BIP-44 derivation paths, multisig wallet schemes, and Shamir Secret Sharing.",
      "keywords": ["BIP-39", "BIP-44", "BIP-32", "derivation path", "mnemonic seed", "hardware wallet", "multisig", "key management"]
    },
    {
      "id": "cryptocurrency_tokenomics_basics",
      "name": "Tokenomics Fundamentals & Emission Schedules",
      "description": "Inflationary vs deflationary token models, burn mechanisms (EIP-1559), staking yields, vesting schedules, and supply caps.",
      "keywords": ["tokenomics", "EIP-1559", "burn mechanism", "emission schedule", "vesting", "inflationary", "deflationary", "circulating supply"]
    },
    {
      "id": "mining_and_validator_incentives",
      "name": "Validator Economics, Slashing & Staking",
      "description": "Proof of Stake validator duties, attestation rewards, slashing conditions (double signing, surround voting), and effective balance mechanics.",
      "keywords": ["staking", "slashing", "validator rewards", "attestation", "effective balance", "double signing", "inactivity leak"]
    },
    {
      "id": "hard_and_soft_forks",
      "name": "Network Forks & Protocol Upgrades",
      "description": "Hard forks vs soft forks, backward compatibility, chain splits, replay protection, and social consensus governance.",
      "keywords": ["hard fork", "soft fork", "chain split", "replay protection", "backward compatibility", "network upgrade", "EIP activation"]
    },
    {
      "id": "sybil_resistance_mechanisms",
      "name": "Sybil Resistance Mechanisms (PoW, PoS, PoA)",
      "description": "Comparative analysis of Sybil defenses: Proof of Work hash rate, Proof of Stake capital locking, and Proof of Authority reputation.",
      "keywords": ["Sybil resistance", "Proof of Work", "Proof of Stake", "Proof of Authority", "energy consumption", "validator quorum"]
    },
    {
      "id": "advanced_consensus_mechanisms",
      "name": "Advanced Consensus Algorithms (Tendermint, PoH, Avalanche)",
      "description": "Tendermint Core (PBFT-derived), Solana Proof of History (VDF sequencing), Avalanche Snow family DAG consensus, and Casper FFG/LMD-GHOST.",
      "keywords": ["Tendermint", "Proof of History", "Avalanche consensus", "Casper FFG", "LMD-GHOST", "VDF", "deterministic finality"]
    },
    {
      "id": "zero_knowledge_primitives_foundations",
      "name": "Zero-Knowledge Proof Foundations (zk-SNARKs & zk-STARKs)",
      "description": "Cryptographic zero-knowledge foundations: arithmetic circuits, R1CS, QAP, pairing cryptography, trusted setups vs transparent STARKs.",
      "keywords": ["zk-SNARK", "zk-STARK", "arithmetic circuits", "R1CS", "trusted setup", "transparent proofs", "cryptographic zero knowledge"]
    },
    {
      "id": "state_machine_replication",
      "name": "State Machine Replication & Deterministic Execution",
      "description": "Deterministic state transitions, world state trie transitions, EVM state rollback semantics, and multi-validator state synchronization.",
      "keywords": ["State Machine Replication", "world state", "deterministic execution", "state synchronization", "snapshot sync", "warp sync"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Elliptic curve signature generation, verification, and BIP-39/44 key derivation",
        "detection": "content_analysis",
        "pattern": "ethers\\.Wallet\\.fromMnemonic|bip39\\.mnemonicToSeed|secp256k1|noble/curves|ecrecover\\(",
        "strength": 0.9,
        "maps_to": [
          "blockchain_core_concepts.asymmetric_cryptography_signatures",
          "blockchain_core_concepts.crypto_wallets_key_management"
        ]
      },
      {
        "signal": "Token vesting contracts, EIP-1559 baseFee calculations, and staking distribution logic",
        "detection": "content_analysis",
        "pattern": "vestingSchedule|calculateBurn|stake\\(|withdrawRewards|slashingPeriod",
        "strength": 0.85,
        "maps_to": [
          "blockchain_core_concepts.cryptocurrency_tokenomics_basics",
          "blockchain_core_concepts.mining_and_validator_incentives"
        ]
      },
      {
        "signal": "Zero-knowledge circuit definitions (Circom, Halo2) and consensus simulation algorithms",
        "detection": "content_analysis",
        "pattern": "template\\s+[A-Za-z0-9_]+\\s*\\(\\)|circom|snarkjs|groth16|plonk|tendermint",
        "strength": 0.9,
        "maps_to": [
          "blockchain_core_concepts.zero_knowledge_primitives_foundations",
          "blockchain_core_concepts.advanced_consensus_mechanisms",
          "blockchain_core_concepts.state_machine_replication",
          "blockchain_core_concepts.hard_and_soft_forks",
          "blockchain_core_concepts.sybil_resistance_mechanisms"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Designed cryptographic wallet recovery schemes and implemented signature verification algorithms (ECDSA, BLS)",
        "strength": 0.6,
        "maps_to": [
          "blockchain_core_concepts.asymmetric_cryptography_signatures",
          "blockchain_core_concepts.crypto_wallets_key_management",
          "blockchain_core_concepts.cryptocurrency_tokenomics_basics"
        ]
      },
      {
        "signal": "Engineered custom consensus validators and authored zero-knowledge zk-SNARK circuits for privacy-preserving protocols",
        "strength": 0.6,
        "maps_to": [
          "blockchain_core_concepts.mining_and_validator_incentives",
          "blockchain_core_concepts.advanced_consensus_mechanisms",
          "blockchain_core_concepts.zero_knowledge_primitives_foundations",
          "blockchain_core_concepts.state_machine_replication"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Cryptographic Engineering, Zero-Knowledge Proofs, Consensus Mechanisms, and Tokenomics",
        "strength": 0.4,
        "maps_to": [
          "blockchain_core_concepts.asymmetric_cryptography_signatures",
          "blockchain_core_concepts.crypto_wallets_key_management",
          "blockchain_core_concepts.cryptocurrency_tokenomics_basics",
          "blockchain_core_concepts.mining_and_validator_incentives",
          "blockchain_core_concepts.hard_and_soft_forks",
          "blockchain_core_concepts.sybil_resistance_mechanisms",
          "blockchain_core_concepts.advanced_consensus_mechanisms",
          "blockchain_core_concepts.zero_knowledge_primitives_foundations",
          "blockchain_core_concepts.state_machine_replication"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive blockchain core concepts assessment covering ECDSA, BIP-39 derivation, slashing conditions, Tendermint consensus, and zk-SNARKs",
        "strength": 1.0,
        "maps_to": [
          "blockchain_core_concepts.asymmetric_cryptography_signatures",
          "blockchain_core_concepts.crypto_wallets_key_management",
          "blockchain_core_concepts.cryptocurrency_tokenomics_basics",
          "blockchain_core_concepts.mining_and_validator_incentives",
          "blockchain_core_concepts.hard_and_soft_forks",
          "blockchain_core_concepts.sybil_resistance_mechanisms",
          "blockchain_core_concepts.advanced_consensus_mechanisms",
          "blockchain_core_concepts.zero_knowledge_primitives_foundations",
          "blockchain_core_concepts.state_machine_replication"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "asymmetric_cryptography_signatures",
        "crypto_wallets_key_management",
        "cryptocurrency_tokenomics_basics"
      ],
      "description": "Applies ECDSA signature verification, manages BIP-39/44 HD wallet derivation paths, and understands token emission schedules."
    },
    "mid": {
      "expected_subskills": [
        "mining_and_validator_incentives",
        "hard_and_soft_forks",
        "sybil_resistance_mechanisms"
      ],
      "description": "Models validator staking rewards and slashing conditions, manages protocol fork upgrades, and compares PoW/PoS Sybil resistance."
    },
    "senior": {
      "expected_subskills": [
        "advanced_consensus_mechanisms",
        "zero_knowledge_primitives_foundations",
        "state_machine_replication"
      ],
      "description": "Designs Tendermint/PBFT consensus state machines, constructs zk-SNARK arithmetic circuits, and orchestrates deterministic state replication."
    }
  }
}

# 3. blockchain_networks
skills["blockchain_networks"] = {
  "skill_id": "blockchain_networks",
  "name": "Multi-Chain Networks & Cross-Chain Infrastructure",
  "category": "blockchain_networks",
  "description": "Architecture of EVM chains, Layer 2 networks, Solana/SVM, Alt-VMs (Move, WASM, TVM), cross-chain bridges, CCIP/IBC interoperability, and modular data availability networks.",
  "subskills": [
    {
      "id": "evm_based_chains_ethereum_polygon",
      "name": "EVM Network Architecture (Ethereum, Polygon, BSC)",
      "description": "EVM architecture, chain IDs, gas token mechanics, JSON-RPC specifications, and differences across EVM-compatible L1s and sidechains.",
      "keywords": ["EVM", "Ethereum", "Polygon PoS", "BNB Chain", "Chain ID", "JSON-RPC", "eth_call", "gas limits"]
    },
    {
      "id": "testnets_faucets_rpc_providers",
      "name": "Testnets, Faucets & RPC Node Providers",
      "description": "Operating on public testnets (Sepolia, Holesky), managing RPC rate limits, private RPC endpoints (Infura, Alchemy, QuickNode), and fallback providers.",
      "keywords": ["Sepolia", "Holesky", "testnet", "faucets", "Alchemy", "Infura", "QuickNode", "RPC fallback"]
    },
    {
      "id": "block_explorers_network_monitoring",
      "name": "Block Explorers & Network Telemetry",
      "description": "Navigating and querying block explorers (Etherscan, Blockscout, Solscan), contract verification, internal transaction tracing, and validator telemetry.",
      "keywords": ["Etherscan", "Blockscout", "Solscan", "internal transactions", "trace_transaction", "gas tracker", "block explorer API"]
    },
    {
      "id": "l2_rollups_arbitrum_optimism_base",
      "name": "Layer 2 Rollups Ecosystem (Arbitrum, Optimism, Base)",
      "description": "Rollup architectures: Arbitrum Nitro, OP Stack (Optimism, Base), sequencer role, L1 batch submission, and L1-L2 message passing.",
      "keywords": ["Arbitrum Nitro", "OP Stack", "Base", "sequencer", "batch posting", "L1 to L2 bridge", "Optimism Bedrock"]
    },
    {
      "id": "solana_sealevel_architecture",
      "name": "Solana Sealevel Runtime & Account Architecture",
      "description": "Solana runtime architecture: parallel execution (Sealevel), Gulf Stream mempool-less forwarding, Turbine block propagation, and Program Derived Addresses (PDAs).",
      "keywords": ["Solana", "Sealevel", "parallel execution", "PDA", "Turbine", "Gulf Stream", "SVM", "rent exemption"]
    },
    {
      "id": "cross_chain_bridges_relayers",
      "name": "Cross-Chain Bridges & Relayer Security",
      "description": "Lock-and-mint, burn-and-mint, liquidity pool bridges, relayer incentive networks, and bridge security threat models.",
      "keywords": ["cross-chain bridge", "lock and mint", "burn and mint", "relayer", "bridge security", "wormhole", "layerzero"]
    },
    {
      "id": "interoperability_protocols_ccip_ibc",
      "name": "Cross-Chain Interoperability Protocols (CCIP, IBC)",
      "description": "Standardized cross-chain communication protocols: Chainlink Cross-Chain Interoperability Protocol (CCIP), Cosmos Inter-Blockchain Communication (IBC), and cross-chain token transfers.",
      "keywords": ["Chainlink CCIP", "IBC", "Cosmos", "cross-chain messaging", "programmable token transfer", "risk management network"]
    },
    {
      "id": "alt_vm_chains_move_tvm_wasm",
      "name": "Alt-VM Ecosystems (Move, TVM, CosmWasm)",
      "description": "Non-EVM smart contract platforms: Move VM (Aptos, Sui), TON Virtual Machine (TVM), and CosmWasm/Near WASM runtimes.",
      "keywords": ["Move VM", "Sui", "Aptos", "TVM", "TON blockchain", "CosmWasm", "WASM smart contracts", "resource-oriented programming"]
    },
    {
      "id": "modular_blockchains_celestia_avail",
      "name": "Modular Blockchain Architecture & Data Availability",
      "description": "Decoupling execution, settlement, consensus, and data availability; sovereign rollups; and Data Availability (DA) layers (Celestia, EigenDA, Avail).",
      "keywords": ["modular blockchain", "Celestia", "EigenDA", "Avail", "Data Availability Sampling", "sovereign rollup", "settlement layer"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Multi-network deployment scripts and RPC configuration matrices",
        "detection": "content_analysis",
        "pattern": "networks:\\s*\\{\\s*sepolia:|arbitrum:|optimism:|polygon:|mainnet:",
        "strength": 0.85,
        "maps_to": [
          "blockchain_networks.evm_based_chains_ethereum_polygon",
          "blockchain_networks.testnets_faucets_rpc_providers",
          "blockchain_networks.l2_rollups_arbitrum_optimism_base"
        ]
      },
      {
        "signal": "Solana Anchor program configurations and SVM account deserialization",
        "detection": "file_presence",
        "pattern": "Anchor\\.toml|declare_id!|@solana/web3\\.js",
        "strength": 0.9,
        "maps_to": [
          "blockchain_networks.solana_sealevel_architecture",
          "blockchain_networks.block_explorers_network_monitoring"
        ]
      },
      {
        "signal": "Chainlink CCIP cross-chain token transfer scripts, IBC configs, and Move/WASM modules",
        "detection": "content_analysis",
        "pattern": "IRouterClient|ccipReceive|Move\\.toml|Celestia|EigenDA|IL2ToL1MessagePasser",
        "strength": 0.9,
        "maps_to": [
          "blockchain_networks.cross_chain_bridges_relayers",
          "blockchain_networks.interoperability_protocols_ccip_ibc",
          "blockchain_networks.alt_vm_chains_move_tvm_wasm",
          "blockchain_networks.modular_blockchains_celestia_avail"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Deployed multi-chain smart contracts across Ethereum, Arbitrum, Optimism, Base, and Solana",
        "strength": 0.6,
        "maps_to": [
          "blockchain_networks.evm_based_chains_ethereum_polygon",
          "blockchain_networks.l2_rollups_arbitrum_optimism_base",
          "blockchain_networks.solana_sealevel_architecture",
          "blockchain_networks.testnets_faucets_rpc_providers"
        ]
      },
      {
        "signal": "Architected cross-chain token transfers with Chainlink CCIP and integrated modular DA layers with Celestia",
        "strength": 0.6,
        "maps_to": [
          "blockchain_networks.cross_chain_bridges_relayers",
          "blockchain_networks.interoperability_protocols_ccip_ibc",
          "blockchain_networks.alt_vm_chains_move_tvm_wasm",
          "blockchain_networks.modular_blockchains_celestia_avail",
          "blockchain_networks.block_explorers_network_monitoring"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Endorsements in Multi-Chain Architecture, Layer 2 Solutions, Solana Development, and Cross-Chain Protocols",
        "strength": 0.4,
        "maps_to": [
          "blockchain_networks.evm_based_chains_ethereum_polygon",
          "blockchain_networks.testnets_faucets_rpc_providers",
          "blockchain_networks.block_explorers_network_monitoring",
          "blockchain_networks.l2_rollups_arbitrum_optimism_base",
          "blockchain_networks.solana_sealevel_architecture",
          "blockchain_networks.cross_chain_bridges_relayers",
          "blockchain_networks.interoperability_protocols_ccip_ibc",
          "blockchain_networks.alt_vm_chains_move_tvm_wasm",
          "blockchain_networks.modular_blockchains_celestia_avail"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive multi-chain networks assessment covering OP Stack rollups, Solana Sealevel, CCIP cross-chain messaging, and Celestia modular DA",
        "strength": 1.0,
        "maps_to": [
          "blockchain_networks.evm_based_chains_ethereum_polygon",
          "blockchain_networks.testnets_faucets_rpc_providers",
          "blockchain_networks.block_explorers_network_monitoring",
          "blockchain_networks.l2_rollups_arbitrum_optimism_base",
          "blockchain_networks.solana_sealevel_architecture",
          "blockchain_networks.cross_chain_bridges_relayers",
          "blockchain_networks.interoperability_protocols_ccip_ibc",
          "blockchain_networks.alt_vm_chains_move_tvm_wasm",
          "blockchain_networks.modular_blockchains_celestia_avail"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "evm_based_chains_ethereum_polygon",
        "testnets_faucets_rpc_providers",
        "block_explorers_network_monitoring"
      ],
      "description": "Configures RPC providers for EVM networks, uses testnet faucets, and inspects transactions on block explorers."
    },
    "mid": {
      "expected_subskills": [
        "l2_rollups_arbitrum_optimism_base",
        "solana_sealevel_architecture",
        "cross_chain_bridges_relayers"
      ],
      "description": "Deploys onto OP Stack/Arbitrum rollups, builds programs on Solana runtime, and configures bridge relay mechanisms."
    },
    "senior": {
      "expected_subskills": [
        "interoperability_protocols_ccip_ibc",
        "alt_vm_chains_move_tvm_wasm",
        "modular_blockchains_celestia_avail"
      ],
      "description": "Architects cross-chain messaging with CCIP/IBC, develops on Move/Alt-VM platforms, and designs modular Celestia/EigenDA stacks."
    }
  }
}

# 4. blockchain_scaling
skills["blockchain_scaling"] = {
  "skill_id": "blockchain_scaling",
  "name": "Layer 2 Scaling & Rollup Architecture",
  "category": "blockchain_scaling",
  "description": "Scalability techniques including state channels, Optimistic Rollups (fraud proofs), ZK Rollups (validity proofs), Validium, Proto-Danksharding (EIP-4844), zkEVM circuits, and parallel execution.",
  "subskills": [
    {
      "id": "state_and_payment_channels",
      "name": "State Channels & Payment Channel Networks",
      "description": "Off-chain transaction channels (Bitcoin Lightning Network, Raiden), opening/closing state transactions, dispute periods, and multi-hop routing.",
      "keywords": ["state channel", "payment channel", "Lightning Network", "dispute window", "HTLC", "off-chain state", "channel closing"]
    },
    {
      "id": "data_availability_basics",
      "name": "Data Availability & CallData Optimization",
      "description": "Data availability problem, calldata cost mechanics in rollups, compression algorithms, and zero-byte calldata optimization.",
      "keywords": ["data availability", "calldata cost", "calldata compression", "zero byte optimization", "DA problem", "rollup batching"]
    },
    {
      "id": "gas_optimization_fundamentals",
      "name": "Gas Profiling & Execution Cost Fundamentals",
      "description": "EVM opcodes gas costs, storage vs memory allocation, warm vs cold storage reads (EIP-2929), and gas profiling techniques.",
      "keywords": ["gas cost", "EVM opcodes", "SLOAD", "SSTORE", "EIP-2929", "gas profiling", "cold read", "warm storage"]
    },
    {
      "id": "optimistic_rollups_fraud_proofs",
      "name": "Optimistic Rollups & Interactive Fraud Proofs",
      "description": "Optimistic execution model, single-round vs multi-round interactive fraud proofs (Arbitrum BOLD, Cannon), and 7-day challenge periods.",
      "keywords": ["Optimistic Rollup", "fraud proof", "fault proof", "challenge window", "7-day withdrawal", "sequencer", "Cannon", "BOLD"]
    },
    {
      "id": "zk_rollups_validity_proofs",
      "name": "ZK-Rollups & Validity Proof Verification",
      "description": "ZK-Rollup architecture (Starknet, zkSync Era, Scroll, Linea), off-chain state transition proving, on-chain verification, and instant finality.",
      "keywords": ["ZK-Rollup", "validity proof", "zkSync Era", "Starknet", "Scroll", "instant finality", "verifier contract", "prover network"]
    },
    {
      "id": "validium_and_sidechains",
      "name": "Validium, Volition & Sidechain Architectures",
      "description": "Validium architectures (off-chain DA with validity proofs), Data Availability Committees (DACs), Volition hybrid models, and autonomous sidechains.",
      "keywords": ["Validium", "Volition", "DAC", "Data Availability Committee", "sidechain", "Polygon CDK", "hybrid scaling"]
    },
    {
      "id": "proto_danksharding_eip4844",
      "name": "Proto-Danksharding & Blob-Carrying Transactions (EIP-4844)",
      "description": "EIP-4844 blob-carrying transactions, KZG polynomial commitments, temporary blob storage lifespan, and decoupled blob gas market.",
      "keywords": ["EIP-4844", "Proto-Danksharding", "blob transaction", "KZG commitment", "blob gas", "data blobs", "point evaluation precompile"]
    },
    {
      "id": "zk_evm_architecture_circuits",
      "name": "zkEVM Architecture & Types (Type 1 to Type 4)",
      "description": "Vitalik's zkEVM classification (Type 1 Ethereum-equivalent to Type 4 high-level-language-equivalent), polynomial arithmetic, and circuit efficiency tradeoffs.",
      "keywords": ["zkEVM", "Type 1 zkEVM", "Type 2 zkEVM", "Type 4 zkEVM", "zk circuit", "opcode translation", "prover latency"]
    },
    {
      "id": "sharding_and_parallel_execution",
      "name": "Danksharding & Parallel EVM Execution Engines",
      "description": "Full Danksharding roadmap, Monad/Sei parallel execution engines, software transactional memory (STM), and optimistic concurrency for EVM.",
      "keywords": ["Danksharding", "parallel EVM", "Monad", "Sei", "Software Transactional Memory", "optimistic concurrency", "state access conflict"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "EIP-4844 blob transaction constructors and calldata compression scripts",
        "detection": "content_analysis",
        "pattern": "maxFeePerBlobGas|blobVersionedHashes|kzg|Blob|calldataCompress",
        "strength": 0.9,
        "maps_to": [
          "blockchain_scaling.proto_danksharding_eip4844",
          "blockchain_scaling.data_availability_basics",
          "blockchain_scaling.gas_optimization_fundamentals"
        ]
      },
      {
        "signal": "Rollup deposit/withdrawal bridge contracts and fraud proof dispute game interactions",
        "detection": "content_analysis",
        "pattern": "proveFault|resolveDispute|initiateWithdrawal|finalizeWithdrawal|bridgeERC20",
        "strength": 0.85,
        "maps_to": [
          "blockchain_scaling.optimistic_rollups_fraud_proofs",
          "blockchain_scaling.state_and_payment_channels"
        ]
      },
      {
        "signal": "zkEVM verifier contracts, validity proof submissions, and Starknet/Cairo code",
        "detection": "content_analysis",
        "pattern": "verifyProof\\(|PlonkVerifier|Groth16Verifier|starknet|zksync",
        "strength": 0.9,
        "maps_to": [
          "blockchain_scaling.zk_rollups_validity_proofs",
          "blockchain_scaling.validium_and_sidechains",
          "blockchain_scaling.zk_evm_architecture_circuits",
          "blockchain_scaling.sharding_and_parallel_execution"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Optimized smart contract gas usage and integrated EIP-4844 blob-carrying transactions",
        "strength": 0.6,
        "maps_to": [
          "blockchain_scaling.gas_optimization_fundamentals",
          "blockchain_scaling.data_availability_basics",
          "blockchain_scaling.proto_danksharding_eip4844"
        ]
      },
      {
        "signal": "Architected L2 scaling strategies across Optimistic (Arbitrum/OP) and ZK (zkSync/Starknet) rollups with zkEVM circuits",
        "strength": 0.6,
        "maps_to": [
          "blockchain_scaling.optimistic_rollups_fraud_proofs",
          "blockchain_scaling.zk_rollups_validity_proofs",
          "blockchain_scaling.validium_and_sidechains",
          "blockchain_scaling.zk_evm_architecture_circuits",
          "blockchain_scaling.sharding_and_parallel_execution"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Layer 2 Scaling, ZK-Rollups, Optimistic Rollups, EIP-4844, and zkEVM Architecture",
        "strength": 0.4,
        "maps_to": [
          "blockchain_scaling.state_and_payment_channels",
          "blockchain_scaling.data_availability_basics",
          "blockchain_scaling.gas_optimization_fundamentals",
          "blockchain_scaling.optimistic_rollups_fraud_proofs",
          "blockchain_scaling.zk_rollups_validity_proofs",
          "blockchain_scaling.validium_and_sidechains",
          "blockchain_scaling.proto_danksharding_eip4844",
          "blockchain_scaling.zk_evm_architecture_circuits",
          "blockchain_scaling.sharding_and_parallel_execution"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive blockchain scaling assessment covering fraud proofs, validity proofs, EIP-4844 blob gas, zkEVM types, and parallel EVM engines",
        "strength": 1.0,
        "maps_to": [
          "blockchain_scaling.state_and_payment_channels",
          "blockchain_scaling.data_availability_basics",
          "blockchain_scaling.gas_optimization_fundamentals",
          "blockchain_scaling.optimistic_rollups_fraud_proofs",
          "blockchain_scaling.zk_rollups_validity_proofs",
          "blockchain_scaling.validium_and_sidechains",
          "blockchain_scaling.proto_danksharding_eip4844",
          "blockchain_scaling.zk_evm_architecture_circuits",
          "blockchain_scaling.sharding_and_parallel_execution"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "state_and_payment_channels",
        "data_availability_basics",
        "gas_optimization_fundamentals"
      ],
      "description": "Profiles EVM opcode gas costs, minimizes calldata footprint, and understands state channel lifecycle."
    },
    "mid": {
      "expected_subskills": [
        "optimistic_rollups_fraud_proofs",
        "zk_rollups_validity_proofs",
        "validium_and_sidechains"
      ],
      "description": "Deploys on Optimistic and ZK-Rollups, analyzes fraud/validity proof verification, and evaluates DAC validium models."
    },
    "senior": {
      "expected_subskills": [
        "proto_danksharding_eip4844",
        "zk_evm_architecture_circuits",
        "sharding_and_parallel_execution"
      ],
      "description": "Architects EIP-4844 blob-carrying transactions, evaluates zkEVM circuit tradeoffs, and designs parallel execution strategies."
    }
  }
}

# 5. blockchain_security
skills["blockchain_security"] = {
  "skill_id": "blockchain_security",
  "name": "Smart Contract Security & Vulnerability Auditing",
  "category": "blockchain_security",
  "description": "Auditing smart contracts against common threat vectors (reentrancy, oracle manipulation, frontrunning), utilizing static analysis tools (Slither), fuzz testing (Echidna), symbolic execution (Manticore), and OpenZeppelin security standards.",
  "subskills": [
    {
      "id": "common_threat_vectors",
      "name": "Common Smart Contract Vulnerabilities (OWASP Top 10)",
      "description": "Reentrancy, integer overflow/underflow, access control bypass (tx.origin), signature replay, denial of service, and uninitialized proxies.",
      "keywords": ["reentrancy", "Checks-Effects-Interactions", "tx.origin", "access control", "integer overflow", "uninitialized proxy", "replay attack"]
    },
    {
      "id": "openzeppelin_security_contracts",
      "name": "OpenZeppelin Security Architecture & Contracts",
      "description": "Leveraging audited security building blocks: ReentrancyGuard, Ownable2Step, AccessControl, Pausable, and SafeERC20.",
      "keywords": ["OpenZeppelin", "ReentrancyGuard", "Ownable2Step", "AccessControl", "Pausable", "SafeERC20", "ECDSA library"]
    },
    {
      "id": "version_control_smart_contracts",
      "name": "Security-Conscious Solidity Pragma & Compiler Versioning",
      "description": "Managing compiler versions, strict pragma locking, floating pragma risks, and compiler bug advisories.",
      "keywords": ["pragma solidity", "locked pragma", "compiler bugs", "SafeMath", "Solidity 0.8.x", "overflow checks"]
    },
    {
      "id": "slither_static_analysis",
      "name": "Static Analysis with Slither",
      "description": "Configuring and running Slither static analyzer, writing custom Slither detectors, and interpreting control flow graphs (CFG).",
      "keywords": ["Slither", "static analysis", "detector", "Slither CFG", "crytic-compile", "vulnerability scan", "automated security"]
    },
    {
      "id": "randomness_attacks_frontrunning",
      "name": "MEV, Frontrunning & Randomness Exploits",
      "description": "Miner/Maximal Extractable Value (MEV), sandwich attacks, block timestamp manipulation, on-chain pseudo-randomness exploits, and commit-reveal schemes.",
      "keywords": ["MEV", "frontrunning", "sandwich attack", "block.timestamp", "pseudo-randomness", "commit-reveal", "private mempools", "Flashbots"]
    },
    {
      "id": "fuzz_testing_unit_security",
      "name": "Property-Based Unit Fuzzing in Foundry",
      "description": "Writing stateless and stateful property-based fuzz tests in Foundry (vm.assume, fuzz runs, bound functions, invariant testing).",
      "keywords": ["Foundry fuzzing", "property-based testing", "vm.assume", "invariant", "stateless fuzzing", "fuzz runs", "bound()"]
    },
    {
      "id": "echidna_property_testing",
      "name": "Advanced Invariant Fuzzing with Echidna",
      "description": "Configuring Echidna property-based fuzzer, defining contract invariants in Solidity, corpus generation, and automated break testing.",
      "keywords": ["Echidna", "property testing", "invariant", "echidna_config.yaml", "assertion mode", "corpus generation", "crytic"]
    },
    {
      "id": "manticore_symbolic_execution",
      "name": "Symbolic Execution with Manticore",
      "description": "Applying symbolic execution to explore all reachable program paths, generate constraint models (Z3 solver), and prove invariant validity.",
      "keywords": ["Manticore", "symbolic execution", "Z3 solver", "path exploration", "constraint solving", "formal reachability"]
    },
    {
      "id": "mythx_formal_audit_workflows",
      "name": "Professional Security Auditing & Threat Modeling",
      "description": "Conducting manual audits, threat modeling, writing comprehensive audit reports, calculating CVSS scores, and managing remediations.",
      "keywords": ["security audit", "threat modeling", "audit report", "CVSS score", "MythX", "remediation verification", "competitive audits", "Code4rena"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Slither configs, Echidna invariant test files, and custom security modifiers",
        "detection": "file_presence",
        "pattern": "slither\\.config\\.json|echidna.*\\.ya?ml|test/invariants/.*\\.sol|test/fuzz/.*\\.sol",
        "strength": 0.9,
        "maps_to": [
          "blockchain_security.slither_static_analysis",
          "blockchain_security.echidna_property_testing",
          "blockchain_security.fuzz_testing_unit_security"
        ]
      },
      {
        "signal": "OpenZeppelin ReentrancyGuard, Ownable2Step, and SafeERC20 inheritance",
        "detection": "content_analysis",
        "pattern": "import\\s+['\"].*openzeppelin/contracts/security/ReentrancyGuard|import\\s+['\"].*openzeppelin/contracts/access/Ownable2Step|nonReentrant",
        "strength": 0.85,
        "maps_to": [
          "blockchain_security.openzeppelin_security_contracts",
          "blockchain_security.common_threat_vectors",
          "blockchain_security.version_control_smart_contracts"
        ]
      },
      {
        "signal": "Flashbots RPC configs, commit-reveal contracts, and Manticore symbolic scripts",
        "detection": "content_analysis",
        "pattern": "flashbots|relay\\.flashbots\\.net|commitHash|Manticore\\(|manticore\\.ethereum",
        "strength": 0.9,
        "maps_to": [
          "blockchain_security.randomness_attacks_frontrunning",
          "blockchain_security.manticore_symbolic_execution",
          "blockchain_security.mythx_formal_audit_workflows"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Conducted smart contract security audits and resolved critical reentrancy and access control vulnerabilities",
        "strength": 0.6,
        "maps_to": [
          "blockchain_security.common_threat_vectors",
          "blockchain_security.openzeppelin_security_contracts",
          "blockchain_security.version_control_smart_contracts",
          "blockchain_security.slither_static_analysis"
        ]
      },
      {
        "signal": "Built invariant fuzzing suites with Echidna/Foundry and performed symbolic execution with Manticore on top DeFi protocols",
        "strength": 0.6,
        "maps_to": [
          "blockchain_security.fuzz_testing_unit_security",
          "blockchain_security.echidna_property_testing",
          "blockchain_security.manticore_symbolic_execution",
          "blockchain_security.randomness_attacks_frontrunning",
          "blockchain_security.mythx_formal_audit_workflows"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Certified Smart Contract Security Auditor, Code4rena / Sherlock contest competitor",
        "strength": 0.4,
        "maps_to": [
          "blockchain_security.common_threat_vectors",
          "blockchain_security.openzeppelin_security_contracts",
          "blockchain_security.version_control_smart_contracts",
          "blockchain_security.slither_static_analysis",
          "blockchain_security.randomness_attacks_frontrunning",
          "blockchain_security.fuzz_testing_unit_security",
          "blockchain_security.echidna_property_testing",
          "blockchain_security.manticore_symbolic_execution",
          "blockchain_security.mythx_formal_audit_workflows"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive smart contract security assessment covering reentrancy, MEV defense, Echidna invariant fuzzing, Slither CFG, and formal verification",
        "strength": 1.0,
        "maps_to": [
          "blockchain_security.common_threat_vectors",
          "blockchain_security.openzeppelin_security_contracts",
          "blockchain_security.version_control_smart_contracts",
          "blockchain_security.slither_static_analysis",
          "blockchain_security.randomness_attacks_frontrunning",
          "blockchain_security.fuzz_testing_unit_security",
          "blockchain_security.echidna_property_testing",
          "blockchain_security.manticore_symbolic_execution",
          "blockchain_security.mythx_formal_audit_workflows"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "common_threat_vectors",
        "openzeppelin_security_contracts",
        "version_control_smart_contracts"
      ],
      "description": "Identifies common OWASP smart contract vulnerabilities (reentrancy, access control) and integrates OpenZeppelin security contracts."
    },
    "mid": {
      "expected_subskills": [
        "slither_static_analysis",
        "randomness_attacks_frontrunning",
        "fuzz_testing_unit_security"
      ],
      "description": "Runs Slither static analysis, mitigates MEV frontrunning and on-chain randomness risks, and writes property fuzz tests in Foundry."
    },
    "senior": {
      "expected_subskills": [
        "echidna_property_testing",
        "manticore_symbolic_execution",
        "mythx_formal_audit_workflows"
      ],
      "description": "Authors mathematical invariant test suites with Echidna, executes Manticore symbolic verification, and leads professional protocol audit reviews."
    }
  }
}

# 6. dapp_development
skills["dapp_development"] = {
  "skill_id": "dapp_development",
  "name": "Full-Stack DApp Development & Web3 Integration",
  "category": "dapp_development",
  "description": "Building full-stack decentralized applications: Web3 wallet connections (Wagmi, RainbowKit), DeFi protocol integrations (Uniswap, Aave), NFT standards, DAO governance, decentralized indexers (The Graph), and ERC-4337 Account Abstraction.",
  "subskills": [
    {
      "id": "web3_wallet_integration_wagmi_ethers",
      "name": "Web3 Wallet Connectors (Wagmi, Viem, RainbowKit)",
      "description": "Integrating browser wallets (MetaMask, Coinbase Wallet, WalletConnect), handling chain switching, signature requests, and reactive contract hooks.",
      "keywords": ["Wagmi", "Viem", "RainbowKit", "WalletConnect", "MetaMask", "useAccount", "useConnect", "signMessage"]
    },
    {
      "id": "frontend_dapp_frameworks",
      "name": "Frontend DApp Frameworks & State Architecture",
      "description": "Building responsive DApps with Next.js/React, handling asynchronous blockchain latency, optimistic UI updates, and transaction toast notifications.",
      "keywords": ["Next.js", "React", "optimistic UI", "transaction toast", "useWaitForTransactionReceipt", "DApp frontend", "Web3 UI"]
    },
    {
      "id": "node_as_a_service_rpc_infura_alchemy",
      "name": "RPC Infrastructure & WebSocket Event Subscriptions",
      "description": "Connecting to node infrastructure (Alchemy, Infura, QuickNode), managing WebSocket subscriptions (`eth_subscribe`), and batching JSON-RPC requests.",
      "keywords": ["Alchemy", "Infura", "WebSocket", "eth_subscribe", "JSON-RPC batching", "RPC rate limits", "live event feed"]
    },
    {
      "id": "defi_protocols_integration_uniswap_aave",
      "name": "DeFi Protocol Integrations (Uniswap, Aave, Curve)",
      "description": "Integrating with decentralized exchanges (Uniswap v2/v3/v4 routers, flash swaps) and lending protocols (Aave v3 flash loans, aTokens, collateral health factors).",
      "keywords": ["Uniswap Router", "Aave v3", "flash loan", "liquidity pool", "exactInputSingle", "health factor", "Curve Finance", "DeFi integration"]
    },
    {
      "id": "nft_standards_metadata_ipfs",
      "name": "NFT Minting, IPFS Metadata & Marketplaces",
      "description": "Decentralized metadata storage (IPFS, Arweave), ERC-721/ERC-1155 minting dapps, royalties (ERC-2981), and OpenSea/Reservoir API integrations.",
      "keywords": ["ERC-721", "ERC-1155", "IPFS", "Arweave", "tokenURI", "ERC-2981 royalty", "NFT minting DApp", "Pinata"]
    },
    {
      "id": "dao_governance_voting_snapshot",
      "name": "DAO Governance, Multi-Sig & Off-Chain Voting",
      "description": "Integrating on-chain Governor contracts (Compound Governor Bravo, OpenZeppelin Governor), Safe (Gnosis Safe) multi-sig transactions, and off-chain Snapshot gasless voting.",
      "keywords": ["DAO governance", "Governor Bravo", "Snapshot", "Gnosis Safe", "Safe Apps SDK", "gasless voting", "delegation"]
    },
    {
      "id": "full_node_client_rpc_architecture",
      "name": "Self-Hosted Full Nodes & Client Architecture (Geth, Reth)",
      "description": "Running and maintaining Ethereum execution clients (Geth, Nethermind, Reth, Besu) and consensus clients (Lighthouse, Prysm) for high-throughput RPC clusters.",
      "keywords": ["Geth", "Reth", "Nethermind", "Lighthouse", "Prysm", "Execution Client", "Consensus Client", "self-hosted node", "Engine API"]
    },
    {
      "id": "indexer_subgraphs_the_graph_envio",
      "name": "Decentralized Indexing & Subgraphs (The Graph, Envio)",
      "description": "Authoring custom GraphQL subgraphs with The Graph (AssemblyScript mapping handlers, entity schemas) and Envio hyper-indexers for fast querying.",
      "keywords": ["The Graph", "subgraph.yaml", "schema.graphql", "AssemblyScript mapping", "Envio", "GraphQL", "blockchain indexing", "Goldsky"]
    },
    {
      "id": "account_abstraction_erc4337_bundlers",
      "name": "ERC-4337 Account Abstraction & Paymasters",
      "description": "ERC-4337 smart accounts: UserOperations, EntryPoint contract mechanics, Bundlers (Alto, Rundler), Paymasters (gas sponsorship in ERC-20), and Session Keys (Passkeys).",
      "keywords": ["ERC-4337", "Account Abstraction", "UserOperation", "EntryPoint", "Paymaster", "Bundler", "Passkeys", "gas sponsorship", "Biconomy", "ZeroDev"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Wagmi, Viem, and RainbowKit configuration and custom Web3 hooks",
        "detection": "content_analysis",
        "pattern": "createConfig\\(|createPublicClient\\(|http\\(\\)|@rainbow-me/rainbowkit|wagmi",
        "strength": 0.85,
        "maps_to": [
          "dapp_development.web3_wallet_integration_wagmi_ethers",
          "dapp_development.frontend_dapp_frameworks",
          "dapp_development.node_as_a_service_rpc_infura_alchemy"
        ]
      },
      {
        "signal": "The Graph subgraph definitions, schema.graphql, and AssemblyScript handlers",
        "detection": "file_presence",
        "pattern": "subgraph\\.ya?ml|schema\\.graphql|src/mapping\\.ts",
        "strength": 0.9,
        "maps_to": [
          "dapp_development.indexer_subgraphs_the_graph_envio"
        ]
      },
      {
        "signal": "Uniswap/Aave integrations, NFT IPFS minting, Safe transactions, and ERC-4337 UserOperations",
        "detection": "content_analysis",
        "pattern": "ISwapRouter|IPoolAddressesProvider|pinata\\.pinJSONToIPFS|SafeAppsSDK|getUserOperationHash|SimpleAccountFactory",
        "strength": 0.9,
        "maps_to": [
          "dapp_development.defi_protocols_integration_uniswap_aave",
          "dapp_development.nft_standards_metadata_ipfs",
          "dapp_development.dao_governance_voting_snapshot",
          "dapp_development.full_node_client_rpc_architecture",
          "dapp_development.account_abstraction_erc4337_bundlers"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Built responsive full-stack Web3 applications with Next.js, Wagmi, Viem, and Uniswap/Aave protocol integrations",
        "strength": 0.6,
        "maps_to": [
          "dapp_development.web3_wallet_integration_wagmi_ethers",
          "dapp_development.frontend_dapp_frameworks",
          "dapp_development.node_as_a_service_rpc_infura_alchemy",
          "dapp_development.defi_protocols_integration_uniswap_aave"
        ]
      },
      {
        "signal": "Engineered custom GraphQL subgraphs with The Graph and implemented ERC-4337 Account Abstraction paymaster gas sponsorship",
        "strength": 0.6,
        "maps_to": [
          "dapp_development.indexer_subgraphs_the_graph_envio",
          "dapp_development.account_abstraction_erc4337_bundlers",
          "dapp_development.nft_standards_metadata_ipfs",
          "dapp_development.dao_governance_voting_snapshot",
          "dapp_development.full_node_client_rpc_architecture"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Full-Stack DApp Engineering, Web3 UI/UX, The Graph Subgraphs, and Account Abstraction (ERC-4337)",
        "strength": 0.4,
        "maps_to": [
          "dapp_development.web3_wallet_integration_wagmi_ethers",
          "dapp_development.frontend_dapp_frameworks",
          "dapp_development.node_as_a_service_rpc_infura_alchemy",
          "dapp_development.defi_protocols_integration_uniswap_aave",
          "dapp_development.nft_standards_metadata_ipfs",
          "dapp_development.dao_governance_voting_snapshot",
          "dapp_development.full_node_client_rpc_architecture",
          "dapp_development.indexer_subgraphs_the_graph_envio",
          "dapp_development.account_abstraction_erc4337_bundlers"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes full-stack DApp development assessment covering Wagmi hooks, Uniswap flash swaps, The Graph schema design, and ERC-4337 Paymasters",
        "strength": 1.0,
        "maps_to": [
          "dapp_development.web3_wallet_integration_wagmi_ethers",
          "dapp_development.frontend_dapp_frameworks",
          "dapp_development.node_as_a_service_rpc_infura_alchemy",
          "dapp_development.defi_protocols_integration_uniswap_aave",
          "dapp_development.nft_standards_metadata_ipfs",
          "dapp_development.dao_governance_voting_snapshot",
          "dapp_development.full_node_client_rpc_architecture",
          "dapp_development.indexer_subgraphs_the_graph_envio",
          "dapp_development.account_abstraction_erc4337_bundlers"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "web3_wallet_integration_wagmi_ethers",
        "frontend_dapp_frameworks",
        "node_as_a_service_rpc_infura_alchemy"
      ],
      "description": "Integrates browser wallets via Wagmi/RainbowKit, builds reactive Next.js frontends, and connects to Alchemy/Infura RPCs."
    },
    "mid": {
      "expected_subskills": [
        "defi_protocols_integration_uniswap_aave",
        "nft_standards_metadata_ipfs",
        "dao_governance_voting_snapshot"
      ],
      "description": "Integrates Uniswap routers, handles IPFS NFT metadata pinning, and coordinates Gnosis Safe/Snapshot governance."
    },
    "senior": {
      "expected_subskills": [
        "full_node_client_rpc_architecture",
        "indexer_subgraphs_the_graph_envio",
        "account_abstraction_erc4337_bundlers"
      ],
      "description": "Architects custom GraphQL indexing subgraphs, configures high-throughput execution clients, and deploys ERC-4337 smart accounts."
    }
  }
}

# 7. smart_contract_development (11 subskills, absorbs Oracle ecosystem cleanly)
skills["smart_contract_development"] = {
  "skill_id": "smart_contract_development",
  "name": "Smart Contract Architecture & Engineering",
  "category": "smart_contracts",
  "description": "End-to-end smart contract development in Solidity/Vyper/Rust: ERC token standards, testing frameworks, proxy upgrade patterns, Yul inline assembly, Chainlink Data Feeds / VRF randomness, Chainlink Functions / Automation, and formal verification.",
  "subskills": [
    {
      "id": "solidity_core_and_advanced_syntax",
      "name": "Solidity Core & Advanced Syntax",
      "description": "Solidity object-oriented patterns, custom errors, storage layouts, function visibility, immutability, constant caching, and events.",
      "keywords": ["Solidity", "custom errors", "storage layout", "memory vs storage", "immutable", "constant", "events", "function modifiers"]
    },
    {
      "id": "erc_token_standards_20_721_1155",
      "name": "ERC Standards Implementation (ERC-20, 721, 1155, 4626)",
      "description": "Authoring compliant ERC-20 fungible tokens, ERC-721/1155 non-fungible tokens, and ERC-4626 Tokenized Vault standard.",
      "keywords": ["ERC-20", "ERC-721", "ERC-1155", "ERC-4626", "tokenized vault", "transferFrom", "permit ERC-2612", "allowance"]
    },
    {
      "id": "contract_unit_and_integration_testing",
      "name": "Contract Unit & Fork Testing (Foundry / Hardhat)",
      "description": "Writing test suites in Solidity (Foundry `forge test`) and TypeScript, mainnet forking, time travel (`vm.warp`), and address prank simulation (`vm.prank`).",
      "keywords": ["Foundry", "forge test", "vm.prank", "vm.warp", "vm.roll", "fork testing", "unit tests", "integration tests"]
    },
    {
      "id": "contract_deployment_and_verification",
      "name": "Contract Deployment & Multi-Chain Verification",
      "description": "Deterministic deployments with CREATE2 (`CREATE2` factory, salt mining), constructor initialization, and programmatic verification across block explorers.",
      "keywords": ["CREATE2", "deterministic deployment", "forge script", "salt mining", "constructor", "bytecode verification", "Etherscan API"]
    },
    {
      "id": "oracle_data_feeds_and_vrf_randomness",
      "name": "Oracle Data Feeds & Verifiable Randomness (Chainlink, Pyth)",
      "description": "Integrating Chainlink Price Feeds (AggregatorV3Interface, heartbeat, deviation threshold), Pyth Network real-time prices, and Chainlink VRF v2.5 for provably fair randomness.",
      "keywords": ["Chainlink Data Feeds", "AggregatorV3Interface", "Chainlink VRF", "VRFConsumerBaseV2", "Pyth Network", "verifiable randomness", "stale price check"]
    },
    {
      "id": "upgradeable_contracts_proxy_patterns",
      "name": "Upgradeable Smart Contracts & Proxy Patterns",
      "description": "Architecting upgradeability: Transparent Proxy, Universal Upgradeable Proxy Standard (UUPS - ERC-1822), Beacon Proxies, and Diamond Multi-Facet Proxy (ERC-2535).",
      "keywords": ["UUPS", "Transparent Proxy", "Diamond Pattern", "ERC-2535", "ERC-1967", "storage collision", "delegatecall", "initializer"]
    },
    {
      "id": "vyper_and_alternative_smart_contract_languages",
      "name": "Vyper & Alternative Smart Contract Languages",
      "description": "Writing secure Pythonic smart contracts in Vyper, understanding syntax differences, elimination of recursion/infinite loops, and gas optimizations in Curve contracts.",
      "keywords": ["Vyper", "Pythonic smart contracts", "no recursion", "Curve Finance", "vyper compiler", "fixed point decimals"]
    },
    {
      "id": "gas_optimization_assembly_yul",
      "name": "Inline Assembly & Yul Gas Optimization",
      "description": "Writing inline assembly (Yul) in Solidity: custom memory pointers, bitwise shifts, custom storage slot access (`sload`/`sstore`), and bypass of compiler overhead.",
      "keywords": ["Yul", "inline assembly", "mload", "mstore", "sload", "sstore", "gas optimization", "bitwise operations", "Solady"]
    },
    {
      "id": "rust_smart_contracts_solana_near",
      "name": "Rust Smart Contracts (Solana Anchor & NEAR)",
      "description": "Writing Rust smart contracts using Anchor framework on Solana (Accounts validation struct, instructions, cross-program invocations - CPI) and NEAR SDK.",
      "keywords": ["Rust smart contract", "Anchor framework", "Solana", "CPI", "AccountInfo", "Context", "NEAR SDK", "Borsh serialization"]
    },
    {
      "id": "hybrid_smart_contracts_offchain_computation",
      "name": "Hybrid Smart Contracts & Off-Chain Automation",
      "description": "Chainlink Functions for fetching arbitrary Web2 APIs with consensus, Chainlink Automation (Keepers) for autonomous cron execution, and Decentralized Oracle Networks.",
      "keywords": ["hybrid smart contract", "Chainlink Functions", "Chainlink Automation", "Keepers", "DON", "checkUpkeep", "performUpkeep", "Web2 API oracle"]
    },
    {
      "id": "formal_verification_and_invariant_testing",
      "name": "Formal Verification & Mathematical Invariants",
      "description": "Proving correctness with formal verification tools (Certora Prover, Halmos, SMTChecker), defining rules/invariants in CVL (Certora Verification Language).",
      "keywords": ["formal verification", "Certora", "CVL", "Halmos", "SMTChecker", "mathematical proof", "state space exploration", "invariant rule"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Solidity/Vyper contract files, ERC-20/721/1155/4626 implementations, and Foundry tests",
        "detection": "file_presence",
        "pattern": "contracts/.*\\.sol|src/.*\\.sol|contracts/.*\\.vy|test/.*\\.t\\.sol",
        "strength": 0.95,
        "maps_to": [
          "smart_contract_development.solidity_core_and_advanced_syntax",
          "smart_contract_development.erc_token_standards_20_721_1155",
          "smart_contract_development.contract_unit_and_integration_testing",
          "smart_contract_development.contract_deployment_and_verification",
          "smart_contract_development.vyper_and_alternative_smart_contract_languages"
        ]
      },
      {
        "signal": "Chainlink Price Feed AggregatorV3, VRFConsumerBase, Automation, and Functions imports",
        "detection": "content_analysis",
        "pattern": "AggregatorV3Interface|VRFConsumerBaseV2|FunctionsClient|AutomationCompatible|checkUpkeep|fulfillRandomWords",
        "strength": 0.9,
        "maps_to": [
          "smart_contract_development.oracle_data_feeds_and_vrf_randomness",
          "smart_contract_development.hybrid_smart_contracts_offchain_computation"
        ]
      },
      {
        "signal": "UUPS proxy patterns, Yul inline assembly blocks, Solana Anchor programs, and Certora specs",
        "detection": "content_analysis",
        "pattern": "UUPSUpgradeable|ERC1967Proxy|assembly\\s*\\{|anchor_lang|#[account]|certora/.*\\.spec|rule\\s+[A-Za-z0-9_]+",
        "strength": 0.9,
        "maps_to": [
          "smart_contract_development.upgradeable_contracts_proxy_patterns",
          "smart_contract_development.gas_optimization_assembly_yul",
          "smart_contract_development.rust_smart_contracts_solana_near",
          "smart_contract_development.formal_verification_and_invariant_testing"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Developed and deployed production ERC-20/721/4626 smart contracts in Solidity with Foundry unit/fork testing",
        "strength": 0.6,
        "maps_to": [
          "smart_contract_development.solidity_core_and_advanced_syntax",
          "smart_contract_development.erc_token_standards_20_721_1155",
          "smart_contract_development.contract_unit_and_integration_testing",
          "smart_contract_development.contract_deployment_and_verification"
        ]
      },
      {
        "signal": "Integrated Chainlink Price Feeds & VRF randomness, built UUPS upgradeable proxies, and optimized gas with inline Yul assembly",
        "strength": 0.6,
        "maps_to": [
          "smart_contract_development.oracle_data_feeds_and_vrf_randomness",
          "smart_contract_development.upgradeable_contracts_proxy_patterns",
          "smart_contract_development.gas_optimization_assembly_yul",
          "smart_contract_development.hybrid_smart_contracts_offchain_computation"
        ]
      },
      {
        "signal": "Built Solana smart contracts in Rust (Anchor) and conducted formal verification using Certora Prover",
        "strength": 0.6,
        "maps_to": [
          "smart_contract_development.rust_smart_contracts_solana_near",
          "smart_contract_development.formal_verification_and_invariant_testing",
          "smart_contract_development.vyper_and_alternative_smart_contract_languages"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Recognized for Solidity Architecture, Smart Contract Engineering, Yul Optimization, and Oracle Integrations",
        "strength": 0.4,
        "maps_to": [
          "smart_contract_development.solidity_core_and_advanced_syntax",
          "smart_contract_development.erc_token_standards_20_721_1155",
          "smart_contract_development.contract_unit_and_integration_testing",
          "smart_contract_development.contract_deployment_and_verification",
          "smart_contract_development.oracle_data_feeds_and_vrf_randomness",
          "smart_contract_development.upgradeable_contracts_proxy_patterns",
          "smart_contract_development.vyper_and_alternative_smart_contract_languages",
          "smart_contract_development.gas_optimization_assembly_yul",
          "smart_contract_development.rust_smart_contracts_solana_near",
          "smart_contract_development.hybrid_smart_contracts_offchain_computation",
          "smart_contract_development.formal_verification_and_invariant_testing"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes comprehensive smart contract architecture assessment covering ERC-4626 vaults, Chainlink VRF integration, UUPS proxies, Yul assembly, and Certora formal proofs",
        "strength": 1.0,
        "maps_to": [
          "smart_contract_development.solidity_core_and_advanced_syntax",
          "smart_contract_development.erc_token_standards_20_721_1155",
          "smart_contract_development.contract_unit_and_integration_testing",
          "smart_contract_development.contract_deployment_and_verification",
          "smart_contract_development.oracle_data_feeds_and_vrf_randomness",
          "smart_contract_development.upgradeable_contracts_proxy_patterns",
          "smart_contract_development.vyper_and_alternative_smart_contract_languages",
          "smart_contract_development.gas_optimization_assembly_yul",
          "smart_contract_development.rust_smart_contracts_solana_near",
          "smart_contract_development.hybrid_smart_contracts_offchain_computation",
          "smart_contract_development.formal_verification_and_invariant_testing"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "solidity_core_and_advanced_syntax",
        "erc_token_standards_20_721_1155",
        "contract_unit_and_integration_testing",
        "contract_deployment_and_verification"
      ],
      "description": "Writes production Solidity, implements standard ERC token interfaces, tests with Foundry, and executes deployment scripts."
    },
    "mid": {
      "expected_subskills": [
        "oracle_data_feeds_and_vrf_randomness",
        "upgradeable_contracts_proxy_patterns",
        "vyper_and_alternative_smart_contract_languages",
        "gas_optimization_assembly_yul"
      ],
      "description": "Integrates Chainlink Data Feeds and VRF randomness, builds UUPS proxy architectures, and writes custom Yul assembly for gas reduction."
    },
    "senior": {
      "expected_subskills": [
        "rust_smart_contracts_solana_near",
        "hybrid_smart_contracts_offchain_computation",
        "formal_verification_and_invariant_testing"
      ],
      "description": "Develops Rust programs on Solana/Anchor, orchestrates hybrid smart contract automation with Chainlink Functions, and proves invariants via Certora."
    }
  }
}

# 8. smart_contract_tooling
skills["smart_contract_tooling"] = {
  "skill_id": "smart_contract_tooling",
  "name": "Smart Contract Tooling, Testing & DevOps",
  "category": "blockchain_tooling",
  "description": "Development environments, local testnets, and CI/CD automation: Foundry (Forge/Cast/Anvil), Hardhat, Tenderly debuggers, decentralized storage (IPFS/Arweave), and automated fuzz testing tools.",
  "subskills": [
    {
      "id": "hardhat_framework_plugins",
      "name": "Hardhat Development Environment & Plugins",
      "description": "Configuring Hardhat (`hardhat.config.ts`), Hardhat Network, typechain bindings, hardhat-deploy, and custom TypeScript tasks.",
      "keywords": ["Hardhat", "hardhat.config.ts", "typechain", "hardhat-deploy", "Hardhat Network", "npx hardhat", "TypeScript tasks"]
    },
    {
      "id": "foundry_forge_cast_anvil",
      "name": "Foundry Toolchain (Forge, Cast, Anvil)",
      "description": "High-performance Rust-based Ethereum toolkit: fast compiling (`forge build`), script deployments (`forge script`), RPC queries (`cast`), and local node (`anvil`).",
      "keywords": ["Foundry", "forge", "cast", "anvil", "foundry.toml", "forge test", "cast call", "cast send"]
    },
    {
      "id": "crypto_wallets_development_faucets",
      "name": "Developer Wallets & Testnet Tooling",
      "description": "Managing programmatic signer wallets, private keys in `.env`, mnemonic generation, faucet APIs, and test ether funding strategies.",
      "keywords": ["signer", "private key management", ".env", "faucet API", "testnet ether", "automated funding", "local accounts"]
    },
    {
      "id": "decentralized_storage_ipfs_arweave",
      "name": "Decentralized Storage Tooling (IPFS, Arweave, Filecoin)",
      "description": "Pinning services (Pinata, Web3.Storage), IPFS CLI node management, Arweave permanent storage upload tools (Irys/Bundlr), and decentralized pinning gateways.",
      "keywords": ["IPFS", "Pinata", "Arweave", "Irys", "Bundlr", "Web3.Storage", "Filecoin", "CID", "gateway"]
    },
    {
      "id": "evm_trace_debuggers_tenderly",
      "name": "EVM Execution Trace Debugging & Tenderly",
      "description": "Transaction call trace analysis, opcode-by-opcode debugging, Tenderly Virtual TestNets, simulation APIs, and revert reason decoding.",
      "keywords": ["Tenderly", "trace debugging", "transaction simulation", "revert decoder", "call trace", "Virtual TestNet", "debug_traceTransaction"]
    },
    {
      "id": "contract_verification_blockscout_etherscan",
      "name": "Automated Multi-Chain Contract Verification",
      "description": "Automated sourcify and standard-json-input verification with `forge verify-contract` and hardhat-verify across Etherscan and Blockscout APIs.",
      "keywords": ["forge verify-contract", "hardhat-verify", "sourcify", "Standard-JSON-Input", "Etherscan API", "Blockscout"]
    },
    {
      "id": "ci_cd_smart_contract_automation",
      "name": "Smart Contract CI/CD Pipelines (GitHub Actions)",
      "description": "Automated GitHub Actions workflows for building, gas snapshot regression testing (`forge snapshot`), linting (solhint, prettier), and automated PR feedback.",
      "keywords": ["GitHub Actions", "CI/CD smart contract", "forge snapshot", "solhint", "prettier-plugin-solidity", "gas regression", "automated test runner"]
    },
    {
      "id": "fuzzing_invariant_tooling_echidna_medusa",
      "name": "Fuzzing Tooling & Automated Test Orchestration (Medusa, Echidna)",
      "description": "Configuring and running modern smart contract fuzzer tools (Medusa, Echidna) in automated security regression suites.",
      "keywords": ["Medusa fuzzer", "Echidna", "automated fuzzing", "invariant runner", "security regression", "crytic-compile"]
    },
    {
      "id": "gas_profilers_snapshot_testing",
      "name": "Gas Profiling & Snapshot Regression Tooling",
      "description": "Continuous gas benchmarking using `forge snapshot --diff`, hardhat-gas-reporter, identifying opcode-level gas spikes, and gas budget gating.",
      "keywords": ["forge snapshot", "hardhat-gas-reporter", "gas benchmark", "gas regression gate", "gas report", "opcode profile"]
    }
  ],
  "evidence": {
    "github": [
      {
        "signal": "Foundry config, Hardhat config, and package.json smart contract scripts",
        "detection": "file_presence",
        "pattern": "foundry\\.toml|hardhat\\.config\\.(ts|js)|solhint\\.json",
        "strength": 0.9,
        "maps_to": [
          "smart_contract_tooling.foundry_forge_cast_anvil",
          "smart_contract_tooling.hardhat_framework_plugins",
          "smart_contract_tooling.crypto_wallets_development_faucets"
        ]
      },
      {
        "signal": "Tenderly simulation config, Pinata/Arweave pinning scripts, and verification commands",
        "detection": "content_analysis",
        "pattern": "tenderly|pinata|@irys/sdk|forge verify-contract|hardhat-verify",
        "strength": 0.85,
        "maps_to": [
          "smart_contract_tooling.evm_trace_debuggers_tenderly",
          "smart_contract_tooling.decentralized_storage_ipfs_arweave",
          "smart_contract_tooling.contract_verification_blockscout_etherscan"
        ]
      },
      {
        "signal": "GitHub Actions workflows running Forge test, Forge snapshot, Medusa, or Echidna",
        "detection": "file_presence",
        "pattern": "\\.github/workflows/*test*\\.ya?ml|\\.github/workflows/*foundry*\\.ya?ml|\\.gas-snapshot",
        "strength": 0.9,
        "maps_to": [
          "smart_contract_tooling.ci_cd_smart_contract_automation",
          "smart_contract_tooling.fuzzing_invariant_tooling_echidna_medusa",
          "smart_contract_tooling.gas_profilers_snapshot_testing"
        ]
      }
    ],
    "cv": [
      {
        "signal": "Configured Hardhat and Foundry development toolchains with automated unit testing and contract verification",
        "strength": 0.6,
        "maps_to": [
          "smart_contract_tooling.hardhat_framework_plugins",
          "smart_contract_tooling.foundry_forge_cast_anvil",
          "smart_contract_tooling.crypto_wallets_development_faucets",
          "smart_contract_tooling.contract_verification_blockscout_etherscan"
        ]
      },
      {
        "signal": "Built CI/CD automated testing pipelines with gas regression snapshots, Tenderly simulations, and IPFS pinning",
        "strength": 0.6,
        "maps_to": [
          "smart_contract_tooling.ci_cd_smart_contract_automation",
          "smart_contract_tooling.gas_profilers_snapshot_testing",
          "smart_contract_tooling.evm_trace_debuggers_tenderly",
          "smart_contract_tooling.decentralized_storage_ipfs_arweave",
          "smart_contract_tooling.fuzzing_invariant_tooling_echidna_medusa"
        ]
      }
    ],
    "linkedin": [
      {
        "signal": "Expertise in Foundry, Hardhat, Smart Contract Tooling, CI/CD Pipelines, and Tenderly Debugging",
        "strength": 0.4,
        "maps_to": [
          "smart_contract_tooling.hardhat_framework_plugins",
          "smart_contract_tooling.foundry_forge_cast_anvil",
          "smart_contract_tooling.crypto_wallets_development_faucets",
          "smart_contract_tooling.decentralized_storage_ipfs_arweave",
          "smart_contract_tooling.evm_trace_debuggers_tenderly",
          "smart_contract_tooling.contract_verification_blockscout_etherscan",
          "smart_contract_tooling.ci_cd_smart_contract_automation",
          "smart_contract_tooling.fuzzing_invariant_tooling_echidna_medusa",
          "smart_contract_tooling.gas_profilers_snapshot_testing"
        ]
      }
    ],
    "assessment": [
      {
        "signal": "Passes smart contract tooling assessment covering Foundry cheatcodes, CI/CD pipeline automation, Tenderly traces, and gas snapshot gates",
        "strength": 1.0,
        "maps_to": [
          "smart_contract_tooling.hardhat_framework_plugins",
          "smart_contract_tooling.foundry_forge_cast_anvil",
          "smart_contract_tooling.crypto_wallets_development_faucets",
          "smart_contract_tooling.decentralized_storage_ipfs_arweave",
          "smart_contract_tooling.evm_trace_debuggers_tenderly",
          "smart_contract_tooling.contract_verification_blockscout_etherscan",
          "smart_contract_tooling.ci_cd_smart_contract_automation",
          "smart_contract_tooling.fuzzing_invariant_tooling_echidna_medusa",
          "smart_contract_tooling.gas_profilers_snapshot_testing"
        ]
      }
    ]
  },
  "levels": {
    "junior": {
      "expected_subskills": [
        "hardhat_framework_plugins",
        "foundry_forge_cast_anvil",
        "crypto_wallets_development_faucets"
      ],
      "description": "Uses Foundry (forge/cast/anvil) and Hardhat for compiling, local testing, and managing dev testnet wallets."
    },
    "mid": {
      "expected_subskills": [
        "decentralized_storage_ipfs_arweave",
        "evm_trace_debuggers_tenderly",
        "contract_verification_blockscout_etherscan"
      ],
      "description": "Integrates IPFS/Arweave storage, inspects execution traces on Tenderly, and verifies contracts programmatically."
    },
    "senior": {
      "expected_subskills": [
        "ci_cd_smart_contract_automation",
        "fuzzing_invariant_tooling_echidna_medusa",
        "gas_profilers_snapshot_testing"
      ],
      "description": "Architects smart contract CI/CD pipelines in GitHub Actions, sets up gas snapshot regression gates, and integrates Medusa/Echidna fuzzer suites."
    }
  }
}

# Write all 8 skill files
for skill_id, skill_data in skills.items():
    file_path = os.path.join(skills_dir, f"{skill_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(skill_data, f, indent=2, ensure_ascii=False)
    print(f"Generated blockchain skill: {file_path}")

# ==============================================================================
# 2. BLOCKCHAIN ROLE DEFINITIONS (Junior, Mid, Senior)
# ==============================================================================
roles = {
  "junior": {
    "role_id": "blockchain_developer",
    "level": "junior",
    "title": "Junior Blockchain Developer",
    "description": "Entry-level blockchain developer focusing on foundational distributed systems, writing and unit-testing standard ERC-20/721 smart contracts in Solidity, using Foundry/Hardhat, integrating wallets via Wagmi/Viem, and testing on public testnets.",
    "experience_range": "0-2 years",
    "skills": [
      {
        "skill_id": "smart_contract_development",
        "importance": 0.95,
        "rationale": "Writing clean Solidity contracts and implementing ERC-20/721 standards is core for daily work."
      },
      {
        "skill_id": "smart_contract_tooling",
        "importance": 0.90,
        "rationale": "Using Foundry and Hardhat for compiling, testing, and script deployments."
      },
      {
        "skill_id": "dapp_development",
        "importance": 0.85,
        "rationale": "Connecting frontend DApps to Web3 wallets with Wagmi and interacting with RPCs."
      },
      {
        "skill_id": "blockchain_fundamentals",
        "importance": 0.85,
        "rationale": "Understanding the blockchain data structure, UTXO/account models, and transaction lifecycle."
      },
      {
        "skill_id": "blockchain_security",
        "importance": 0.80,
        "rationale": "Applying OpenZeppelin security contracts and avoiding basic vulnerabilities like reentrancy."
      },
      {
        "skill_id": "blockchain_core_concepts",
        "importance": 0.75,
        "rationale": "Grasping asymmetric cryptography, ECDSA signatures, and BIP-39 wallet derivation."
      },
      {
        "skill_id": "blockchain_networks",
        "importance": 0.70,
        "rationale": "Navigating EVM testnets, RPC providers, and block explorer verification."
      },
      {
        "skill_id": "blockchain_scaling",
        "importance": 0.60,
        "rationale": "Basic gas profiling and understanding Layer 2 rollups concepts."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Weighted average of skill readiness scores multiplied by importance weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.35, "description": "Insufficient Solidity and testing fundamentals." },
        "partially_ready": { "min": 0.35, "max": 0.60, "description": "Writes basic contracts but struggles with Foundry testing or wallet hooks." },
        "ready": { "min": 0.60, "max": 0.85, "description": "Competent junior developer delivering tested ERC contracts and Wagmi DApp frontends." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceeds junior expectations with strong grasp of L2s and gas optimization." }
      }
    }
  },
  "mid": {
    "role_id": "blockchain_developer",
    "level": "mid",
    "title": "Mid-level Blockchain Developer",
    "description": "Mid-level blockchain engineer capable of building complex DeFi/NFT protocols, designing UUPS upgradeable proxies, integrating Chainlink Data Feeds and VRF randomness, running Slither and fuzz testing suites, authoring The Graph subgraphs, and deploying across EVM L2s and Solana.",
    "experience_range": "2-5 years",
    "skills": [
      {
        "skill_id": "smart_contract_development",
        "importance": 0.95,
        "rationale": "Designing upgradeable proxies, Chainlink Oracle integration, Vyper contracts, and Yul gas optimization."
      },
      {
        "skill_id": "blockchain_security",
        "importance": 0.95,
        "rationale": "Running Slither static analysis, property-based fuzz testing, and frontrunning/MEV mitigation."
      },
      {
        "skill_id": "dapp_development",
        "importance": 0.90,
        "rationale": "DeFi integrations (Uniswap, Aave), custom The Graph subgraphs, and DAO governance."
      },
      {
        "skill_id": "blockchain_networks",
        "importance": 0.85,
        "rationale": "Deploying across OP Stack, Arbitrum Nitro, Solana SVM, and cross-chain bridge mechanisms."
      },
      {
        "skill_id": "blockchain_scaling",
        "importance": 0.85,
        "rationale": "Architecting across Optimistic and ZK-Rollups, Validium, and gas profiling."
      },
      {
        "skill_id": "smart_contract_tooling",
        "importance": 0.80,
        "rationale": "EVM trace debugging in Tenderly and IPFS/Arweave decentralized storage pinning."
      },
      {
        "skill_id": "blockchain_core_concepts",
        "importance": 0.75,
        "rationale": "Validator staking models, network fork mechanics, and Sybil resistance."
      },
      {
        "skill_id": "blockchain_fundamentals",
        "importance": 0.70,
        "rationale": "Mempool propagation dynamics and Merkle proof verification."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Weighted average of skill readiness scores multiplied by importance weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.35, "description": "Lacks independent smart contract architecture and security auditing skills." },
        "partially_ready": { "min": 0.35, "max": 0.60, "description": "Comfortable with basic DeFi, but struggles with proxy patterns, fuzz testing, or cross-chain messaging." },
        "ready": { "min": 0.60, "max": 0.85, "description": "Meets all mid-level expectations: delivers upgradeable contracts, Slither audits, subgraphs, and L2 deployments." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceeds mid-level requirements with deep zk-Rollup knowledge and formal verification skills." }
      }
    }
  },
  "senior": {
    "role_id": "blockchain_developer",
    "level": "senior",
    "title": "Senior Blockchain Developer / Protocol Architect",
    "description": "Staff/Senior blockchain architect who designs mission-critical DeFi protocols, conducts formal verification (Certora) and Echidna invariant testing, architects EIP-4844/zkEVM scaling solutions, deploys ERC-4337 Account Abstraction paymasters, and directs cross-chain CCIP/IBC interoperability.",
    "experience_range": "5+ years",
    "skills": [
      {
        "skill_id": "blockchain_security",
        "importance": 0.95,
        "rationale": "Leading invariant fuzzing (Echidna), symbolic execution (Manticore), and professional protocol audits."
      },
      {
        "skill_id": "smart_contract_development",
        "importance": 0.95,
        "rationale": "Formal verification (Certora), Rust/Solana Anchor programs, and hybrid Chainlink Functions architectures."
      },
      {
        "skill_id": "blockchain_scaling",
        "importance": 0.90,
        "rationale": "Proto-Danksharding (EIP-4844), zkEVM circuit evaluation, and parallel EVM execution engines."
      },
      {
        "skill_id": "blockchain_networks",
        "importance": 0.90,
        "rationale": "Cross-chain interoperability with CCIP/IBC, Alt-VM architectures (Move/WASM), and modular Celestia DA."
      },
      {
        "skill_id": "dapp_development",
        "importance": 0.85,
        "rationale": "ERC-4337 Account Abstraction paymasters, self-hosted node clusters (Geth/Reth), and Envio indexers."
      },
      {
        "skill_id": "smart_contract_tooling",
        "importance": 0.85,
        "rationale": "CI/CD smart contract pipelines, automated Medusa fuzzer suites, and gas snapshot gates."
      },
      {
        "skill_id": "blockchain_core_concepts",
        "importance": 0.85,
        "rationale": "Advanced consensus (Tendermint/PBFT), zk-SNARK primitives, and deterministic state replication."
      },
      {
        "skill_id": "blockchain_fundamentals",
        "importance": 0.75,
        "rationale": "BFT theoretical limits and blockchain trilemma tradeoffs."
      }
    ],
    "scoring": {
      "method": "weighted_average",
      "description": "Weighted average of skill readiness scores multiplied by importance weights.",
      "thresholds": {
        "not_ready": { "min": 0.0, "max": 0.40, "description": "Lacks protocol-level architectural depth, invariant testing, and multi-chain leadership." },
        "partially_ready": { "min": 0.40, "max": 0.65, "description": "Strong developer but lacks formal verification, zk-Rollup internals, and Account Abstraction architecture." },
        "ready": { "min": 0.65, "max": 0.85, "description": "Seasoned blockchain architect delivering formally verified contracts, L2 scaling, and robust DeFi protocols." },
        "exceeds": { "min": 0.85, "max": 1.0, "description": "Exceptional protocol engineer recognized across the crypto ecosystem for state-of-the-art Web3 architecture." }
      }
    }
  }
}

for level_name, role_data in roles.items():
    file_path = os.path.join(roles_dir, f"{level_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(role_data, f, indent=2, ensure_ascii=False)
    print(f"Generated blockchain role: {file_path}")

print("\nBlockchain KB Generation Part 1 Complete.")
