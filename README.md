
# TradeSmartAI (Yantra X) - Autonomous AI Trading Firm

Welcome to TradeSmartAI, now evolving into Yantra X – an autonomous AI-powered trading firm designed to operate 24/7 with intelligent agents, mimicking a real-world trading institution.

This project is built with a focus on modularity, scalability, and self-learning capabilities, aiming for a stealth-mode beta launch.

## Project Structure

*   **`backend/`**: Contains the Flask API, trading logic, AI firm simulation, and data models.
*   **`frontend/`**: (Placeholder for React application - not fully implemented in this phase, but structure is assumed for deployment).
*   **`rl_environment/`**: Reinforcement Learning environment for market simulation.
*   **`rl_agents/`**: Implementations of various RL agents (e.g., DQN).
*   **`rl_training/`**: Scripts for training RL agents.

## Key Features (Current & Planned)

*   **Autonomous AI Firm**: Operates with a multi-agent system across various departments (Market Intelligence, Trade Operations, Risk Control, Performance Lab, Communications).
*   **24/7 Operation**: Designed for continuous, shift-based operation.
*   **Self-Learning & Memory**: Agents learn from past decisions, analyze mistakes, and adapt strategies.
*   **Daily & Weekly Reporting**: Comprehensive reports generated for founder insights.
*   **AI Strategy Plug-in Layer**: Allows injection of custom AI trading strategies.
*   **P&L Simulator Mode**: Test strategies in a simulated environment with realistic trade fills and slippage.
*   **User Management**: Basic authentication and role management.
*   **Deployment Ready**: Configured for cloud deployment platforms like Render.com.

## Getting Started (Local Development)

### Prerequisites

*   Python 3.9+
*   Node.js (for frontend development, if applicable)
*   Docker (optional, for containerized deployment)

### Backend Setup

1.  Navigate to the `backend/` directory:
    `cd backend`
2.  Install Python dependencies:
    `pip install -r requirements.txt`
3.  Copy `.env.example` to `.env` and configure environment variables:
    `cp .env.example .env`
    Edit `.env` with your desired settings (e.g., `TRADING_MODE=paper`).
4.  Run the Flask application:
    `flask run` (or `gunicorn --bind 0.0.0.0:5000 wsgi:app` for production-like)

### Frontend Setup (Conceptual)

1.  Navigate to the `frontend/` directory:
    `cd frontend`
2.  Install Node.js dependencies:
    `npm install`
3.  Start the React development server:
    `npm start`

## How to Test / Simulate / Onboard AI Strategies

1.  **Simulation Mode**: Set `TRADING_MODE=paper` in your `.env` file. The system will use the internal market simulator.
2.  **AI Strategy Injection**: Place your AI strategy Python files (e.g., `my_custom_strategy.py`) in the `backend/src/strategies/` directory. Ensure they adhere to the `BaseStrategy` interface (see `base_strategy.py`). The `strategy_loader.py` will automatically discover and load them.
3.  **RL Agent Training**: To train new RL agents, navigate to `backend/src/rl_training/` and run `python train_agent.py` with your desired data and episodes.

## Deployment

This project includes `Dockerfile` and `render.yaml` for containerized deployment. Refer to these files for deployment configurations on platforms like Render.com.

## Contributing

Contributions are welcome! Please refer to the contribution guidelines (to be added).

## License

This project is licensed under the MIT License.


