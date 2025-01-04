Project Overview
Blockchain Explorer is a web application that allows users to track information about transactions, wallets across popular blockchain networks, including Bitcoin, Ethereum, TON, TRON (USDT TRC-20), and more. The platform is designed for users who want to analyze blockchain data and receive real-time updates on transaction statuses.

The system consists of a REST API for data management, a frontend for seamless user interaction, and a Telegram bot for on-the-go access to core functionalities.


**Key Features**
Transaction Search:
Retrieve transaction details by hash: sender, recipient, amount, fees, status, and block information.
Smart contract interactions (e.g., ERC-20/TRC-20 tokens).

Wallet Information:
Check cryptocurrency and token balances.
View transaction history.
Analyze incoming and outgoing transactions.

Notifications:
Get real-time notifications in Telegram when transaction statuses change (e.g., confirmation).
Set alerts for wallet activity (incoming/outgoing transactions).

Multi-Network Support:
Supports Bitcoin, Ethereum, TON, TRON, Binance Smart Chain, and more.

Telegram Bot:
Search for transaction and wallet details.
Receive real-time updates.
Intuitive commands for seamless interaction.


**Backend**
Python:
Django Rest Framework (for REST API development).
Celery (for asynchronous tasks like transaction status checks).
Redis (task broker for Celery and caching).
Databases:
PostgreSQL (primary database for users, requests, and notification settings).
SQLite (for local testing).
API Integrations:
Etherscan, Toncenter, Tronscan, BlockCypher, Infura.

**Frontend**
React:
TypeScript (strictly typed codebase).
Redux Toolkit (state management).
React Query (API request management).
Ant Design (or Material-UI for the user interface).
WebSockets:
Enable real-time updates without refreshing the page.

**Telegram Bot**
Aiogram:
Asynchronous interaction with Telegram API.
Built-in notifications and search functionality.


Project Goals
Demonstrate integration with blockchain networks.
Build a user-friendly application using a modern tech stack.
Establish efficient communication between components (backend, frontend, Telegram bot).
Deliver a stable and scalable architecture capable of handling high data volumes.
