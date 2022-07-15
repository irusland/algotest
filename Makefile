TEMPLATE := template


init:
	@read -p "Enter name: " name; \
	cp -r $(TEMPLATE) $$name; \
	realpath $$name
