# 🤖 Optimus Prime Desktop Assistant

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> **"Autobots, roll out!"** - Transform your desktop experience with this advanced AI assistant inspired by the Transformers franchise.

## 🌟 Overview

Optimus Prime is a sophisticated Python-based desktop assistant that combines speech recognition, automation, and self-learning capabilities to provide a comprehensive desktop experience. Built with modular architecture, it offers voice control, web automation, system management, and much more.

### ✨ Key Features

- 🎤 **Voice Control** - Speech-to-text and text-to-speech capabilities
- 🌐 **Web Automation** - Browser control and website navigation
- ⚙️ **System Control** - Volume, brightness, system information
- 📋 **Task Management** - Process monitoring and control
- 🧠 **Self-Learning** - Adaptive behavior based on usage patterns
- ⏰ **Scheduling** - Alarm and schedule management
- 📁 **File Operations** - Create and manage files
- 📱 **WhatsApp Integration** - Send messages and files
- 🌤️ **Weather & Internet** - Real-time information retrieval
- 📸 **Screen Control** - Screenshots and screen recording

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Chrome browser
- Microphone access
- Internet connection
- Windows 10/11 (primary support)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/optimus-prime-assistant.git
   cd optimus-prime-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run setup**
   ```bash
   python setup.py
   ```

4. **Start Optimus Prime**
   ```bash
   python Optimus.py
   ```

## 📖 Usage Examples

### Basic Commands

| Command | Action |
|---------|--------|
| `"open website google"` | Opens Google website |
| `"play music despacito"` | Plays Despacito on YouTube |
| `"check battery percentage"` | Shows battery status |
| `"take a screenshot"` | Captures screen |
| `"check weather in London"` | Shows London weather |

### Advanced Commands

| Command | Action |
|---------|--------|
| `"set alarm for 7:00 AM"` | Sets morning alarm |
| `"tell me to take medicine at 2:00 PM"` | Sets reminder |
| `"send whatsapp message to John"` | Opens WhatsApp chat |
| `"create file my_notes.txt"` | Creates text file |
| `"play theme song"` | Plays Transformers theme |

### System Control

| Command | Action |
|---------|--------|
| `"volume up"` | Increases system volume |
| `"brightness high"` | Sets high brightness |
| `"system info"` | Shows system information |
| `"running apps"` | Lists active applications |
| `"kill chrome"` | Terminates Chrome process |

## 🏗️ Project Structure

```
Optimus2/
├── Optimus.py                 # Main entry point
├── co_brain.py               # Main assistant brain
├── requirements.txt          # Python dependencies
├── setup.py                 # Installation script
├── API_KEY.txt              # External API keys
├── schedule.txt             # User schedules
├── Alam_data.txt            # Alarm data
├── Automation/              # Automation modules
│   ├── Automation_Brain.py  # Automation controller
│   ├── Web_Open.py         # Website navigation
│   ├── open_App.py         # Application launcher
│   ├── Battery.py          # Battery monitoring
│   ├── youtube_playback.py # YouTube control
│   ├── scroll_system.py    # Browser scrolling
│   ├── tab_automation.py   # Browser tab management
│   └── Play_Music_YT.py    # YouTube music player
├── Features/               # Feature modules
│   ├── conversation.py     # Conversation handler
│   ├── self_learning.py    # Adaptive learning system
│   ├── system_control.py   # System management
│   ├── quick_notes.py      # Note taking
│   ├── screen_control.py   # Screen operations
│   ├── task_manager.py     # Process management
│   ├── check_internet_speed.py # Speed testing
│   ├── create_file.py      # File creation
│   └── play_theme.py       # Theme music
├── Time_Operations/        # Time-based operations
│   ├── brain.py           # Schedule management
│   └── throw_alert.py     # Alert system
├── Data/                  # Data management
│   ├── DLG_Data.py        # Dialogue system
│   ├── learning_data.json # Learning data
│   ├── learned_features.json # Learned features
│   └── new_questions.json # Learned Q&A pairs
├── SpeachToText/          # Speech recognition
│   └── SpeachToText.py    # Speech-to-text module
├── TextToSpeach/          # Text-to-speech
│   └── Fast_DF_TTS.py     # TTS module
├── UI/                    # User interface
│   ├── ui.htm            # Web interface
│   └── server.py         # UI server
├── Whatsapp_automation/   # WhatsApp integration
│   └── Whatsapp.py       # WhatsApp automation
├── Weather_Check/         # Weather system
│   └── check_weather.py  # Weather information
├── Device_info/           # Device information
│   └── device_info.py    # System information
└── chrome-data/           # Chrome configuration
```

## 🔧 Configuration

### File Paths
Update the following file paths in `Optimus.py` for your system:
```python
Alam_path = r'C:\Users\YourUsername\Desktop\Optimus2\Alam_data.txt'
file_path = r'C:\Users\YourUsername\Desktop\Optimus2\schedule.txt'
```

