# DevSutra

Master coding from Beginner to Pro with structured learning paths and 1000+ challenges.

## 🚀 Overview

DevSutra is a modern coding challenge platform designed to help developers progress from beginner to professional level through a structured learning path. With a warm, eye-friendly interface and carefully curated problems, DevSutra makes learning to code an enjoyable experience.

## ✨ Features

- **4 Difficulty Levels**: Beginner, Intermediate, Advanced, and Pro
- **1000+ Coding Problems**: Carefully curated challenges across multiple topics
- **Progressive Learning Path**: Unlock new levels as you complete challenges
- **Eye-Friendly Design**: Warm color palette optimized to reduce eye strain
- **Dark & Light Modes**: Beautiful themes for any preference
- **User Authentication**: Secure sign-in with Clerk
- **Multi-Language Support**: Practice in multiple programming languages
- **Real-time Code Execution**: Test your solutions instantly

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS with custom design system
- **Authentication**: Clerk
- **Fonts**: Inter & Space Grotesk from Google Fonts

### Backend
- **Framework**: Django
- **Database**: SQLite (development)
- **API**: Django REST Framework

## 📦 Installation

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Backend Setup

```bash
# Navigate to project root
cd DevSutra

# Install Python dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Import sample problems
python manage.py import_problems

# Start Django server
python manage.py runserver
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://127.0.0.1:8000

## 🎨 Design Philosophy

DevSutra uses a warm, eye-friendly color palette designed to reduce eye strain during long coding sessions:

- **Light Mode**: Warm beige tones (#F3EAD8, #EDE4DB) instead of harsh whites
- **Dark Mode**: Soft charcoal backgrounds instead of pure black
- **Accent Colors**: Muted terracotta and earthy tones
- **Typography**: Optimized for readability with Inter and Space Grotesk fonts

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

Made with ❤️ for aspiring developers
