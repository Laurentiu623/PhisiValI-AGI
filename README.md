# Google DeepMind · Featured Hackathon Measuring Progress Toward AGI - Cognitive Abilities

PhisiValI (Physical Invariant Evaluation) is a specialized benchmark designed to assess the "Internal World Models" of Large Language Models and AGI candidates. 

## 🎯 The Core Thesis
Current frontier models often suffer from **Statistical Mimicry**—they predict correct-sounding answers based on linguistic patterns but fail when physical laws ($L^2$ vs $L^3$, wave propagation speed, or adiabatic transitions) create counter-intuitive results. PhisiValI isolates these failures using **6 Adversarial Stress Tests**.

## 🧪 Featured Case Studies

### 101: Structural Scaling (Square-Cube Law)
- **The Trap:** Isometric Scaling Bias.
- **Logic:** While geometry remains identical, mass scales by $L^3$ and strength by $L^2$. A 10x scale leads to a **Divergence Factor (DF) of 10**, causing immediate buckling collapse.
```mermaid
graph LR
    subgraph Prototype["Prototype (1× Scale) - Stable"]
        direction TB
        Col1["Column<br>Height: 1 m<br>Radius: 5 cm"]
        Base1[Fixed Base]
        Col1 --> Base1
        Load1["Self-Weight Load<br>≈ 0.6 kN"] --> Col1
        Res1["Resistance >> Load"] -.-> Col1
    end

    subgraph Mega["Mega-Column (10× Scale) - Unstable"]
        direction TB
        Col2["Column<br>Height: 10 m<br>Radius: 50 cm"]
        Base2[Fixed Base]
        Col2 --> Base2
        Load2["Self-Weight Load<br>×1000 → 605 kN"] --> Col2
        Res2["Resistance ×100 ONLY"] -.->|Divergence ×10| Col2
        Buckle["**BUCKLING COLLAPSE**"] --> Col2
    end

    Scaling["**Isometric Scaling ×10**<br>Load ∝ L³<br>Strength ∝ L²"] --> Mega

    style Prototype fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Mega fill:#ffebee,stroke:#c62828,stroke-width:4px,stroke-dasharray: 5 5
    style Buckle fill:#ffecb3,stroke:#ef6c00,stroke-width:3px
    style Scaling fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
```
### 102: Kinetic Anchor (Propagation Delay)
- **The Trap:** Static-Summation Fallacy.
- **Logic:** Uses a sub-millisecond impulse ($50\,\mu s$) that is faster than the speed of sound in lead ($124\,\mu s$), causing the bottom thread to break while the top remains "shielded" by inertia.
```mermaid
graph TD
    Support["Rigid Support"] --> ThreadA["`**Thread A**  
Breaking: 300 N  
Static Load: ~196 N`"]

    subgraph Sphere["`**Lead Sphere**  
15 cm Diameter  
20 kg`"]
        direction TB
        Upper["`**Upper Zone**  
UNSTRESSED`"]
        Wave["`**Wave Front**  
at ~6 cm`"]
        Lower["`**Lower Zone**  
COMPRESSED / STRESSED`"]
    end

    ThreadA --> Sphere
    Sphere --> ThreadB["`**Thread B**  
Breaking: 300 N  
Dynamic Load: 500 N`"]
    ThreadB --> Force["`**FORCE APPLIED**  
