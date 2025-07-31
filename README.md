# CrewAI Trip Planner Agent

An intelligent AI-powered trip planning system built with CrewAI that helps users plan their travels by analyzing destinations, weather, prices, and creating personalized itineraries.

## 🚀 Features

- **Smart City Selection**: Analyzes weather, season, and prices to recommend the best destinations
- **Local Expert Insights**: Provides detailed information about attractions, customs, and local knowledge
- **Travel Concierge**: Creates comprehensive itineraries with budget and packing suggestions
- **Multi-Agent Collaboration**: Uses specialized AI agents working together for optimal planning

## 🏗️ Architecture

The project uses a multi-agent system with three specialized agents:

### Agents

1. **City Selection Expert** (`trip_agents.py`)
   - Role: Analyzes travel data to pick ideal destinations
   - Tools: Internet search, website scraping
   - Goal: Select the best city based on weather, season, and prices

2. **Local Expert** (`trip_agents.py`)
   - Role: Knowledgeable local guide with extensive city information
   - Tools: Internet search, website scraping
   - Goal: Provide the BEST insights about the selected city

3. **Travel Concierge** (`trip_agents.py`)
   - Role: Specialist in travel planning and logistics
   - Tools: Internet search, website scraping, calculations
   - Goal: Create amazing travel itineraries with budget and packing suggestions

### Tasks

The system executes three main tasks (`trip_tasks.py`):

1. **Identify Task**: City selection based on preferences
2. **Gather Task**: Collect detailed information about the destination
3. **Plan Task**: Create comprehensive travel itinerary

## 🛠️ Installation

### Prerequisites

- Python 3.10+ (tested with Python 3.13)
- Poetry (for dependency management)

### Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:krasimirkostadinov/crewAI-trip-planner-agent.git
   cd crewAI-trip-planner-agent
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry env activate
   # or
   source /path/to/poetry/virtualenv/bin/activate
   ```

4. **Set up environment variables**:
   Create a `.env` file with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Usage

Run the trip planner:

```bash
python main.py
```

The application will prompt you for:
- **Origin**: Where you're traveling from
- **Cities**: Options you're interested in visiting
- **Date Range**: When you want to travel
- **Interests**: Your hobbies and preferences

## 📁 Project Structure

```
crewAI-trip-planner-agent/
├── main.py              # Main application entry point
├── trip_agents.py       # Agent definitions
├── trip_tasks.py        # Task definitions
├── pyproject.toml       # Poetry dependencies
├── README.md           # This file
└── .env                # Environment variables (create this)
```

## 🔧 Dependencies

- **crewai**: AI agent framework
- **langchain**: LLM integration
- **langchain-openai**: OpenAI integration
- **python-dotenv**: Environment variable management
- **unstructured**: Data processing
- **pyowm**: Weather data
- **requests**: HTTP requests
- **beautifulsoup4**: Web scraping

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI) framework
- Inspired by the need for intelligent travel planning
- Uses OpenAI's language models for natural language processing

## 🚀 Future Improvements

### Planned Enhancements

- **Local Model Integration**: Switch from OpenAI to local models (Ollama, Llama, Mistral) for privacy and cost reduction
- **Weather API Integration**: Real-time weather data using OpenWeatherMap API for better destination recommendations
- **Budget Tracking**: Add expense tracking and budget management features
- **Multi-language Support**: Support for multiple languages for international travelers
- **Social Features**: Share itineraries and collaborate with travel companions
- **AI-Powered Photos**: Generate destination images using AI for visual planning
- **Voice Interface**: Add voice commands for hands-free trip planning
- **Offline Mode**: Cache data for offline access during travel
- **Integration APIs**: Connect with booking platforms (Booking.com, Airbnb, etc.)

### Technical Improvements

- **Performance Optimization**: Implement caching and async processing
- **Error Handling**: Robust error handling and fallback mechanisms
- **Testing Suite**: Comprehensive unit and integration tests
- **Docker Support**: Containerized deployment for easy setup
- **CI/CD Pipeline**: Automated testing and deployment
- **Monitoring**: Add logging and performance monitoring

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the maintainer.

---

**Happy Traveling! ✈️**