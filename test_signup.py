import asyncio
from app.core.supabase import get_supabase_client
from supabase_auth.errors import AuthApiError
from app.core.config import settings

client = get_supabase_client()
import random
try:
    auth_response = client.auth.sign_up({
        "email": f"test{random.randint(1, 1000)}@kolably.com",
        "password": "Password123!",
        "options": {"data": {"role": "creator"}}
    })
    print("User:", auth_response.user)
    print("Session:", auth_response.session)
except AuthApiError as e:
    print("Error:", e)
