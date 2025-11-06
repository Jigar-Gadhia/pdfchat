# 📄 PDF Q&A Bot with Gemini & LangChain

Ask natural language questions about your PDF documents and get accurate, grounded answers using **Google Gemini** and **Retrieval-Augmented Generation (RAG)** — all running locally with no external hosting required.

Built with:
- **LangChain** for orchestration
- **Gemini 2.5 pro** for smart answers
- **FAISS + Hugging Face embeddings** for local, private document search
- **Pipenv** for dependency management

Perfect for researchers, analysts, students, or anyone who needs to quickly extract insights from long reports, manuals, or papers — without reading them cover to cover.

## 🚀 Quick Start

### Clone the repo
```
git clone https://github.com/Jigar-Gadhia/pdfchat.git
```
```
cd pdfchat
```

### Set up your environment

### 1. **Install dependencies with Pipenv**
```
pipenv install
```

### 2. **Activate the virtual environment**
```
pipenv shell
```

### Add your PDF

### 1. **Place your PDF(s) in the data/source_pdfs/ folder**
```
cp /path/to/your/document.pdf data/source_pdfs/
```

### Set up your Gemini API key

### 1. **Create a .env file in the project root**
### Generate the api key from below url
https://aistudio.google.com/api-keys
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Ingest your PDF(s)

### 1. Run the ingestion script to build the searchable vector database
```
python -m pdf_qa.ingest
```

### Ask questions!

### 1. Start the interactive Q&A console
```
python app.py
```
### Example
```
❓ Your question: What are the main conclusions of the report?
💡 Answer: The study concludes that renewable energy adoption has increased by 42% since 2020...
```
