# Automated Job Updates Guide

## Overview

Your Placement-Updates-Dashboard is configured to **automatically fetch and update job listings daily** from official sources. This guide explains how the automation works and how to manage it.

## How It Works

### Daily Automated Workflow

**Schedule:** Every day at **8:00 AM IST** (2:30 AM UTC)

**Process:**
1. GitHub Actions workflow triggers automatically
2. Python script fetches latest job openings from:
   - DevNetJobsIndia.org (Largest NGO job portal in India)
   - Ashoka.org (Social entrepreneur opportunities)
   - NASSCOM Foundation (Tech-for-social-impact roles)
   - Government career portals
3. Dashboard markdown file is updated with new job data
4. GitHub automatically commits the changes
5. GitHub Pages rebuilds your static website
6. **Changes live within 1-2 minutes**

### Components

#### 1. GitHub Actions Workflow
**File:** `.github/workflows/auto-update-jobs.yml`

- Runs on schedule: Daily at 8 AM IST
- Can be triggered manually anytime
- Automatically detects changes
- Commits only if new data found
- Rebuilds and deploys website

#### 2. Python Scraper Script
**File:** `scripts/fetch-job-updates.py`

- Fetches latest job listings from official sources
- Parses HTML/JSON responses
- Generates markdown content
- Handles errors gracefully
- Includes logging for monitoring

#### 3. Dashboard Updates
**File:** `jobs-openings-2026.md`

- Automatically updated with latest opportunities
- Maintains historical data
- Timestamps each update
- Shows last update time

---

## Manual Updates

### Trigger Manual Update Anytime

**Option 1: Via GitHub Web Interface**

1. Go to your repository: `https://github.com/GONMEI-PETER/Placement-Updates-Dashboard`
2. Click **Actions** tab
3. Select **"Auto-Update Job Openings"** workflow on the left
4. Click **"Run workflow"** button
5. Select `main` branch
6. Click **"Run workflow"** to confirm
7. **Check your live website within 2 minutes**

**Option 2: Using GitHub CLI (Command Line)**

```bash
gh workflow run auto-update-jobs.yml --ref main
```

---

## Monitoring & Status

### Check Update Status

1. Go to **Actions** tab in your repository
2. Look at **"Auto-Update Job Openings"** workflow
3. **Green checkmark** = Update successful
4. **Red X** = Update failed (check logs)
5. **Orange circle** = Update in progress

### View Workflow Logs

1. Click on any workflow run
2. See detailed step-by-step logs
3. Identify any errors or issues
4. Timestamp shows when it ran

### Check Live Website

Your live dashboard is at:
```
https://gonmei-peter.github.io/Placement-Updates-Dashboard/
```

Check the "Last Updated" timestamp to confirm it's current.

---

## Configuration & Customization

### Change Update Schedule

**To run at a different time:**

1. Edit `.github/workflows/auto-update-jobs.yml`
2. Find the line: `cron: '30 2 * * *'`
3. Change the time (format: MM HH * * *)
   - Current: 2:30 AM UTC = 8:00 AM IST
   - Examples:
     - `0 5 * * *` = 5:30 AM IST
     - `30 19 * * *` = 1:00 AM IST next day
4. Commit changes

**Cron Format Explanation:**
```
┌──────── minute (0-59)
│ ┌─────── hour (0-23)
│ │ ┌────── day of month (1-31)
│ │ │ ┌───── month (1-12)
│ │ │ │ ┌──── day of week (0-6, Sunday=0)
│ │ │ │ │
30 2 * * *
```

### Add More Job Sources

**To add more job portals:**

1. Edit `scripts/fetch-job-updates.py`
2. Add a new function: `fetch_[source]_jobs()`
3. Follow the pattern of existing functions
4. Add error handling
5. Update `update_jobs_file()` to call your function

**Example Template:**

