SHELL :=/bin/bash

.PHONY: clean check setup
.DEFAULT_GOAL=help
VENV_DIR = .venv
PYTHON_VERSION = python3.12

check: # Ruff check
	@ruff check .
	@echo "✅ Check complete!"

fix: # Fix auto-fixable linting issues
	@ruff check app_api.py --fix

clean: # Clean temporary files
	@rm -rf __pycache__ .pytest_cache
	@find . -name '*.pyc' -exec rm -r {} +
	@find . -name '__pycache__' -exec rm -r {} +
	@rm -rf build dist
	@find . -name '*.egg-info' -type d -exec rm -r {} +

api: # Run the API application
	@python app_api.py --port=8888
	@echo "✅ API is running!"

chat: # Run the chat_bot script
	@streamlit run ./app/web/chat_bot.py --server.port=8081
	@echo "✅ ChatBot is running!"

chathistory: # Run the chat_history script
	@streamlit run ./app/web/chat_history.py --server.port=8082
	@echo "✅ Chat history is running!"

chatpdf: # Run the chat_pdf script
	@streamlit run ./app/web/chat_pdf.py --server.port=8083
	@echo "✅ Chat PDF is running!"

translate: # Run the chat_translation script
	@streamlit run ./app/web/chat_translation.py --server.port=8084
	@echo "✅ Translation is running!"

extract: # Run the chat_extraction script
	@streamlit run ./app/web/chat_extraction.py --server.port=8085
	@echo "✅ Extraction is running!"

setup: # Initial project setup
	@echo "Creating virtual env at: $(VENV_DIR)"s
	@$(PYTHON_VERSION) -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	@source $(VENV_DIR)/bin/activate && pip install -r requirements/requirements-dev.txt && pip install -r requirements/requirements.txt
	@echo -e "\n✅ Done.\n🎉 Run the following commands to get started:\n\n ➡️ source $(VENV_DIR)/bin/activate\n ➡️ make run\n"


help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
