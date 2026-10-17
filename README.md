# AI Job Matcher
![Automated Tests](https://github.com/4pi314/ai-job-matcher/actions/workflows/tests.yml/badge.svg)

A Python and Streamlit web application that compares a résumé with a job description, calculates a similarity score, and identifies matched and missing technical skills.

## Live Demo

[Try the AI Job Matcher](https://alaa-ai-job-matcher.streamlit.app)

## Features

- Calculates résumé-to-job similarity using TF-IDF
- Uses cosine similarity to generate a match percentage
- Extracts recognized technical skills from both texts
- Displays matched and missing skills
- Handles empty or invalid input
- Includes automated tests with pytest
- Provides an interactive Streamlit interface
- Supports PDF, DOCX, and TXT résumé uploads
- Calculates separate text-similarity and skill-coverage scores
- Combines both measurements into a transparent overall score
- Supports containerized deployment with Docker

## Technologies

- Python 3
- Streamlit
- scikit-learn
- pytest
- Git and GitHub
- Ubuntu through WSL 2
- pypdf
- python-docx
- GitHub Actions
- Docker

## How It Works

1. The user enters résumé text and a job description.
2. TF-IDF converts both documents into numerical vectors.
3. Cosine similarity measures how closely the documents match.
4. The skill-analysis engine extracts recognized technical skills.
5. The application displays:
   - Overall match percentage
   - Matched skills
   - Missing skills

## Project Structure

```text
ai-job-matcher/
├── app.py
├── document_parser.py
├── matcher.py
├── pyproject.toml
├── requirements.txt
├── tests/
│   └── test_matcher.py
├── Dockerfile
├── .dockerignore
└── README.md

```

## Installation

Clone the repository:

```bash
git clone https://github.com/4pi314/ai-job-matcher.git
cd ai-job-matcher
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser if it does not open automatically.

## Run with Docker

Build the Docker image:

```bash
docker build -t ai-job-matcher:latest .
```

Run the container:

```bash
docker run --rm -d \
  --name ai-job-matcher \
  -p 8501:8501 \
  ai-job-matcher:latest
```

Open `http://localhost:8501` in your browser.

Stop the container:

```bash
docker stop ai-job-matcher
```

## Run the Tests

```bash
pytest -v
```

## Example

**Résumé skills:**

```text
Python SQL Git
```

**Job requirements:**

```text
Python SQL Docker Git
```

**Result:**

- Match score: 77.7%
- Matched skills: Git, Python, SQL
- Missing skill: Docker

## Current Limitations

- Skill detection currently uses a predefined technical-skills list.
- The match score measures textual similarity rather than candidate suitability.
- The application currently accepts pasted text rather than uploaded documents.

## Planned Improvements


- Expanded skill recognition
- Résumé improvement recommendations
- Public cloud deployment



## Author

**Alaa Alahmad**

Computer Science graduate and MSCS student interested in software engineering, artificial intelligence, machine learning, NLP, and computer vision.