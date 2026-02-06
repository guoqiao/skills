cli := clawhub

i:
	npm i -g ${cli}

login:
	@echo "login vit oauth"
	${cli} $@

list:
	@echo "list installed skills"
	${cli} $@

