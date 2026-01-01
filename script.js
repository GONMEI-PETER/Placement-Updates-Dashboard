// Placement Data
const placementData = [
  { id: 1, title: 'Program Manager', sector: 'education', org: 'Education NGO', description: 'Lead educational programs in rural areas' },
  { id: 2, title: 'Field Coordinator', sector: 'development', org: 'Development Org', description: 'Coordinate field operations and community engagement' },
  { id: 3, title: 'Health Officer', sector: 'healthcare', org: 'Health Ministry', description: 'Public health program coordination' },
  { id: 4, title: 'Finance Manager', sector: 'finance', org: 'Social Enterprise', description: 'Financial management and reporting' },
  { id: 5, title: 'Research Associate', sector: 'development', org: 'Research Institute', description: 'Data collection and analysis' },
  { id: 6, title: 'HR Specialist', sector: 'admin', org: 'Corporate Foundation', description: 'Human resources and administration' },
  { id: 7, title: 'Environmental Officer', sector: 'environment', org: 'Green Initiative', description: 'Environmental conservation programs' },
  { id: 8, title: 'Tech Developer', sector: 'technology', org: 'EdTech Startup', description: 'Software development for social impact' }
];

// DOM Elements
const filterBtns = document.querySelectorAll('.filter-btn');
const placementsGrid = document.getElementById('placements-grid');
const navLinks = document.querySelectorAll('.nav-link');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  displayPlacements(placementData);
  setupFilterListeners();
  setupNavListeners();
});

// Display Placements
function displayPlacements(data) {
  placementsGrid.innerHTML = '';
  data.forEach(placement => {
    const card = document.createElement('div');
    card.className = 'placement-card';
    card.innerHTML = `
      <h3>${placement.title}</h3>
      <span class='sector'>${placement.sector.toUpperCase()}</span>
      <p><strong>Organization:</strong> ${placement.org}</p>
      <p>${placement.description}</p>
    `;
    placementsGrid.appendChild(card);
  });
}

// Filter Setup
function setupFilterListeners() {
  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      filterBtns.forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      
      const filter = e.target.dataset.filter;
      if (filter === 'all') {
        displayPlacements(placementData);
      } else {
        const filtered = placementData.filter(p => p.sector === filter);
        displayPlacements(filtered);
      }
    });
  });
}

// Navigation Listeners
function setupNavListeners() {
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      target.scrollIntoView({ behavior: 'smooth' });
    });
  });
}
