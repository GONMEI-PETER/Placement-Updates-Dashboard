const fetch = require("node-fetch");

async function getLatestJob() {
  // TODO: change this to your real latest‑job JSON or API
  const res = await fetch("https://example.com/latest-job.json");
  const job = await res.json();

  const subject = `New ${job.domain} opportunity: ${job.title} at ${job.organization}`;

  const bodyText = `
Latest job update

Title: ${job.title}
Organization: ${job.organization}
Location: ${job.location}
Domain: ${job.domain}
Type: ${job.type}
Deadline: ${job.deadline}

Short description:
${job.description}

Apply link: ${job.applyUrl}
  `.trim();

  const bodyHtml = `
    <h2>Latest job update</h2>
    <p><strong>Title:</strong> ${job.title}</p>
    <p><strong>Organization:</strong> ${job.organization}</p>
    <p><strong>Location:</strong> ${job.location}</p>
    <p><strong>Domain:</strong> ${job.domain}</p>
    <p><strong>Type:</strong> ${job.type}</p>
    <p><strong>Deadline:</strong> ${job.deadline}</p>
    <p><strong>Description:</strong><br>${job.description}</p>
    <p><a href="${job.applyUrl}">Apply here</a></p>
  `;

  return { subject, bodyText, bodyHtml };
}

module.exports = { getLatestJob };
