# 🚀 Deployment Update Guide

## Quick Update for Render

### Step 1: Update Start Command
1. Go to your Render dashboard: https://dashboard.render.com
2. Navigate to your backend service: `dynamic-personal-pertfolio`
3. Go to **Settings**
4. Find **Start Command**
5. Change from:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
   To:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
6. Click **Save Changes**
7. Render will automatically redeploy

### Step 2: Verify Deployment
After deployment completes (usually 2-3 minutes):
1. Visit: https://dynamic-personal-pertfolio.onrender.com/docs
2. Verify the API documentation loads
3. Test the `/api/skills/` endpoint
4. Test admin login

### Step 3: Test Frontend Connection
1. Open your deployed frontend (Vercel)
2. Check if skills section loads
3. Test login functionality
4. Verify all API calls work

---

## Alternative: Manual Git Push

If you want to push changes to GitHub first:

```bash
# Add all changes
git add .

# Commit with descriptive message
git commit -m "refactor: migrate to professional backend structure

- Reorganize code into app/ package structure
- Migrate 13 routers to app/api/v1/endpoints/
- Upgrade password hashing from SHA256 to bcrypt
- Update all imports to use new structure
- Add production-ready configs (Dockerfile, .dockerignore)
- Maintain backward compatibility with existing database"

# Push to GitHub
git push origin main
```

Then Render will auto-deploy if you have auto-deploy enabled.

---

## Environment Variables

No changes needed! The new structure uses the same `.env` file format:

```env
# Database (SQLite - already configured)
DATABASE_URL=sqlite:///./portfolio.db

# SMTP Settings (for contact form & OTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Admin Account (default)
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123

# CORS Origins (already configured for your frontend)
CORS_ORIGINS=["https://your-frontend.vercel.app"]
```

---

## Rollback Plan (if something goes wrong)

If the new structure causes issues on Render:

### Option 1: Revert Start Command
Change start command back to:
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Option 2: Use Old Files
The old structure files still exist:
- `backend/main.py` (old entry)
- `backend/routers/*.py` (old routers)

Just change the start command back and it will use the old structure.

---

## Testing Commands (Local)

Before deploying, test locally:

```bash
# Start backend
cd backend
python -m uvicorn app.main:app --reload

# In another terminal, test endpoints
curl http://localhost:8000/api/skills/
curl http://localhost:8000/docs  # Should show API documentation
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'app'"
**Solution**: Verify start command is `uvicorn app.main:app` (not `uvicorn main:app`)

### Issue: Import errors after deployment
**Solution**: Check Render build logs for missing dependencies. All dependencies are in `requirements.txt`.

### Issue: Database not found
**Solution**: Database file `portfolio.db` should be in `backend/` folder. Check if it exists.

### Issue: Uploads folder not found
**Solution**: Uploads folder should be in `backend/uploads/`. Check if it exists.

---

## Post-Deployment Checklist

After updating Render:
- [ ] API docs accessible at `/docs`
- [ ] Health check endpoint responds
- [ ] Skills endpoint returns data
- [ ] Login works correctly
- [ ] File uploads work (resume, gallery, etc.)
- [ ] Contact form sends emails
- [ ] Frontend can connect to backend
- [ ] No errors in Render logs

---

## Next Steps After Successful Deployment

1. **Test thoroughly** - All features, especially admin functions
2. **Monitor logs** - Check Render logs for any errors
3. **Update frontend** - If backend URL changed
4. **Clean up old files** - After confirming everything works:
   ```bash
   cd backend
   rm main.py config.py database.py models.py auth.py email_service.py
   rm -rf routers/
   ```
5. **Commit cleanup**:
   ```bash
   git add .
   git commit -m "chore: remove old backend structure files"
   git push
   ```

---

## Support

If you encounter any issues:
1. Check Render deployment logs
2. Review `REFACTOR_COMPLETE.md` for structure details
3. Test locally first with `uvicorn app.main:app --reload`
4. Verify all imports are correct in router files

**Remember**: The old structure files are still in place, so you can always revert by changing the start command!
