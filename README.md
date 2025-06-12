# 🍽️  Recipe Generator

Welcome to the **Smart Recipe Generator**, a Flask-based web application that uses AI to generate personalized recipes based on the ingredients you have and your dietary preferences. It's a fun and helpful tool for home cooks, students, and anyone looking to make something delicious without searching for hours.


## 🌟 Features

- 🥗 Generate unique recipes using available ingredients.
- 🌱 Supports dietary preferences: Vegetarian, Vegan, Halal, Gluten-Free.
- 🎨 Beautiful modern dark-themed UI with gradient effects.
- 🤖 Powered by LLaMA model through the Together API for AI recipe generation.

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3
- **Backend**: Python (Flask)
- **AI Model**: [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) via [Together.xyz API](https://www.together.xyz/)
- **Design**: Responsive UI, modern gradient themes, animated buttons

## 🚀 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ilyaslayyah123/Recipe-Generator.git
   cd Recipe-Generator
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3.**Set API Key**
   Open utils.py and replace your_api_key_here with your actual Together.xyz API key.
4. **Run the App**
    ```bash
    python app.py
5. **Visit in Browser**
   Open http://127.0.0.1:5000 in your browser.
6. 📁 **Project Structure**
   smart-recipe-generator/
├── app.py
├── templates/
│   ├── index.html
│   └── recipie.html
├── static/
│   ├── style.css
│   └── restaurant-bg.jpg
├── utils.py
├── requirements.txt
└── README.md

7. 🧠 **Behind the Scenes**
   This app uses generative AI via the LLaMA/Mistral model to generate realistic and creative recipes. It sends user input (ingredients + dietary preference) to the model API, processes the response, and displays a step-by-step recipe on the frontend.
8. ✅ To-Do / Future Enhancements
📲 Add login and user profiles

📦 Store and favorite generated recipes

📱 Make the app mobile-responsive

🔊 Add voice input support
9. 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
🧑‍💻 Author
Muhammad Ilyas – AI Developer & Python Enthusiast

Connect with me on LinkedIn: www.linkedin.com/in/muhammad-ilyas-a59bb0289
