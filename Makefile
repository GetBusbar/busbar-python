# Busbar Admin API — Python SDK
#
# The client under busbar_admin/ is generated from openapi.json and committed so
# consumers install without regenerating. `make generate` re-derives it.

GENERATOR_VERSION := 0.29.1
CONFIG := openapi-python-client.yaml
SPEC := openapi.json
PACKAGE := busbar_admin

.PHONY: generate verify install-generator check-generator clean

# Re-derive the committed client from the OpenAPI spec.
# openapi-python-client --meta setup emits a full project into ./busbar-admin/;
# we flatten it into the repo root (package dir + setup.py) to match the layout.
generate: check-generator
	openapi-python-client generate \
		--path $(SPEC) \
		--meta setup \
		--config $(CONFIG) \
		--custom-template-path templates \
		--overwrite
	rm -rf $(PACKAGE) setup.py
	mv busbar-admin/$(PACKAGE) ./
	mv busbar-admin/setup.py ./
	mv busbar-admin/README.md ./GENERATED_CLIENT.md
	rm -rf busbar-admin
	python scripts/generate_compatibility.py
	@echo "Generated $(PACKAGE)/ from $(SPEC)."

# Refuse toolchain drift before touching generated sources.
check-generator:
	@test "$$(openapi-python-client --version)" = "openapi-python-client version: $(GENERATOR_VERSION)" || { echo "Install the pinned generator with 'make install-generator'." >&2; exit 1; }

# Pin the generator (used by CI + `make generate`).
install-generator:
	pip install "openapi-python-client==$(GENERATOR_VERSION)"

# Editable install + import smoke test.
verify:
	pip install -e .
	python -c "from busbar_admin.api.default import get_api_v1_admin_info; from busbar_admin.models import InfoView; print('import OK; typed InfoView =', InfoView)"

clean:
	rm -rf build dist *.egg-info
