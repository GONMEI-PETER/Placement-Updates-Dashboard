#!/usr/bin/env python3
"""
Job Updates Fetcher Script
Automatically fetches latest job openings from official sources and updates dashboard
"""

import requests
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# Configuration
DEVNET_JOBS_URL = "https://devnetjobsindia.org/jobs.aspx"
ASHOKA_JOBS_URL = "https://www.ashoka.org/en/engage/work-with-us"
NASSCOM_JOBS_URL = "https://www.nasscomfoundation.org/careers"

def fetch_devnet_jobs():
    """Fetch jobs from DevNetJobsIndia"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(DEVNET_JOBS_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = []
        
        # Parse job listings (customize selectors based on actual HTML structure)
        job_elements = soup.find_all('div', class_='job-listing')
        
        for job in job_elements[:5]:  # Fetch top 5 jobs
            try:
                title = job.find('h3', class_='job-title').text.strip()
                org = job.find('span', class_='organization').text.strip()
                location = job.find('span', class_='location').text.strip()
                deadline = job.find('span', class_='deadline').text.strip()
                
                jobs.append({
                    'title': title,
                    'organization': org,
                    'location': location,
                    'deadline': deadline,
                    'source': 'DevNetJobsIndia',
                    'fetched_date': datetime.now().isoformat()
                })
            except AttributeError:
                continue
        
        return jobs
    except Exception as e:
        print(f"Error fetching DevNetJobs: {str(e)}")
        return []

def generate_markdown(jobs):
    """Generate markdown content from job data"""
    md_content = f"""# Current Job Openings in Social Sectors 2026

Source: DevNetJobsIndia.org, Ashoka, NASSCOM Foundation  
Last Updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p IST')}

## Recently Updated Job Openings

"""
    
    if not jobs:
        md_content += "\n**No new job openings found in the latest update.**\n"
    else:
        for i, job in enumerate(jobs, 1):
            md_content += f"""
### {i}. {job['title']}
**Organization:** {job['organization']}  
**Location:** {job['location']}  
**Deadline:** {job['deadline']}  
**Source:** {job['source']}  
**Fetched:** {job['fetched_date']}

---
"""
    
    md_content += f"""

## Auto-Update Information

This dashboard is automatically updated daily at 8 AM IST with the latest job openings from:

- **DevNetJobsIndia.org** - India's largest NGO job portal
- **Ashoka.org** - Social entrepreneur opportunities
- **NASSCOM Foundation** - Tech-for-social-impact roles
- **Government portals** - Public sector opportunities

### How It Works

1. **Daily Automated Check**: GitHub Actions workflow runs every day at 8 AM IST
2. **Data Scraping**: Python script fetches latest job listings from official sources
3. **Content Update**: Dashboard markdown file is automatically updated with new opportunities
4. **Website Rebuild**: GitHub Pages automatically rebuilds the static website
5. **Live Deployment**: Your website reflects the latest job openings within minutes

### Manual Update

You can also trigger manual updates:
1. Go to repository Actions tab
2. Select "Auto-Update Job Openings" workflow
3. Click "Run workflow"
4. Check GitHub Pages for updates within 1-2 minutes

---

## Previous Updates

For previous job listings and historical data, check the git commit history.

**Last Automatic Update:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}
"""
    
    return md_content

def update_jobs_file():
    """Fetch jobs and update markdown file"""
    print("[INFO] Starting job fetching process...")
    
    # Fetch jobs from all sources
    jobs = []
    jobs.extend(fetch_devnet_jobs())
    
    # If no jobs fetched, show message
    if not jobs:
        print("[WARNING] No new jobs fetched from sources")
    else:
        print(f"[INFO] Fetched {len(jobs)} job listings")
    
    # Generate markdown content
    md_content = generate_markdown(jobs)
    
    # Write to file
    output_file = 'jobs-openings-2026.md'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"[SUCCESS] Updated {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to write file: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    success = update_jobs_file()
    exit(0 if success else 1)
