# Busbar Admin API — Python SDK
#
# The client under busbar_admin/ is generated from openapi.json and committed so
# consumers install without regenerating. `make generate` re-derives it.

GENERATOR_VERSION := 0.29.0
CONFIG := openapi-python-client.yaml
SPEC := openapi.json
PACKAGE := busbar_admin

.PHONY: generate verify install-generator clean

# Re-derive the committed client from the OpenAPI spec.
# openapi-python-client --meta setup emits a full project into ./busbar-admin/;
# we flatten it into the repo root (package dir + setup.py) to match the layout.
generate:
	rm -rf $(PACKAGE) setup.py busbar-admin
	openapi-python-client generate \
		--path $(SPEC) \
		--meta setup \
		--config $(CONFIG) \
		--overwrite
	mv busbar-admin/$(PACKAGE) ./
	mv busbar-admin/setup.py ./
	mv busbar-admin/README.md ./GENERATED_CLIENT.md
	rm -rf busbar-admin
	@echo "Generated $(PACKAGE)/ from $(SPEC)."

# Pin the generator (used by CI + `make generate`).
install-generator:
	pip install "openapi-python-client==$(GENERATOR_VERSION)"

# Editable install + import smoke test.
verify:
	pip install -e .
	python -c "from busbar_admin.api.default import get_api_v1_admin_info; from busbar_admin.models import InfoView; print('import OK; typed InfoView =', InfoView)"

clean:
	rm -rf build dist *.egg-info
