.ONESHELL:
SHELL =/usr/bin/bash

DOCKER=docker compose -f compose.yml -f data.compose.yml -f llm.compose.yml
llm_pull:
	# git clone --depth 1 git@github.com:armandobs14/unitycatalog.git build/unitycatalog
	# docker compose build unity_catalog
	# models:
	# - llama3.2:3b
	# - qwen2:0.5b
	# - deepseek-r1
	$(DOCKER) exec ollama sh -c "ollama pull $(model)"


up:
	$(DOCKER) up -d

down:
	$(DOCKER) down

logs:
	$(DOCKER) logs $(service)

restart:
	$(DOCKER) restart $(service)