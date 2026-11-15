.DEFAULT_GOAL := help
.PHONY: help check todos roadmap stats

help: ## Show this help
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

check: ## Integrity check (duplicate IDs, dangling references, tasks)
	@python3 scripts/kb_check.py

todos: ## Ranked open tasks (filters: FUENTE=mail ACTOR=@lead TAG=venue)
	@python3 scripts/kb_todos.py $(if $(FUENTE),--fuente "$(FUENTE)") \
		$(if $(ACTOR),--actor "$(ACTOR)") $(if $(TAG),--tag "$(TAG)")

roadmap: ## Generate roadmap.html (projects, calendar and open tasks) and open it
	@python3 scripts/kb_roadmap.py && open roadmap.html

stats: ## Counts per entity type
	@printf "resources (R): %s\n"  "$$(grep -cE '^\| *R-[0-9]{4} ' registry/resources.md)"
	@printf "decisions (D): %s\n"  "$$(grep -cE '^\| *D-[0-9]{4} ' registry/decisions.md)"
	@printf "findings  (F): %s\n"  "$$(grep -cE '^\| *F-[0-9]{4} ' registry/findings.md)"
	@printf "questions (Q): %s\n"  "$$(grep -cE '^\| *Q-[0-9]{4} ' registry/questions.md)"
	@printf "people    (M): %s\n"  "$$(grep -cE '^\| *M-[0-9]{4} ' registry/people.md)"
	@printf "ideas     (I): %s\n"  "$$(grep -cE '^\| *I-[0-9]{4} ' registry/ideas.md)"
	@printf "domains:       %s\n"  "$$(find domains -name '*.md' | wc -l | tr -d ' ')"
	@printf "projects:      %s\n"  "$$(find projects -name '*.md' | wc -l | tr -d ' ')"
