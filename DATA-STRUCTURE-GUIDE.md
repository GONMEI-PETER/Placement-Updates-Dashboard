# Mock Interview Dashboard - Data Structure Guide

## Required Excel Sheet Format

Your Excel file must have the following structure for the dashboard to work correctly. The dashboard expects data to be organized into multiple sheets.

---

## Sheet 1: "Schedule" (or "Sheet Schedule")

This sheet contains all mock interview scheduling information.

### Column Headers (Row 1)
| Column | Field Name | Description | Example |
|--------|-----------|-------------|----------|
| A | Month | Start month of the batch | 2025-12-01 |
| B | Date | Scheduled interview date | 2025-12-08 |
| C | Time | Interview time slot | 193000 |
| D | Student Name | Full name of the student | Shubham Kumar |

### Data Format Requirements

**Month Column (A):**
- Format: YYYY-MM-DD
- Example: 2025-12-01, 2026-01-01, 2026-02-01
- Purpose: Identifies the batch/month the student belongs to

**Date Column (B):**
- Format: YYYY-MM-DD
- Example: 2025-12-08, 2025-12-09, 2025-12-10
- Must be a valid date
- Should be after the month date

**Time Column (C):**
- Format: HHMMSS (24-hour format, no colons)
- Examples:
  - 193000 = 19:30 (7:30 PM)
  - 194500 = 19:45 (7:45 PM)
  - 200000 = 20:00 (8:00 PM)
  - 093000 = 09:30 (9:30 AM)
- Three time slots are color-coded in dashboard:
  - 193000 (Blue)
  - 194500 (Purple)
  - 200000 (Green)

**Student Name Column (D):**
- Text field with student's full name
- Examples: "Shubham Kr.", "Shruti Jain", "John Doe"
- Can include spaces, dots, hyphens

### Sample Data

```
Month       | Date       | Time   | Student Name
2025-12-01  | 2025-12-08 | 193000 | Shubham Kr.
2025-12-01  | 2025-12-08 | 194500 | Shruti Jain
2025-12-01  | 2025-12-08 | 200000 | koteswara rao
2025-12-01  | 2025-12-09 | 193000 | Gaurav Mahawar
2025-12-01  | 2025-12-09 | 194500 | Krishna P J
2025-12-01  | 2025-12-09 | 200000 | (empty)
2026-01-01  | 2026-01-06 | 193000 | Chanchal Isokar
2026-01-01  | 2026-01-06 | 194500 | Khimeshwar Kokode
2026-01-01  | 2026-01-06 | 200000 | Suraj Kumar Jaiswal
```

---

## Sheet 2: "Questions" (or "Questions and Meeting Link")

This sheet contains the interview questions and Google Meet link.

### Column Headers (Row 1)
| Column | Field Name | Description |
|--------|-----------|-------------|
| A | Questions Sharing | Interview Question 1 |
| B | (blank) | Interview Question 2 |
| C | (blank) | Interview Question 3 |

### Alternative Structure

Alternatively, use a single column with label-value pairs:

```
Label           | Value
Question 1      | What are your strengths and why do you think so?
Question 2      | What are your areas of improvement and why do you think so?
Question 3      | What is your desirable role and org and why so?
Meeting Link    | https://meet.google.com/pei-pptg-nih
```

### Sample Data

**Structure 1 (Horizontal):**
```
What are your strengths and why do you think so? | What are your areas of improvement and why do you think so? | What is your desirable role and org and why so?
```

**Structure 2 (Vertical with Labels):**
```
Question 1: What are your strengths and why do you think so?
Question 2: What are your areas of improvement and why do you think so?
Question 3: What is your desirable role and org and why so?
Meeting Link: https://meet.google.com/pei-pptg-nih
```

---

## Sheet 3: "Sheet19" (Optional - Voting/Committee)

This sheet is used for placement committee voting (currently not displayed in dashboard).

### Column Headers
| Column | Field Name | Description |
|--------|-----------|-------------|
| A | SL. No. | Serial number |
| B | Placement Committee Final Nominees | Candidate name |
| C | Mark | Vote marking |

### Sample Data

```
SL. No. | Placement Committee Final Nominees | Mark
1       | Aakriti Sharma                    | ✓
2       | Abiwaquash Ansari                 | (blank)
3       | Ansh Chopra                       | ✓
4       | Ansh Kumar Gupta                  | ✓
5       | Azruddin Sadik Nadaf              | (blank)
```

---

## Data Validation Checklist

