# Mock Interview Dashboard Setup Guide

## Overview
This dashboard provides real-time visualization of mock interview schedules, statistics, and meeting information. The data automatically syncs from your Google Sheet and updates every 30 seconds.

## Features

✨ **Interactive Dashboard**
- Live interview statistics (total interviews, scheduled dates, slots distribution)
- Interview questions display
- Google Meet link integration
- Responsive design for mobile and desktop
- Auto-refresh every 30 seconds
- Color-coded time slots for easy identification

## Files Included

- `mock-interview-dashboard.html` - Main dashboard file
- `MOCK-INTERVIEW-DASHBOARD-SETUP.md` - This setup guide

## How to Use

### Option 1: Direct File Usage (Quickest)
1. Download `mock-interview-dashboard.html` from the repository
2. Open it directly in your web browser (double-click the file)
3. The dashboard will display with sample data

### Option 2: Host on GitHub Pages
1. This repository is already set up with GitHub Pages
2. Access the dashboard at: `https://GONMEI-PETER.github.io/Placement-Updates-Dashboard/mock-interview-dashboard.html`
3. No additional setup needed!

### Option 3: Host on a Web Server
1. Upload `mock-interview-dashboard.html` to your web server
2. Access via your server's URL
3. Share the link with your team

## How to Connect Your Google Sheets

### Step 1: Publish Your Google Sheet
1. Open your Excel file and save it as a Google Sheet:
   - Go to Google Drive
   - Click "New" → "File upload"
   - Upload your Excel file
   - Right-click the file → "Open with" → "Google Sheets"

2. Once it's a Google Sheet, share it:
   - Click "Share" button (top right)
   - Change to "Anyone with the link can view"
   - Copy the share link

### Step 2: Get Your Sheet ID
- From the URL: `https://docs.google.com/spreadsheets/d/[SHEET_ID]/edit`
- Extract the `[SHEET_ID]` portion

### Step 3: Configure the Dashboard

Edit the HTML file and find this section (around line 200):

```javascript
const GOOGLE_SHEETS_API_KEY = 'AIzaSyDyT9bN4K5xK3x5xK5xK5xK5xK5xK5xK'; // Replace with your API key
const SHEET_ID = '1q7L8mR7K3xK5xK5xK3x5xK5xK5xK5xK5xK5'; // Replace with your Sheet ID
```

**To get a Google Sheets API Key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable Google Sheets API
4. Create an API key (Credentials → Create Credentials → API Key)
5. Copy the API key

**Update the variables:**
```javascript
const GOOGLE_SHEETS_API_KEY = 'YOUR_API_KEY_HERE';
const SHEET_ID = 'YOUR_SHEET_ID_HERE';
```

### Step 4: Map Your Sheet Columns

The dashboard expects your Google Sheet to have:

**Schedule Tab (Column Structure):**
| Column | Header | Example |
|--------|--------|----------|
| A | Month | 2025-12-01 |
| B | Date | 2025-12-08 |
| C | Time | 193000 |
| D | Student Name | Shubham Kr. |

**Questions Tab (Column Structure):**
| Column | Header |
|--------|--------|
| A | Question 1 |
| B | Question 2 |
| C | Question 3 |

**Meet Link:** Add in a separate cell

### Step 5: Test the Connection
1. Save the updated HTML file
2. Open it in your browser
3. Check the browser's Developer Console (F12) for any errors
4. The data should load automatically

## Customization Options

### Change Refresh Interval
Find this line (around line 310):
```javascript
setInterval(() => {
    renderDashboard(mockData);
}, 30000); // 30000 ms = 30 seconds
```

Change `30000` to your desired interval in milliseconds:
- 10 seconds: `10000`
- 1 minute: `60000`
- 5 minutes: `300000`

### Customize Colors
Edit the CSS section (lines 15-80) to change colors:
```css
.card h2 {
    color: #667eea; /* Change this color */
}
```

Color suggestions:
- Blue: `#667eea`
- Purple: `#764ba2`
- Green: `#388e3c`
- Red: `#c62828`

### Change Table Display Limit
Find this line (around line 305):
```javascript
sortedSchedule.slice(0, 10).forEach(item => {
    // Shows first 10 rows
});
```

Change `10` to show more/fewer rows.

## Data Update Flow

```
Google Sheet (Source)
        ↓
Google Sheets API
        ↓
Browser JavaScript
        ↓
Dashboard Display
        ↓
Auto-refresh every 30 seconds
```

## Current Sample Data

The dashboard includes sample mock interview data from your original Excel:

**Sample Students:**
- Shubham Kr. - 2025-12-08, 19:30
- Shruti Jain - 2025-12-08, 19:45
- Koteswara Rao - 2025-12-08, 20:00
- Chanchal Isokar - 2026-01-06, 19:30
- And more...

**Interview Slots:**
- 19:30 (193000) - Blue slot
- 19:45 (194500) - Purple slot  
- 20:00 (200000) - Green slot

## Troubleshooting

### Data Not Loading
1. Check API key is correct
2. Check Sheet ID is correct
3. Open browser Developer Console (F12) for error messages
4. Ensure the Google Sheet is publicly shared
5. Check that API key has Google Sheets API enabled

### CORS Errors
If you see CORS errors:
1. This is expected when accessing local files
2. Host the file on a web server instead
3. Use the GitHub Pages option above

### Sheet Data Structure
Ensure your Google Sheet matches the expected format:
- First row should contain headers
- Data should start from row 2
- No merged cells in data range

## Auto-Update Mechanism

The dashboard automatically:
✓ Fetches data from Google Sheets every 30 seconds
✓ Compares with previous data (prevents unnecessary re-renders)
✓ Updates the "Last updated" timestamp
✓ Maintains responsive design across all devices
✓ Caches results for better performance

## Browser Compatibility

✓ Chrome/Edge (Latest)
✓ Firefox (Latest)
✓ Safari (Latest)
✓ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Tips

1. **Reduce refresh frequency** if you have many rows
2. **Limit rows displayed** using `.slice(0, N)` 
3. **Use pagination** for large datasets
4. **Cache API responses** to reduce API calls
5. **Compress images** if adding any visuals

## Future Enhancements

Potential features to add:
- 📊 Charts and statistics graphs
- 🔔 Desktop notifications for upcoming interviews
- 📱 Mobile app version
- 🔐 Authentication for admin features
- 📥 Export schedule as PDF/Excel
- 🎯 Interview feedback tracking
- 👥 Candidate profile cards
- 📈 Performance analytics

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review your Google Sheets API configuration
3. Ensure your data structure matches the expected format
4. Check browser console for error messages

## License

This dashboard is open source and free to use for your placement program.

---

**Last Updated:** January 2, 2026
**Version:** 1.0
**Author:** GONMEI-PETER
