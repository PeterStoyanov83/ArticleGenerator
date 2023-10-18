![image](https://github.com/PeterStoyanov83/ArticleGenerator/assets/108938447/854c24f8-c55c-4829-b2b1-90b521ee0644)
![image](https://github.com/PeterStoyanov83/ArticleGenerator/assets/108938447/c4b53a1c-a506-496a-a983-81acf0b33a47)


---

# Article Generator with Django and GPT-4

## Overview

This project is a Django-based web application that automatically generates articles on various topics using OpenAI's GPT-4 language model. The application allows users to select a topic, and then it generates an article related to that topic.
---

*__Note: This project is just an idea that I have started. It needs a lot more work to be complete. Contributions are welcomed.__*

---

## Features

- **Random Topic Selection**: Picks a random topic from a predefined list of topics stored in the database.
- **Article Generation**: Uses GPT-4 to generate a unique article based on the selected topic.
- **Database Storage**: Stores the generated articles in a database for future reference.
- **Management Commands**: Custom Django management command to trigger article generation.

## Tech Stack

- **Backend**: Python, Django
- **Database**: SQL
- **Other Libraries**: OpenAI's GPT-4

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/YourUsername/ArticleGenerator.git
    ```
2. Navigate to the project directory
    ```bash
    cd ArticleGenerator
    ```
3. Create a virtual environment and activate it
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the root directory to store your OpenAI API key
    ```bash
    OPENAI_API_KEY=your-api-key-here
    ```
6. Run migrations
    ```bash
    python manage.py migrate
    ```
7. Start the development server
    ```bash
    python manage.py runserver
    ```

## Usage

get yourself an API Key - Replace the existing one (since OpenAI don't allow public view on private keys) 



To generate an article, run the custom management command:

```bash
python manage.py generate_article
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