```python
def fetch_new_source_jobs():
    """Fetch jobs from new source"""
    try:
        # Your scraping code here
        jobs = []
        # Parse and append jobs
        return jobs
    except Exception as e:
        print(f"Error: {str(e)}")
        return []
```

### Modify Update Frequency

**To update more frequently:**

```yaml
on:
  schedule:
    - cron: '0 * * * *'  # Every hour
    # - cron: '*/30 * * * *'  # Every 30 minutes
```

**⚠️ Note:** GitHub Actions has free tier limits (~2,000 minutes/month)

---

## Troubleshooting

### Updates Not Showing

**Problem:** Manual trigger didn't update website

**Solution:**
1. Check Actions tab for errors
2. Wait 2-3 minutes for GitHub Pages to rebuild
3. Clear browser cache: Ctrl+Shift+Delete (or Cmd+Shift+Delete)
4. Check incognito/private browsing mode

### Workflow Failed

**Problem:** Red X on workflow

**Solution:**
1. Click on failed workflow run
2. Check logs under "Run job scraper script"
3. Common issues:
   - Network timeout: Try manual trigger again
   - Website structure changed: Update selectors in script
   - Missing dependencies: Check Python requirements

### Old Data Still Showing

**Problem:** Dashboard shows outdated jobs

**Solution:**
1. Go to `jobs-openings-2026.md` file
2. Check "Last Updated" timestamp
3. If old: Manually trigger update
4. If recent: Clear browser cache

### Python Script Errors

**To debug locally:**

```bash
# Install requirements
pip install requests beautifulsoup4 feedparser

# Run script
python scripts/fetch-job-updates.py

# Check output
cat jobs-openings-2026.md
```

---

## Best Practices

### ✅ Do's

- ✓ Check workflow logs regularly
- ✓ Monitor live website for updates
- ✓ Keep source websites in working order
- ✓ Update HTML selectors if websites change
- ✓ Test script locally before pushing
- ✓ Document any customizations

### ❌ Don'ts

- ✗ Don't modify `jobs-openings-2026.md` manually (it's auto-generated)
- ✗ Don't disable the GitHub Actions workflow
- ✗ Don't schedule updates too frequently (wasted resources)
- ✗ Don't commit Python script changes without testing
- ✗ Don't remove `.github/workflows` folder

---

## Advanced Options

### Email Notifications on Failure

**Add to workflow file:**

```yaml
- name: Send email on failure
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: ${{ secrets.EMAIL_SERVER }}
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: 'Job Update Failed'
    body: 'Check GitHub Actions for details'
    to: your-email@example.com
```

### Slack Notifications

**When update completes, post to Slack:**

```yaml
- name: Notify Slack
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "Job dashboard updated successfully"
      }
```

### Database Backup

**Keep historical records:**

```bash
# Add to workflow to backup old data
git log --oneline jobs-openings-2026.md | head -10
```

---

## Support & Questions

### Common Questions

**Q: Will GitHub Actions cost me money?**
A: No! Free tier includes 2,000 minutes/month for private repos. Daily updates = ~2.5 minutes/month.

**Q: Can I test the script locally?**
A: Yes! Download `scripts/fetch-job-updates.py`, install requirements, and run `python fetch-job-updates.py`

**Q: What if a source website changes?**
A: Update the HTML selectors in the script. Check "Run job scraper script" logs for error messages.

**Q: Can I update more than once per day?**
A: Yes! Change the cron schedule. But GitHub free tier has limits.

---

## Next Steps

1. ✅ Verify workflow is enabled
2. ✅ Check Actions tab for successful runs
3. ✅ Monitor your live website
4. ✅ Keep source websites accessible
5. ✅ Update script if websites change structure
6. ✅ Share dashboard with students

---

**Dashboard URL:** https://gonmei-peter.github.io/Placement-Updates-Dashboard/

**Repository:** https://github.com/GONMEI-PETER/Placement-Updates-Dashboard

**Last Updated:** January 2, 2026
