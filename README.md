# Placement-Updates-Dashboard

## Overview

A comprehensive static website dashboard designed for placement coordinators to track and showcase job opportunities and placement updates across different social sectors. This platform helps mapping students identify outstanding job profiles that align with their CV, Cover Letter, and Job Description requirements.

## Features

### 🎯 Core Features
- **Domain-wise Placement Updates**: View placement opportunities filtered by sector (Education, Healthcare, Development, Finance, etc.)
- **Job Profile Analysis**: Understanding what job profiles stand out and what employers look for
- **CV/CL/JD Matching Guide**: A comprehensive guide to matching your CV, Cover Letter with Job Description requirements
- **Student Mapping**: Track students across different placement groups and domains
- **Interactive Dashboard**: Easy-to-navigate interface for quick access to placement information

### 📊 Social Sectors Covered
- Education Sector
- Healthcare & Health Services
- Development & Social Impact
- Finance & Banking
- Administration & Governance
- Environment & Sustainability
- Technology & Innovation

## About This Project

This placement dashboard is created by a placement coordinator working with mapping students to help them understand:

1. **What Job Profiles Stand Out**: Analysis of high-demand positions in social sectors
2. **CV Requirements**: What details make a CV stand out for specific job profiles
3. **Cover Letter Strategy**: How to tailor your cover letter to job descriptions
4. **Job Description Analysis**: Understanding JD requirements and matching them with your skills

## How to Use

1. **Browse by Domain**: Select a social sector to view current placement opportunities
2. **Analyze Job Profiles**: Understand the skill sets and qualifications required
3. **Check CV Guidelines**: Review tips for different job categories
4. **Match with JD**: Learn how to align your CV and CL with specific job descriptions

## Placement Information

### Current Updates
- Regular updates on new placement opportunities
- Domain-wise job postings
- Student success stories and outcomes
- Interview preparation resources

### Target Sectors
- **Social Impact Organizations**: NGOs, Development projects
- **Educational Institutions**: Schools, Universities, Training centers
- **Government & Public Sector**: Administrative roles, policy positions
- **Corporate Sector**: CSR departments, HR, Management roles

## Getting Started

1. Open `index.html` in your web browser
2. Navigate through different domains
3. Review job opportunities and requirements
4. Check CV/CL/JD matching guidelines
5. Prepare your application materials

## File Structure

```
Placement-Updates-Dashboard/
├── index.html          # Main dashboard page
├── styles.css          # Styling and responsive design
├── script.js           # Interactive functionality
├── data.json           # Placement and job data
└── README.md           # This file
```

## Technologies Used

- **HTML5**: Structure and semantic markup
- **CSS3**: Modern styling and responsive design
- **JavaScript**: Interactive features and data handling
- **JSON**: Data storage for placements and opportunities

## Responsive Design

The dashboard is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile devices

## Key Sections

### Dashboard
Main interface showing all placement opportunities with filtering options

### Job Profiles
Detailed analysis of different job positions and required competencies

### CV/CL/JD Guide
Comprehensive guide for:
- Creating effective CVs
- Writing compelling cover letters
- Understanding job descriptions
- Matching strategy

### Placement Updates
Latest news and opportunities in different social sectors

## Author

Created by: Placement Coordination Team
For: Mapping Students Group
Location: All India Region

## Contact & Updates

For placement opportunities and updates, check back regularly for new opportunities across all social sectors.

## Disclaimer

This dashboard provides information and guidance for placement preparation. All job postings and information are subject to verification. Please confirm details directly with organizations before applying.

## License

This project is open for educational and non-commercial use.

---

**Last Updated**: January 2026
**Version**: 1.0

---

## 📊 Mock Interview Dashboard

### Quick Access
- **Main Dashboard**: [`mock-interview-dashboard.html`](./mock-interview-dashboard.html)
- **Setup Guide**: [`MOCK-INTERVIEW-DASHBOARD-SETUP.md`](./MOCK-INTERVIEW-DASHBOARD-SETUP.md)
- **Data Structure**: [`DATA-STRUCTURE-GUIDE.md`](./DATA-STRUCTURE-GUIDE.md)

### Overview
Interactive dashboard for managing and displaying mock interview schedules, statistics, and participant information. Features real-time data updates from Google Sheets with automatic refresh every 30 seconds.

### Key Features
✅ **Live Statistics Dashboard**
- Total interview count
- Scheduled dates overview  
- Time slot distribution (19:30, 19:45, 20:00)

