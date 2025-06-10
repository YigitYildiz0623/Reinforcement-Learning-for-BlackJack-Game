# 🃏 Reinforcement Learning for Blackjack Game

This project implements a simple reinforcement learning (RL) agent that learns to play the game of Blackjack using Monte Carlo methods.

## 📌 Overview

The goal of this project is to explore fundamental concepts in reinforcement learning by training an agent to make decisions in the card game Blackjack. The environment is based on OpenAI Gym's `Blackjack-v1`.

The agent learns from experience by playing games repeatedly and updating its policy based on observed rewards, without requiring a model of the environment.

## ⚙️ Technologies Used

- Python
- NumPy

## 🧠 Learning Method

- **Monte Carlo Control (On-Policy / Exploring Starts)**
- Policy is improved iteratively through value estimation.
- No prior knowledge of the environment is assumed.

## 📈 Results

After training over thousands of episodes, the RL agent converges to a reasonable strategy for playing Blackjack, balancing the risk of busting with potential rewards.