✓ **Schedule Sheet**
- [ ] Column A contains valid YYYY-MM-DD dates for months
- [ ] Column B contains valid YYYY-MM-DD dates for interview dates
- [ ] Column C contains HHMMSS time format (no colons)
- [ ] Column D contains student names (not blank)
- [ ] All rows have data (no blank rows in middle)
- [ ] No merged cells in the data range
- [ ] Data starts from Row 2 (Row 1 is headers)

✓ **Questions Sheet**
- [ ] Contains 3 interview questions
- [ ] Questions are clear and meaningful
- [ ] Google Meet link is valid and accessible
- [ ] Meeting link format: https://meet.google.com/XXX-XXXX-XXX

✓ **General**
- [ ] File saved as Excel (.xlsx) or Google Sheets
- [ ] No special characters in column headers
- [ ] No extra spaces in data cells (trim whitespace)
- [ ] Date formats are consistent throughout

---

## Common Data Issues & Solutions

### Issue 1: Time not displaying correctly
**Problem:** Time shows as "193000" instead of "19:30"
**Solution:** Time is converted in the dashboard. Ensure column C is formatted as TEXT in Excel, not as a number.

### Issue 2: Dates showing as numbers
**Problem:** Dates display as "45000" instead of "2025-12-08"
**Solution:** Format the date columns as DATE in Excel. Use Format > Cells > Date > YYYY-MM-DD

### Issue 3: Student names are missing
**Problem:** Some rows show empty student names
**Solution:** Check if Column D is empty. Fill in all student names. Empty cells will cause that row to be skipped.

### Issue 4: Dashboard not updating
**Problem:** Changes in Excel don't reflect in dashboard
**Solution:** 
1. Save the Excel file
2. If using Google Sheets, ensure it's shared publicly
3. Wait 30 seconds for auto-refresh
4. Clear browser cache (Ctrl+Shift+Delete)
5. Check browser console (F12) for error messages

---

## Import Instructions

### From Excel to Google Sheets

1. **Open Google Drive**
   - Go to https://drive.google.com

2. **Upload Excel File**
   - Click "+ New" > "File upload"
   - Select your Excel file
   - Wait for upload to complete

3. **Convert to Google Sheets**
   - Right-click uploaded file
   - Select "Open with" > "Google Sheets"
   - Google will convert it automatically

4. **Verify Sheet Names**
   - Check that sheet tabs match expected names
   - Rename if needed (right-click sheet tab)

5. **Share the Sheet**
   - Click "Share" button
   - Select "Anyone with the link can view"
   - Copy the sheet URL
   - Extract Sheet ID from URL: `...d/[SHEET_ID]/edit`

---

## Data Size Recommendations

| Metric | Recommended | Maximum |
|--------|------------|----------|
| Total Rows | 100-500 | 10,000 |
| Sheets | 3-5 | Unlimited |
| Columns per sheet | 4-10 | Unlimited |
| Characters per cell | 100 | 50,000 |
| Refresh frequency | 30s | 10s |

---

## Example Complete Dataset

Here's a complete example with actual sample data:

### Schedule Sheet
```
Month       | Date       | Time   | Student Name
2025-12-01  | 2025-12-08 | 193000 | Shubham Kr.
2025-12-01  | 2025-12-08 | 194500 | Shruti Jain
2025-12-01  | 2025-12-08 | 200000 | koteswara rao
2025-12-01  | 2025-12-09 | 193000 | Gaurav Mahawar
2025-12-01  | 2025-12-09 | 194500 | Krishna P J
2025-12-01  | 2025-12-09 | 200000 | (blank)
2025-12-01  | 2025-12-10 | 193000 | Prachi
2025-12-01  | 2025-12-10 | 194500 | Shubham Bhardwaj
2025-12-01  | 2025-12-10 | 200000 | Mithila Raut
2026-01-01  | 2026-01-06 | 193000 | Chanchal Isokar
2026-01-01  | 2026-01-06 | 194500 | Khimeshwar Kokode
2026-01-01  | 2026-01-06 | 200000 | Suraj Kumar Jaiswal
2026-02-01  | 2026-02-02 | 193000 | Reena Kumari
2026-02-01  | 2026-02-02 | 194500 | Harsh Khandelwal
2026-02-01  | 2026-02-02 | 200000 | Shreyash Gupta
```

### Questions Sheet
```
What are your strengths and why do you think so?
What are your areas of improvement and why do you think so?
What is your desirable role and org and why so?
https://meet.google.com/pei-pptg-nih
```

---

## Need Help?

Refer to the **MOCK-INTERVIEW-DASHBOARD-SETUP.md** file for:
- Complete setup instructions
- Google Sheets API configuration
- Dashboard customization options
- Troubleshooting guide

---

**Last Updated:** January 2, 2026
**Version:** 1.0
