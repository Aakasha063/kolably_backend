-- Superadmin Seed Script
-- ════════════════════════════════════════════════════════
--
-- How to use:
-- 1. Create a user via Supabase Auth Dashboard → Authentication → Users → Add User
-- 2. Copy the user's UUID from the dashboard
-- 3. Replace '<supabase-auth-uid>' and 'admin@kolably.com' below
-- 4. Run this SQL in Supabase SQL Editor
--
-- NOTE: The auth trigger will auto-create a profiles row with the default role.
--       This script updates that row to 'superadmin'.
-- ════════════════════════════════════════════════════════

UPDATE public.profiles
SET role = 'superadmin'
WHERE auth_id = '<supabase-auth-uid>'
  AND email = 'admin@kolably.com';
