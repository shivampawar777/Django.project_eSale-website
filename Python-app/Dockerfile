# ___Stage 1: Base build stage___
FROM python:3.13-slim AS builder

# Set environment variables to optimize python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /build

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean



# ___Stage 2: Production stage___
FROM python:3.13-slim

#1.copy the Python dependencies from the builder stage
#2.also copy binaries from builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

#create non-root user for security
#create directory
#assign directory ownership to non-root user
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

#set working directory for production stage
WORKDIR /app

#copy source code to container alongwith set ownership & group to non-root user
COPY --chown=appuser:appuser src /app/

#switch to non-root user
USER appuser

#expose port & set env variable for real-time logs
EXPOSE 8000
ENV PYTHONUNBUFFERED=1

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "eSaleproject.wsgi:application"]