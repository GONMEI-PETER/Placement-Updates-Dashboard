// Placement Dashboard Data - January 2026

// PlaceComm Member Allocation Statistics
const placementData = {
    members: [
        { name: 'Aakriti Sharma', count: 7 },
        { name: 'Azruddin Sadik Nadaf', count: 10 },
        { name: 'G Peter', count: 10 },
        { name: 'Jahnavi Taak', count: 10 },
        { name: 'Justin Jacob', count: 10 },
        { name: 'Abiwaquash Ansari', count: 12 },
        { name: 'Subhajit Chandra', count: 10 }
    ],
    totalStudents: 102,
    totalAllocated: 69
};

// Photo Capture Status
const photoStatus = {
    cameraPhoto: {
        count: 100,
        percentage: 98.04,
        status: 'Yes - Camera Photo'
    },
    idPicture: {
        count: 2,
        percentage: 1.96,
        status: 'No - ID Picture'
    },
    total: 102
};

// Draft Submission Status
const draftSubmission = {
    submitted: 100,
    notSubmitted: 2,
    total: 102,
    submissionPercentage: 98.04
};

// Draft Review Status
const draftReview = {
    reviewed: 102,
    pending: 0,
    total: 102,
    reviewPercentage: 100
};

// Final Status
const finalStatus = {
    closed: 102,
    open: 0,
    total: 102,
    status: 'All Profiles Closed'
};

// Summary Statistics
const summaryStats = {
    reportDate: 'January 2, 2026',
    academicYear: '2025-2026',
    totalStudents: 102,
    allocationComplete: true,
    draftSubmissionComplete: true,
    reviewComplete: true,
    finalStatusComplete: true,
    completionPercentage: 100
};

// Member-wise breakdown
const memberWiseBreakdown = {
    'Aakriti Sharma': {
        allocated: 7,
        cameraPhoto: 6,
        idPicture: 1,
        draftSubmitted: 7,
        draftReviewed: 7,
        finalStatus: 'Closed'
    },
    'Azruddin Sadik Nadaf': {
        allocated: 10,
        cameraPhoto: 10,
        idPicture: 0,
        draftSubmitted: 10,
        draftReviewed: 10,
        finalStatus: 'Closed'
    },
    'G Peter': {
        allocated: 10,
        cameraPhoto: 10,
        idPicture: 0,
        draftSubmitted: 10,
        draftReviewed: 10,
        finalStatus: 'Closed'
    },
    'Jahnavi Taak': {
        allocated: 10,
        cameraPhoto: 10,
        idPicture: 0,
        draftSubmitted: 10,
        draftReviewed: 10,
        finalStatus: 'Closed'
    },
    'Justin Jacob': {
        allocated: 10,
        cameraPhoto: 10,
        idPicture: 0,
        draftSubmitted: 10,
        draftReviewed: 10,
        finalStatus: 'Closed'
    },
    'Abiwaquash Ansari': {
        allocated: 12,
        cameraPhoto: 12,
        idPicture: 0,
        draftSubmitted: 12,
        draftReviewed: 12,
        finalStatus: 'Closed'
    },
    'Subhajit Chandra': {
        allocated: 10,
        cameraPhoto: 10,
        idPicture: 0,
        draftSubmitted: 10,
        draftReviewed: 10,
        finalStatus: 'Closed'
    }
};

// Export data (for use in HTML if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        placementData,
        photoStatus,
        draftSubmission,
        draftReview,
        finalStatus,
        summaryStats,
        memberWiseBreakdown
    };
}
