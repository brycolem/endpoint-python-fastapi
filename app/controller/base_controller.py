from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
def root(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "_links": {
            "self": {"href": f"{base_url}/"},
            "swagger_docs": {"href": f"{base_url}/docs", "method": "GET"},
            "get_all_applications": {"href": f"{base_url}/application", "method": "GET"},
            "get_application": {"href": f"{base_url}/application/{{application_id}}", "method": "GET"},
            "create_application": {"href": f"{base_url}/application", "method": "POST"},
            "update_application": {"href": f"{base_url}/application/{{application_id}}", "method": "PUT"},
            "patch_application": {"href": f"{base_url}/application/{{application_id}}", "method": "PATCH"},
            "delete_application": {"href": f"{base_url}/application/{{application_id}}", "method": "DELETE"}
        }
    }
