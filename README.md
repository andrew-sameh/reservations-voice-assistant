# Voice Assistant Project

This project implements a Voice Assistant composed of three main services. Each service plays a distinct role in the overall functionality of the assistant. Below, you will find a brief overview of these services, followed by detailed setup and usage instructions.

![Screenshot of the frontend application.](/.github/assets/Reservations-VA.png)

## Overview of Services

1. **Livekit Service (Agent)**:
   - A Python-based WebRTC agent that connects to the Livekit cloud.
   - Handles real-time voice communication and manages interactions for booking reservations at a private cinema.
   - Integrates Speech-to-Text (STT), Text-to-Speech (TTS), and Language Learning Models (LLM).

2. **FastAPI Service (Reservations API)**:
   - A backend server that provides endpoints for creating, checking, and managing reservations.
   - Interacts with the Livekit agent and serves the frontend for displaying reservation data.

3. **Next.js Frontend**:
   - A web interface based on the LiveKit Next.js template, enhanced with ShadCN components.
   - Allows users to view and manage reservations in real-time.

## Documentation and Resources
- **Livekit**:
  - Documentation: [Livekit Docs](https://docs.livekit.io/home/)
  - To set up a project and get environment variables: [Livekit Cloud](https://cloud.livekit.io/)
- **TMDB API**:
  - Get your API key: [TMDB](https://www.themoviedb.org/)
- **Deepgram**:
  - For Speech-to-Text (STT) and Text-to-Speech (TTS): [Deepgram](https://deepgram.com/)

---

## Livekit Service - (Agent)

### Overview
The Livekit Service serves as the WebRTC agent connected to the Livekit cloud. This service is implemented in Python and is responsible for facilitating voice interactions and managing reservation-related functionalities for a private cinema. 

### Requirements
The service dependencies can be installed using either `poetry` or `requirements.txt`.

#### Using Poetry
1. Install Poetry if not already installed:
   ```bash
   pip install poetry
   ```
2. Install dependencies:
   ```bash
   poetry install --no-root
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

#### Using `requirements.txt`
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
The `.env` file must be configured with the following variables:
- **LIVEKIT_URL**: The URL of the Livekit server.
- **LIVEKIT_API_KEY**: The API key for authenticating with Livekit.
- **LIVEKIT_API_SECRET**: The secret key for authenticating with Livekit.
- **DEEPGRAM_API_KEY**: The API key for Deepgram (if used as the STT/TTS provider).
- **CARTESIA_API_KEY**: The API key for Cartesia (if used as the TTS provider).
- **ELEVENLABS_API_KEY**: The API key for ElevenLabs (if used as the TTS provider).
- **OPENAI_API_KEY**: The API key for OpenAI (if used as the LLM or TTS provider).
- **TMDB_READ_ACCESS_KEY**: The API key for The Movie Database (TMDB) API.
- **TMDB_BASE_URL**: The base URL for the TMDB API.
- **RES_BASE_URL**: The base URL for the Reservations API.

### Running the Service
To start the Livekit Service, run the following command:
```bash
python main.py dev
```

### Additional Dependencies
- **TMDB API**: Used to retrieve details about movies. An API key is required.
- **Reservation API**: Another service that will be explained later, responsible for handling reservation requests.


## FastAPI Service - (Reservations API)

### Overview
The Reservations API is a FastAPI server that hosts endpoints to manage reservations. It interacts with the Voice Assistant to create and check reservations and is also used by the frontend to display all reservation data in real-time.

### Requirements
The service requires a PostgreSQL database to store reservation data. A `docker-compose.yml` file is provided to set up the database.

#### Using Poetry
1. Install Poetry if not already installed:
   ```bash
   pip install poetry
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

#### Using `requirements.txt`
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
The `.env` file for this service must include the following variables:
- **POSTGRES_USER**: The username for the PostgreSQL database.
- **POSTGRES_PASSWORD**: The password for the PostgreSQL database.
- **POSTGRES_DB**: The name of the PostgreSQL database.
- **POSTGRES_HOST**: The host where the PostgreSQL database is running.
- **POSTGRES_PORT**: The port for connecting to the PostgreSQL database.

### Running the Service
1. Set up the PostgreSQL database using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Start the FastAPI server:
   ```bash
   python main.py
   ```

### Usage
The Reservations API provides the following endpoints:
- **POST /reservations**: Create a new reservation.
- **GET /reservations/{reservation_id}**: Retrieve details of a specific reservation.
- **GET /reservations**: List all reservations.
- **PUT /reservations/{reservation_id}**: Update a reservation.


## Next.js Frontend

### Overview
The Next.js frontend is based on the LiveKit Next.js base template, enhanced with ShadCN components. It serves as the user interface for interacting with the Voice Assistant and Reservations API.

### Requirements
The frontend uses `pnpm` for package management. Ensure `pnpm` is installed before proceeding.

### Environment Variables
The `.env` file for the frontend must include the following variables:
- **LIVEKIT_URL**: The WebSocket URL for connecting to the Livekit server.
- **LIVEKIT_API_KEY**: The API key for Livekit authentication.
- **LIVEKIT_API_SECRET**: The secret key for Livekit authentication.
- **API_URL**: The base URL for the Reservations API.

### Running the Service
1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Start the development server:
   ```bash
   pnpm dev
   ```

3. Open your browser and navigate to `http://localhost:3000` to view the application.

