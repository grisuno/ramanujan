# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 1 | **Total Symbols Extracted:** 1 | **Total Imports:** 1

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    pi_py["pi.py (py)"]
    class pi_py mod;
    pi_py_calcular_pi_ramanujan["calcular_pi_ramanujan"]
    class pi_py_calcular_pi_ramanujan fn;
    pi_py --> pi_py_calcular_pi_ramanujan
    ext_mpmath["mpmath"]
    class ext_mpmath ext;
    pi_py -.->|imports| ext_mpmath
```

---

## Architecture Reference

### PY (1 files)

#### `pi.py`
**Path:** `pi.py`

**Functions:**
- `calcular_pi_ramanujan` (line 5) `def calcular_pi_ramanujan()`
