FROM python:3.11



# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code into the container
COPY . /app
 