# AI-chatbot
chatgpt-clone/
│
├── backend/
│   ├── app.py                     # Flask entry point (backend API)
│   ├── requirements.txt           # Python dependencies
│   ├── .env                       # Contains your OpenAI API key
│   │
│   ├── config/
│   │   └── __init__.py            # Config for Flask app (CORS, logging, etc.)
│   │
│   ├── routes/
│   │   └── chat.py                # Chat API route (handles POST /chat)
│   │
│   ├── services/
│   │   └── openai_service.py      # Logic to talk to OpenAI API
│   │
│   ├── utils/
│   │   └── helpers.py             # Optional helper functions
│   │
│   ├── tests/
│   │   └── test_chat.py           # Unit tests for backend
│   │
│   └── __init__.py
│
├── frontend/
│   ├── package.json               # React dependencies
│   ├── vite.config.js             # or webpack config
│   ├── src/
│   │   ├── App.jsx                # Main chat UI component
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx     # Chat display
│   │   │   └── MessageInput.jsx   # Input box + send button
│   │   └── styles/
│   │       └── app.css            # Chat styling
│   └── public/
│       └── index.html
│
├── README.md                      # Project setup & usage instructions
└── .gitignore                     # Ignore .env, __pycache__, node_modules, etc.
