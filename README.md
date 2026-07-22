# Custom 2048-Bit RSA Cryptosystem Implementation

A modular, zero-dependency Python implementation of the Rivest-Shamir-Adleman (RSA) asymmetric cryptographic protocol built entirely from foundational computer science and mathematical principles.


---

## System Architecture & Modularity

The project rejects monolithic scripting in favor of a modern, decoupled package design. Logic is strictly separated by operational responsibility:

*   `rsa/generator.py`: Manages cryptographically secure bit-generation, deterministic filtering, and primality testing routines.
*   `rsa/engine.py`: Handles high-precision mathematical core operations and data serialization pipelines.
*   `rsa/storage.py`: Abstracts persistent session file handling securely via isolated context managers.
*   `rsa/constants.py`: Stores algorithmic parameters, such as industry-standard public exponents and mathematical screening constants.
*   `main.py`: Serve as an isolated execution entry point managing user input and terminal workflows.

---

## Key Engineering Features

### 1. Cryptographically Secure Pseudo-Random Prime Generation
Rather than utilizing standard pseudo-random number generators (PRNGs) which are predictable, the generation pipeline integrates Python's `secrets` module to capture OS-level entropy. It generates 1024-bit candidates, automatically setting the highest bit to ensure structural size compliance and the lowest bit to guarantee an odd integer.

### 2. Dual-Layer Primality Verification Workflow
To optimize runtime performance during key generation, candidates undergo a two-tier screening process:
*   **Low-Level Filtering:** Efficient division checks against the first 85 prime numbers quickly eliminate obvious composites.
*   **Probabilistic Verification:** Surviving candidates are subjected to a rigorous 20-round Miller-Rabin Primality Test, minimizing the probability of a composite number passing as prime to less than $4^{-20}$ ($9.09 \times 10^{-13}$).

### 3. High-Precision Mathematical Optimization
*   **Modular Multiplicative Inverse:** Solved efficiently using a custom implementation of the Extended Euclidean Algorithm to calculate the private exponent $d$ relative to Euler's totient $\phi(n)$.
*   **Modular Exponentiation:** Utilizes square-and-multiply bitwise operations via Python's built-in 3-argument `pow(base, exp, mod)` function, maintaining an efficient time complexity of $O(\log \text{\ exp})$ and preventing memory overflows.

### 4. End-to-End UTF-8 Byte Serialization
To enable the processing of both raw numeric payloads and alphanumeric text strings, the engine implements a bidirectional byte serialization pipeline using big-endian byte-order mapping:
$$\text{String Data} \longrightarrow \text{UTF-8 Bytes} \longrightarrow \text{High-Precision Integer} \longrightarrow \text{RSA Ciphertext}$$

---

## Getting Started

### Prerequisites
*   Python 3.10 or higher
*   Dependencies listed in `requirements.txt`

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/aryanb-95/RSA-Algorithm-Python
   cd rsa-cryptosystem
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Technical Parameters & Constants

| Parameter | Operational Value / Logic | Strategic Purpose |
| :--- | :--- | :--- |
| **Key Size** | 2048-bit ($n = p \times q$) | Aligns with baseline modern cryptographic key length standards. |
| **Public Exponent ($e$)** | $65537$ ($2^{16} + 1$) | Maximizes encryption efficiency while maintaining structural security. |
| **Prime Testing Rounds** | 20 Rounds (Miller-Rabin) | Mitigates the risk of false-positive pseudoprimes. |
| **Byte Order Direction** | `big` (Big-Endian) | Standardizes multi-byte integer conversions across architectures. |

---

