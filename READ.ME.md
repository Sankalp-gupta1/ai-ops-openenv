# AI Ops Autonomous Environment

## Overview
This project simulates real-world system operations where an AI agent manages server health using logs and metrics.

## Features
- Real-time system simulation (CPU, memory, logs)
- Anomaly detection using ML (Isolation Forest)
- Memory-based agent
- Reward-based decision system

## Tasks
1. Easy: Handle CPU spike
2. Medium: Fix memory leak
3. Hard: Multi-failure handling

## Actions
- scale
- restart
- ignore

## Rewards
- Correct action: +1
- Partial: +0.5
- Wrong: -0.5

## Run

```bash
python inference.py
