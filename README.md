# Hacker News Top Stories

This project simply displays the top 10 stories from Hacker News using a Django backend API and a React frontend.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (Latest verison)
- Node.js 
- pip 
- npm 
- After that You can use this API as frontend and backend

## Backend Setup (Django)

1. Clone the repository:
   ```
   git clone https://github.com/shakil-ahmmed-se/hacker-news.git
   cd hacker-news
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   ```
   You can user global but recommmed for this one use virtual environment

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the Django development server:
   ```
   py manage.py runserver
   or
   python manage.py runserver
   ```

The backend API should now be running at `http://localhost:8000`.

## Frontend Setup (React)

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

The frontend should now be running at `http://localhost:3000`.

## Using the Application

Open your web browser and go to `http://localhost:3000`. You should see a list of the top 10 Hacker News stories. Each story displays the title (which links to the original article, when you click the link you will go original stories and see original post), author, score, and time of submission.

## API Endpoints

- To get top 10 Stories you should use `https://hacker-news-ykvv.onrender.com/api/top-stories/`
- `GET /api/top-stories/`: Retrieves the top 10 Hacker News stories.


## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request, or open an issue for discussion.