### API Keys
Configure external API keys in `API_KEY.txt`:
```
WEATHER_API_KEY=your_weather_api_key_here
```

### Schedule Setup
Add your schedule in `schedule.txt`:
```
07:00AM = Wake up and start the day
12:00PM = Lunch break
06:00PM = End of work day
```

### Alarm Setup
Set alarm times in `Alam_data.txt`:
```
07:00AM
08:30AM
```

## 🧠 Self-Learning System

Optimus Prime features an advanced self-learning system that:

- **Learns from Usage**: Adapts to your command patterns
- **Error Recovery**: Automatically recovers from common errors
- **Feature Suggestions**: Suggests new features based on usage
- **Performance Optimization**: Monitors and optimizes system performance

### Learning Capabilities
- Command pattern analysis
- Error pattern recognition
- Feature usage optimization
- Automatic recovery strategies

## 🛠️ Troubleshooting

### Common Issues

#### Speech Recognition Not Working
- Check microphone permissions
- Verify audio drivers
- Test with system speech recognition

#### Browser Automation Fails
- Update Chrome browser
- Check ChromeDriver compatibility
- Verify web automation permissions

#### System Commands Not Working
- Run as administrator if needed
- Check system permissions
- Verify Python path

#### Audio Playback Issues
- Check audio drivers
- Verify pygame installation
- Test system audio

### Debug Mode
- Enable debug logging in configuration
- Check error logs in `Data/` directory
- Monitor system resources

## 📚 Documentation

For detailed documentation, see:
- [Complete Documentation](Optimus_Prime_Documentation.md) - Comprehensive system documentation
- [API Reference](docs/api.md) - API documentation (coming soon)
- [Contributing Guide](CONTRIBUTING.md) - How to contribute

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the Transformers franchise
- Built with Python and various open-source libraries
- Thanks to all contributors and the open-source community

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/optimus-prime-assistant/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/optimus-prime-assistant/discussions)
- **Email**: your.email@example.com

## 🔮 Roadmap

### Planned Features
- [ ] AI Integration - Advanced natural language processing
- [ ] Cloud Sync - Cross-device synchronization
- [ ] Mobile App - Companion mobile application
- [ ] API Integration - More external service connections
- [ ] Voice Customization - Multiple voice options
- [ ] Plugin System - Extensible feature architecture

### Performance Improvements
- [ ] Caching System - Faster response times
- [ ] Predictive Commands - Anticipate user needs
- [ ] Optimized Learning - Better pattern recognition
- [ ] Resource Management - Improved memory usage

## ⭐ Project Flow
├── Alam_data.txt
├── Alert.py
├── Automation
    ├── Automation_Brain.py
    ├── Battery.py
    ├── Play_Music_YT.py
    ├── Web_Data.py
    ├── Web_Open.py
    ├── __pycache__
    │   ├── Automation.cpython-312.pyc
    │   ├── Automation_Brain.cpython-311.pyc
    │   ├── Automation_Brain.cpython-312.pyc
    │   ├── Automation_Brain.cpython-313.pyc
    │   ├── Battery.cpython-311.pyc
    │   ├── Battery.cpython-312.pyc
    │   ├── Battery.cpython-313.pyc
    │   ├── Play_Music_YT.cpython-311.pyc
    │   ├── Play_Music_YT.cpython-312.pyc
    │   ├── Play_Music_YT.cpython-313.pyc
    │   ├── Web_Data.cpython-311.pyc
    │   ├── Web_Data.cpython-312.pyc
    │   ├── Web_Data.cpython-313.pyc
    │   ├── Web_Open.cpython-311.pyc
    │   ├── Web_Open.cpython-312.pyc
    │   ├── Web_Open.cpython-313.pyc
    │   ├── open_App.cpython-311.pyc
    │   ├── open_App.cpython-312.pyc
    │   ├── open_App.cpython-313.pyc
    │   ├── scroll_system.cpython-311.pyc
    │   ├── scroll_system.cpython-312.pyc
    │   ├── scroll_system.cpython-313.pyc
    │   ├── tab_automation.cpython-311.pyc
    │   ├── tab_automation.cpython-312.pyc
    │   ├── tab_automation.cpython-313.pyc
    │   ├── youtube_playback.cpython-311.pyc
    │   ├── youtube_playback.cpython-312.pyc
    │   └── youtube_playback.cpython-313.pyc
    ├── open_App.py
    ├── scroll_system.py
    ├── tab_automation.py
    └── youtube_playback.py
├── Data
    ├── DLG_Data.py
    ├── Notes
    │   └── note_20250218_185828.txt
    ├── Screenshots
    │   └── screenshot_20250220_202303.png
    ├── __pycache__
    │   ├── DLG_Data.cpython-311.pyc
    │   ├── DLG_Data.cpython-312.pyc
    │   ├── DLG_Data.cpython-313.pyc
    │   └── qa_data.cpython-312.pyc
    ├── learned_features.json
    └── learning_data.json
