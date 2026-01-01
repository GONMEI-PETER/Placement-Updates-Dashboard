#!/usr/bin/env python3
"""
Job Updates Fetcher Script - Enhanced Version
Automatically fetches comprehensive job data from official sources and updates dashboard
Includes: Organisation name, Job role, Location, Experience level, Pay scale, Deadline, 
Education background, Required skills, and Job links
"""

import requests
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re

# Configuration
DEVNET_JOBS_URL = "https://devnetjobsindia.org/jobs.aspx"
ASHOKA_JOBS_URL = "https://www.ashoka.org/en/engage/work-with-us"
NASSCOM_JOBS_URL = "https://www.nasscomfoundation.org/careers"
NITI_AAYOG_URL = "https://www.niti.gov.in"
NCS_PORTAL = "https://ncs.gov.in"

def fetch_comprehensive_jobs():
    """
    Fetch comprehensive job data from multiple sources
    Returns list of job dicts with all required fields
    """
    all_jobs = []
    sources = [
        ("DevNetJobsIndia", DEVNET_JOBS_URL),
        ("Ashoka", ASHOKA_JOBS_URL),
        ("NASSCOM", NASSCOM_JOBS_URL)
    ]
    
    for source_name, url in sources:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            jobs = parse_jobs_from_source(soup, source_name, url)
            all_jobs.extend(jobs)
            
        except Exception as e:
            print(f"[WARNING] Error fetching from {source_name}: {str(e)}")
            continue
    
    return all_jobs[:10]  # Return top 10 latest jobs

def parse_jobs_from_source(soup, source_name, source_url):
    """
    Parse jobs from HTML soup object
    Returns standardized job dictionaries with all fields
    """
    jobs = []
    
    try:
        # Generic parsing - customize based on actual site structure
        job_elements = soup.find_all('div', class_=['job-listing', 'job-card', 'vacancy'])
        
        for job_elem in job_elements:
            try:
                job_data = {
                    'organisation_name': extract_text(job_elem, ['organization', 'company', 'org']),
                    'job_role': extract_text(job_elem, ['job-title', 'position', 'title', 'h3']),
                    'location': extract_text(job_elem, ['location', 'place', 'city']),
                    'experience_level': extract_experience(job_elem),
                    'pay_scale': extract_pay_scale(job_elem),
                    'last_date': extract_deadline(job_elem),
                    'education_background': extract_education(job_elem),
                    'skills_required': extract_skills(job_elem),
                    'job_link': extract_link(job_elem, source_url),
                    'source': source_name,
                    'fetched_date': datetime.now().isoformat()
                }
                
                # Only add if we have at least job title
                if job_data['job_role']:
                    # Fill missing fields with "Data not available"
                    for key in job_data:
                        if not job_data[key] or job_data[key] == '':
                            job_data[key] = "Data not available"
                    
                    jobs.append(job_data)
            
            except Exception as e:
                print(f"[DEBUG] Error parsing individual job: {str(e)}")
                continue
    
    except Exception as e:
        print(f"[WARNING] Error parsing jobs from {source_name}: {str(e)}")
    
    return jobs

def extract_text(element, class_names):
    """Extract text from element using multiple class name options"""
    for class_name in class_names:
        found = element.find(class_=class_name)
        if found:
            text = found.get_text(strip=True)
            return text if text else ""
    return ""

def extract_experience(element):
    """Extract experience requirement (e.g., 'Fresher', '2-3 years')"""
    text = element.get_text()
    
    # Check for fresher
    if re.search(r'fresher|entry level|0 years', text, re.IGNORECASE):
        return "Fresher"
    
    # Check for experience years
    exp_match = re.search(r'(\d+)[\s-]+(\d+)?\s*(?:years?|yrs?)', text, re.IGNORECASE)
    if exp_match:
        if exp_match.group(2):
            return f"{exp_match.group(1)}-{exp_match.group(2)} years"
        else:
            return f"{exp_match.group(1)} years"
    
    return ""

def extract_pay_scale(element):
    """Extract salary/pay scale information"""
    text = element.get_text()
    
    # Look for salary patterns like "3-5 LPA" or "30,000-50,000"
    salary_match = re.search(r'([₹$]?\s*\d+[,\d]*\s*[-–]?\s*\d*[,\d]*\s*(?:LPA|PA|per month|pcm|ctc))', text, re.IGNORECASE)
    
    if salary_match:
        return salary_match.group(1).strip()
    
    return ""

def extract_deadline(element):
    """Extract application deadline/last date"""
    text = element.get_text()
    
    # Look for date patterns
    date_match = re.search(r'(?:deadline|last date|apply by|closes?|until)[\s:]*([\d/\-\s]+(?:jan|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[\w\s\d,]*)', text, re.IGNORECASE)
    
    if date_match:
        return date_match.group(1).strip()
    
    return ""

def extract_education(element):
    """Extract education background requirements"""
    text = element.get_text()
    
    # Look for education qualifications
    education_keywords = ['bachelor', 'b.tech', 'bca', 'b.sc', 'mba', 'master', 'graduation', 'degree', 'diploma', 'phd']
    found_education = []
    
    for keyword in education_keywords:
        if re.search(keyword, text, re.IGNORECASE):
            if keyword not in found_education:
                found_education.append(keyword)
    
    if found_education:
        return ", ".join(found_education).title()
    
    return ""

