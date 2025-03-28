# 🎉 Event Management API

## Overview

A robust, scalable Event Management System built with Python, FastAPI, and PostgreSQL. This API provides comprehensive event and attendee management capabilities, designed to streamline event organization and tracking.

## 🚀 Key Features

### Event Management
- Create, update, and manage events
- Flexible event status tracking
- Automated event status updates
- Advanced event filtering

### Attendee Management
- Event registration with capacity limits
- Individual and bulk attendee check-ins
- Detailed attendee tracking

### Technical Highlights
- RESTful API design
- PostgreSQL database integration
- Comprehensive error handling
- JWT Authentication (Extra Credit)
- Docker containerization
- Extensive unit testing

## 🛠 Technology Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Containerization**: Docker
- **Testing**: pytest

## 📋 Project Structure

```
event_management_api/
│── app/
│   ├── api/                # API routes
│   ├── core/               # Core configurations
│   ├── models/             # Database models
│   ├── schemas/            # Pydantic models
│   ├── services/           # Business logic
│   └── main.py             # Application entry point
│── tests/                  # Unit and integration tests
│── docker-compose.yml      # Container orchestration
│── Dockerfile              # Docker configuration
└── requirements.txt        # Python dependencies
```

## 🔧 Prerequisites

- Python 3.10+
- Docker
- Docker Compose

## 🚀 Quick Start

### Local Development

1. Clone the repository
```bash
git clone https://github.com/yourusername/event-management-api.git
cd event-management-api
```

2. Create a `.env` file with your configurations
```bash
# Example .env contents
DATABASE_URL=postgresql://user:password@localhost/eventdb
SECRET_KEY=your-secret-key
```

3. Start the application
```bash
docker-compose up --build
```

## 📦 Core Endpoints

- `POST /api/v1/events/`: Create a new event
- `PUT /api/v1/events/{event_id}`: Update event details
- `POST /api/v1/attendees/register`: Register for an event
- `POST /api/v1/attendees/{event_id}/check-in`: Check-in attendees
- `GET /api/v1/events/`: List events with filters


## 🔒 Authentication

Optional JWT authentication secures all endpoints, ensuring only authorized users can interact with the API.

## 📝 Business Logic

- Prevents event registration beyond maximum capacity
- Automatically updates event status based on time
- Supports bulk attendee check-ins via CSV
- Comprehensive error handling with meaningful messages

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

MIT License

## 🐛 Issues

Found a bug? Please open an issue on our GitHub repository.

---

**Built with ❤️ by Your Name**