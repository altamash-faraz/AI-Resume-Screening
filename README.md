# 📄 AI Resume Screening & Ranking System

Rank resumes based on job descriptions using AI-powered similarity matching. Built with Streamlit for an interactive web experience.

## Features

- Upload multiple PDF resumes
- Enter a job description
- AI ranks resumes by similarity to the job description
- Color-coded ranking table

## Demo Screenshot

![Demo Screenshot](demo_screenshot.png) <!-- Add screenshot if available -->

## Getting Started

### Prerequisites

- Python 3.8+
- The following Python packages (see `requirements.txt`):
  - streamlit
  - PyPDF2
  - pandas
  - scikit-learn

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/altamash-faraz/AI-Resume-Screening.git
   cd AI-Resume-Screening
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

```bash
streamlit run AI-Resume-Screening.py
```

Open the provided local URL in your browser.

## Deploying for Free (Streamlit Community Cloud)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub and create a new app
3. Select your repository and set the main file to `AI-Resume-Screening.py`
4. Streamlit will auto-install from `requirements.txt` and deploy your app

## Usage

1. Enter the job description in the left panel
2. Upload one or more PDF resumes in the right panel
3. View ranked resumes in the results table

## License

MIT

## Author

[altamash-faraz](https://github.com/altamash-faraz)
