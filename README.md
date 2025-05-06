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


### Step 1: **Clone the Repository**

1. First, clone your GitHub repository to your local machine:

   ```bash
   git clone https://github.com/your-username/health-assistant-bot.git
   ```
2. Navigate into the project folder:

   ```bash
   cd health-assistant-bot
   ```

### Step 2: **Set Up a Virtual Environment (Optional but Recommended)**

1. Create a virtual environment to keep your dependencies isolated:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   * **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```
   * **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

### Step 3: **Install Dependencies**

1. Install the required dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

### Step 4: **Create the `.env` File**

1. In the root directory of your project, create a file named **`.env`**.
2. Add your **Telegram Bot Token** inside the `.env` file:

   ```
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   ```

### Step 5: **Run the Bot**

1. After setting up everything, run the bot using the following command:

   ```bash
   python bot.py
   ```

### Step 6: **Start Interacting with Your Bot**

1. Open your Telegram app.
2. Search for VeenaSahuBot.
3. Start a conversation by typing **`/start`**.
4. The bot will respond with the available options.

