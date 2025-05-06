# Health Assistant Telegram Bot

A simple Telegram bot that provides health-related information and tips to users. This bot allows users to get personalized health tips, check their BMI, track their hydration, calculate calories of common foods, and more!

## Features

- **Health Tips**: Get random health tips to stay fit and healthy.
- **BMI Calculation**: Users can calculate their BMI by providing their weight and height.
- **Hydration Reminder**: The bot reminds users to stay hydrated and drink water regularly.
- **Calorie Tracker**: Get calorie information for common foods like apple, banana, chicken, rice, etc.
- **Daily Wellness Reminder**: Provides daily wellness tasks like stretching, drinking water, breathing exercises, etc.
- **Mental Health Tips**: Tips for managing stress and improving mental well-being.

## Technologies Used

- Python
- `python-telegram-bot` library
- `random` library
- Telegram Bot API

## Installation

### Prerequisites

- Python 3.x
- A Telegram Bot Token (obtainable by creating a bot via [BotFather](https://core.telegram.org/bots#botfather)).

### Steps to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/health-assistant-bot.git
````

2. Navigate to the project directory:

   ```bash
   cd health-assistant-bot
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   * **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```
   * **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the root directory and add your Telegram Bot Token:

   ```bash
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```

7. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

* Start a conversation with your bot by clicking **Start** or typing `/start`.
* The bot will provide buttons with different health options (Health Tips, BMI, Hydration, etc.).
* You can also use commands like `/tips`, `/bmi`, `/calories food_name`, `/hydration`, `/stress`, and more!

## Contributing

1. Fork the repository.
2. Create your feature branch:

   ```bash
   git checkout -b new-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to your branch:

   ```bash
   git push origin new-feature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Explanation:
- **Project Description**: This section describes the functionality of the bot.
- **Technologies**: Lists the technologies used in the project.
- **Installation Steps**: Describes how to set up the project locally, including how to install dependencies.
- **Usage**: Provides instructions on how to interact with the bot.
- **Contributing**: Outlines how others can contribute to the project.
- **License**: Mentions the licensing for the project.
