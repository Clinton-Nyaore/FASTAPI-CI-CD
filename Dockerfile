#-----------------------------------------
# BUILD STAGE - Install dependencies only 
#-----------------------------------------

# Base image using Python 3.11
FROM python:3.11-slim AS builder

# Set working directory inside container to /app
WORKDIR /app

# Copy all files from host dir to container /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#-----------------------------------------
# RUNTIME STAGE - Final runtime image
#-----------------------------------------

FROM python:3.11-slim
WORKDIR /app

# Create non-root user
RUN adduser --disabled-password appuser
USER appuser

# Coppy Dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Cop application files 
COPY main.py .
COPY modules/ modules/
COPY models/ models/

# Environment Variable
ENV PYTHONUNBUFFERED=1

# Expose port 8000
EXPOSE 8000

# Default CMD executed when container starts
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]