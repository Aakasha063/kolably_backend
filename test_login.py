import asyncio
from app.core.supabase import get_supabase_client
from supabase_auth.errors import AuthApiError
from app.core.config import settings

client = get_supabase_client()
try:
    auth_response = client.auth.sign_in_with_password({
        "email": "aakasha063@gmail.com",
        "password": "aakasha063",
    })
    print("User:", auth_response.user)
    print("Session:", auth_response.session)
except AuthApiError as e:
    print("Error:", e)
