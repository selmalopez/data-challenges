
FUNCTION_NAME=hacker-scrap
REGION=europe-west1
CODE_SOURCE_PATH=.
CODE_ENTRY_POINT=storage_upload
RUNTIME=python39
TIMEOUT=60s

deploy_function:
	gcloud functions deploy ${FUNCTION_NAME} \
		--region ${REGION} \
		--trigger-http \
		--no-allow-unauthenticated \
		--source ${CODE_SOURCE_PATH} \
		--entry-point ${CODE_ENTRY_POINT} \
		--runtime ${RUNTIME} \
		--timeout ${TIMEOUT}
