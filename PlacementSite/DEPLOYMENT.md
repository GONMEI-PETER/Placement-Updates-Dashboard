# Deployment Guide - PlacementSite

## Quick Start

The PlacementSite is a **100% static website** - no backend, no database, no build process needed.

## Deployment Options

### Option 1: GitHub Pages (Free, Recommended)

1. **Enable GitHub Pages** in your repository:
   - Go to Settings → Pages
   - Select "main" branch as source
   - Click Save
   
2. **Access your site:**
   - Your site will be live at: `https://GONMEI-PETER.github.io/Placement-Updates-Dashboard/PlacementSite/`

3. **Custom Domain (Optional):**
   - Purchase a domain (e.g., placementdashboard.com from Namecheap)
   - Add CNAME file or update DNS records
   - Point to GitHub Pages

### Option 2: Netlify (Free, Easy Deployment)

1. **Sign up at netlify.com**

2. **Connect GitHub:**
   - Click "New site from Git"
   - Select GitHub repository
   - Branch: main
   - Publish directory: PlacementSite

3. **Site goes live immediately**
   - Default URL: `https://[random-name].netlify.app`
   - Add custom domain if desired

4. **Auto-deploy on push:**
   - Every commit to main automatically redeploys

### Option 3: Vercel (Free, Ultra-Fast)

1. **Sign up at vercel.com**

2. **Import GitHub project**
   - Select Placement-Updates-Dashboard repo
   - Root directory: PlacementSite
   - Click Deploy

3. **Get instant global CDN**
   - Live at: `https://[project-name].vercel.app`

### Option 4: Traditional Hosting (Shared/VPS)

If using providers like Bluehost, GoDaddy, HostGator:

1. **Download index.html and README.md**
2. **Connect via FTP/SFTP**
3. **Upload files to public_html folder**
4. **Access via your domain**

### Option 5: Self-Host on Local Server

**Python (3.x):**
```bash
cd PlacementSite
python -m http.server 8000
# Visit http://localhost:8000
```

**Node.js:**
```bash
npm install -g http-server
http-server PlacementSite
# Visit http://localhost:8080
```

**PHP:**
```bash
cd PlacementSite
php -S localhost:8000
# Visit http://localhost:8000
```

## Custom Domain Setup

### With Netlify/Vercel:
1. Go to Site Settings → Domain Management
2. Add custom domain
3. Follow DNS configuration instructions
4. Wait 24-48 hours for DNS propagation

### With GitHub Pages:
1. Add CNAME file to repository root with domain name
2. Update DNS A records:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
3. Or add CNAME record: `pages.github.com`

## SSL/HTTPS

- **GitHub Pages**: ✅ Automatic (required)
- **Netlify**: ✅ Automatic (free Let's Encrypt)
- **Vercel**: ✅ Automatic
- **Traditional Hosting**: May need to purchase SSL or use free CloudFlare

## Performance Tips

1. **Use a CDN:** Netlify and Vercel are global CDNs
2. **Enable Gzip:** Automatic on most platforms
3. **Minify HTML:** Optional (single HTML keeps it simple)
4. **Cache headers:** Netlify/Vercel handle this automatically

## Analytics Setup

### Google Analytics
1. Create account at analytics.google.com
2. Add this code before closing </head> tag:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_ID');
   </script>
   ```

### Plausible Analytics (Privacy-Friendly)
1. Sign up at plausible.io
2. Add tracking script before closing </head>:
   ```html
   <script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
   ```

## WhatsApp Integration (Future)

When ready to add WhatsApp notifications:
1. Use Twilio WhatsApp API
2. Set up webhook for new placement updates
3. Send automatic messages to student group

## Troubleshooting

**Site not loading:**
- Clear browser cache (Ctrl+Shift+Del)
- Check DNS propagation: dnschecker.org
- Verify file paths are correct

**Styling looks broken:**
- All CSS is embedded in index.html (no external files)
- Clear browser cache
- Try different browser

**Performance issues:**
- Use Lighthouse in Chrome DevTools
- Check CDN status
- Reduce image sizes if adding images

## Monitoring

Set up uptime monitoring (free):
- **Uptime Robot:** uptimerobot.com
- **Monitor Domain:** https://yourdomain.com
- **Check Interval:** 5 minutes
- **Get alerts** if site goes down

## Next Steps

1. **Choose deployment platform** (Netlify recommended for beginners)
2. **Set up custom domain** (optional but professional)
3. **Enable analytics** to track student interest
4. **Add Google Calendar** once decided on hosting
5. **Set up WhatsApp notifications** when ready

## Cost Breakdown

| Option | Cost | Features |
|--------|------|----------|
| GitHub Pages | Free | Limited, GitHub.io URL |
| Netlify | Free | Full features, custom domain, auto-deploy |
| Vercel | Free | Fast, auto-deploy, analytics |
| Custom Domain | $1-15/year | Professional, memorable |
| SSL Certificate | Free | All modern hosts include |
| Email (optional) | Free-Free | Gmail or domain email |
| **TOTAL** | **Free-15/year** | **Fully functional site** |

## Deployed Successfully? 🎉

Once live:
1. Share link in WhatsApp group
2. Test on mobile and desktop
3. Gather feedback from students
4. Iterate based on usage
5. Add calendar integration next

---

**Questions?** Open an issue on GitHub or reach out to GONMEI-PETER