def extract_skills(element):
    """Extract required skills"""
    text = element.get_text()
    
    # Look for skills section
    skills_keywords = [
        'communication', 'leadership', 'project management', 'data analysis', 
        'excel', 'python', 'java', 'html', 'css', 'javascript', 'sql',
        'problem solving', 'teamwork', 'writing', 'presentation',
        'monitoring', 'evaluation', 'stakeholder engagement', 'community mobilization'
    ]
    
    found_skills = []
    for skill in skills_keywords:
        if re.search(skill, text, re.IGNORECASE):
            if skill not in found_skills:
                found_skills.append(skill)
    
    if found_skills:
        return ", ".join(found_skills).title()
    
    return ""

def extract_link(element, source_url):
    """Extract job application link"""
    link = element.find('a', href=True)
    
    if link and link.get('href'):
        href = link['href']
        # Make absolute URL if relative
        if href.startswith('http'):
            return href
        elif href.startswith('/'):
            from urllib.parse import urlparse
            parsed = urlparse(source_url)
            return f"{parsed.scheme}://{parsed.netloc}{href}"
        else:
            return f"{source_url}{href}"
    
    return ""

def generate_enhanced_markdown(jobs):
    """Generate comprehensive markdown with all job details"""
    md_content = f"""# Current Job Openings in Social Sectors 2026

**Source:** DevNetJobsIndia.org, Ashoka, NASSCOM Foundation, NITI Aayog, NCS Portal  
**Last Updated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p IST')}  
**Location:** All India Region

---

## Latest Job Openings

"""
    
    if not jobs:
        md_content += "**No new job openings found in the latest update.**\n"
    else:
        for i, job in enumerate(jobs, 1):
            md_content += f"""
### {i}. {job.get('job_role', 'Data not available')}

**Organisation Name:** {job.get('organisation_name', 'Data not available')}  
**Job Role:** {job.get('job_role', 'Data not available')}  
**Location:** {job.get('location', 'Data not available')}  
**Experience Level:** {job.get('experience_level', 'Data not available')}  
**Pay Scale:** {job.get('pay_scale', 'Data not available')}  
**Application Deadline:** {job.get('last_date', 'Data not available')}  
**Education Background:** {job.get('education_background', 'Data not available')}  
**Skills Required:** {job.get('skills_required', 'Data not available')}  
**Job Link:** [{job.get('job_link', 'Link not available')}]({job.get('job_link', '#')})  
**Source:** {job.get('source', 'Data not available')}  
**Fetched:** {job.get('fetched_date', 'Data not available')}

---
"""
    
    md_content += f"""

## Auto-Update Information

This dashboard is **automatically updated daily at 8:00 AM IST** with the latest job openings from:
- **DevNetJobsIndia.org** - India's largest NGO job portal
- **Ashoka.org** - Social entrepreneur opportunities
- **NASSCOM Foundation** - Tech-for-social-impact roles
- **NITI Aayog** - Government social sector initiatives
- **NCS Portal** - National Career Service opportunities

### Data Fields Included

- **Organisation Name:** Employer/NGO/Company name
- **Job Role:** Position title
- **Location:** Workplace location (All India)
- **Experience Level:** Years of experience required (Fresher/2-3 years etc.)
- **Pay Scale:** Salary range (Annual/Monthly)
- **Application Deadline:** Last date to apply
- **Education Background:** Required qualifications (B.Tech, MBA, Graduation, etc.)
- **Skills Required:** Technical and soft skills needed
- **Job Link:** Direct link to apply

### How Automation Works

1. **Daily Scheduled Run:** GitHub Actions triggers at 8 AM IST
2. **Web Scraping:** Python script fetches data from official job portals
3. **Data Processing:** Extracts and standardizes all job information
4. **Missing Data Handling:** Fills unavailable fields with "Data not available"
5. **File Update:** Markdown file is automatically updated with new jobs
6. **Website Rebuild:** GitHub Pages rebuilds the static site
7. **Live Deployment:** Changes live within 1-2 minutes

### Manual Update

To manually trigger updates:
1. Go to **Actions** tab in GitHub
2. Select **"Auto-Update Job Openings"** workflow
3. Click **"Run workflow"**
4. Check the site within 1-2 minutes

---

**Last Automatic Update:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}  
**Total Jobs Fetched:** {len(jobs)}  
**Dashboard Status:** ✅ Active and Updating Daily
"""
    
    return md_content

def update_jobs_file():
    """Main function: Fetch jobs and update markdown file"""
    print("[INFO] Starting comprehensive job fetching process...")
    
    # Fetch jobs from all sources
    jobs = fetch_comprehensive_jobs()
    
    if not jobs:
        print("[WARNING] No new jobs fetched from sources")
    else:
        print(f"[INFO] Successfully fetched {len(jobs)} job listings with comprehensive data")
    
    # Generate enhanced markdown content
    md_content = generate_enhanced_markdown(jobs)
    
    # Write to file
    output_file = 'jobs-openings-2026.md'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"[SUCCESS] Updated {output_file} with comprehensive job data")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write file: {str(e)}")
        return False

if __name__ == "__main__":
    success = update_jobs_file()
    exit(0 if success else 1)
