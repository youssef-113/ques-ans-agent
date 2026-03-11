# 1️⃣ Base image with Conda installed
FROM continuumio/miniconda3:latest

# 2️⃣ Environment variables (production-safe)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Set working directory inside container
WORKDIR /app

# 4️⃣ Copy conda environment file first (for caching)
COPY environment.yml .

# 5️⃣ Create conda environment
RUN conda env create -f environment.yml && conda clean -afy

# 6️⃣ Make conda env the default shell
SHELL ["conda", "run", "-n", "ai-agent", "/bin/bash", "-c"]

# 7️⃣ Copy application code
COPY app/ ./app/

# 8️⃣ Expose FastAPI port
EXPOSE 8000

# 9️⃣ Start the application (production command)
CMD ["conda", "run", "-n", "ai-agent", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