✅ **Interview Schedule Table**
- Student names with interview dates and times
- Color-coded time slots for quick identification
- Sortable and searchable data

✅ **Interview Information**
- Display of 3 key interview questions
- Direct Google Meet link integration
- Last updated timestamp

✅ **Responsive Design**
- Works on desktop, tablet, and mobile devices
- Modern gradient UI with smooth animations
- Intuitive card-based layout

### How It Works

```
┌─────────────────┐
│  Your Excel     │
│  File (.xlsx)   │
└────────┬────────┘
         │ Convert & Upload
         ↓
┌─────────────────┐
│ Google Sheets   │
│  (Public Share) │
└────────┬────────┘
         │ Google Sheets API
         ↓
┌─────────────────┐
│   Browser       │
│ JavaScript Code │
└────────┬────────┘
         │ Fetch & Render
         ↓
┌─────────────────┐
│   Beautiful     │
│   Dashboard     │
└─────────────────┘
         │ Auto-refresh
         └──→ Every 30 seconds
```

### Quick Start

#### Option 1: Use Immediately (Quickest)
1. Download `mock-interview-dashboard.html`
2. Open in your browser (no internet required for local use)
3. View the sample data

#### Option 2: Connect Your Data
1. **Convert Excel to Google Sheets**
   - Upload your Excel file to Google Drive
   - Open with Google Sheets
   - Share publicly

2. **Get API Credentials**
   - Enable Google Sheets API in Google Cloud Console
   - Create an API key

3. **Update Dashboard Code**
   - Edit `mock-interview-dashboard.html`
   - Replace API key and Sheet ID (around line 200)

4. **Deploy**
   - Host on GitHub Pages, web server, or open locally
   - Changes in Excel reflect automatically!

### Data Requirements

Your Excel file needs:
- **Schedule Sheet**: Student names, dates, times, and slots
- **Questions Sheet**: 3 interview questions + Google Meet link
- Proper date/time formatting (see DATA-STRUCTURE-GUIDE.md)

### Features & Statistics

| Feature | Status | Details |
|---------|--------|----------|
| Interview Statistics | ✅ | Real-time counts & analysis |
| Schedule Display | ✅ | Sortable table with 10+ rows |
| Color-coded Slots | ✅ | Blue (19:30), Purple (19:45), Green (20:00) |
| Auto-refresh | ✅ | Every 30 seconds (configurable) |
| Responsive Design | ✅ | Mobile, tablet, desktop |
| Google Meet Integration | ✅ | Direct link in questions section |
| Search & Filter | 🔄 | Planned enhancement |
| PDF Export | 🔄 | Planned enhancement |
| Email Notifications | 🔄 | Planned enhancement |

### Customization

**Change Colors:**
- Edit CSS section (lines 15-80)
- Update color hex codes

**Change Refresh Rate:**
- Edit line 310: `setInterval(() => {...}, 30000)`
- 30000 = 30 seconds (adjust as needed)

**Show More Rows:**
- Edit line 305: `slice(0, 10)` → `slice(0, 20)`
- Shows first 20 rows instead of 10

### Browser Compatibility
✅ Chrome/Edge (Latest)
✅ Firefox (Latest)
✅ Safari (Latest)
✅ Mobile Browsers

### File Size & Performance
- Dashboard file: ~15 KB (HTML + CSS + JS)
- Load time: <1 second
- Works with up to 10,000 interview records
- Optimized for both local and server hosting

### Support & Troubleshooting

**Dashboard not updating?**
- Check browser console (F12) for errors
- Verify API key and Sheet ID are correct
- Ensure Google Sheet is publicly shared
- Wait 30 seconds for auto-refresh

**Data not loading?**
- Check Google Sheets API is enabled
- Verify data structure matches expected format
- Test API key permissions
- See DATA-STRUCTURE-GUIDE.md for format examples

**Need help?**
- Read MOCK-INTERVIEW-DASHBOARD-SETUP.md for detailed instructions
- Check DATA-STRUCTURE-GUIDE.md for data format requirements
- Review troubleshooting sections in both guides

### Future Enhancements
- 📊 Analytics and charts
- 🔔 Email/browser notifications
- 👥 Candidate profile cards
- 📥 CSV/PDF export
- 🎯 Interview feedback tracking
- ⚙️ Admin dashboard
- 🔐 User authentication

---