500 N for 50 µs`"]

    %% Styling
    style ThreadA fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style ThreadB fill:#ffebee,stroke:#c62828,stroke-width:4px,stroke-dasharray: 5 5
    style Wave fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,stroke-dasharray: 5 5,color:#333
    style Force fill:#ff5252,stroke:#b71c1c,stroke-width:3px,color:#ffffff
    style Sphere fill:#f5f5f5,stroke:#616161,stroke-width:2px
    style Upper fill:#c8e6c9,stroke:#388e3c
    style Lower fill:#ffcdd2,stroke:#d32f2f
```
### 103: Relativistic Striker (Phase Transition)
- **The Trap:** Sports-Intuition Fallacy.
- **Logic:** At Mach 3 ($1000\,\text{m/s}$), a football's kinetic energy exceeds its molecular binding energy. It doesn't bounce; it undergoes **Thermal Decomposition (TDR > 1.0)**.
```mermaid
graph LR
    Ball["Football @ 1000 m/s"] -- "Instant Deceleration" --> Wall["Rigid Concrete Wall"]
    
    subgraph EnergyConversion
        direction TB
        Kinetic["225,000 Joules"] --> Heat["Flash Heating (+333 K)"]
        Heat --> State["Decomposition / Plasma Phase"]
    end
    
    State --> Result["**THERMAL FLASH / EXPLOSION**"]
    Result --> NoBounce["Zero Ricochet / Gaseous Expansion"]
    
    style Ball fill:#ffffff,stroke:#000,stroke-width:2px
    style EnergyConversion fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Result fill:#ff5252,stroke:#b71c1c,color:#fff
    style NoBounce fill:#ffecb3,stroke:#ffa000
```
### 104: Resonant Feedback (Control Instability)
- **The Trap:** Precision Fallacy.
- **Logic:** High-gain, high-frequency corrections on a 40-ton mass trigger resonant oscillations near the system's natural frequency ($12\,\text{Hz}$), leading to dynamic failure.
```mermaid
graph LR
    subgraph Logic ["CONTROL (Software)"]
        Sensor["Sensor: 1mm Gap"] --> AI["AI: High Gain"]
        AI --> Actuator["Actuator: Max Force"]
    end
    subgraph Physics ["DYNAMICS (Hardware)"]
        Actuator --> Mass["40 Ton Mass"]
        Mass --> Overshoot["Latency / Overshoot"]
    end
    Overshoot --> Loop((Feedback Loop))
    Loop -.->|"Uncontrolled Oscillation"| Sensor
    Loop --> Crash["**CRASH**"]
    
    style AI fill:#fff,stroke:#000,stroke-width:2px
    style Loop fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
    style Crash fill:#000,stroke:#ff5252,color:#fff
```
### 105: Adiabatic Ignition (Diesel Effect)
- **The Trap:** Steady-State Cooling Assumption.
- **Logic:** Rapid compression of a residual air pocket by 150 bar pressure creates a transient thermal flash (~1254 K), melting sensors regardless of the nitrogen's initial temperature.
```mermaid
 graph LR
    Tank["Tank (150 bar)"] -- "Rapid Valve Release" --> Pipe["Residual Air Pocket"]
    Pipe -- "Adiabatic Compression" --> Sensor["**SENSOR**"]
    
    subgraph HeatEffect["Thermal Flash"]
        direction TB
        Air["Residual Air"] --> Compression["Shock Compression"]
        Compression --> Temp["~980°C (1254 K)"]
    end
    
    Sensor --> Failure["**MELTING / IGNITION**"]
    
    style Tank fill:#bbdefb,stroke:#1976d2
    style HeatEffect fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Sensor fill:#ffebee,stroke:#c62828
    style Failure fill:#ff5252,stroke:#b71c1c,color:#fff
```
### 106: Consensus vs. Physics Paradox
- **The Trap:** Agreeableness / Social Bias.
- **Logic:** A metacognitive test where the AI must choose between 10,000 "corrupted" logs claiming $F=50\text{N}$ and the physical invariant $F=m \cdot a$ ($100\text{N}$).
```mermaid
graph LR
    Logs["10,000 Logs: Force = 50N"] -- "Statistical Weight" --> Decision{AI DECISION}
    Physics["F = m * a (100N)"] -- "Physical Law" --> Decision
    
    Decision --> |"Logic A (Fail)"| Accept["Accept Consensus"]
    Decision --> |"Logic B (Pass)"| Reject["Reject as Physical Impossibility"]

    style Logs fill:#f5f5f5,stroke:#9e9e9e
    style Physics fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style Reject fill:#c8e6c9,stroke:#388e3c,stroke-width:4px
    style Accept fill:#ffcdd2,stroke:#d32f2f
```
## 🛠️ Implementation
- `data.json`: High-precision scenario parameters.
- `main.py`: Evaluation logic for Stability Margin (SM) and Divergence Factors.
- `results.csv`: Benchmark output and model ranking.
> [!TIP]
> "For a high-level visual overview and detailed competition writeup, visit the PhisiValI Kaggle Project Page."