├── Device_info
    ├── __pycache__
    │   ├── device_info.cpython-311.pyc
    │   ├── device_info.cpython-312.pyc
    │   └── device_info.cpython-313.pyc
    └── device_info.py
├── Features
    ├── Transformers Prime Opening.mp3
    ├── __pycache__
    │   ├── check_internet_speed.cpython-311.pyc
    │   ├── check_internet_speed.cpython-312.pyc
    │   ├── check_internet_speed.cpython-313.pyc
    │   ├── conversation.cpython-311.pyc
    │   ├── conversation.cpython-312.pyc
    │   ├── conversation.cpython-313.pyc
    │   ├── create_file.cpython-311.pyc
    │   ├── create_file.cpython-312.pyc
    │   ├── create_file.cpython-313.pyc
    │   ├── location.cpython-312.pyc
    │   ├── mood_music.cpython-312.pyc
    │   ├── play_theme.cpython-311.pyc
    │   ├── play_theme.cpython-312.pyc
    │   ├── play_theme.cpython-313.pyc
    │   ├── quick_notes.cpython-311.pyc
    │   ├── quick_notes.cpython-312.pyc
    │   ├── quick_notes.cpython-313.pyc
    │   ├── screen_control.cpython-311.pyc
    │   ├── screen_control.cpython-312.pyc
    │   ├── screen_control.cpython-313.pyc
    │   ├── self_learning.cpython-311.pyc
    │   ├── self_learning.cpython-312.pyc
    │   ├── self_learning.cpython-313.pyc
    │   ├── system_control.cpython-311.pyc
    │   ├── system_control.cpython-312.pyc
    │   ├── system_control.cpython-313.pyc
    │   ├── task_manager.cpython-311.pyc
    │   ├── task_manager.cpython-312.pyc
    │   └── task_manager.cpython-313.pyc
    ├── check_internet_speed.py
    ├── conversation.py
    ├── create_file.py
    ├── play_theme.py
    ├── quick_notes.py
    ├── screen_control.py
    ├── self_learning.py
    ├── system_control.py
    └── task_manager.py
├── LICENSE
├── Optimus.py
├── Optimus_Prime_Documentation.md
├── README.md
├── SpeachToText
    ├── SpeachToText.py
    ├── __init__.py
    └── __pycache__
    │   ├── SpeachToText.cpython-311.pyc
    │   ├── SpeachToText.cpython-312.pyc
    │   ├── SpeachToText.cpython-313.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── __init__.cpython-312.pyc
    │   └── __init__.cpython-313.pyc
├── TextToSpeach
    ├── Fast_DF_TTS.py
    └── __pycache__
    │   ├── Fast_DF_TTS.cpython-311.pyc
    │   ├── Fast_DF_TTS.cpython-312.pyc
    │   └── Fast_DF_TTS.cpython-313.pyc
├── Time_Operations
    ├── __pycache__
    │   ├── brain.cpython-311.pyc
    │   ├── brain.cpython-312.pyc
    │   ├── brain.cpython-313.pyc
    │   ├── throw_alert.cpython-311.pyc
    │   ├── throw_alert.cpython-312.pyc
    │   └── throw_alert.cpython-313.pyc
    ├── brain.py
    └── throw_alert.py
├── UI
    ├── __pycache__
    │   ├── optimus_interface.cpython-312.pyc
    │   ├── server.cpython-312.pyc
    │   └── web_interface.cpython-312.pyc
    ├── input.txt
    ├── server.py
    └── ui.htm
├── Weather_Check
    ├── __pycache__
    │   ├── check_weather.cpython-311.pyc
    │   ├── check_weather.cpython-312.pyc
    │   └── check_weather.cpython-313.pyc
    └── check_weather.py
├── Whatsapp_automation
    ├── Whatsapp.py
    └── __pycache__
    │   ├── Whatsapp.cpython-311.pyc
    │   ├── Whatsapp.cpython-312.pyc
    │   └── Whatsapp.cpython-313.pyc
├── __pycache__
    ├── Alert.cpython-311.pyc
    ├── Alert.cpython-312.pyc
    ├── Alert.cpython-313.pyc
    ├── co_brain.cpython-311.pyc
    ├── co_brain.cpython-312.pyc
    ├── co_brain.cpython-313.pyc
    ├── internet_check.cpython-311.pyc
    ├── internet_check.cpython-312.pyc
    ├── internet_check.cpython-313.pyc
    └── test.cpython-312.pyc
├── chrome-data
    ├── Default
    │   └── Preferences
    ├── First Run
    └── Local State
├── co_brain.py
├── input.txt
├── internet_check.py
├── logo.jpeg
├── requirements.txt
├── schedule.txt
└── setup.py



---

**"Freedom is the right of all sentient beings."** - Optimus Prime

Made with ❤️ by Somendra Kumar Yadav

